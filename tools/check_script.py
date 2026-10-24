# -*- coding: utf-8 -*-
"""剧本能力覆盖检查

用法:
    python check_script.py <剧本.md> [--md 报告.md] [--per-shot] [--semantic] [--target wan3]

作用:
    1. 解析剧本，识别它需要哪些「影视化生产能力」（镜头/动作/张力/特效...）
    2. 对照本地知识库统计每项能力的供给条目数
    3. 标出缺失与薄弱项，并给出应优先加载的条目文件

选项:
    --per-shot   逐段推荐应加载的条目
    --semantic   用字符 bigram TF-IDF 余弦做语义相似度匹配，替代能力词表匹配
    --target     只统计目标模型的条目（wan3 = 万相/可灵/WAN3 通用条目，剔除仅适配其他模型的条目）
"""
import io
import math
import os
import re
import sys
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

KB_ROOT = os.path.dirname(os.path.abspath(__file__))


def resolve_entries():
    """兼容多种布局：entries/ 子目录，或分类目录直接在根/上一级。"""
    parent = os.path.dirname(KB_ROOT)
    for base in (KB_ROOT, parent):
        p = os.path.join(base, "entries")
        if os.path.isdir(p):
            return p
    for base in (KB_ROOT, parent):
        try:
            if any(re.match(r"^\d\d-", d) for d in os.listdir(base)):
                return base
        except OSError:
            continue
    return os.path.join(KB_ROOT, "entries")


ENTRIES = resolve_entries()

# 能力维度：名称 -> 触发词（剧本中出现即视为需要该能力）
DIMENSIONS = {
    "镜头与运镜": ["景别", "全景", "中景", "近景", "特写", "大特写", "推镜", "拉镜", "摇镜", "移镜", "跟拍",
                 "环绕", "升降", "航拍", "俯拍", "仰拍", "低机位", "长镜头", "手持", "机位", "视角", "主观镜头"],
    "构图与画面": ["构图", "三分", "对称", "留白", "前景", "背景", "层次", "剪影", "画框", "透视", "纵深", "轴线"],
    "动作与打斗": ["出拳", "踢", "刀", "剑", "枪", "斩", "劈", "刺", "格挡", "闪避", "翻滚", "冲刺", "突进",
                 "腾空", "落地", "居合", "拔刀", "收刀", "对刀", "连击", "受击", "击退", "摔", "锁喉", "招式"],
    "张力与节奏": ["对峙", "蓄势", "爆发", "停顿", "静止", "慢动作", "升格", "加速", "冲击帧", "定格", "压迫",
                 "窒息", "悬停", "延迟", "沉默", "爆点"],
    "情绪与表演": ["哭", "泪", "怒", "笑", "恐惧", "颤抖", "绝望", "崩溃", "悲", "喜", "惊", "犹豫", "咬牙",
                 "呼吸", "眼神", "表情", "瞳孔", "回头", "低头"],
    "特效与作画": ["火", "雷", "电", "冰", "光效", "粒子", "烟", "尘", "破碎", "裂", "残影", "速度线", "冲击波",
                 "能量", "发光", "爆炸", "水花", "雨", "风"],
    "法术与超能": ["法术", "魔法", "结界", "召唤", "觉醒", "变身", "咒", "符", "阵", "气", "灵气", "超能力", "浮空"],
    "分镜与连贯": ["分镜", "转场", "剪辑点", "匹配", "跳切", "蒙太奇", "正反打", "视线", "越轴", "连贯", "衔接",
                 "插入镜", "过肩"],
    "光影与色彩": ["逆光", "侧光", "顶光", "底光", "阴影", "高光", "色调", "冷暖", "色温", "环境光", "轮廓光",
                 "剪影", "暗部", "光比"],
    "音频与配音": ["音效", "配乐", "BGM", "环境声", "静音", "无声", "配音", "旁白", "拟音", "鼓点", "心跳"],
    "角色与一致性": ["角色", "服装", "发型", "道具", "设定", "面容", "年龄", "体型", "伤", "血迹", "武器设定"],
    "场景与空间": ["场景", "空间", "环境", "天气", "地面", "屋顶", "室内", "室外", "街道", "山林", "庙", "雪", "夜"],
    "剪辑与输出": ["时长", "卡点", "节奏点", "片头", "片尾", "字幕", "调色", "合成", "输出", "分辨率", "帧率"],
    "叙事与结构": ["开场", "铺垫", "转折", "高潮", "结局", "伏笔", "闪回", "悬念", "钩子", "旁支", "收束"],
}

