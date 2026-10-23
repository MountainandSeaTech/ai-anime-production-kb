---
title: 技能魔法特效与提示词模板二十连⑥——风与气流：无形之力的视觉代理、压缩空气与龙卷风分级
category: 提示词技巧
tags: [风, 气流, wind, air, tornado, gust, 提示词模板, VFX, AI视频, 无形之力]
source: 网络学习
created: 2026-10-17
updated: 2026-10-17
summary: 风是看不见的：必须选至少两个视觉代理（头发/布料/植被/碎片）锚定风的存在；先定风速风向再写提示词；压缩空气爆发与螺旋气流是AI可识别的魔法风；提供3套模板
related: [378, 380, 381, 355, 357]
---

# 技能魔法特效与提示词模板二十连⑥：风与气流

## 核心要点

- **风本身不可见**：AI画不出"风"，只能画出被风影响的东西——必须写至少两个视觉代理（visual proxies）：头发、布料、植被、尘土、碎片
- 先定**物理参数**再写词：风速（gentle breeze / hurricane-force）、方向（from left / spiraling upward）、持续时间（gust / sustained）
- 魔法风与自然风的区别：魔法风有**形状**（螺旋、锥形、定向刃）和**颜色微粒**（尘埃被魔法染色、可见气流纹路）
- 压缩空气爆发（air blast）是最实用的魔法风：写 `compressed air burst, visible shockwave distortion, debris scattering outward`

## 详细内容

### 一、视觉代理清单（按风力等级）

| 风力 | 代理选择 | 提示词示例 |
|---|---|---|
| 微风（起手式） | 发丝、轻纱、草叶 | `a few strands of hair lifting gently, silk scarf fluttering` |
| 强风（攻击） | 全身衣物、小树、尘土 | `clothing whipping violently, small trees bending, dust rolling across ground` |
| 飓风（大招） | 碎片、招牌、身体被推 | `debris flying horizontally, signposts rattling, character bracing against force` |

### 二、魔法风三形态

1. **定向气刃**：`compressed air blade, visible distortion wave, cutting through grass`
2. **螺旋气流/龙卷风**：`spiraling vortex, tightly-coiled funnel, debris orbiting upward`
3. **真空领域**：`air vacuum, sudden inward rush of dust and leaves, eerie silence before burst`

### 三、AI生成穿帮与对策

- **无代理**：画面静止但字幕说"大风" → 强制写 `visual proxies: hair and clothing`
- **方向乱**：头发向左吹、尘土向右飞 → 写 `wind blowing from the left, consistent direction`
- **无重量**：碎片悬浮不落 → 写 `debris falling after gust passes, gravity reasserting`
- **过度扭曲**：人物脸被风吹变形 → 写 `face protected, hair and clothing only affected`

### 四、制作路线

- **AI直出**：龙卷风、大范围风暴（背景级）
- **合成**：人物静态拍摄 + 后期头发/布料动画（AE Puppet Pin）+ 尘土粒子层 + 相机震动（Handheld shake）
- 声音：低频呼啸+高频哨音分层（接304）

## 关键参数 / 模板 / 清单

**模板A：风刃术（中景/攻击）**
```
35mm medium shot, slight slow motion. The caster swings their arm,
releasing a compressed air blade. The blade is visible only as a
distortion wave — grass bends flat in its path, a line of dust
erupts from the ground, and leaves split in half as it passes.
The caster's clothing whips backward from the recoil. The air
shimmers briefly along the blade's trajectory. Cinematic, natural
lighting, film grain.
Negative: anime, cartoon, visible sword, glowing blade, energy beam,
no environmental reaction, static grass
```

**模板B：召唤龙卷风（广角/史诗）**
```
24mm wide angle, low angle. A slender tornado funnel descends from
dark storm clouds, touching down in an open field. The funnel is
tightly-coiled and serpentine, made visible by dust and debris
orbiting upward rapidly. Grass and small plants are ripped from
the ground, spiraling into the vortex. The caster stands at the
edge, clothing whipping violently, arms raised. The air is thick
with flying particles. Cinematic, gritty, overcast lighting.
Negative: anime, cartoon, clean funnel, no debris, calm ground,
blue sky, static clothing
```

**模板C：飓风领域（全景/防御）**
```
35mm wide shot, slow orbit. A dome of compressed wind surrounds
the caster, visible as a shimmering distortion in the air. Rain
and arrows curve around the dome, deflected by the force. Inside,
the caster's hair and clothing are completely still, protected.
Outside the dome, hurricane-force winds bend trees and send debris
flying horizontally. The boundary between calm and chaos is sharp.
Cinematic, photorealistic, subtle film grain.
Negative: anime, cartoon, visible shield, glowing dome, no wind outside,
calm trees, uniform lighting
```

**关键负向词（风系专用）**
```
anime, cartoon, visible energy beams, glowing wind, no visual proxies,
static clothing, calm hair, floating debris without wind, inconsistent
direction, face distortion, 3D render
```

## 备注

- 海裂映射：弦音的"声弦"与风系共享"可见气流纹路"写法，但需区分——风是 `dust and debris`，声是 `heat-haze style distortion rings`；深渊之核的静默领域可用"真空领域"模板反写（无风、无尘、无声）
- 与380雷电联动：雷暴=风+电，提示词中先写风代理再写电弧，确保环境一致
- 与357节制原则联动：风系最易"全程满屏吹"，建议L1微风起手→L2强风攻击→L3短暂飓风→L4真空静默（接374显形级）
