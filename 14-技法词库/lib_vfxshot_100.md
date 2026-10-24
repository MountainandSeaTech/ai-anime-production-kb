# 特效镜头拍法库（141 条）

> 用途：动漫 AI 视频创作的特效作画/拍法参考。与《镜头语言技法库》互补——那库管"机位怎么动"，本库管"画面里的特效怎么画"。
> 对接《对战编排总纲》法则 27（冲击三级制）、法则 24（单粒子多层结构）、法则 32-41（作画签名技法）。
> 用法：先按"三级冲击配套表"定基调，再到正文按类别检索复制英文提示词短语。

---

## 三级冲击配套表（对接总纲法则 27）

| 级别 | 推荐叠加技法（编号） | 说明 |
|---|---|---|
| 轻碰 | 6 局部冲击帧 + 13 跳帧 + 15 集中线 + 85 汗珠飞溅 | 克制，反馈只给在"点"上；镜头微震即止 |
| 重击 | 2 反相负片 + 7 放射冲击帧 + 65 中村方块 + 41 尘环 + 56 光尾 + 27 方向性运动模糊 | 三层流体爆 + 冲击环；碎片分层（68）必须遵守 |
| 爆发 | 3 白闪 + 5 凝滞帧 + 31 吉成爆炸 或 37 球状膨胀爆 + 94 冲散云层 + 55 Bloom + 111 静音帧 | 全屏事件；先拉远看清全貌（总纲法则 39），再切瞳孔 ECU |

> 配套原则：**主导粒子每镜只有一种**（总纲法则 24）；冲击帧是剪辑语言，写在镜头描述里，不写在角色动作里。

---

## 一、冲击表现类（冲击帧 / 负片 / 白闪 / 凝滞）

### 1. 黑白冲击帧（Impact Frame）
碰撞瞬间插入 1-2 帧高反差黑白画，角色与背景反转为纯黑白剪影。中村丰在《我的英雄学院》23 话 31 秒内用了 41 个。
- **什么量级用它**：轻碰~爆发全级通用；越重的击配越长停留帧数。
- **AI提示词写法**：`high-contrast black-and-white impact frame at the moment of collision, 0.1s, characters rendered as inverted monochrome silhouettes`

### 2. 反相负片帧（Negative / Color-inverted Frame）
命中帧整画面颜色反相，如照片负片，常与黑白冲击帧成对卡在节奏点上。
- **什么量级用它**：重击以上；轻碰只用局部负片（见 #6）。
- **AI提示词写法**：`0.1s full-screen color-inverted negative frame on impact`

### 3. 白闪（White Flash / White-out）
画面闪白数帧模拟瞳孔生理：闪入约 2 帧（收缩快）、闪出约 15 帧（恢复慢）。
- **什么量级用它**：爆发级、大招命中、场景转换遮罩。
- **AI提示词写法**：`white flash filling the screen for 0.15s at the moment of detonation, fading out slowly`

### 4. 黑闪（Black Flash）
与白闪相反：命中瞬间画面切纯黑，只留一道白色斩线——"收刀才知已斩"的居合美学。
- **什么量级用它**：重击~爆发；斩击系必杀专用。
- **AI提示词写法**：`the screen cuts to pure black for a split second as the blade lands, the slash visible only as a single white line`

### 5. 凝滞帧 / 时间冻结（Freeze Frame / Time Stop）
动作停在最富张力的姿势上，碎片粒子悬浮空中，只留镜头缓推或微震。
- **什么量级用它**：爆发前的悬置、终结一击命中后、逆转瞬间。
- **AI提示词写法**：`time freezes at the peak of the impact, debris suspended mid-air, locked-off camera with a subtle push-in`

### 6. 局部冲击帧（Partial Impact Frame）
只有碰撞点周围一小块区域做黑白/负片闪烁，画面其余部分保持正常。
- **什么量级用它**：轻碰专用——反馈收敛在"点"上。
- **AI提示词写法**：`a localized black-and-white impact flash only around the point of contact, the rest of the frame unchanged`

### 7. 放射冲击帧（Radiating Impact Frame）
冲击帧中从碰撞点画出放射状高反差线条，如版画般的爆闪。
- **什么量级用它**：重击。
- **AI提示词写法**：`an impact frame with high-contrast radial burst lines emanating from the collision point, woodcut style`

### 8. β闪（Beta Flash）
效果线一种：画面中央一条极亮光带向四周渐暗，表现电流/冲击的一瞬。
- **什么量级用它**：轻碰~重击；电击系技能。
- **AI提示词写法**：`a beta flash: a brilliant white band across the frame center fading to dark edges, an electric discharge`

### 9. 止め絵 / Postcard Memory（出崎统 Harmony 定格）
关键瞬间画面定格并转化为粉彩/水彩质感静止画，源自出崎统对歌舞伎"见得"的引用。
- **什么量级用它**：非打击技——高潮余韵、情感顶点、关系定音镜头（对应总纲法则 19 特写预算）。
- **AI提示词写法**：`the frame freezes and repaints itself as a pastel watercolor still, postcard-memory style`

### 10. 凝滞后碎裂（Freeze-then-Shatter）
时间冻结一拍后，被冻结的目标如玻璃般整体碎裂散开。
- **什么量级用它**：爆发；冰系/空间系终结技。
- **AI提示词写法**：`frozen in time for a beat, then the target shatters like glass in slow motion`

### 11. Umakoshi 眼（瞳孔震颤预兆）
马越嘉彦式极端眼部特写：致命一击出手前毫秒级，瞳孔高频颤动 + 侵略性粗粝阴影。杀气先于动作到达。
- **什么量级用它**：杀招出手前的预告帧，不占打击本身（与总纲法则 35 对接）。
- **AI提示词写法**：`extreme close-up of a trembling pupil with aggressive rough shadows, a split second before the killing blow`

### 12. 冲击余白（Overexposed Hold）
白闪之后画面保持轻微过曝数帧，世界像被"漂掉一层色"，再缓缓恢复正常。
- **什么量级用它**：爆发级余波段。
- **AI提示词写法**：`after the white flash, the scene holds slightly overexposed for a few frames, colors slowly returning`

### 13. 跳帧 / 抽帧（Frame Skip）
命中瞬间抽掉 2-3 帧，动作"瞬移"到位，制造超越肉眼的速度感。
- **什么量级用它**：轻碰 0.05s 跳帧、重击 0.1s 跳帧（总纲法则 27 剪辑处理）。
- **AI提示词写法**：`frames dropped at the moment of impact, the strike teleporting to its target, snappy limited-animation feel`

### 14. 漫画静止帧（Tome-e / Held Pose）
动作突然停在招牌姿势上，背景换成速度线或纯色，人物不动数秒。
- **什么量级用它**：登场亮相、喊招式名的顿点、终结定格。
- **AI提示词写法**：`the character holding the finishing pose completely still while speed lines streak behind, manga tome-e style`

---

## 二、速度表现类（速度线 / 残影 / 涂抹帧 / 背景流动）

### 15. 集中线（Concentration Lines）
从画面四边向焦点收束的细线群，把视线钉在一点上。
- **什么量级用它**：蓄力、对峙、发现真相——任何"看这里"的瞬间。
- **AI提示词写法**：`concentration lines converging toward the focal point, manga focus lines`

### 16. 平行速度线（Parallel Speed Lines）
与运动方向平行的均匀线条流，表现高速直线位移。
- **什么量级用它**：冲刺、飞行、突进全程。
- **AI提示词写法**：`parallel speed lines streaming horizontally, the character dashing at high velocity`