# 目标模型过滤：只保留与该模型相关、或未绑定特定模型的条目
TARGET_MODELS = {
    "wan3": {
        "hit": ["wan", "万相", "万相2", "可灵", "kling", "通义", "即梦", "seedance", "vidu"],
        "drop": ["midjourney", "stable diffusion", "sd1.5", "sdxl", "sora", "runway gen-2", "pika", "luma"],
    },
}


def parse_frontmatter(text):
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
            for line in parts[1].splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip("'\"")
    return meta, body


def lib_key(stem):
    """识别技法库文件的去重键：472-lib-emotion-100 / lib_emotion_100 → lib_emotion。"""
    s = re.sub(r"^\d+-", "", stem)
    s = s.replace("-100", "").replace("_100", "").replace("-", "_")
    return s if s.startswith("lib_") else ""


def load_kb(target=None):
    """读取全部条目：标题、标签、简介、正文。"""
    items = []
    rule = TARGET_MODELS.get(target or "", None)
    dropped = 0
    seen_lib = {}
    for cat in sorted(os.listdir(ENTRIES)):
        cat_dir = os.path.join(ENTRIES, cat)
        if not os.path.isdir(cat_dir):
            continue
        for fn in sorted(os.listdir(cat_dir)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(cat_dir, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            meta, body = parse_frontmatter(text)
            if rule:
                blob = (meta.get("title", "") + " " + meta.get("tags", "") + " " +
                        meta.get("summary", "") + " " + body).lower()
                if any(w in blob for w in rule["drop"]) and not any(w in blob for w in rule["hit"]):
                    dropped += 1
                    continue
            key = lib_key(os.path.splitext(fn)[0])
            if key:
                # 同一技法库存在多份拷贝时，只保留 14-技法词库 下的版本
                if key in seen_lib:
                    if cat == "14-技法词库":
                        items[seen_lib[key]] = None
                    else:
                        dropped += 1
                        continue
                seen_lib[key] = len(items)
            items.append({
                "title": meta.get("title") or os.path.splitext(fn)[0],
                "tags": meta.get("tags", ""),
                "summary": meta.get("summary", ""),
                "body": body,
                "path": f"{cat}/{fn}",
                "cat": cat,
            })
    return [it for it in items if it], dropped


def analyze_script(text):
    """按二级标题切段，统计每段命中的能力维度。"""
    body = re.sub(r"^\s*>\s*.*$", "", text, flags=re.M)  # 去掉元信息引用行
    sections = re.split(r"^(?=##\s)", body, flags=re.M)
    result = []
    for sec in sections:
        if not sec.strip():
            continue
        head = sec.splitlines()[0].strip("# ").strip()
        if not head:
            head = "（开篇）"
        sec = re.sub(r"^\s*>\s*.*$", "", sec, flags=re.M)
        hits = {}
        for dim, words in DIMENSIONS.items():
            n = sum(sec.count(w) for w in words)
            if n:
                hits[dim] = n
        result.append((head, sec, hits))
    return result


# ---------- 语义匹配：字符 bigram TF-IDF 余弦 ----------

def tokens(text):
    text = re.sub(r"[^\w\u4e00-\u9fff]+", " ", text.lower())
    toks = []
    for chunk in text.split():
        if re.search(r"[\u4e00-\u9fff]", chunk):
            toks.extend(chunk[i:i + 2] for i in range(len(chunk) - 1))
            toks.extend(chunk)  # 单字也保留，短词可命中
        else:
            toks.append(chunk)
    return toks


def build_vectors(items):
    docs = [Counter(tokens(it["title"] + " " + it["tags"] + " " + it["summary"] + " " + it["body"]))
            for it in items]
    df = Counter()
    for d in docs:
        df.update(set(d))
    n = len(docs)
    idf = {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()}
    vecs = []
    for d in docs:
        v = {t: (1 + math.log(c)) * idf[t] for t, c in d.items() if t in idf}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs.append({t: x / norm for t, x in v.items()})
    return vecs, idf


def cosine(qvec, dvec):
    if len(qvec) > len(dvec):
        qvec, dvec = dvec, qvec
    return sum(x * dvec.get(t, 0.0) for t, x in qvec.items())


def semantic_rank(section_text, items, vecs, idf):
    q = Counter(tokens(section_text))
    qv = {t: (1 + math.log(c)) * idf[t] for t, c in q.items() if t in idf}
    norm = math.sqrt(sum(x * x for x in qv.values())) or 1.0
    qv = {t: x / norm for t, x in qv.items()}
    scored = [(cosine(qv, v), it) for v, it in zip(vecs, items)]
    scored.sort(key=lambda x: -x[0])
    return scored


def main():
    argv = sys.argv[1:]
    md_out = None
    if "--md" in argv:
        i = argv.index("--md")
        md_out = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    target = None
    if "--target" in argv:
        i = argv.index("--target")
        target = argv[i + 1].lower()
        argv = argv[:i] + argv[i + 2:]
    per_shot = "--per-shot" in argv
    semantic = "--semantic" in argv
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print("用法: python check_script.py <剧本.md> [--md 报告.md] [--per-shot] [--semantic] [--target wan3]")
        return

    script_path = args[0]
    text = open(script_path, encoding="utf-8", errors="replace").read()
    sections = analyze_script(text)
    kb, dropped = load_kb(target)

    need = {d: 0 for d in DIMENSIONS}
    need_raw = {d: 0 for d in DIMENSIONS}
    for _, _, hits in sections:
        for d, n in hits.items():
            need[d] += 1
            need_raw[d] += n

    supply = {d: [] for d in DIMENSIONS}
    for it in kb:
        blob = f"{it['title']} {it['tags']} {it['summary']}"
        for d, words in DIMENSIONS.items():
            if any(w in blob for w in words):
                supply[d].append(it)

    order = sorted(DIMENSIONS, key=lambda d: -need[d])
    lines = [f"# 剧本能力覆盖报告\n"]
    lines.append(f"- 剧本：`{os.path.basename(script_path)}`（{len(sections)} 个分段）")
    scope_note = f"（target={target}，剔除非目标模型条目 {dropped} 条）" if target else f"（全部 {len(kb)} 条）"
    lines.append(f"- 知识库：`{ENTRIES}` {scope_note}")
    if semantic:
        lines.append("- 匹配方式：字符 bigram TF-IDF 语义相似度")
    lines.append("")

    lines.append("## 一、需求 × 供给总览\n")
    lines.append("| 能力维度 | 需要段落 | 剧本提及次数 | 知识库条目 | 判定 |")
    lines.append("|---|---|---|---|---|")
    gaps, weak = [], []
    for d in order:
        if need[d] == 0:
            continue
        s = len(supply[d])
        if s == 0:
            verdict = "**缺失**"
            gaps.append(d)
        elif s < 3:
            verdict = "薄弱"
            weak.append(d)
        else:
            verdict = "充足"
        lines.append(f"| {d} | {need[d]} | {need_raw[d]} | {s} | {verdict} |")
    unneeded = [d for d in order if need[d] == 0]
    if unneeded:
        lines.append(f"\n剧本未涉及：{'、'.join(unneeded)}\n")

    lines.append("\n## 二、缺口处理建议\n")
    if not gaps and not weak:
        lines.append("全部能力维度均有 3 条以上条目支撑，可直接进入分镜制作。\n")
    for d in gaps:
        lines.append(f"- **{d}**：剧本需要但库里没有对应条目 → 需新增")
    for d in weak:
        names = "、".join(t["title"] for t in supply[d])
        lines.append(f"- **{d}**：仅 {len(supply[d])} 条（{names}）→ 建议补充 2–3 条专项")

    lines.append("\n## 三、推荐加载\n")
    if semantic:
        vecs, idf = build_vectors(kb)
        lines.append("| 分段 | 最相关条目（相似度） |")
        lines.append("|---|---|")
        for head, sec, _ in sections:
            top = [(s, it) for s, it in semantic_rank(sec, kb, vecs, idf) if s > 0.02][:3]
            if not top:
                continue
            cell = "<br>".join(f"`{it['path']}` {it['title']}（{s:.2f}）" for s, it in top)
            lines.append(f"| {head} | {cell} |")
    elif per_shot:
        for head, _, hits in sections:
            dims = sorted(hits, key=lambda d: -hits[d])
            recs = []
            for d in dims:
                for it in supply[d][:2]:
                    if it not in recs:
                        recs.append(it)
                if len(recs) >= 3:
                    break
            if recs:
                lines.append(f"### {head}")
                for it in recs:
                    lines.append(f"- `{it['path']}` {it['title']}")
                lines.append("")
    else:
        lines.append("（加 `--per-shot` 输出逐段推荐；加 `--semantic` 输出语义相似推荐）\n")

    report = "\n".join(lines)
    print(report)
    if md_out:
        with open(md_out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(report)
        print(f"\n报告已写入 {md_out}")


if __name__ == "__main__":
    main()
