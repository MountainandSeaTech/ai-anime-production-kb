---
title: Skill解剖学——SKILL.md结构与frontmatter字段
category: 工具与模型
tags: [Skill编写, frontmatter, SKILL.md, 结构规范, Agent能力]
source: 网络学习
created: 2026-10-13
updated: 2026-10-13
summary: Skill就两块：frontmatter决定"会不会被触发"，正文决定"触发后干得好不好"；90%的翻车死在第一块
related: [172, 173, 174, 180]
---

# Skill解剖学——SKILL.md结构与frontmatter

## 核心要点
- Agent只读 **name + description** 来决定是否触发——这两个字段是全部身家性命
- 正文（Markdown body）**触发后才加载**——把流程细节塞frontmatter等于在名片背面印说明书
- 这是**两阶段加载**设计：描述常驻系统提示词，正文按需入场，省token又防干扰
- frontmatter必须从**文件第一个字节**开始：无前置空行、无BOM头，否则直接解析失败

## 文件结构规范

### 最小结构
```
my-skill/
└── SKILL.md          # 必需，唯一硬性要求
```

### 完整结构（按需）
```
my-skill/
├── SKILL.md          # 入口：frontmatter + 指令正文
├── scripts/          # 可执行脚本（确定性的活别交给模型现编）
├── references/       # 深读材料（触发后才读，正文里给链接）
└── assets/           # 模板、示例输出等静态资源
```
- 原则：**渐进披露**——能放references的别放正文，能放正文的别放frontmatter
- 关联 176 知识沉淀型skill对references目录的重度使用

## frontmatter字段速查

| 字段 | 必需 | 作用 | 坑 |
|---|---|---|---|
| name | 是 | 唯一标识，小写连字符 | 和目录名不一致会混乱 |
| description | 是 | 触发的唯一依据 | 写"如何做"=模型跳过正文（172） |
| license | 否 | 分发时声明 | 个人用可省 |
| allowed-tools | 否 | 限制可用工具 | 超配权限=信任崩塌（174） |

## 格式硬性要求（Lint规则）
```
✅ 正确：
---
name: my-skill
description: ...
---
（正文）

❌ 找死：
- 文件开头有空行 → 解析失败
- UTF-8 BOM头 → 解析失败  
- frontmatter里写tab缩进 → YAML报错
- description超1024字符 → 截断，触发词丢失
```
- LF/CRLF换行都兼容——这是唯一的宽容

## description的两段论（详见172）
```yaml
# 反面教材：只说了what没说when
description: 处理PDF文件

# 及格线：what + when
description: 从PDF提取文本和表格。当用户需要读取、分析或转换PDF内容时使用。

# 优秀线：what + when + 边界
description: 从PDF提取文本和表格，支持表单填充与批量处理。当用户需要读取、分析、合并PDF时使用；纯文档编辑走docx skill，不要用于PDF生成图片。
```

## 正文与frontmatter的分工铁律
```
frontmatter = 简历（决定要不要你）
正文 = 上岗培训（决定你干得怎样）

简历里写工作流程 → 面试官照着简历让你干活，培训白做
正文体里藏触发条件 → 永远不触发，培训材料没人看
```
- 网络实证：description里写"runs X, then Y, then reviews Z"的流程摘要，模型会**照着description直接执行，跳过正文**——正文里精心设计的两阶段步骤只跑了一遍
- 所以：description只命名**产出物和范围**，过程步骤全部留给正文（173）

## 常见坑
- **前置空行/BOM**：编辑器默认保存带BOM=skill静默失效，排查两小时起步
- **正文塞frontmatter**：description写800字流程=触发逻辑噪声化，别的skill被带歪
- **name用大写/下划线**：`My_Skill` 在部分平台直接拒绝加载，统一小写连字符
- **scripts里装聪明人**：脚本里调LLM API=不确定性套娃，脚本只做确定性操作
- **assets当网盘用**：塞50MB参考视频=加载慢且无用，assets只放模板级小文件

## 进阶
- **单文件起步，痛了再拆**：先写纯SKILL.md，正文超过500行再抽references
- **name即域名**：加个人前缀防冲突（`h3-storyboard-rework`而不是`rework`）
- **自检**：写完用纯文本编辑器重开文件，看第一个字符是不是`-`
- **版本意识**：frontmatter不加version字段，版本管理交给git（179）

## 备注
- 两阶段加载：description常驻，正文按需
- frontmatter从第一字节开始，无BOM无空行
- name+description是全部身家，正文是触发后的事
- 关联：172 description写法、173 正文写法、174 反模式、176 references目录、180 体系规划