### 17. 放射线（Radiating Burst Lines）
从角色身后向外放射的亮色线条，表现喜悦/气势/华丽登场。
- **什么量级用它**：情绪高光、变身完成、喜剧高光。
- **AI提示词写法**：`bright radiating lines bursting outward behind the character, triumphant reveal`

### 18. 阴り线 / Odoro 线（Gloom Lines）
竖直下垂的暗色线群挂在角色头顶，表现不安、沮丧、被吐槽后的低落。
- **什么量级用它**：喜剧低落、反派阴郁氛围。
- **AI提示词写法**：`dark vertical gloom lines hanging over the character's head, oppressive mood lines`

### 19. 纵向冲击线（Vertical Shock Lines）
画面整体竖向密线快速扫过，表现震惊恐惧时的"血压上冲"。
- **什么量级用它**：震惊、恐惧、怒气冲顶。
- **AI提示词写法**：`vertical shock lines rushing across the frame, the character frozen in disbelief`

### 20. 上升线（Rising Lines）
线条自下而上流动，表现斗气/能量升腾。
- **什么量级用它**：蓄力、觉醒、气场全开。
- **AI提示词写法**：`rising effect lines flowing upward around the character as energy builds`

### 21. 揺れ线（Trembling Lines）
背景效果线高频微颤，配合画面震动表现"大地在抖"。
- **什么量级用它**：巨物逼近、爆炸持续段。
- **AI提示词写法**：`trembling background effect lines vibrating with the continuous rumble`

### 22. 背景流动（Background Streaking / 背景流し）
角色保持清晰，背景拉成水平色带长条纹——赛璐珞时代的跑步签名。
- **什么量级用它**：奔跑、追逐、长距离位移。
- **AI提示词写法**：`the background streaked into horizontal color bands, the character running sharp in the foreground, anime background-flow style`

### 23. 拉长涂抹帧（Elongated Smear Frame）
中间帧把肢体/武器沿运动轨迹拉成橡皮状长条：单帧看荒谬、连放极流畅。
- **什么量级用它**：一切快速挥击的中间帧。
- **AI提示词写法**：`an elongated smear frame, the arm stretched along the swing arc, rubbery motion-blur anatomy`

### 24. 多重影涂抹帧（Multiples Smear）
中间帧里同一肢体复制出 2-3 个半透明残影沿轨迹排列。
- **什么量级用它**：连续快攻、踢击连段。
- **AI提示词写法**：`a smear frame with multiple ghosted copies of the fist along the punch trajectory`

### 25. 干刷涂抹帧（Dry-brush Smear）
涂抹帧用干笔刷质感呈现，笔触断裂飞白，自带力量纹理。
- **什么量级用它**：重击挥击、和风/毛笔风格作品。
- **AI提示词写法**：`a dry-brush smear frame, a jagged brush-stroke motion trail with rough bristle texture`

### 26. 残像（Afterimage / Zanzō）
高速移动后原位置留下一个短暂不消失的"壳"，真身已在别处。
- **什么量级用它**：瞬步、极速闪避、以快打快。
- **AI提示词写法**：`an afterimage lingering where the fighter stood a moment ago, the real body already gone`

### 27. 方向性运动模糊（Directional Motion Blur）
模糊严格沿运动方向拉伸，模糊方向 = 力的方向。忌用全屏径向模糊充数。
- **什么量级用它**：所有快速运动部件（拳、刀、脚）的通用法则。
- **AI提示词写法**：`directional motion blur strictly along the swing vector, no radial blur`

### 28. 剪影化对冲（Silhouette Pass）
两人对冲交错瞬间切为纯色背景上的黑色剪影，只留刀光一线。
- **什么量级用它**：交错斩、决胜一合。
- **AI提示词写法**：`both fighters rendered as black silhouettes against a flat red void as they pass each other, a single white slash line`

---

## 三、爆炸类

### 29. 金田系爆炸（Kanada-style Explosion）
金田伊功开创：刺眼闪光起手、不对称飞溅、碎片带夸张透视，配金田光晕。
- **什么量级用它**：重击~爆发；能量弹命中、炮台轰击。
- **AI提示词写法**：`Kanada-style explosion: a blinding initial flash, asymmetrical flying debris with exaggerated perspective, a backlight halo`

### 30. 金田龙 / 绳状火焰（Rope Flame）
火焰拉成粗绳状蜿蜒扑出，如活物扭动——金田系签名火龙。
- **什么量级用它**：火系大招、龙形能量。
- **AI提示词写法**：`a rope-like flame serpent twisting through the air, Kanada-dragon fire with a thick undulating body`

### 31. 吉成爆炸（Yoshinari Explosion）
吉成曜签名：流线型笔触、胶状质感爆团，烟触手朝八方伸出并二次爆炸，大量碎片。
- **什么量级用它**：爆发级主爆炸。
- **AI提示词写法**：`Yoshinari-style explosion: streamlined brushstrokes, a gelatinous fireball, smoke tendrils reaching in all directions before detonating secondary blasts`

### 32. 桥本敬史爆炸（Hashimoto Explosion）
圆泡泡状爆团层层膨胀、爆炸内部再生爆炸；色彩按亮黄→橙→红→深褐渐变暗示温度层级。
- **什么量级用它**：爆发级；体积感与写实感最强的一种。
- **AI提示词写法**：`Hashimoto-style explosion: nested spherical blast bubbles expanding, a color gradient from bright-yellow core through orange and red to dark-brown smoke`

### 33. 板野马戏团（Itano Circus）
板野一郎签名：导弹群拖着螺旋烟轨以不规则轨迹缠绕穿梭，目标高速回避其间。源自他绑火箭烟花骑摩托的体验。
- **什么量级用它**：弹幕战、空战、火力覆盖——是"群"而非单发。
- **AI提示词写法**：`Itano circus: dozens of missiles with spiraling smoke trails weaving unpredictable interlaced paths around a dodging target`

### 34. EVA 十字架爆炸（Cross-shaped Blast）
爆炸收束成巨大十字形光柱冲天，庵野秀明签名式收场（纯视觉选择，无宗教含义）。
- **什么量级用它**：爆发级终结、巨物级目标消灭。
- **AI提示词写法**：`a towering cross-shaped pillar of light rising from the explosion into the sky, Evangelion-style blast`

### 35. 柱状爆（Fire Pillar / Geyser Blast）
爆炸不横向扩散而垂直冲天，形成火柱/光柱。
- **什么量级用它**：地下能量喷发、蓄力垂直释放。
- **AI提示词写法**：`a vertical pillar of fire erupting skyward from the point of impact`

### 36. 地面连环爆（Advancing Ground Detonations）
爆炸沿直线逐个向前接力炸开，追咬逃跑的目标。
- **什么量级用它**：压制段火力追击。
- **AI提示词写法**：`a chain of explosions detonating one after another, advancing across the ground toward the fleeing target`

### 37. 球状膨胀爆（Expanding Sphere）
能量先缩成奇点小球，再均匀膨胀成完美球体吞没一切，边缘带环形冲击波。
- **什么量级用它**：爆发级、地图炮级技能。
- **AI提示词写法**：`energy collapsing into a pinpoint, then expanding into a perfect glowing sphere engulfing the area, a ring shockwave at its edge`

### 38. 内爆（Implosion）
周围物质与光线先被吸入中心，静默一瞬后才放出冲击。
- **什么量级用它**：爆发前的"吸气"段；重力系技能。
- **AI提示词写法**：`an implosion: debris and light sucked inward toward the core, a beat of silence before the burst`

### 39. 爆炸真空回流（Backdraft Recoil）
爆后火焰一缩，浓烟被负压倒卷回爆心再二次喷出。
- **什么量级用它**：爆发级余波的真实感增强。
- **AI提示词写法**：`after the blast the flames recoil and the smoke is sucked back toward the core before billowing out again`

### 40. 触手二次爆（Secondary Detonations）
主爆的烟触手末端逐个再炸开小爆团，拉长爆炸的观赏时长（常配吉成爆炸）。
- **什么量级用它**：爆发级。
- **AI提示词写法**：`secondary explosions popping along the tips of the smoke tendrils after the main blast`

---

## 四、烟尘类

### 41. 尘环（Dust Ring）
冲击点贴地炸开一圈整齐的白色尘环，快速外扩。
- **什么量级用它**：重击落地、落点标记。
- **AI提示词写法**：`a clean ring of dust blasting outward along the ground from the impact point`

### 42. 拖尾烟（Smoke Trail）
高速物体身后拖出锥形烟迹，头部亮、尾部散。
- **什么量级用它**：飞行道具、突进、导弹。
- **AI提示词写法**：`a tapered smoke trail behind the projectile, bright at the head, dissipating at the tail`

### 43. 翻滚尘云（Billowing Dust Cloud）
大体积尘云缓慢翻滚升腾，内部有涡流结构，遮光压暗全场。
- **什么量级用它**：建筑倒塌、爆炸余波、巨物落地。
- **AI提示词写法**：`a massive billowing dust cloud with internal churning vortices, slowly rising and blocking the light`

### 44. 烟触手（Smoke Tendrils）
烟不呈球状而伸出多条蜿蜒触手——吉成爆炸的核心组件。
- **什么量级用它**：爆发级主烟。
- **AI提示词写法**：`smoke tendrils snaking outward in multiple directions from the blast`

### 45. 贴地尘毯（Ground-hugging Dust Sheet）
尘流贴地如毯铺开横扫，吹过脚踝与碎石。
- **什么量级用它**：冲击波过境、落地滑行。
- **AI提示词写法**：`a sheet of dust hugging the ground and sweeping past rocks and debris`

### 46. 蒸汽喷发（Steam Vent Burst）
高压蒸汽从裂缝/机体喷口斜向喷出，白浓且快。
- **什么量级用它**：巨物受伤、机体过载、水汽系技能。
- **AI提示词写法**：`high-pressure steam bursting diagonally from cracks, dense white jets`

### 47. 烟中剪影（Silhouette in Smoke）
烟尘未散，对手的身影先在烟里显形——只看得见轮廓与发亮的眼睛。
- **什么量级用它**：逆转段揭示、"还没完"瞬间。
- **AI提示词写法**：`a silhouette emerging inside the smoke cloud, only the outline and glowing eyes visible`

### 48. 尘柱（Dust Pillar）
重物垂直砸地激起上冲的柱状尘烟，比爆云矮胖、速度慢。
- **什么量级用它**：巨物跺踏、坠落砸地。
- **AI提示词写法**：`a thick pillar of dust punching upward where the mass slammed into the ground`

### 49. 冲击吹烟（Shockwave Clearing Smoke）
第二波冲击把满屏烟尘瞬间吹出一个干净圆洞，露出中心人物。
- **什么量级用它**：揭示镜头、强者登场。
- **AI提示词写法**：`a shockwave blowing the smoke screen open in a clean circle, revealing the figure at the center`

### 50. 落尘雨（Falling Dust Rain）
大冲击后细碎粉尘如慢雨持续下落数秒，逆光可见。
- **什么量级用它**：一切大冲击的收尾环境层。
- **AI提示词写法**：`fine dust sifting down like slow rain in the aftermath, visible in the backlight`

---

## 五、光效类

### 51. 金田光（Kanada Light / 逆光光晕）
强逆光把角色压成剪影，轮廓外溢出耀眼光晕，配圆圈与十字闪光。
- **什么量级用它**：强者登场、爆发起手。
- **AI提示词写法**：`Kanada light: the character backlit into silhouette, a halo flaring around the outline, circle and cross sparkles`

### 52. 十字闪光（Cross Sparkle / キラリ）
四点星芒十字闪光，贴在刀刃/眼睛/宝石的高光点上。
- **什么量级用它**：点缀级；拔刀、眼神、宝物揭示。
- **AI提示词写法**：`a four-point cross sparkle flashing on the blade's edge`

### 53. 体积光（Volumetric God Rays）
光穿过烟尘/树林形成可见光柱，给场景"空气厚度"。
- **什么量级用它**：氛围层；遗迹、森林、爆后现场。
- **AI提示词写法**：`volumetric god rays cutting through the dust-filled air`

### 54. 边缘光（Rim Light）
逆光在角色边缘勾一圈亮轮廓线，把人从背景中剥离。
- **什么量级用它**：对峙、剪影揭示、夜战。
- **AI提示词写法**：`strong rim light tracing the character's outline against the dark background`

### 55. Bloom 泛光溢出（Bloom Overexposure）
高亮区域向四周溢出柔光，能量越强溢出越大。
- **什么量级用它**：爆发级、能量体接触。
- **AI提示词写法**：`intense bloom, the energy core's light bleeding softly into the surrounding frame`

### 56. 光尾 / 光轨（Light Trail）
高速能量体/武器拖出发光轨迹，数帧后衰减。
- **什么量级用它**：斩击、飞行道具、瞬步路径。
- **AI提示词写法**：`a glowing light trail following the blade's arc, fading over several frames`

### 57. 电弧缠绕（Electric Arcs）
不规则分叉电弧在掌心/武器/全身缠绕跳动，配高频闪烁。
- **什么量级用它**：雷系技能全级。
- **AI提示词写法**：`forked electric arcs crackling and crawling around the clenched fist`

### 58. 雷纹光珠（Lightning-vein Orb）
能量球内部布满雷电枝状纹路，表面有环带旋转。
- **什么量级用它**：蓄力弹、雷系大招。
- **AI提示词写法**：`an orb with branching lightning veins inside, rotating energy bands around its surface`

### 59. 光弹彗尾（Comet-tail Projectile）
光弹出膛后拖彗星状尾迹，尾迹里符文/粒子一闪即灭。
- **什么量级用它**：法系普攻~大招。
- **AI提示词写法**：`a glowing projectile with a comet tail, runic sparks blinking out along the trail`

### 60. 法阵分层点亮（Layered Circle Ignition）
外环符箓逆旋、中环星轨正旋、内环卦象依次点亮——召唤阵的"解剖学"写法（对接总纲法则 23）。
- **什么量级用它**：法系蓄力、召唤、结界展开。
- **AI提示词写法**：`a layered magic circle: the outer rune ring rotating counter-clockwise, the middle star-track ring clockwise, inner sigils igniting one by one`

### 61. 蜂巢屏障纹格（Honeycomb Barrier Cells）
屏障受击处逐格点亮蜂巢纹格，过载的格子变白碎裂。
- **什么量级用它**：法系防御、结界承压。
- **AI提示词写法**：`a honeycomb-patterned barrier, hexagonal cells lighting up around the impact point, overloaded cells turning white`

### 62. 全帧辉光脉冲（Full-frame Glow Pulse）
整个画面随能量节奏做一次"呼吸"式明暗。
- **什么量级用它**：心跳节拍、蓄力节点、领域展开。
- **AI提示词写法**：`the whole frame pulsing with a breathing glow, brightening and dimming with the energy's rhythm`

### 63. 逆光爆发剪影（Backlit Burst Silhouette）
光源从角色身后炸开，角色全黑剪影，光芒从轮廓后扇形喷出。
- **什么量级用它**：觉醒、变身完成、登场。
- **AI提示词写法**：`the character in full black silhouette as light bursts fan out from behind their outline`

### 64. 色温对冲（Color-temperature Clash）
双方能量用冷暖色温区分（青蓝 vs 橙红），对冲处产生白炽交界线。
- **什么量级用它**：双人技能对轰、合体技。
- **AI提示词写法**：`cold-blue energy clashing against warm-orange energy, a white-hot seam where the two fronts meet`

---

## 六、破碎类

### 65. 中村方块（Yutapon Cubes）
中村丰签名（源自宇都宫理）：地面/建筑碎块画成几何立方体翻滚，各自受光——破坏因此有了"质量"（对接总纲法则 34）。
- **什么量级用它**：一切地面爆裂、墙体粉碎。
- **AI提示词写法**：`debris rendered as geometric cubes tumbling with weight, each catching the light, Yutapon cubes`

### 66. 玻璃质碎裂（Glass Shatter）
透明/结晶体沿放射纹裂开后炸成慢镜碎片，碎片映出环境反光。
- **什么量级用它**：冰、结界、镜面空间。
- **AI提示词写法**：`shattering like glass: radial cracks, then slow-motion shards reflecting the surroundings`

### 67. 地面放射龟裂（Radial Ground Cracking）
以落点为圆心的放射状裂缝蔓延，裂缝内透出能量光。
- **什么量级用它**：重击落地、蓄力踩地。
- **AI提示词写法**：`the ground cracking in a radial pattern from the impact point, energy light glowing inside the fissures`

### 68. 碎片分层（Debris Size Layering）
大碎块慢速翻滚、小碎屑高速飞散、粉尘最后落地——用碎片尺寸卖时间尺度（总纲法则 28）。
- **什么量级用它**：一切破碎镜头的真实感法则。
- **AI提示词写法**：`layered debris: large chunks tumbling slowly, small fragments scattering fast, dust settling last`

### 69. 悬浮碎石（Levitating Rubble）
能量场让碎石违反重力缓缓浮起，环身旋转。
- **什么量级用它**：觉醒、超能力全开、大招蓄力。
- **AI提示词写法**：`rubble levitating off the ground, orbiting slowly around the charging figure`

### 70. 慢镜碎片横穿（Slow-mo Shard Flyby）
碎片贴着镜头慢速飞过，景深极浅，背景动作仍在进行。
- **什么量级用它**：爆发中的"子弹时间"观赏窗。
- **AI提示词写法**：`slow-motion shards drifting past the lens in shallow focus, the battle still raging behind`

### 71. 屏障碎作萤火（Barrier-to-Fireflies Dissolve）
屏障碎裂后碎片不落地，化为发光萤火升空熄灭——消散美学（总纲法则 26）。
- **什么量级用它**：法系防御告破的余韵。
- **AI提示词写法**：`the shattered barrier fragments dissolving into glowing fireflies that rise and blink out`

### 72. 武器断裂特写（Blade Break Insert）
刀刃崩断瞬间的插入特写：裂纹爬升→断口→断片旋转飞出。
- **什么量级用它**：资源见底信号、王牌删除（总纲法则 8）。
- **AI提示词写法**：`insert close-up: a crack racing up the blade, the tip snapping off and spinning away in slow motion`

### 73. 冰晶生长后碎裂（Ice Bloom Shatter）
冰面先生长出霜花纹样，再整体爆碎——"先美后破"。
- **什么量级用它**：冰系技能命中。
- **AI提示词写法**：`frost patterns blooming across the surface before the whole structure bursts into ice shards`

### 74. 空间镜面碎裂（Space Shatter）
空气/空间本身如镜面出现裂痕并剥落，露出背后虚空。
- **什么量级用它**：顶级大招、维度级技能。
- **AI提示词写法**：`space itself cracking like a mirror, shards of the sky peeling away to reveal the void behind`

---

## 七、液体类

### 75. 吉卜力果冻水（Ghibli Jelly Water）
水块呈果冻状弹性变形，情绪优先于物理，形变夸张而可爱。
- **什么量级用它**：日常/情感场景的水、喜剧泼溅。
- **AI提示词写法**：`Ghibli-style jelly water, blobs deforming elastically with playful exaggeration`

### 76. 浮世绘浪头（Hokusai Wave / 水之呼吸）
水流画成浮世绘式卷曲浪头与飞沫——《鬼灭之刃》水之呼吸签名视效（对接总纲法则 37 元素即角色）。
- **什么量级用它**：水系剑技全段。
- **AI提示词写法**：`water rendered as Hokusai-style curling waves with stylized foam, flowing along the sword's path`

### 77. 水花皇冠（Splash Crown）
重物落水激起皇冠状对称水幕，顶部抛出大颗水珠。
- **什么量级用它**：坠落入水、拳砸水面。
- **AI提示词写法**：`a symmetrical crown-shaped splash with large droplets thrown from its rim`

### 78. 液体抛物线（Liquid Arc）
液体（酒/汗/药液）甩出成一条完整抛物线，线体分节断裂成珠。
- **什么量级用它**：动作点缀、喜剧泼洒。
- **AI提示词写法**：`a liquid arcing through the air, the stream breaking into segmented beads`

### 79. 水面涟漪（Ripple Spread）
平静水面以触点为中心荡开同心圆涟漪，倒映随之破碎。
- **什么量级用它**：安静张力镜头、落物入水。
- **AI提示词写法**：`concentric ripples spreading across the still water, the reflection breaking apart`

### 80. 重到疼的雨（Totoro Rain）
宫崎骏式大雨：雨滴粗线化、砸在物体上弹起有力——《龙猫》式"重到疼"的雨。
- **什么量级用它**：暴雨战、情绪低谷的环境压力。
- **AI提示词写法**：`heavy rain with thick droplet streaks bouncing hard off surfaces, rain so heavy it looks painful`

### 81. 新海诚雨滴折射（Shinkai Raindrop Refraction）
每颗雨滴内折射出翻转的背景街景与绿意，色匹配精细——《言叶之庭》式。
- **什么量级用它**：雨天抒情、独白场景。
- **AI提示词写法**：`macro raindrops each refracting an inverted miniature of the background, Shinkai-style rain`

### 82. 未落地之雨（Virga）
雨在半空蒸发成斜挂的灰色纱幕，落不到地面——《天气之子》开场。
- **什么量级用它**：压抑氛围、悬念铺陈。
- **AI提示词写法**：`virga: rain evaporating mid-air into slanted grey curtains that never reach the ground`

### 83. 水下气泡柱（Underwater Bubble Column）
水下视角气泡成群上升，随深度变大变快，光束从水面射下。
- **什么量级用它**：落水、水战、沉没。
- **AI提示词写法**：`underwater view, columns of bubbles rising and expanding toward the light filtering from the surface`

### 84. 粘液拉丝（Viscous Strands）
粘稠液体拉出细长不断裂的丝，回弹收缩。
- **什么量级用它**：黏液系怪物、炼金/毒系技能。
- **AI提示词写法**：`viscous fluid stretching into long glistening strands that snap back`

### 85. 汗珠飞溅（Sweat Bead Spray）
急停/受击瞬间汗珠从发梢甩出细小抛物线，逆光发亮——"人体级"受力反馈。
- **什么量级用它**：轻碰~重击；努力可视化。
- **AI提示词写法**：`sweat beads flicking off the hair tips in tiny backlit arcs as the fighter halts`

---

## 八、天气 / 环境类

### 86. 风压压弯（Wind-pressure Bend）
能量过境时草木/旗帜/衣物统一朝风向压弯，弯曲力度 = 能量量级（总纲法则 25）。
- **什么量级用它**：一切能量释放的环境反馈。
- **AI提示词写法**：`grass and banners bending flat under the wind pressure of the passing energy`

### 87. 落叶 / 樱吹雪卷入（Leaf or Petal Spiral）
气流卷起落叶/花瓣绕战场螺旋，美与杀气同屏。
- **什么量级用它**：对峙前静场、剑技余韵。
- **AI提示词写法**：`fallen leaves spiraling up in the wind vortex between the two motionless duelists`

### 88. 逆重力雪升（Snow Rising Upward）
能量场让地面积雪/尘埃缓缓向上升起。
- **什么量级用它**：觉醒、领域展开。
- **AI提示词写法**：`snow lifting off the ground and drifting upward as the energy field expands`

### 89. 空气热扭曲（Heat Haze Distortion）
高温区域上方空气产生折射抖动，景物如水下般晃动。
- **什么量级用它**：火系技能、爆后现场、沙漠。
- **AI提示词写法**：`heat haze shimmering above the scorched ground, the background wavering`

### 90. 空气涟漪（Air Ripple / Shockwave Distortion）
冲击波经过处空气如水面般产生一圈透明折射涟漪。
- **什么量级用它**：重拳、音爆、屏障受击。
- **AI提示词写法**：`a transparent ripple of distorted air expanding outward from the punch`

### 91. 天变（Sky Turn / Cloud Vortex）
大招蓄力时乌云向头顶漩涡汇聚、天色骤变。
- **什么量级用它**：禁咒级蓄力的环境宣告。
- **AI提示词写法**：`storm clouds spiraling into a vortex overhead as the spell charges, daylight dimming`

### 92. 闪电背景定格（Lightning Flash Freeze）
惊雷炸响瞬间画面变负片质感一帧，人物剪影被闪电"钉"在天幕上。
- **什么量级用它**：登场、揭示、逆转宣告。
- **AI提示词写法**：`a lightning flash freezing the character's silhouette against the night sky, one inverted-color frame`

### 93. 雨幕剪影战（Rain-curtain Silhouette Duel）
密雨成幕，两人在雨帘中仅以剪影交锋，刀光劈开雨线。
- **什么量级用它**：夜战高潮、肃杀氛围。
- **AI提示词写法**：`duelists as silhouettes inside a curtain of heavy rain, blade flashes slicing the rain lines`

### 94. 冲散云层（Cloud-splitting Shockwave）
冲天能量把整层云吹出一个巨洞，阳光从洞中直射而下——"天地作证"。
- **什么量级用它**：爆发级终结技的余波。
- **AI提示词写法**：`the ascending blast punching a vast hole through the cloud layer, sunlight spearing down through the gap`

### 95. 气压凹陷（Pressure Crater）
未到实体命中，单是气场就把脚下地面压出圆形浅坑、尘土环状排出。
- **什么量级用它**：强者落地、气场展示。
- **AI提示词写法**：`the ground dishing into a shallow crater under pure pressure, dust pushed out in a ring`

---

## 九、变形 / 异化类

### 96. Obari 强制透视（Obari Pose）
大张正己签名（福田己津央命名）：武器/拳头用极端强制透视直指镜头，近端巨大变形——一帧的解剖失真换最大速度压迫（对接总纲法则 36）。
- **什么量级用它**：高潮定格、必杀起手。
- **AI提示词写法**：`extreme forced perspective, the blade lunging directly at camera, foreground massively enlarged, Obari pose`

### 97. 金田透视（Kanada Perspective）
人物整体透视夸张扭曲（手大脚小、地平线弯斜），服务动势而非解剖。
- **什么量级用它**：高速突进、挥击 pose 帧。
- **AI提示词写法**：`Kanada-style exaggerated warped perspective, the reaching hand oversized, the horizon tilted with the motion`

### 98. 受击形变（Impact Deformation）
被打部位在命中帧产生夸张的挤压/凹陷形变，下一帧回弹。
- **什么量级用它**：喜剧重击、橡胶体质、夸张打斗。
- **AI提示词写法**：`the cheek squashing with exaggerated deformation on the impact frame, snapping back the next`

### 99. 颜艺崩坏（Face Deformation）
五官位移错位、线条崩坏化的极端表情帧。
- **什么量级用它**：震惊、狂气、喜剧崩溃。
- **AI提示词写法**：`an off-model exaggerated face, features displaced in a wild expression, expressive line chaos`

### 100. BLACK 影 / 纯黑化（Black Fill）
金田系手法：角色全身填纯黑只留白眼白牙，背景保持正常。
- **什么量级用它**：杀气外放、黑化、威压。
- **AI提示词写法**：`the character filled in solid black with only white eyes and teeth visible, BLACK silhouette`

### 101. 线稿化（Rough Line-art Frame）
极限瞬间角色变成潦草铅笔线稿，轮廓狂草抖动——刻意的"作画崩坏"演出。
- **什么量级用它**：极限状态、情绪顶点的单帧。
- **AI提示词写法**：`the figure rendered as rough scratchy pencil line-art for a single frame at peak intensity`

### 102. 色彩抽离（Desaturation Drain）
世界褪色成灰阶，只有某一点（能量/眼睛/信物）保留颜色。
- **什么量级用它**：死亡逼近、时间停止、异能领域。
- **AI提示词写法**：`the world draining to grayscale except for the glowing crimson energy at the center`

---

## 十、能量 / 蓄力类

### 103. 气焰缠身（Aura Flame）
能量如火焰从全身向上窜起，轮廓波浪抖动，碎石浮起——龙珠式气场可视化。
- **什么量级用它**：变身、蓄力、怒意解放。
- **AI提示词写法**：`a flame-like aura surging upward around the whole body, the outline wavering, pebbles rising`

### 104. 集气光球（Charge-up Orb）
双手/掌心间光球由小到大聚集，周围能量呈流线被吸入球体。
- **什么量级用它**：波系大招蓄力段。
- **AI提示词写法**：`an orb swelling between the palms, energy streams being drawn into it from the surroundings`

### 105. 能量波纹扩散（Energy Pulse Rings）
从身体中心一圈圈放出半透明能量环，扫过全场。
- **什么量级用它**：威压、探测、领域宣告。
- **AI提示词写法**：`translucent energy rings pulsing outward from the body, sweeping across the battlefield`

### 106. 粒子汇聚吸入（Particle Inhalation）
环境光粒/萤火从四面八方被吸向蓄力点，逆流成河——大招的"吸气"段。
- **什么量级用它**：大招蓄力前段。
- **AI提示词写法**：`ambient light particles streaming inward from all directions toward the charging point`

### 107. 符阵踏亮（Ground Sigil Ignition）
落脚/落掌处地面符阵纹路逐段亮起并向外蔓延。
- **什么量级用它**：结界、召唤、阵地系技能。
- **AI提示词写法**：`glowing sigil lines igniting outward across the ground from the point of contact`

### 108. 音爆环（Sonic Boom Ring / Vapor Cone）
突破音障瞬间身周炸开一圈白色锥形云雾环。
- **什么量级用它**：超音速突进、冲刺起手。
- **AI提示词写法**：`a white vapor-cone ring bursting around the body as it breaks the sound barrier`

---

## 十一、声音视觉化类

### 109. 拟声词具象（Onomatopoeia Kana）
巨大描边拟声字（ドン/ゴゴゴ）作为画面元素砸进构图。
- **什么量级用它**：漫画式演出、喜剧重音、JOJO 式压迫。
- **AI提示词写法**：`giant outlined onomatopoeia characters slamming into the composition, manga sound-effect typography`

### 110. 声波环（Visible Sound Rings）
吼声/钟声以同心圆环从声源扩散，环经过处画面微扭。
- **什么量级用它**：咆哮、钟鸣、音波攻击。
- **AI提示词写法**：`concentric sound rings radiating from the roar, the frame warping slightly as each ring passes`

### 111. 静音帧（The Silent Cut）
最大爆炸的瞬间抽掉所有声音，画面只剩慢动作与漂浮碎片——用"无声"卖"至响"。
- **什么量级用它**：爆发级最高点的反高潮处理。
- **AI提示词写法**：`the moment of the biggest explosion playing in total silence, slow-motion debris drifting, muted impact`

### 112. 心跳缩放脉冲（Heartbeat Frame Pulse）
画面随心跳节奏做两次轻微缩放（咚-咚），视野边缘压暗。
- **什么量级用它**：濒死、极限专注、战前紧张。
- **AI提示词写法**：`the frame pulsing twice with a heartbeat rhythm, the edges vignetting darker with each beat`

### 113. 耳鸣白噪（Tinnitus White-noise Grain）
巨响后画面覆上细密白噪颗粒、高频颤抖，模拟耳鸣。
- **什么量级用它**：爆炸后主观视角、脑震荡体验。
- **AI提示词写法**：`fine white-noise grain and a high-frequency tremble over the frame, post-blast tinnitus POV`

### 114. 低频震动波纹（Bass Rumble Distortion）
整个画面以低频率做小幅波浪式起伏，表现次声波级的压迫。
- **什么量级用它**：巨物逼近、大地震怒。
- **AI提示词写法**：`the whole frame undulating in low-frequency waves, as if warped by an infrasonic rumble`

---

## 十二、坍塌·崩落类

### 115. 建筑整体崩塌分层（Collapsing Structure Layering）
整栋建筑垮塌时按重量分层：深色重块在前缓慢弧线抛落，小碎屑在后高速散射，苍白尘云翻卷吞没残骸——比 #68 更宏观的"整栋"尺度。出处：桥本敬史破坏作画。
- **什么量级用它**：爆发级；建筑/城墙整体垮塌。
- **AI提示词写法**：`a collapsing building bursts into layered debris: heavy dark fragments arcing slowly in front, smaller shards scattering behind, thick pale dust clouds billowing outward and swallowing the wreckage`

### 116. 尘浪推进（Advancing Dust Wave）
大块结构落地后，灰褐色尘墙贴地向镜头方向翻滚推进，吞掉沿途树木与瓦砾，能见度归零。
- **什么量级用它**：重击~爆发；崩塌余波、巨物落地、追逐中切断视线。
- **AI提示词写法**：`a massive wall of gray-brown dust rolling toward the camera across the ground, swallowing trees and rubble, debris silhouettes tumbling inside the cloud, visibility dropping to near zero`

### 117. 巨石滚落追击（Rolling Boulder Pursuit）
巨石弹跳着滚向镜头，反复充满整个画幅再露出前方奔逃的人影，路径上泥土木屑飞溅——用"遮挡-显露"节奏制造追逐紧张。
- **什么量级用它**：重击；陷阱逃生、山道追猎、滚石机关。
- **AI提示词写法**：`a giant boulder rolling downhill toward the camera, bouncing and crushing trees, repeatedly filling the entire frame then revealing the fleeing figure ahead, dirt and splinters spraying from its path`

### 118. 逐级崩解（Progressive Tier Collapse）
高塔/城堡自下而上一层一层剥落，每层碎成方块滑落，各层腾起尘环，连续向下传递瓦解——《天空之城》拉普达式崩解。
- **什么量级用它**：爆发级；高塔、浮空城、巨像瓦解的收尾镜头。
- **AI提示词写法**：`an ancient stone tower collapsing tier by tier from bottom to top, each floor crumbling into blocks that slide off and fall, dust rings erupting at every level in continuous downward motion`

---

## 十三、变身·觉醒类

### 119. 光柱三段式 Bank（Magical Girl Bank）
经典变身序列骨架：道具高举→光柱自脚下升起吞没全身、人悬浮成发光剪影；缎带/光流绕体螺旋、逐段凝成服装（手套→靴→裙）；光散，头冠/额饰最后显形，定格 pose。
- **什么量级用它**：变身登场、形态切换的仪式镜头。
- **AI提示词写法**：`a girl levitating inside a vertical column of pink-white light rising from glowing geometric patterns on the ground, glowing ribbons spiraling around her silhouette and solidifying into gloves, boots and a dress piece by piece, a tiara materializing last on her forehead, hair and ribbons drifting weightless`

### 120. 爆气型觉醒（Aura Eruption）
低头蓄力全身震颤→气焰自体表窜起成柱冲天、头发倒竖变色、瞳色改变→冲击波外推、脚下环形坑成形。《龙珠》超赛谱系。
- **什么量级用它**：爆发级；战力解放、怒气觉醒。
- **AI提示词写法**：`a kneeling fighter trembling, then a golden flame aura erupting from his body shooting skyward as a vertical pillar, hair rising and turning gold, ground cracks spreading in concentric rings, small rocks levitating, a dust shockwave pushing outward, clouds splitting above`

### 121. 肉体变异型觉醒（Titan Reassembly）
金色闪电劈落强白光吞没人形→骨架先行暴长、肌肉纤维攀附增生、表皮覆合→巨躯直立、高温蒸汽自体表喷涌。《进击的巨人》变巨人谱系。
- **什么量级用它**：爆发级；巨大化、异形化觉醒。
- **AI提示词写法**：`a golden lightning bolt striking a figure, white flash engulfing the scene, a giant skeleton expanding rapidly, red muscle fibers crawling and weaving over the bones, skin sealing over, the giant standing upright as thick white steam blasts from its body, heat haze distorting the air`

### 122. 内敛型觉醒（Subtractive Awakening）
减法演出：画面静止、整体去色只剩角色微动→单一元素异变（发丝逆重力浮起/一滴汗悬停）→无声压力波掠过、颜色恢复。《灵能百分百》???% 谱系。
- **什么量级用它**：重击级铺垫；深不可测型角色的觉醒预告。
- **AI提示词写法**：`the scene desaturated to gray and frozen, a boy standing motionless while his hair slowly rises against gravity and a single sweat drop hangs in mid-air, suspended raindrops trembling, a silent pressure wave rippling outward, color flooding back into the frame`

### 123. 代价显形（Visible Cost）
觉醒与损耗同步显形：皮肤泛红/经络发亮→发梢白化蔓延、甲片龟裂剥落、血色蒸汽自毛孔喷出→定格时损耗仍在继续。对接总纲"代价显形律"。
- **什么量级用它**：爆发级觉醒的收尾帧；燃命类大招。
- **AI提示词写法**：`red steam pouring from a fighter's pores as his skin flushes and veins glow, hair whitening from the tips, armor plates cracking and flaking off his shoulders drifting to the ground, heat haze shimmering, the ground beneath his feet scorching and splitting, steam still rising`

---

## 十四、风与气流可视化（6 条）

### 124. 拳风掠伤（Punch Wind Graze）
拳/剑未命中，但脱体风压在后方墙面、地面刮出一道笔直沟痕，灰浆碎石剥落——用环境伤痕卖"这一拳的份量"。
- **什么量级用它**：重击；miss 也要给反馈的回合、展示差距的压制戏。
- **AI提示词写法**：`the punch misses, but its wind pressure carves a straight gouge across the stone wall behind, plaster and pebbles flaking off, the opponent's clothes rippling from the passing force`

### 125. 空压气环（Compressed Air Ring）
冲击点横向推出一圈厚实的白色环形压缩空气，环体卷着碎叶纸片向外飞——区别于 #41 尘环（贴地尘）与 #90 空气涟漪（透明折射），本条是"可见的实体空气甜甜圈"。
- **什么量级用它**：重击~爆发；拳脚相抵、格挡瞬间、空中对波的推力反馈。
- **AI提示词写法**：`a thick white ring of compressed air bursting horizontally from the clash point, leaves and paper scraps caught inside the ring as it expands outward, clothes flapping in its wake`

### 126. 气场落叶显形（Aura Revealed by Leaves）
地面落叶从站立的强者脚下向四面八方退开，露出以人为圆心的裸地圆——用落叶当示踪粒子，画出无形力场的边界。区别于 #86 风压压弯（单向持续）与 #87 落叶卷入（螺旋美感）。
- **什么量级用它**：重击级铺垫；强者入场、霸王色式威慑、觉醒前兆。
- **AI提示词写法**：`fallen leaves on the ground sliding away from the standing fighter in all directions, a bare circle of empty ground forming around his feet, his coat hem swaying gently in the outward wind`

### 127. 真空月牙斩（Flying Crescent Slash Wave）
挥刀放出月牙形压缩空气斩，贴地飞行路径犁开泥土草皮，末端爆散——《死神》月牙天冲 /《犬夜叉》风之伤 / Razor Wind 谱系。
- **什么量级用它**：重击~爆发；剑士远程技、隔空分胜负的一斩。
- **AI提示词写法**：`a glowing crescent of compressed air flying low across the battlefield, gouging a trench of dirt and grass along its path, splitting a boulder in half before bursting apart at the far end`

### 128. 尾流卷吸（Wake Suction）
人影高速掠过已出画，迟半拍沿途纸屑尘土才被真空走廊吸起、向移动轴线卷入——速度不画人，画"他经过之后"。区别于 #42 拖尾烟（物体本体拖烟）与残影（本体叠影）。
- **什么量级用它**：轻碰~重击；瞬步离场、超音速穿插后的余韵镜头。
- **AI提示词写法**：`the figure already gone off-screen, papers and dust belatedly sucked up into the air along his path, debris swirling inward toward the vacuum corridor he left behind, a banner still snapping`

### 129. 风暴眼静区（Calm Eye in the Storm）
碎片、雨点、尘土绕身高速螺旋，唯独以人为轴的一圈直径内无风无雨，发丝微垂、衣角静止——用"乱中之静"卖绝对压制。
- **什么量级用它**：爆发级；觉醒完成态、领域展开、boss 亮真身的定场镜头。
- **AI提示词写法**：`rain and debris spiraling violently around the fighter, but a calm cylinder of still air surrounding his body, his hair hanging motionless, not a single raindrop falling inside the circle`

---

## 十五、夜间光源设计（6 条）

### 130. 发光兵器照明（Weapon as Key Light）
夜战中发光刀刃/法器是画内唯一光源：蓝白色刀光照亮持有者半张脸与脚下地面，挥动时光斑在墙壁、盔甲上扫过，暗部保持全黑——光源随身移动，光影跟着走。区别于 #55 Bloom（整体泛光滤镜）与 #56 光尾（运动轨迹残光）：本条是"兵器当灯用"的照明逻辑。
- **什么量级用它**：重击；夜战单挑、暗巷遭遇、洞窟探索。
- **AI提示词写法**：`pitch-black night battlefield, the glowing blue blade is the only light source, its cold light illuminating the wielder's face from below and a small circle of ground, light sweeping across stone walls as the sword swings, deep shadows swallowing everything beyond reach`

### 131. 满月剪影对峙（Full Moon Backlight Silhouette）
巨大满月悬在身后，人物压成纯黑剪影，只留一圈银白轮廓光与刀刃反光一线——定场镜头用天体当背光板。区别于 #28 剪影化对冲（交错瞬间的纯色背景剪影）与 #63 逆光爆发剪影（身后爆炸扇形喷光）：本条光源是静态满月，节奏是缓慢对峙而非瞬间爆点。
- **什么量级用它**：轻碰~重击铺垫；夜战定场、高手登场、决斗开局。
- **AI提示词写法**：`a giant full moon filling the night sky, a lone swordsman standing as a solid black silhouette against it, thin silver rim light tracing his outline, one bright specular line along the katana edge, coat hem swaying slowly, deep blue night haze`

### 132. 闪光弹揭示（Flashbang Reveal）
爆炸/闪术炸开的瞬间白光吞屏，把整个夜战战场（地形、敌阵、掩体）一次性照亮如白昼，随后光迅速衰减、黑暗重新合拢只剩余烬亮点——一次照明完成一次"战场情报揭示"。区别于 #3 白闪（命中帧过曝数帧即恢复）：本条有完整的"亮起-展示-回落"三段明暗过程，功能是叙事揭示而非冲击强调。
- **什么量级用它**：重击~爆发；夜战开局亮地形、伏兵现身、大招前奏。
- **AI提示词写法**：`a flash spell detonating in the night, blinding white light instantly revealing the entire battlefield — ruined walls, scattered soldiers, a treeline — every shadow erased for a moment, then the light fading fast, darkness closing back in until only ember dots remain glowing`

### 133. 瞳孔映火（Firelight Reflected in the Eye）
眼部大特写：瞳孔表面映出橙红火球逼近的倒影，火光在瞳面上晃动变大，睫毛边缘染上暖色——观众从眼睛里"看到"即将到来的攻击。区别于 #11 Umakoshi 眼（瞳孔高频震颤卖杀气）：本条画"映像"的物理反射，不卖情绪卖画外事件。
- **什么量级用它**：重击；大招命中前的主观反应镜、同伴目睹爆炸。
- **AI提示词写法**：`extreme close-up of an eye in darkness, a bright orange fireball reflected on the pupil's surface growing larger and flickering, warm light edging the eyelashes, the reflection shaking as the fireball approaches`

### 134. 暗中发光眼（Glowing Eyes in the Dark）
画面全黑，唯有一双发光眼睛缓缓睁开或平移，瞳色冷光在黑暗中拖出微弱光晕，靠近时才隐约照亮自己的眼眶——未知威胁的最低信息量登场。区别于 #47 烟中剪影（烟尘介质中轮廓+亮眼）：本条无任何介质与轮廓，纯黑背景只有眼。
- **什么量级用它**：轻碰铺垫；夜袭预警、巨物潜伏、反派亮相当口。
- **AI提示词写法**：`total darkness, a pair of glowing golden eyes slowly opening in the black void, a faint halo of light around the pupils, the eyes drifting sideways leaving a weak glow trail, nothing else visible`

### 135. 雷电频闪照明（Lightning Strobe Illumination）
雷暴夜战：闪电一亮一灭间歇照亮战场，每次亮起的瞬间人物位置已变化（更近/倒地/刀已出鞘），灭灯期全靠脑补——用频闪节奏推进战况而非连续动作。区别于 #92 闪电背景定格（单帧负片剪影）：本条是多次频闪的环境照明节拍，画面不变负片，人物是立体受光而非剪影。
- **什么量级用它**：重击~爆发；雷雨天决斗、高速交换的回合计量、jump scare 式逼近。
- **AI提示词写法**：`a thunderstorm night duel lit only by strobing lightning — each flash freezing the two fighters at a new distance, closer with every strike, wet armor catching the brief white light, rain streaks visible only during the flashes, total darkness between bolts`

---

## 十六、声音可视化（6 条）

> 与"十一、声音视觉化类"（#108-114）互补：那组管"整画面的听觉滤镜"，本组管"声音在画内物体上留下的物理痕迹"。

### 136. 胸口鼓动（Visible Heartbeat Bulge）
心跳不画画面缩放，画身体本身：胸口衣料随"咚-咚"两下向外鼓起，纽扣绷紧，领口/衣缝随每次鼓动透出一明一灭的光——把心跳画成体内的物理冲击。区别于 #112 心跳缩放脉冲（整画面两次缩放+边缘压暗的镜头处理）：本条是角色身体上的局部形变，画面本身不动。
- **什么量级用它**：重击级铺垫；濒死硬撑、秘药副作用、变身/觉醒前兆。
- **AI提示词写法**：`close-up of a fighter's chest, the fabric over his heart bulging outward twice with a heavy thump-thump, a button straining, red light leaking and fading through the gaps of his collar with each beat, the rest of his body held still`

### 137. 音爆云斗篷（Sustained Vapor Cone Cape）
持续超音速飞行中白色锥形凝结云不散，像斗篷/裙摆一样箍在腰后随人一起飞，尾缘不断剥落水汽丝——普朗特-格劳厄脱凝结云的"巡航版"。区别于 #108 音爆环（突破音障瞬间炸开一圈即消）：本条是全程挂在身上的持续云锥。
- **什么量级用它**：重击~爆发；空中追击、全速俯冲、援军天降的在途镜头。
- **AI提示词写法**：`a figure flying at supersonic speed with a white cone of condensed cloud wrapped around his waist like a cape, the vapor collar traveling with him, wisps of moisture constantly shedding from its trailing edge, clear sky behind`

### 138. 杯中水共振纹（Rippling Cup Omen）
威胁还在画外，近景一杯水/一洼积水先泛起细密同心涟漪，一圈接一圈节奏稳定，桌面灰尘随每次震颤轻跳——用液体当"远方脚步/咆哮"的示波器。《侏罗纪公园》水杯谱系。区别于 #79 水面涟漪（物体触点为中心荡开）：本条无任何接触，震动源在画外。
- **什么量级用它**：轻碰铺垫；巨物逼近预告、boss 登场前、远处大战传来的余波。
- **AI提示词写法**：`extreme close-up of a cup of water on a table, fine concentric ripples pulsing across the surface in a steady rhythm, dust jumping off the tabletop with each tremor, nothing touching the water, the approaching threat still unseen`

### 139. 高音共振碎玻璃（Resonance Glass Shatter）
持续高音/尖啸下，整面玻璃先高频微颤、表面泛出细密同心光纹，裂纹顺纹路爬成蛛网，随后无接触整体崩碎——"声音自己打碎物体"，碎前有"颤-纹-裂"三段前摇。区别于 #66 玻璃质碎裂（受击点碎裂）与 #10 凝滞后碎裂（冻结后碎）：本条驱动力是声压共振，无任何碰撞。
- **什么量级用它**：重击；歌姬/尖啸系攻击、音波兵器、巨物咆哮的环境反馈。
- **AI提示词写法**：`a wall of glass windows trembling at high frequency under a sustained piercing note, fine concentric patterns shimmering on the panes, cracks crawling along the patterns into a spiderweb, then the whole glass wall bursting inward without anything touching it`

### 140. 克拉德尼沙纹（Cymatics Sand Pattern）
低频吼声/轰鸣中，石板上的沙尘不飞扬，反而随震动跳动迁移，自动排成同心环与几何驻波图形——驻波波节把沙"钉"成图案（克拉德尼图形）。区别于 #114 低频震动波纹（整画面波浪起伏的镜头滤镜）：本条是画内物理粒子的真实迁移排布，镜头稳定。
- **什么量级用它**：重击级铺垫；远古祭坛、巨兽低吟、音系法阵发动。
- **AI提示词写法**：`sand scattered on a stone slab jumping and migrating under a deep rumble, the grains gathering into concentric rings and a geometric standing-wave pattern, a figure chanting at the center, dust motes hovering at the vibration nodes`

### 141. 拟声字实体（Solid Onomatopoeia Prop）
巨大描边拟声字（"斩""轰"）不再是平面字幕，而是有重量的实体：砸进地面砸出浅坑扬起尘土、被角色一刀劈成两半、碎块崩落滚散——漫画描き文字传统（字号=音量、笔触=音质）的立体化。区别于 #109 拟声词具象（平面 typography 砸进构图）：本条拟声字与场景有物理交互，会受击、会碎、会扬尘。
- **什么量级用它**：漫画式演出、喜剧重音、JOJO 式压迫、大招报名的定场。
- **AI提示词写法**：`a giant outlined kanji sound-effect character crashing into the ground like a solid object, carving a shallow crater and kicking up dust, a swordsman slicing the massive character in half, its fragments toppling and crumbling apart`

---

## 参考来源

- Sakugabooru 特效标签体系（explosions / smoke / liquid / debris / fire / lightning / sparks）：https://sakugabooru.com
- Sakuga Blog（作画分析、中村丰/吉成曜/桥本敬史专题）：https://blog.sakugabooru.com
- Yutapon Cubes 考据（中村方块起源与《我的英雄学院》23 话冲击帧统计）：YouTube「Yutapon Cubes / Impact Frames in My Hero Academia」相关作画 MAD 与解析
- Smear Frames 分类（Elongated / Multiples / Dry-brush）：动画原理文献与 Animator Island「Smear Frames」条目
- 金田系作画（金田透视/金田光/金田流线/BLACK 影）：金田伊功相关作画研究资料、Anime News Network 金田伊功纪念文
- 板野马戏团（Itano Circus）：板野一郎访谈与《超时空要塞》作画分析
- EVA 十字架爆炸：庵野秀明相关访谈与《新世纪福音战士》演出分析
- 出崎统 Postcard Memory / 止め絵 / Harmony 技法：《网球甜心》《明日之丈》演出研究
- ufotable 合成管线（《鬼灭之刃》水之呼吸/炎特效）：ufotable 制作访谈与第 19 话作画分析
- 吉卜力水物理与《龙猫》雨、《波妞》17 万张手绘：宫崎骏/吉卜力制作资料
- 新海诚雨（《言叶之庭》雨滴折射、《天气之子》virga）：新海诚作品美术访谈
- 速度线/效果线分类（集中线/放射线/阴り线/揺れ线/β闪）：日本漫画表现技法资料（エフェクト線・効果線体系）

---

*本库为活文档，后续每轮实战返工教训继续沉淀进来。*
