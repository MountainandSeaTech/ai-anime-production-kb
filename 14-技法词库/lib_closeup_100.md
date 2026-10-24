# 特写镜头技法库 · 166 条

> 与《对战编排总纲》配套使用。总纲法则19（特写预算制）、法则35（Umakoshi Eye）管"何时用、用几个"；本库管"具体用哪个、怎么写提示词"。  
> 特写只有两种职能：**信息**（剧情齿轮——观众必须看到的物证/线索/资源状态）与**情绪**（角色状态——说不出口的心理活动）。不为"帅"而设。

---

## 特写选择决策树

```
剧情节点                           →  首选特写类型                     →  条目索引
─────────────────────────────────────────────────────────────────────────────
开打前立赌注/立关系                →  信物类插入镜头（戒指/赌约/信纸）  →  64, 65, 69
互认底细（试探段收束）             →  双眼对视轮切 / 眯眼               →  5, 15, 18
杀招/王牌出手前 0.5 秒             →  Umakoshi Eye 瞳孔预兆            →  1, 19
读招完成（"看穿了"的瞬间）         →  眼球转动定格 / 嘴角微扬           →  17, 24
逆转信号（资源见底/主场易手）      →  资源可视化插入（裂纹/卷刃/余压）  →  72, 73, 74
破绽暴露                           →  伤口渗血 / 断刃缺口              →  78, 80
伤害无效化的绝望宣告               →  再生愈合倒放                     →  82
巨物/灾难逼近                      →  先大全景 → 再受害者瞳孔 ECU      →  2, 20（配合总纲法则39）
角色觉醒/变身                      →  闭眼→睁眼切换 / 发丝被能量吹起   →  10, 56
疼痛与代价                         →  手按伤口 / 血沿指尖滴落          →  40, 53
压抑情绪（不能哭出声）             →  泪光积聚未落 / 颤抖的唇          →  7, 28
黑化/绝望                          →  高光消失 / 眼神失焦              →  11, 12
需要观众自己下结论                 →  库里肖夫中性脸反应镜头            →  84
第三方解说战力差                   →  旁观者惊愕反应群像                →  85
隐藏信息/伏笔                      →  道具标签 / 印记特写              →  101, 102, 103
高潮前的绝对静场                   →  静态特写+微动（单细节动）         →  109
节奏断裂/冲击                      →  Cut-in 跳切 / 冲击帧             →  105, 107
段落的诗意收束                     →  Dezaki 定格 / 微相学长特写       →  106, 93
角色死亡/放下                      →  松开的五指                       →  36
```

**预算提醒**：60 秒打戏全场 5 个特写额度（总纲法则19）；文戏独白段可放宽至每 30 秒 1-2 个微相学特写；插入镜头（纯信息）不占情绪特写额度，但也不超过每 15 秒 1 个。

---

## 第一编 · 眼部特写（20 条）

> 巴拉兹："特写不仅使脸部在空间上更接近我们，而且超越空间进入另一个领域——心灵的领域，即'微相学'的世界。"眼睛是微相学的首都。

### 1. Umakoshi Eye（极致瞳孔预兆）

杀招出手前几毫秒，给攻击方单眼 ECU：瞳孔高频震颤、虹膜细节拉满、粗粝阴影切割眼部。出处：马越嘉彦，《Casshern Sins》(2008) 定型，《我的英雄学院》《Berserk 1997》《Baki》沿用——少年漫"技能发动预告"的标准件。

- **揭示什么**：情绪=杀气先于动作到达；信息="下一击是致命的"。
- **AI提示词写法**：`extreme close-up of a single eye, pupil trembling at high frequency, hyper-detailed iris, harsh sketch-like shadows across the eyelid, killing intent`

### 2. 瞳孔骤缩（恐惧反射）

受击/目击恐怖瞬间，瞳孔在 0.2 秒内缩成针尖，其余面部全静止。出处：《Requiem for a Dream》(2000) 以瞳孔变化 ECU 作全片反复母题。

- **揭示什么**：情绪=本能级恐惧，比尖叫更诚实；灾难逼近运镜的终点帧（总纲法则39）。
- **AI提示词写法**：`extreme close-up of an eye, pupil shrinking rapidly to a pinpoint, everything else motionless, cold sweat sheen on skin`

### 3. 瞳孔地震（信念动摇）

听到颠覆认知的台词时，眼球小幅不规则颤动，虹膜高光随之晃动——"世界观在震"的具象化。出处：日系动画通用演出，《进击的巨人》艾伦听闻真相处多次使用。

- **揭示什么**：情绪=认知崩塌进行中；适合配静默无 BGM。
- **AI提示词写法**：`close-up of a single eye, iris quivering irregularly, highlight shaking, unfocused gaze, muted colors`

### 4. 泪光在虹膜上积聚但不落

眼泪只在眼眶里形成一层反光膜，视线因此轻微折射变形——"忍住不哭"的量化表达。

- **揭示什么**：情绪=压抑中的悲伤；比泪落更高级（泪落=释放，泪膜=悬置）。
- **AI提示词写法**：`extreme close-up of an eye with a thin film of tears building up, light refracting through the watery surface, not a single tear falling`

### 5. 眼神对决（不动的战争）

冲突双方各给一个纹丝不动的眼部特写轮切，视线方向严格轴线对位。出处：《飞越疯人院》(1975) 麦克默菲与护士长全片冲突即"一场眼神的战斗"；《黄金三镖客》三方对峙。

- **揭示什么**：情绪=内在张力的冲突；信息=权力关系此消彼长（谁先移开谁输）。
- **AI提示词写法**：`extreme close-up of two characters' eyes in alternating cuts, unblinking stare, sharp focus on irises, tension, static camera`

### 6. 睫毛的颤动

巴拉兹钦定的微相学标本："眼睫毛的颤动、眼神的瞬间变化，被放大到银幕上。"用于角色装睡被识破、强撑镇定被窥破的瞬间。

- **揭示什么**：情绪=伪装下的真实波动；幅度必须小到"差点没看见"。
- **AI提示词写法**：`extreme close-up of closed eyelashes trembling slightly, soft side light, shallow depth of field, the rest of the face in darkness`

### 7. 单泪滑落（伊尔莎之泪）

一行泪单独从眼角滑过面颊，面部其余肌肉保持决绝。出处：《卡萨布兰卡》(1942) 机场诀别，褒曼面颊上的单行泪——"决断与心碎同框"。

- **揭示什么**：情绪=主动选择的牺牲；单泪=体面，泪崩=崩溃，别用混。
- **AI提示词写法**：`close-up on a cheek, a single tear rolling down slowly, resolute expression, soft golden light, shallow depth of field`

### 8. 眼中倒映世界

虹膜/眼镜镜片里倒映火焰、城市、对手剪影或关键线索——一个镜头装两个空间。出处：《Se7en》(1995) 萨默塞特眼镜倒映罪证；《银翼杀手2049》扫描 DNA 时眼中的数据流。

- **揭示什么**：信息=他看见的东西（免切 POV）；情绪=被所见之物占据。
- **AI提示词写法**：`extreme close-up of an eye reflecting a burning city skyline in the iris, the reflection sharp and detailed, static camera, slow motion`

### 9. 闭→睁切换（觉醒帧）

闭眼黑场半秒→猛然睁眼，虹膜颜色/纹路已改变——变身、觉醒、切换人格的一帧宣言。

- **揭示什么**：信息=力量体系切换完成；情绪=新人格降临。剪辑上必须静→动突变。
- **AI提示词写法**：`extreme close-up of closed eyes snapping open, iris glowing with a new color, energy rippling across the eye, sudden cut from darkness`

### 10. 高光熄灭（绝望/黑化）

眼部作画不变，唯独瞳孔里的高光点消失——日系"坏掉了"的最简表达。出处：《魔法少女小圆》沙耶香绝望段及一切"黑化"桥段的通用记号。

- **揭示什么**：情绪=希望断电；改动极小、信息极大，符合一帧一职。
- **AI提示词写法**：`close-up of eyes with the catchlight vanished from the pupils, flat dead irises, face otherwise unchanged, desaturated`

### 11. 眼神失焦（灵魂离线）

视线越过镜头/对手投向虚空，焦点对不上任何东西——精神崩坏或巨大悲恸后的"空"。

- **揭示什么**：情绪=人格暂时退场；常配环境音抽离（声音设计同步）。
- **AI提示词写法**：`close-up of a face with unfocused eyes staring through the camera, vacant gaze, pale light, no highlight in eyes`

### 12. 兵长式死鱼眼凝视

半阖眼+无高光+向下 15 度视线，叠加染血面颊——厌倦的强者。出处：《进击的巨人》利威尔兵长招牌特写；132 话三联眼部特写分解"悲伤五阶段"（否认/讨价还价/抑郁，唯独没有接受）。

- **揭示什么**：情绪=疲惫到极点的杀意；"我很强且我很累"。
- **AI提示词写法**：`extreme close-up of half-lidded piercing gray eyes, tired deadpan stare angled slightly downward, blood stains on cheekbone, harsh shadows`

### 13. 眯眼（算计启动）

眼睑收拢、视线变窄变锐——从"接收模式"切到"评估模式"。用于识破诡计、发现破绽的瞬间。

- **揭示什么**：信息=他注意到了某个细节（诱导观众回看前镜）；情绪=猎人上线。
- **AI提示词写法**：`close-up of eyes narrowing slowly into sharp slits, gaze intensifying, a subtle glint of realization`

### 14. 眨眼节拍（犹豫的摩斯码）

连续两次慢眨眼+一次视线偏移——角色在下决心或撒谎。眨眼次数和节奏就是台词的潜文本。

- **揭示什么**：情绪=内心拉锯；撒谎戏专用（配合法则：说谎者眨眼频率翻倍）。
- **AI提示词写法**：`close-up of eyes blinking twice slowly, gaze darting sideways, micro-tension around the eyelids, natural light`

### 15. 眼球极限转动（读招）

头不动，眼球独自扫向侧方极限——追踪高速对手、计算轨迹。出处：《龙珠》《一拳超人》等战斗番"跟上速度"的标配。

- **揭示什么**：信息=动态视力等级（他能跟上）；情绪=专注。读招型角色的职业特写。
- **AI提示词写法**：`extreme close-up of an eye, the pupil darting to the extreme corner tracking something fast, head perfectly still, motion blur lines in the background reflection`

### 16. 抬眼（挑衅/宣战）

先垂眼再缓缓抬眼直视，下巴保持不动——由下往上的视线=不低头只抬眼的蔑视。

- **揭示什么**：情绪=隐忍转进攻的拐点；逆转段开场的极佳信号帧。
- **AI提示词写法**：`close-up, chin down and eyes slowly lifting to stare directly into the lens, defiant upward gaze, shadow over brow`

### 17. 三方眼部轮切（Sad Hill 圆阵）

三（多）人对峙时眼-眼-眼快速轮切，越切越紧（CU→ECU→ECU），配合渐强配乐把等待拉长成酷刑。出处：《黄金三镖客》(1966) 坟场三方对峙，莱昂内"把对峙拍成交响乐"。

- **揭示什么**：信息=三方互相威慑的几何关系；情绪=张力累积到扳机量级。轮切节奏=倒数读秒。
- **AI提示词写法**：`rapid alternating extreme close-ups of three fighters' eyes in a triangular standoff, sweat beading, each cut tighter than the last, circular composition`

### 18. 浓眉紧锁的眉间特写

不拍眼，拍眉间竖纹——愤怒的"震中"。适合蓄力中的战士，眉间纹越深呼吸越重。

- **揭示什么**：情绪=被压制的怒火；与眼部特写交替使用可避免重复。
- **AI提示词写法**：`extreme close-up of furrowed brows, deep vertical crease between the eyebrows, trembling slightly with suppressed rage`

### 19. 怒目圆睁+血丝

眼白血丝+虹膜纹理全开+眼睑撑到极限——暴怒或燃命透支。与条目1（杀招前）区分：这条是"燃烧中"，那条是"点火前"。

- **揭示什么**：情绪=愤怒/透支的峰值；信息=身体在付代价（血丝=代价）。
- **AI提示词写法**：`extreme close-up of a wide-bloodshot eye, iris veins visible, eyelids stretched to the limit, trembling with fury, high contrast`

### 20. 仰望巨物的视线尽头

受害者眼部 ECU，瞳孔里映出逼近的巨物剪影并缓缓放大——灾难逼近运镜的情绪终点。出处：配合《进击的巨人》巨人出现段落的视线剪辑逻辑。

- **揭示什么**：情绪=被体量碾压的恐惧；信息=威胁的尺度（用瞳孔当标尺）。
- **AI提示词写法**：`extreme close-up of a terrified eye, the silhouette of a colossal figure growing larger in the pupil's reflection, pupil trembling`

---

## 第二编 · 嘴/唇/牙特写（9 条）

> 嘴是表情里唯一可以说谎也可以拆穿谎言的器官。

### 21. 嘴角一毫米上扬（得逞/逆转预告）

全景里都看不见的微小弧度，特写里只动嘴角一根线——"计划通"。出处：一切智斗番的"逆转信号帧"；符合特写预算制中"逆转信号"职。

- **揭示什么**：信息=他藏了一手；情绪=克制的得意。幅度必须小到观众"怀疑自己看错"。
- **AI提示词写法**：`extreme close-up of a corner of a mouth curling up by a millimeter, suppressed smirk, everything else static, dim side lighting`

### 22. 咬唇（忍耐计量表）

下唇被咬住，随压力加深出现齿痕与血色变化——忍痛、忍泪、忍话的通用计量器。

- **揭示什么**：情绪=压抑的总量（齿痕深度=压抑强度）；女性角色高频使用但同样适合隐忍型男性。
- **AI提示词写法**：`extreme close-up of a lower lip being bitten, teeth marks forming, slight trembling, a trace of blood color`

### 23. 虎牙一露（野性上线）

咧嘴瞬间露出一侧虎牙/尖齿——战意、捕食欲、或疯狂的第一信号。出处：《我的英雄学院》爆豪式战意表情。

- **揭示什么**：情绪=享受战斗的野兽面；复调表情（专注+愉悦）的锚点。
- **AI提示词写法**：`extreme close-up of a grinning mouth, one sharp canine catching the light, battle-crazed expression, high contrast shadows`

### 24. 咧嘴逐帧扩大（疯狂升温）

笑容在特写里一帧帧撑大到非人幅度，牙齿数量仿佛变多——理智蒸发的过程可视化。出处：《游戏王》城之内、《寒蝉》黑化颜艺的递进式咧嘴。

- **揭示什么**：情绪=疯狂量级正在爬坡；用于反派暴走或主角失控。
- **AI提示词写法**：`extreme close-up of a grin widening frame by frame beyond human limits, teeth multiplying in shadow, unhinged energy`

### 25. 唇语（无声的台词）

只拍嘴唇缓慢开合，不给声音（或声音压成耳语）——关键词靠观众读唇。出处：悬疑片"那句不能播出来的话"标准处理。

- **揭示什么**：信息=一句被消音的台词（让观众自己补全=参与感）；情绪=秘密的重量。
- **AI提示词写法**：`extreme close-up of lips mouthing words silently in slow motion, no audio cues, soft rim light, mysterious`

### 26. 颤抖的唇（堤坝将溃）

嘴唇小幅高频颤抖但牙关紧闭——哭意/怒意被封印的最后防线。比哭出来更有张力。

- **揭示什么**：情绪=情绪洪峰距溃坝 0.5 秒；适合放在泪落（条目7）之前做递进。
- **AI提示词写法**：`extreme close-up of trembling lips pressed tight, chin quivering, holding back tears, cold blue light`

### 27. 咬牙（痛苦的物理承兑）

后槽牙咬紧、咬肌隆起、齿缝渗出血丝——疼痛被"付现"的瞬间。配合打击三段式的 Relax 段。

- **揭示什么**：情绪=硬扛；信息=伤害已实质到账（打击物理三要素之"重量"）。
- **AI提示词写法**：`extreme close-up of clenched teeth, jaw muscles bulging, a thread of blood seeping between the teeth, skin taut`

### 28. 微笑的面具裂纹

社交微笑保持不动，但法令纹/眼角纹路在特写里"穿帮"——假笑与真悲的裂缝。

- **揭示什么**：情绪=伪装成本；用于腹黑角色或将崩的体面人。与库里肖夫中性脸（条目84）是表里关系。
- **AI提示词写法**：`close-up of a polite smiling mouth, but the creases around it betray strain, mask-like expression cracking, soft but cold light`

### 29. 吞咽（喉结滚动）

喉结上下滚动一次——恐惧、紧张或下定决心的生理签名。出处：西部片决斗前的标配插入。

- **揭示什么**：情绪=压力峰值（把"害怕"翻译成生理动作）；也可反向用于色气场景。
- **AI提示词写法**：`extreme close-up of a throat, Adam's apple bobbing once slowly, skin glistening with sweat, tense stillness`

---

## 第三编 · 手部特写（14 条）

> 手是触觉电影（haptic cinema）的主角：眼负责"看进灵魂"，手负责"抓住世界"。——Tom Gunning 论希区柯克

### 30. 米勒上尉的颤抖之手

角色登场不给脸，先给一只拧水壶时无法自控颤抖的手。出处：《拯救大兵瑞恩》(1998)——斯皮尔伯格用手抖特写替代表演，宣告 PTSD 与"无人能豁免战争"。

- **揭示什么**：情绪=被职务压着的创伤；信息=这个角色带着旧伤上场。登场建立人物的最高效特写。
- **AI提示词写法**：`close-up of a hand unscrewing a flask cap, fingers trembling uncontrollably, face unseen, overcast cold light, documentary realism`

### 31. 握拳到指节发白

拳头收紧→指节逐节变白→掌缘渗血（指甲掐进肉里）——决意的三级进度条。

- **揭示什么**：情绪=从屈辱到决意的转化过程；渗血一级=决心已超越自惜。
- **AI提示词写法**：`extreme close-up of a fist clenching tighter and tighter, knuckles turning white one by one, blood beading at the palm edge`

### 32. 手指敲击（焦躁的节拍器）

食指在桌面/刀柄/膝盖上不规则敲击——等待中的焦虑外放。埃德加·赖特式节奏控制："只用一根手指也能完成喜剧节奏"。

- **揭示什么**：情绪=不耐烦/倒计时压力；敲击节奏可与剪辑节拍同构（手指=节拍器）。
- **AI提示词写法**：`close-up of fingers tapping irregularly on a tabletop, shallow depth of field, the tapping quickens, ambient tension`


### 33. 悬停在武器上方的手

手掌张开悬在枪柄/刀柄上方 2 厘米，五指微颤——拔与不拔之间的一秒钟。出处：《黄金三镖客》对峙中手与枪的 ECU 轮切。

- **揭示什么**：情绪=决意未满；信息=距离出手的物理余量。对峙段张力主力。
- **AI提示词写法**：`extreme close-up of a hand hovering two centimeters above a weapon hilt, fingers twitching, dust particles in the air, locked-off camera`

### 34. 松开的五指（放手/死亡）

紧抓之物从指间滑落，手指逐节松开摊开——死亡、放弃、或释然。出处：《惊魂记》(1960) Marion 的手沿浴室瓷砖无力滑下——希区柯克"最触觉的镜头"。

- **揭示什么**：情绪=生命/执念的退场；用"抓不住任何东西"表现终点，比面部更狠。
- **AI提示词写法**：`extreme close-up of fingers slowly uncurling and releasing, an object slipping from the palm, hand sliding down a smooth surface, going slack`

### 35. 换手/正反手切换（觉悟时刻）

武器从一只手换到另一只手，或反手握转正手握——打法性格切换的手语。出处：剑戟片与《鬼灭》呼吸法切换的仪式感处理。

- **揭示什么**：信息=战术切换完成（认真了）；情绪=仪式感。逆转段的信号弹。
- **AI提示词写法**：`close-up of a blade being transferred from one hand to the other in slow motion, grip reversing, calloused fingers, dust falling`

### 36. 指尖相隔一毫米（未触及）

两只手（或手与物）的指尖停在即将接触的一毫米，空气凝固。出处：《爱在黎明破晓前》(1995) 试听间"将触未触"——期待比接触更有叙事重量。

- **揭示什么**：情绪=渴望与克制的最大张力；感情线专用，也可用于"够不着的救命稻草"。
- **AI提示词写法**：`extreme close-up of two fingertips one millimeter apart, trembling slightly, frozen mid-reach, soft warm light, shallow focus`

### 37. 按住伤口的手（疼痛可视化）

手掌死压伤口，血从指缝漫出——不见伤口本身，血量全靠指缝表达。

- **揭示什么**：信息=伤势量级（指缝渗血速度=失血曲线）；情绪=咬牙硬撑。比直拍伤口更高级。
- **AI提示词写法**：`close-up of a hand pressed hard against a side wound, blood seeping between the fingers and dripping, knuckles white, ragged breathing motion`

### 38. 结印/施法手势被打断

法印结到一半，指尖光纹熄灭、手势被外力拍散——法师职业的"资源被打断"可视化（呼应总纲职业行为锁）。

- **揭示什么**：信息=施法失败+原因；情绪=节奏被夺。法师被压制的标准特写。
- **AI提示词写法**：`extreme close-up of fingers mid-incantation, glowing sigils on the fingertips flickering out, the hand knocked aside, sparks dissipating`

### 39. 手伸向镜头（打破第四面墙的手）

手掌直接向镜头探来并占满画幅——求救、抓取、或邀请观众进入。

- **揭示什么**：情绪=绝望/渴望的直达投递；信息=距离归零。慎用，全场最多一次。
- **AI提示词写法**：`close-up of a hand reaching directly toward the camera, fingers spreading as they fill the frame, forced perspective, desperate`

### 40. 转动戒指/小物件（神经质的签名）

无意识转动婚戒、硬币、打火机——思虑或身份焦虑的下意识外泄。出处：ECU 经典范式"被摘下的婚戒=一段关系的终结"（Story2Board 词条）。

- **揭示什么**：信息=该物件绑定的人物关系正在松动；情绪=焦虑的地下河。
- **AI提示词写法**：`extreme close-up of fingers absently rotating a wedding ring, hesitant, the ring catching light, blurred background`

### 41. 老手与新手（茧的叙事）

两只手的特写对照：一只布满老茧伤痕，一只干净细瘦——不用一句台词讲完资历差。

- **揭示什么**：信息=经验值差距（身体履历）；情绪=传承或碾压。师徒/老兵新兵关系一镜立。
- **AI提示词写法**：`extreme close-up of two hands side by side, one calloused and scarred, one clean and slender, same grip pose, telling contrast`

### 42. 笨拙的第一次（手生）

手指对着陌生工具笨拙试探、打滑、重来——成长线的起点帧。

- **揭示什么**：信息=他是外行（为后期成长埋对照点）；情绪=可爱/不安。
- **AI提示词写法**：`close-up of clumsy fingers fumbling with an unfamiliar tool, slipping, trying again, warm natural light`

### 43. 祈祷式交握（掩饰）

双手合十/交握置于面前遮住嘴——掩盖表情的手势建筑。出处：《EVA》碇源堂招牌姿势：用手的特写隐藏脸的特写。

- **揭示什么**：情绪=深不可测的算计；信息=这个角色拒绝被读。特写套娃：用手特写当面具。
- **AI提示词写法**：`close-up of interlaced fingers held before the face, hiding the mouth, still and deliberate, cold office light`

---

## 第四编 · 汗/泪/血/体液特写（11 条）

> 体液是身体的字幕：把看不见的生理状态变成看得见的信息。

### 44. 汗珠沿下颌线旅行

一滴汗从太阳穴出发，沿颧骨、下颌线滚动，在下巴尖悬停半秒——莱昂内式等待的具象时间。出处：《西部往事》(1968) 开场：汗湿的三人组等待火车，连停在脸上的苍蝇都成戏。

- **揭示什么**：情绪=等待的煎熬（汗=时间的汗）；信息=环境温度与紧张度双高。
- **AI提示词写法**：`extreme close-up of a bead of sweat traveling down a stubbled jawline, pausing at the chin, glistening, sweltering light`

### 45. 汗滴落地（决胜发令枪）

一滴汗砸在地面/榻榻米/剑刃上碎开——寂静中的发令枪，出手常在这一帧后 0.1 秒。出处：剑戟片对决的听觉特写传统（水滴音=杀气开关）。

- **揭示什么**：情绪=张力归零瞬间的引爆点；节奏功能=全场动作的发令枪。
- **AI提示词写法**：`extreme close-up of a single drop of sweat hitting the ground in slow motion, shattering into micro-droplets, dead silence, then sudden motion`

### 46. 一滴血落在白物上

血滴落在白纸/白雪/白衣上晕开——污染、牺牲或"再也回不去"的最小表达。

- **揭示什么**：信息=伤害已造成且不可逆；情绪=纯洁物的丧失。红白对比是核心构图。
- **AI提示词写法**：`extreme close-up of a drop of blood falling onto white snow, blooming outward in a red stain, macro lens, stark contrast`

### 47. 血泪

血泪替代眼泪从眼角划下——悲痛超越肉体阈值的极端表达。出处：恐怖/悲剧高潮的通用极端件。

- **揭示什么**：情绪=伤痛已达身体无法承载级；慎用，一部作品一次。
- **AI提示词写法**：`extreme close-up of an eye shedding a single tear of blood, the red trail stark against pale skin, dim religious light`

### 48. 鼻血喷泉（漫符系统）

鼻血柱状喷出——日漫"兴奋/好色"的官方符号，完全脱离生理 realism 的喜剧记号。出处：漫画图标学（manga iconography）体系。

- **揭示什么**：情绪=喜剧级兴奋；使用即宣告本段为搞笑区，严肃段落禁用。
- **AI提示词写法**：`close-up of an anime character with a sudden comedic nosebleed, exaggerated spray, sparkle-eyed expression, bright flat colors, manga iconography style`

### 49. 巨大汗滴符号（动画专属）

太阳穴旁凭空出现一颗 oversized 汗珠——日漫"焦虑/无语/尴尬"的万能标点。出处：manga iconography 核心符号，汗滴数量=焦虑等级。

- **揭示什么**：情绪=社交性焦虑/吐槽能量；非写实，是"情感标点符号"，Q 版段落专属。
- **AI提示词写法**：`close-up of an anime character's temple with one giant symbolic sweat drop sliding down, deadpan expression, flat comedic style`

### 50. 泪崩瀑布（喜剧版哭泣）

眼泪画成两道夸张水帘喷涌——与单泪（条目7）构成光谱两端：一端体面一端爆笑。

- **揭示什么**：情绪=夸张化的悲伤/感动（喜剧）；真实悲剧场景禁用。
- **AI提示词写法**：`close-up of an anime character crying with two waterfall streams of tears, comedic exaggeration, wavy trembling mouth`

### 51. 血沿手臂滴落指尖

血顺着手臂内侧流到指尖、聚集、滴落——用"血的路程"丈量伤势。

- **揭示什么**：信息=伤口位置与出血量（不拍伤口拍血流）；情绪=流失中的生命力。
- **AI提示词写法**：`close-up of blood tracing a line down a forearm to the fingertips, pooling at the fingertip, dripping in slow motion`

### 52. 汗湿贴额的发丝

湿透的发绺贴在额头/脸颊上——鏖战后体力见底的体面写法。

- **揭示什么**：信息=体力槽已红（资源曲线可视化的人肉版）；情绪=狼狈中的坚韧。
- **AI提示词写法**：`close-up of sweat-soaked hair strands stuck to a forehead and cheek, heavy breathing, flushed skin, exhaustion`

### 53. 呕吐感上涌（咽回）

喉部特写+角色强行咽回呕吐物——恐惧/惨状超越承受力的身体证言。

- **揭示什么**：情绪=他在硬撑不崩溃；用于见识到真正恐怖的"入伙礼"时刻。
- **AI提示词写法**：`extreme close-up of a throat convulsing, a character forcing bile back down, sweat breaking out, nauseated pallor`

### 54. 口水/血线拉丝

受重击后嘴角拉出一条血丝/口水丝——打击到账的明细单。出处：格斗番受击后的标准余韵帧。

- **揭示什么**：信息=打击量级（丝的长度=伤害额度）；配合打击三段式 Relax 段。
- **AI提示词写法**：`extreme close-up of a thin string of blood-streaked saliva stretching from a split lip, dazed expression, harsh arena light`

---

## 第五编 · 发丝/身体细节特写（8 条）

### 55. 发丝遮眼（情绪的帘子）

垂落的发丝遮住眼睛，观众看不见眼神——角色主动退入内心的视觉宣告。

- **揭示什么**：情绪=拒绝被读取（自闭/黑化前兆/独白开始）；信息=下一段是内心戏。
- **AI提示词写法**：`close-up of a face with loose hair strands falling over and hiding the eyes, lips barely visible, muted tones, stillness`

### 56. 能量场吹起发丝（觉醒气象学）

无风自动：发丝被自下而上的能量气流托起——气场/魔力量级的气象学表达。出处：超级赛亚人变身的行业范式。

- **揭示什么**：信息=能量输出档位正在上调；情绪=力量涌流的体感。变身/爆气专用。
- **AI提示词写法**：`close-up of hair strands lifting and waving in an upward energy current, faint glow outlining each strand, power surging`

### 57. 耳廓微动（听觉雷达）

耳朵轻轻一颤转向声源——察觉/警戒的最低信号。兽耳角色加倍有效。

- **揭示什么**：信息=他听到了观众还没听到的（悬念前置）；情绪=警觉上线。
- **AI提示词写法**：`extreme close-up of an ear twitching slightly toward an off-screen sound, fine hairs catching the light, alert stillness`

### 58. 肩颈起伏（喘息计量器）

不拍脸，只拍肩膀与锁骨的起伏频率——疲惫/紧张全靠呼吸的形体语言表达。

- **揭示什么**：信息=体力余量（呼吸频率=剩余血条）；情绪=硬撑。打戏换气口（总纲法则38）的最佳填充。
- **AI提示词写法**：`close-up of shoulders and collarbones heaving with heavy breaths, sweat sheen, torn fabric edge, rhythm slowing gradually`

### 59. 赤足触地（锚定/回归）

赤裸脚掌踩上地面/水面/灰烬，脚趾因触感微曲——回到现实、踏上战场的锚点帧。

- **揭示什么**：情绪=与此地的连接（或决绝）；触觉电影的延伸，大地的质地=世界的质地。
- **AI提示词写法**：`extreme close-up of a bare foot pressing onto wet ground, toes curling slightly at the texture, ripples spreading, dawn light`

### 60. 睫毛上的雪/灰

雪花或灰烬落在睫毛上，眨眼时簌簌落下——环境极端化的优雅证明。

- **揭示什么**：信息=环境温度/灾后现场（不用全景就交代了世界状态）；情绪=安静的诗意。
- **AI提示词写法**：`extreme close-up of snowflakes resting on eyelashes, melting as the eye slowly blinks, soft diffused winter light`

### 61. 颈部暴起的青筋（极限输出）

脖颈青筋与血管暴起——力量输出到极限的解剖学证明。出处：《进击的巨人》变身/发力段的招牌细节作画。

- **揭示什么**：信息=输出已超身体安全阈（代价前置）；情绪=燃命的狠劲。
- **AI提示词写法**：`extreme close-up of a neck with veins bulging and pulsing, skin flushed, straining at the limit, dramatic side light`

### 62. 脊背发凉的竖毛

后颈/手臂汗毛竖起的微距镜头——被猎杀者盯上的动物本能。

- **揭示什么**：情绪=生物级恐惧（比表情更诚实）；信息=威胁已进入本能感知圈。
- **AI提示词写法**：`macro close-up of fine hairs standing up on the back of a neck, goosebumps rising, cold blue shadow creeping in`

---

## 第六编 · 插入镜头类（道具/伤口/装备细节，20 条）

> 插入镜头（Insert Shot）= 观众与角色共享同一视角的信息窗口。诺兰："物件能建立一种叙事连接。"——《记忆碎片》的宝丽来、《盗梦空间》的陀螺，半部电影建立在插入镜头上。

### 63. 旋转的陀螺（悬而未决）

陀螺在桌面旋转，将倒未倒——结局开放性的物化。出处：《盗梦空间》(2010) 结尾：全片悬念压在一个旋转的道具上。

- **揭示什么**：信息=验证机制的结果悬置；情绪=把焦虑交给一个物体承担。收束段专用。
- **AI提示词写法**：`extreme close-up of a spinning top wobbling on a table, slow motion, about to fall but still spinning, shallow depth of field, silent tension`

### 64. 宝丽来照片显影（记忆实体化）

照片从空白缓缓显影出关键画面——信息/记忆逐步到账的过程可视化。出处：《记忆碎片》(2000) 的叙事引擎。

- **揭示什么**：信息=证据浮现（显影速度=真相逼近速度）；情绪=对记忆的执念。
- **AI提示词写法**：`extreme close-up of a polaroid photo slowly developing, an image emerging from blank white, fingers holding it steady`

### 65. 被摘下的婚戒

手指缓缓退下戒指，戒痕犹在——关系终结的不动声色的宣判。出处：ECU 经典教学案例（Story2Board）："一个摘下婚戒的 ECU 不说一句台词就讲完一段关系的终结。"

- **揭示什么**：信息=关系状态变更；情绪=决定已下（戒痕=过去仍在）。文戏分手/决裂的顶配。
- **AI提示词写法**：`extreme close-up of a ring being slowly slipped off a finger, a pale ring mark left on the skin, soft cold window light`

### 66. 钥匙进锁孔（开/不开）

钥匙插入锁孔，停顿、转动或卡住——"进不进得去"的悬念最小单元。

- **揭示什么**：信息=通行权/秘密的可及性；情绪=越界前的最后一道闸门。
- **AI提示词写法**：`extreme close-up of a key sliding into a rusty lock, hesitating, then turning with a click, macro detail of the mechanism`

### 67. 倒计时读秒（时间压力表）

炸弹/法阵/沙漏的数字跳动——时间压力的唯一合法仪表。出处：动作片标准件；配合"新信息需停留更久"律（条目115）调整读秒节奏。

- **揭示什么**：信息=剩余时间（硬信息）；情绪=压力值的官方读数。一场戏只插 2-3 次，插在跳变点。
- **AI提示词写法**：`extreme close-up of a countdown timer ticking down, red digits flickering, reflection of a face in the glossy display`

### 68. 信纸/报纸头条（Karel Reisz 停留律）

文件、信纸、通缉令、诊断书的文字特写——纯信息投放。出处：从早期电影的书信插入到韦斯·安德森（《Rushmore》"建立在 insert 上的电影"）。

- **揭示什么**：信息=剧情齿轮；铁律=新信息镜头的停留时间必须长于熟信息（Reisz《电影剪辑技巧》）。
- **AI提示词写法**：`extreme close-up of a creased letter, key line of text in sharp focus, paper texture and ink visible, trembling slightly in a hand`

### 69. 子弹上膛/弹巢转动

弹壳入膛、击锤扳起、弹巢转出黄铜反光——暴力的预备仪式。出处：西部片与黑帮片的出手前奏标准件。

- **揭示什么**：信息=武器状态（还有几发=资源信息）；情绪=杀戮的仪式感。金属声效与画面同等重要。
- **AI提示词写法**：`extreme close-up of a revolver cylinder rotating, brass bullet casings catching light, hammer cocking back, oiled metal texture`

### 70. 刀出鞘一寸

刀刃离鞘一寸，寒光在鞘口一闪——"要不要拔"的金属化表达。比整条拔刀更克制。

- **揭示什么**：情绪=杀意的临界点；信息=武器的成色（寒光质量=刀的等级）。
- **AI提示词写法**：`extreme close-up of a blade drawn one inch from its scabbard, a sliver of cold light gleaming at the opening, dust motes`

### 71. 晶石三态（满槽→裂纹→熄灭）

魔力晶石特写序列：充盈→出现裂纹→光熄——资源曲线的三格仪表盘。出处：呼应总纲法则7"资源见底全程可视化"。

- **揭示什么**：信息=魔力余量（败因是资源烧到终点而非被打倒）；情绪=耗尽感。一场消耗战插 3 次，构成进度条。
- **AI提示词写法**：`extreme close-up of a mana crystal, hairline cracks spreading across its facets, inner light dimming from bright to ember, held in a trembling palm`


### 72. 刀刃卷口/崩刃

刃口在格挡后崩出缺口，金属翻卷——"他的刀在替他说话：撑不住了"。出处：呼应总纲法则7/12 装备消耗线。

- **揭示什么**：信息=武器耐久（装备损耗=人类方倒计时）；情绪=劣势的无声确认。
- **AI提示词写法**：`extreme close-up of a chipped and rolled blade edge, metal curling at the notch, a crack spider-webbing from the impact point`

### 73. 气瓶余压表针

立体机动装置/潜水装备的压力表指针打进红区——现代装备的倒计时。出处：《进击的巨人》瓦斯消耗设定的仪表化。

- **揭示什么**：信息=机动余量（红区=主场即将丧失）；情绪=机械宣判的冷酷。
- **AI提示词写法**：`extreme close-up of a pressure gauge needle dropping into the red zone, glass face reflecting a strained eye, steam hissing at the seams`

### 74. 地图上的标记/红线

手指在地图上划过路线、戳向目标点——战略信息的最经济投放。

- **揭示什么**：信息=计划全貌（免台词交代）；情绪=谋定后动的从容或孤注一掷。
- **AI提示词写法**：`extreme close-up of a finger tracing a route on a worn map, stopping and tapping a marked point, ink and paper texture, candlelight`

### 75. 怀表/钟楼指针（正午将至）

指针逼近整点——西部片决斗前的官方计时器。出处：《正午》(1952) 的时钟蒙太奇范式。

- **揭示什么**：信息=死线逼近；情绪=宿命的脚步声。与汗特写（条目44）联用效果翻倍。
- **AI提示词写法**：`extreme close-up of a pocket watch, the second hand trembling toward twelve, engraved metal case, oppressive stillness`

### 76. 燃烧的信/照片一角

火焰从照片一角吞噬面孔——过去正在销毁进行时。

- **揭示什么**：信息=证据/记忆的物理消亡；情绪=诀别或灭证。烧的是谁的脸=剧情的题眼。
- **AI提示词写法**：`extreme close-up of a photograph catching fire at one corner, flames consuming a face, embers curling the paper, darkness around`

### 77. 法阵纹路逐格点亮

阵环上的符文按序亮起/受击格过载变白——法术系统的状态栏。出处：呼应总纲法则23 法术解剖学。

- **揭示什么**：信息=法术充能进度/屏障受损分布（体系内观众读得懂）；情绪=蓄力的庄重感。
- **AI提示词写法**：`extreme close-up of magic circle runes igniting one by one along a ring, engraved grooves filling with light, one cell overloading to white`

### 78. 伤口渗血染红衣料

不拍伤口，拍血在布料上晕开的面积扩大——过审友好且更克制的伤势表达。

- **揭示什么**：信息=出血速度与位置（晕开速率=伤势曲线）；情绪=隐忍（角色不哼声，布料替他出血）。
- **AI提示词写法**：`extreme close-up of blood blooming and spreading through fabric, the stain widening in slow motion, threads soaking dark`

### 79. 新伤叠旧疤

新伤口旁露出层层叠叠的旧疤痕——战斗履历刻在皮肤上的年表。

- **揭示什么**：信息=角色的战斗史（一镜交代资历）；情绪=代价的长期主义。
- **AI提示词写法**：`extreme close-up of a fresh cut beside layers of old faded scars, skin texture like a battle chronology, raking light`

### 80. 断刃的缺口特写

断剑截面、崩飞的半截刀片旋转插入地面——武器的死亡=主人处境的物化。

- **揭示什么**：信息=王牌/武器已废（王牌删除条款的物证）；情绪=孤注一掷的前奏。
- **AI提示词写法**：`extreme close-up of a blade's jagged broken cross-section, the severed half spinning and embedding into the ground nearby`

### 81. 巨物的单眼（尺度对比）

巨物一只眼睛占满画幅，瞳孔里映出蚂蚁般的人类——用特写反向丈量体型差。出处：巨人战/巨兽片的尺度宣告。

- **揭示什么**：信息=体型量级（不靠全景靠对比）；情绪=被注视的压迫。呼应总纲法则12 体型即灾害。
- **AI提示词写法**：`extreme close-up of a colossal creature's single eye filling the frame, a tiny human figure reflected in its vast pupil, the eye swiveling to focus`

### 82. 再生愈合倒放

伤口以肉眼可见的速度收拢、皮肉重织——"刚才一切都白打了"的绝望宣告。出处：呼应总纲法则12 伤害幻觉条款。

- **揭示什么**：信息=普通伤害无效（战术体系作废）；情绪=绝望的机制化。播放速度=再生能力的恐怖等级。
- **AI提示词写法**：`extreme close-up of a wound knitting itself shut in accelerated time, flesh reweaving, steam rising from sealing skin, unnatural smoothness`

---

## 第七编 · 反应镜头类（8 条）

> 库里肖夫效应：观众从"脸+对象"的并置中读出的意义，大于任何单一镜头。反应镜头是剪辑的杠杆——你拍的不是脸，是观众自己的投影。

### 83. 库里肖夫中性脸

同一张无表情特写，接在不同对象镜头（汤/棺中女童/沙发上的女人）之后，观众自动读出饥饿/悲伤/情欲。出处：库里肖夫实验（1918）；希区柯克升级为"特写→POV→反应"三段式纯电影。

- **揭示什么**：情绪=观众自己补全的（参与度最高的表情）；用法=预算有限时，一张好特写反复接不同信息镜。
- **AI提示词写法**：`close-up of a perfectly neutral face, minimal expression, steady gaze looking slightly off-camera, even lighting`

### 84. 旁观者惊愕群像（战力解说员）

不拍强者本人，拍围观者瞳孔地震+下巴掉地——用别人的脸给实力差定价。出处：少年漫"旁人反应"传统（《一拳超人》每一战）。

- **揭示什么**：信息=实力差的官方读数（观众的嘴替）；情绪=敬畏/恐惧的传染性。无敌流必备。
- **AI提示词写法**：`close-up of a bystander's face, eyes wide, pupils shrunk, mouth slightly agape, cold sweat, lit by the flash of an off-screen explosion`

### 85. 反应先于动作（希区柯克三段式）

顺序：角色的脸→他看见的东西→他表情的变化。出处：希区柯克"纯电影"公式（close-up → POV → reaction），《后窗》(1954) 全片即此公式的长篇论证。

- **揭示什么**：信息=因果链（先看脸再看物，观众理解"他在看什么"）；情绪=代入感的生产线。
- **AI提示词写法**：`sequence: close-up of a watching face, then point-of-view of the object, then close-up of the face changing expression, seamless eyeline`

### 86. 延迟反应（慢半拍）

事情发生后角色表情迟滞 0.5-1 秒才崩坏/才笑——处理信息需要时间的人性化瞬间。出处：喜剧节奏与悲剧接受共用的节拍器。

- **揭示什么**：情绪=认知追不上现实的钝感（比即时反应更真实）；喜剧=呆萌，悲剧=无法承受。
- **AI提示词写法**：`close-up of a face frozen in a neutral stare, then the expression slowly crumbling into realization, delayed reaction, one second of stillness first`

### 87. 无表情反应（面瘫的杠杆）

全场最激烈的事件配一张纹丝不动的脸——信息全交给前后镜头，反差即力量。出处：无敌流/冷面主角的招牌（《灵能百分百》Mob 静默前置体系）。

- **揭示什么**：情绪=深不见底（或为爆发蓄压）；用法=静后之暴（总纲法则38）的表情层实现。
- **AI提示词写法**：`close-up of an utterly expressionless face amid chaos, not a muscle moving, dust and debris drifting past the frame, dead calm`

### 88. 集体倒吸凉气

观众席/围观者齐刷刷后仰+吸气——群体情绪的一帧普查。

- **揭示什么**：信息=事件的公共冲击量级；情绪=共识的形成。适合规则级事件（禁术/反转/身份揭晓）。
- **AI提示词写法**：`close-ups of multiple faces gasping in unison, heads recoiling, hands flying to mouths, a collective intake of breath`

### 89. 镜中反射的自己

角色在镜子/水面/刀面反光中与自己对视——自我审视、身份动摇的标配。出处：巴拉兹《可见的人》所述：特写使脸成为"风景"，镜中特写=风景看风景。

- **揭示什么**：情绪=自我对话（他眼中的自己 vs 我们眼中的他）；信息=人格分裂/伪装主题的可视化。
- **AI提示词写法**：`close-up of a face reflected in a cracked mirror or a blade's surface, the reflection staring back, fragmented, cold light`

### 90. 敌手的表情塌方（被读招者的脸）

读招完成后切对手：自信表情一寸寸裂开——逆转的确认帧打在败者脸上。出处：呼应总纲四阶段弧"逆转段"。

- **揭示什么**：信息=优势易手的官方确认；情绪=从掌控到恐慌的渐变全程。与嘴角上扬（条目21）成对使用：一笑一塌=动量易手。
- **AI提示词写法**：`close-up of a confident face cracking millimeter by millimeter, smile faltering, eyes widening as realization dawns, sweat forming`

---

## 第八编 · 情绪特写类（微相学，8 条）

> 巴拉兹："好的特写宛如诗句般感情洋溢，只有用心而非用眼去看，方可感知。"——特写是抒情工具，不是放大工具。

### 91. 微相学长特写（65 秒的转头）

镜头在脸上一动不动地停留远超惯例的时长，让微表情自己发酵。出处：《飞越疯人院》(1975) 结尾麦克默菲 65 秒特写：头缓缓转向窗外，"时间被放慢、延长，精神升华无法用语言描述"。

- **揭示什么**：情绪=超越台词的内心风暴（时长久违=内容密度）；用法=一部作品 1-2 次，留给角色弧顶点。
- **AI提示词写法**：`a single unbroken close-up held for an uncomfortably long time, face slowly turning toward the window, subtle micro-expressions shifting, locked-off camera`

### 92. 圣女贞德受难式（纯脸电影）

剃光头发、无妆、无布景，全片几乎只有脸部特写——把脸拍成一片"经历的地貌"。出处：德莱叶《圣女贞德蒙难记》(1928)，Falconetti 的表演被视为影史特写丰碑；巴拉兹理论的电影实证。

- **揭示什么**：情绪=信仰/冤屈/恐惧的原始状态；证明了"特写可以独立支撑整部电影"。
- **AI提示词写法**：`extreme close-up of a shaven-headed face, no makeup, glistening sweat and tears, plain grey background, stark frontal light, raw anguish`

### 93. 复调表情（双情绪同帧）

一张脸同时承载两种矛盾情绪：专注+极限（汗珠）、疲惫+亲昵（舔唇）。出处：总纲法则19 复调表情条款；动画作画中"上半脸怒+下半脸笑"的复合技法。

- **揭示什么**：情绪=矛盾的并存（角色厚度）；用于关键帧，不复用于常态。
- **AI提示词写法**：`close-up of a face holding two contradictory emotions at once: focused eyes with a twitching smile, sweat beading, layered tension`

### 94. 假笑真哭（社交面具承压）

嘴角维持上扬、眼眶同时泛红——社交场景里"快撑不住了"的体面崩坏。

- **揭示什么**：情绪=伪装成本到达极限；观众比剧中人先看穿=信息差快感。
- **AI提示词写法**：`close-up of a face maintaining a social smile while the eyes redden and glisten, the smile straining at the corners`

### 95. 无表情+一行泪

面部肌肉零动作，唯独一行泪自主滑落——"身体先于意志投降"。出处：悲剧高潮的最高级写法（与条目7 的"决断之泪"区分：这条是"失控之泪"）。

- **揭示什么**：情绪=意志与身体的分裂；比嚎啕大哭更疼。
- **AI提示词写法**：`close-up of a completely still, expressionless face with a single tear escaping and rolling down, involuntary, soft grey light`

### 96. 怒极反静

愤怒越过峰值后表情反而归零、眼神变冷——"越生气越安静"的恐怖。出处：冷面强者发怒的通用范式（兵长式）。

- **揭示什么**：情绪=最高级威胁（吼叫=泄压，安静=全部转化为行动）；信息=对方要动真格了。
- **AI提示词写法**：`close-up of a face going utterly calm at the peak of rage, eyes turning cold and still, jaw set, dangerous quiet`

### 97. 脸颊抽动（忍住的那一下）

咬肌或眼轮匝肌不受控地跳一下——强撑镇定时的唯一穿帮帧。

- **揭示什么**：情绪=自制力的裂缝（一跳即可，不可连跳）；微相学的最小叙事单位。
- **AI提示词写法**：`extreme close-up of a cheek muscle twitching once involuntarily, the rest of the face composed, hard side light`

### 98. 脸的"风景化"（皱纹与伤痕的地貌）

以拍风景的方式拍脸：皱纹是沟壑、伤疤是断崖、汗是天气——巴拉兹"脸即风景"的直接实践。出处：莱昂内对西部片演员们"风化的脸"的凝视。

- **揭示什么**：信息=角色全部过往刻在脸上（免闪回）；情绪=时间的重量。
- **AI提示词写法**：`extreme close-up of a weathered face treated like a landscape, deep wrinkles like ravines, an old scar like a fault line, raking golden-hour light`

---

## 第九编 · 信息特写类（线索与伏笔，5 条）

> 信息特写=剧情的齿轮。巴拉兹论特写的揭示功能："它放大实物原形的过程中使之变形，揭示出正常条件下看不见的物质现实的新方面。"

### 99. 签字笔落（契约成立）

笔尖在文件落款处停半秒→落下签名——不可逆决定的官方时刻。

- **揭示什么**：信息=契约/判决成立（剧情齿轮正式咬合）；情绪=落笔前的半秒犹豫是全部戏。
- **AI提示词写法**：`extreme close-up of a pen nib hovering over a signature line, hesitating, then touching paper, ink bleeding into the fibers`

### 100. 屏幕上的数据扫描（机械式检索）

字符流高速滚动，角色眼神以同样节奏机械扫动——人机一体的信息检索。出处：《银翼杀手2049》K 查 DNA：维伦纽瓦用"眼的机械扫动+数据 ECU"并置。

- **揭示什么**：信息=检索过程与发现时刻（数据特写必须停在关键行）；情绪=非人化的专注。
- **AI提示词写法**：`extreme close-up of a screen streaming data, then a close-up of eyes scanning in the same mechanical rhythm, screen glow reflecting on the face`

### 101. 名牌/徽章/刺青（身份揭晓）

制服上的徽记、衣领下的刺青、倒下的尸体手牌——身份反转的物证特写。

- **揭示什么**：信息=身份真相（一句话不用说）；情绪=认知翻转。伏笔回收专用，埋设时给一个 0.5 秒"差点看清"。
- **AI提示词写法**：`extreme close-up of an insignia/badge half-hidden under a collar being revealed, engraved detail sharp, a hand holding it steady`

### 102. 注射器与药液（道具恐惧）

针尖挤出的一滴药液悬垂欲滴——医疗/毒品/肾上腺素场景的张力阀。出处：《低俗小说》(1994) 肾上腺注射段：ECU 把针管拍成了刑具。

- **揭示什么**：信息=即将进入身体的东西（不可逆）；情绪=对侵入的本能恐惧。
- **AI提示词写法**：`extreme close-up of a syringe, a drop of liquid trembling at the needle tip, harsh light, skin texture visible beneath`

### 103. 怀表内盖的照片（动机的圣物）

打开怀表/吊坠盒，内藏一张小照片——角色全部动机的浓缩载体。出处：西部片与战争片的"为什么而战"标准件。

- **揭示什么**：信息=动机（为谁而战）；情绪=柔软的命门。阵亡/黑化场景的回扣道具。
- **AI提示词写法**：`extreme close-up of a locket/pocket watch opening to reveal a tiny photograph inside, thumb brushing it gently, warm nostalgic light`

---

## 第十编 · 节奏功能类（12 条）

> 特写是剪辑台上的标点符号：跳切是感叹号，定格是破折号，蒙太奇连发是顿号。

### 104. Cut-in 跳切（无过渡的景别落差）

全景→ECU 直接跳切，砍掉一切中间景别——景别落差本身就是冲击。出处：总纲法则16 极距跳切、法则19"Cut-in 不经过渡"；日本动画的カットイン（cut-in）传统。

- **揭示什么**：信息=该细节在此刻压过全场；情绪=惊吓/顿悟的体感。一场戏可用 2-3 次。
- **AI提示词写法**：`hard cut from a wide shot directly to an extreme close-up, no intermediate frames, jarring scale jump, the detail filling the entire screen`

### 105. 斜插入框 Cut-in（游戏化技能发动）

人物面部大特写以斜切画框的方式"插入"主画面上层，占屏 25-30%——技能发动的游戏化宣告。出处：日系手游必杀卡/UI 卡面美学向动画的回流入。

- **揭示什么**：信息=技能发动（带 UI 仪式感）；情绪=爽点宣告。爽番/游戏改专用，写实片场禁用。
- **AI提示词写法**：`anime-style skill activation cut-in: a diagonal overlay panel slicing across the screen, inside it a dramatic close-up of the character's face with glowing eyes, dynamic energy background, high contrast cel-shading`

### 106. Dezaki Freeze Frame（和谐赛璐珞定格）

高潮瞬间画面冻结并转为粉彩/水粉画风格——时间停止，情绪以"画"的形式被装裱。出处：出崎统（Osamu Dezaki）发明，《明日之丈》燃尽定格为影史标志。

- **揭示什么**：情绪=把这一刻升格为"纪念"；用法=段落终结帧，一部作品 1-2 次。
- **AI提示词写法**：`the frame freezes mid-action and repaints itself in pastel/gouache illustration style, rough brush texture, background and figure unified as a painting, lingering hold`

### 107. 冲击帧（负片白闪）

命中瞬间插入 1-2 帧黑白反转/负片画面——剪辑层的痛感，不属于画面内容。出处：总纲法则27 冲击三级制；森康二-Hisashi Punch 传统（命中强调+黑白闪烁）。

- **揭示什么**：信息=打击量级（帧数与反色范围=伤害等级）；情绪=生理级痛感。必须写进剪辑描述而非角色动作。
- **AI提示词写法**：`at the moment of impact, insert 1-2 frames of inverted black-and-white negative flash, screen-filling white burst, then snap back to color`


### 108. 蓄力慢放→爆发常速（微观变速特写）

特写内完成变速：蓄力段 0.3 倍速（瞳孔收缩、肌肉隆起逐帧呈现）→出手瞬间常速。出处：总纲法则4 微观变速；打击三段式 Prepare-Strike-Relax。

- **揭示什么**：情绪=观众的呼吸点（变速转折点=呼吸同步点）；信息=力量蓄满的全过程证据。
- **AI提示词写法**：`extreme close-up in extreme slow motion: muscles coiling, pupil contracting, then the strike releases at full speed, motion blur only at release`

### 109. 静态特写+微动（高潮前的静）

画面 95% 静止，只有一个细节在动（火星明灭/嘴角微动/瞳孔收放）——爆发前的真空。出处：总纲法则19"静态特写+微动"；法则38 静后之暴。

- **揭示什么**：情绪=张力峰值（静=引信烧到最后）；铁律=最静的一镜必须放在最高潮之前。
- **AI提示词写法**：`a nearly frozen close-up where only one detail moves: an ember pulsing, a lip trembling, everything else perfectly still, held breath`

### 110. ECU 蒙太奇连发（节奏即内容）

一连串 ECU 按音乐节拍快切（口红→眼线→武器→靴跟）——用特写堆出仪式感与节奏。出处：《无耻混蛋》(2009) 苏珊娜化妆段；埃德加·赖特"导演=掌控节奏"的 ECU 连发蒙太奇。

- **揭示什么**：信息=准备工作的全部工序（快切=娴熟）；情绪=大战前的亢奋蓄能。每颗 ECU 时长 ≤ 0.5s。
- **AI提示词写法**：`rapid montage of extreme close-ups cutting on the beat: lipstick, weapon check, boot laces, eyes, each under half a second, punchy rhythm`

### 111. 特写预算制（全场 5 个上限）

60 秒打戏只配 5 个特写/大特写，每个都是剧情转折点，无一为"帅"而设。出处：总纲法则19；Story2Board 亦警告"ECU 因稀有而有力，滥用即失效"。

- **揭示什么**：信息=特写是货币不是装饰；五连剧情任务：①互认底细 ②逆转信号 ③读招完成 ④破绽暴露 ⑤关系定音。
- **AI提示词写法**：`（预算规则，非画面提示词）——排分镜时先数特写个数，超编即砍，砍到每个特写都能答出"它转动哪一格剧情齿轮"`

### 112. 一帧一职（单细节驱动）

一个特写镜头里只允许一个细节在动/一个信息被读取——多动即糊。出处：总纲法则19"一帧一职"；Story2Board："ECU 必须立即可读，观众花时间辨认=镜头失败"。

- **揭示什么**：信息=单点聚焦（特写≠信息压缩包）；自检=遮住那个动点，画面应该完全静止。
- **AI提示词写法**：`extreme close-up with a single moving element specified: only the pupil dilates / only a bead of sweat falls, everything else locked still`

### 113. 插入镜头作剪辑缓冲（遮罩接缝）

两个不接的机位之间插一颗物体特写当"创可贴"——掩盖跳轴/跳时间的接缝。出处：插入镜头的传统工业职能（cover footage）；访谈片的 B-roll 逻辑。

- **揭示什么**：信息=无（纯功能）；用法=救场而非创作，正片创作中优先用反应镜头（条目83-90）代替。
- **AI提示词写法**：`neutral insert shot between two discontinuous angles: close-up of an object on the table, matching lighting, brief`

### 114. 新信息停留律（Reisz 定律）

引入新信息的插入镜头停留时间必须 > 重复旧信息的镜头——观众需要读取时间。出处：Karel Reisz《电影剪辑技巧》："引入意外事实的镜头必须比重现熟物的镜头停留更久。"

- **揭示什么**：信息=读取成本（新线索 2-3s，熟物回扣 0.5s 即可）；错误示范=关键信物一闪而过被观众漏掉。
- **AI提示词写法**：`（时长规则，非画面提示词）——新信息 insert ≥ 2 秒，熟物回扣 insert ≤ 0.5 秒，写分镜表时在镜头时长列标注`

### 115. 焦点即权力（特写内的景深政治）

双人特写中，占优方在焦内、劣势方在焦外虚化；权力翻转时做焦点交接（rack focus）。出处：总纲法则40；《拯救大兵瑞恩》教堂戏：米勒颤抖的手在前景失焦，焦点让位给士兵们的注视。

- **揭示什么**：信息=权力关系（焦内=此刻的叙事主人）；情绪=被虚化的羞辱/被对焦的权重。可与角度即权力（法则14）叠加或故意错位。
- **AI提示词写法**：`close-up two-shot, the dominant character in razor-sharp focus, the other melting into bokeh; rack focus transfers sharpness as power shifts`

### 116. 指节发白握柄（White-Knuckle Grip ECU）

手部大特写：指节发白、缠带/刀柄勒进皮肉、伴随微颤，一滴血从指缝渗出。出处：EVA-01 握拳作画；《鬼灭之刃》日轮刀柄握紧的决意符号。

- **揭示什么**：信息=压抑到极限的决意或恐惧——身体先于意志表态，手比脸先"下决心"；是出手前的最后一格蓄能。
- **AI提示词写法**：`extreme close-up of a fist gripping a sword hilt, knuckles white, leather wrap digging into skin, a faint tremor, a drop of blood sliding between the fingers`

### 117. 阴影抬眼（Shadow-to-Light Eye Lift）

垂首、刘海遮眼→头部微抬→眼瞳自阴影中被一道硬轮廓光点亮。出处：《火影忍者》resolve shot 惯例；大量热血番"犹豫结束"的定式镜头。

- **揭示什么**：信息=犹豫结束、决意成立——一场戏的转折点；常接在特写预算的"逆转信号"格上。
- **AI提示词写法**：`close-up, head lowered with eyes hidden in the shadow of bangs, slowly tilting up, the eyes catching a hard rim light from the darkness, pupils steady`

### 118. 缠带渗血再握紧（Re-tightening Bloody Wrap）

已受伤的手用牙齿咬住松脱的缠带拉紧、再绕一圈，血渍加深，手指重新扣回武器。出处：负伤续战类作品的"拒绝退场"符号（浪客剑心/剑风传奇系手部作画）。

- **揭示什么**：信息=负伤续战、拒绝退场；把"还剩多少战力"写在一只手上，无需台词。
- **AI提示词写法**：`close-up of an injured hand pulling a cloth wrap tight with the teeth, blood-soaked bandage, jaw clenching, fingers flexing back around the weapon`

### 119. 拔刀居合（Iai Draw / Saya Thrust）

拇指抵住刀镡向前一推，刀身松动半寸；随即刀刃贴着鞘口滑出，一线寒光沿刃纹走过。出处：《浪客剑心》逆刃刀出鞘瞬。

- **揭示什么**：战斗开始的信号音；拔刀速度即实力宣言，观众注意力被"一线反光"钉在刀上。
- **AI提示词写法**：`extreme close-up of katana tsuba, thumb pushing the guard forward, blade sliding out of the lacquered saya, a thin line of cold light traveling along the steel edge, subtle vibration at the sheath mouth, shallow depth of field`

### 120. 血振·纳刀（Chiburi & Sheathing）

手腕一翻挥落血珠，血在空气里划出弧线砸落地面；刀身归鞘到最后一寸"咔"地一顿；收刀完成的刹那，身后的敌人才缓缓倒下。出处：《座头市》《鬼灭》通用语法。

- **揭示什么**：胜负早在收刀前已分；"延迟倒地"是无敌流的标准句号，仪式感=碾压感。
- **AI提示词写法**：`close-up of the blade flicking downward, droplets of blood arcing off the edge and spattering on the ground, the katana returning into its sheath with a final click, hand resting on the hilt, dust settling`

### 121. 刀镡碰撞（Tsuba Clash）

两刀格挡，镡与镡咬死在一起，金属护手被压出轻微形变，火花从咬合点迸出，两把刀都在高频震颤。出处：《死神》一护 vs 白哉的锷迫り合い。

- **揭示什么**：力量对等的僵持；镡的形变和火花把"看不见的角力"变成看得见的金属哀鸣。
- **AI提示词写法**：`extreme close-up of two sword guards locked together, the metal tsuba denting under pressure, sparks bursting from the contact point, both blades trembling, sweat flicking off the steel`

### 122. 刀穗·缠带战斗动态（Tassel & Wrapping Motion）

刀穗随挥砍甩出鞭状弧线，格挡急停时穗子继续前甩再回落；柄上缠带被震松，一端在风里飘抖。出处：《浪客剑心追忆篇》。

- **揭示什么**：软质配饰是挥砍轨迹的"拖尾"，读出刀的速度与方向；缠带松脱=战斗烈度升级。
- **AI提示词写法**：`close-up of a katana hilt, the silk tassel whipping through the air following the swing, a loose wrapping cord unraveling and fluttering, motion blur on the tassel, the grip tightening`

### 123. 小道具崩坏特写（Prop Damage Cutaway）

斩击掠过后——发带断成两截缓缓飘落、纽扣崩飞旋转落地、眼镜镜片爬满裂纹从脸上滑脱。出处：《银魂》《Fate》惯用的物损代人损。

- **揭示什么**：不画伤口也能传达"刚才那刀有多险"；物的毁坏代替人的流血，合规的惊险标点。
- **AI提示词写法**：`slow-motion close-up of a severed hair ribbon drifting down in two pieces, a button spinning as it pops off and hits the ground, cracked glasses sliding off a face, fragments catching the light`

### 124. 武器损坏渐进（Progressive Blade Damage）

刃口先卷出一个小缺口；下一击缺口连成锯齿；裂纹从缺口向刀身中段蔓延；木刀被劈开露出白色茬口。出处：《鬼灭》炭治郎断刀、《海贼王》索隆换刀前兆。

- **揭示什么**：武器是角色生命条的外化——刀的崩坏进度=战斗倒计时，逼出下一阶段的觉悟。
- **AI提示词写法**：`extreme close-up of a chipped katana edge, a crack slowly crawling from the notch across the blade surface, metal fatigue lines spreading, a wooden sword splitting open to reveal fresh pale splinters, fragments falling`

### 125. 咬牙/牙龈（Clenched Jaw / Bared Gums）

强忍剧痛时咬肌在颧弓下绷出硬块，下颌角外扩；牙关紧咬到后槽牙外露，牙龈线清晰，单颗牙缝渗血沿牙龈下爬。出处：《剑风》格斯、《进击的巨人》艾伦变身前咬手。

- **揭示什么**：角色在"还能忍住"与"即将崩断"的临界点，痛苦被强行内化为身体张力。
- **AI提示词写法**：`extreme close-up of a clenched jaw, the masseter muscle bulging under the cheekbone, molar teeth exposed with a visible gum line, a thin thread of blood seeping between the teeth, jaw tendons straining, low-key dramatic lighting`

### 126. 呼吸白雾与喘息节奏（Ragged Breath Vapor）

力竭或严寒中，张口喷出的白雾一团比一团大，中间突然截断——牙齿咬住嘴唇强行屏住半口气，只剩鼻息两缕细烟断续漏出。出处：《鬼灭》炭治郎雪地修炼、《紫罗兰永恒花园》雪地喘息。

- **揭示什么**：克制本身是一种表演——角色在敌人/队友面前假装自己还没垮。
- **AI提示词写法**：`close-up on the lower face exhaling thick white vapor plumes in cold air, the breath rhythm abruptly cut off as teeth bite the lower lip, two thin streams of mist leaking from the nostrils, frost on the eyelashes, shallow depth of field`

### 127. 嘴角血丝（Trailing Blood Line）

不是喷血，是一根极细的血线从嘴角垂直拉长、在下巴汇成一滴悬而不坠；或鼻血被手背一抹在脸上蹭成半干涸暗痕。出处：《火影》洛克·李八门遁甲、《EVA》真嗣鼻血抹脸。

- **揭示什么**：伤势被压低呈现，观众读到的不是血腥而是"他还没停"。
- **AI提示词写法**：`close-up of a single thin blood thread trailing from the corner of the mouth down to the chin forming a suspended droplet, a smeared half-dried blood streak across the cheek wiped by a knuckle, matte skin texture, anime dramatic cel shading`

### 128. 含泪不落的眼睛（Tears Held Back）

泪膜在眼眶下缘积成一道弧形液面，随眼球微颤晃动、折射高光碎成光点；一滴泪悬在睫尖不落，角色反而瞪大眼睛阻止它坠落。出处：《紫罗兰》薇尔莉特"我不哭"名场面。

- **揭示什么**：倔强比嚎哭更痛——情绪已到极限，意志仍在压制。
- **AI提示词写法**：`extreme close-up of eyes with a trembling film of tears pooled along the lower eyelid, refracted highlights breaking into glittering points, a glistening wet waterline, a single tear hanging from the eyelash tip refusing to fall, a defiant wide-eyed stare, soft rim light`

### 129. 面部肌肉失控边缘（Twitching Forced Smile）

强撑的微笑只抬起嘴角，眼周肌肉完全没跟上（无杜兴微笑）；一侧嘴角高频小幅抽动，半张脸在笑半张脸在忍。出处：《死亡笔记》夜神月憋笑。

- **揭示什么**：角色正在撒谎或自我欺骗，且谎言快要装不下去了。
- **AI提示词写法**：`close-up of a forced half-smile with a twitching corner of the mouth, asymmetric facial muscles, one cheek quivering while the other strains, the eyes completely unmoved and hollow, an unsettling stillness`

### 130. 吞咽/喉结（Throat Swallow）

颈部特写：喉结先微微上浮、停顿半拍，然后沉重地滚落一次；颈侧颈动脉随心跳搏动可见；吞咽前唇部一次极轻的抿紧。出处：《进击的巨人》兵长决死前、《怪物》天马举枪前。

- **揭示什么**：决断前最后一秒的恐惧被身体诚实说出——嘴硬，喉咙不硬。
- **AI提示词写法**：`tight close-up on the neck and jaw, the Adam's apple rising with a half-beat pause then sinking in one heavy swallow, a visible carotid pulse throbbing on the side of the neck, muscles under the jawline tensing and releasing, a subtle lip press before the gulp, chiaroscuro side lighting`

### 131. 完整结印序列（Twelve-Seal Weaving）

双手在胸前按固定次序连续变换手印，指形一印接一印相扣，指尖拖出极淡的微光轨迹，最后一印在胸前定格锁死。出处：《火影忍者》十二地支印（子丑寅卯辰巳午未申酉戌亥，官方设定明言源自中国十二地支）与道教九字真言手印（临兵斗者皆阵列前行）。

- **揭示什么**：信息=术式规格（印链越长术越大，单手结印=高手特权）；情绪=施法者的专注与庄重。一镜到底不切分，双手同主体协同，是 AI 视频安全的法术前摇特写。
- **AI提示词写法**：`extreme close-up of two hands weaving a continuous sequence of intricate finger-signs at the chest, fingertips interlocking shape after shape, faint glowing trails following the fingertips, finishing on a final locked seal held at the sternum, steady locked-off camera, dim ritual lighting`

### 132. 指尖聚灵（Fingertip Spirit Charge）

并指成枪前指，一粒光珠在指尖由小到大持续凝聚膨胀，气流吹动袖口与碎发——把全身力量压缩到一点的蓄能预告。出处：《幽游白书》灵丸（灵气聚集在指尖形成能量球）；武侠剑指传统。

- **揭示什么**：信息=大招充能进度（光珠体积=威力档位）；情绪=孤注一掷。单点发光、无多体协同、无帧级节奏要求，WAN3 友好。
- **AI提示词写法**：`extreme close-up of two extended fingers held like a gun, a bead of glowing energy swelling steadily at the fingertip, sleeve cloth and stray hairs stirred by rising airflow, dark background, the point of light growing brighter and larger`

### 133. 张掌示空（Empty Palm Disarm）

握着武器的手缓缓张开五指、掌心外翻朝前亮出，武器从画面下缘沉出画框——主动解除杀意的手语。出处：西部片与剑戟片的对峙降级惯例（举掌示空=谈判开始）；与条目34（无力松开的五指）相反，这是清醒的、有意志的放手。

- **揭示什么**：情绪=放下杀意/示弱求谈；信息=战意值主动归零。对手未出手，战局已被这只手改变。
- **AI提示词写法**：`extreme close-up of a hand slowly uncurling from a weapon hilt, fingers opening one by one, the palm turning outward to show it empty, the weapon sinking out of the lower frame, tense stillness, hard side light`

### 134. 逐节攥拳（Finger-by-Finger Resolve Curl）

摊开的手掌从小指开始逐节收拢，无名指、中指、食指依序扣下，最后拇指压紧锁成拳——决意在指间成形的慢动作。出处：少年漫定式作画（鸣人攥护额、炭治郎收掌握锷）；与条目31（已紧的拳继续加压）相反，本条拍"从松到紧"的生成过程。

- **揭示什么**：情绪=犹豫→决意的转化在此刻完成；信息=下一段攻防的发令枪。攥住的对象（护额/信物/刀锷）即动机本体。
- **AI提示词写法**：`extreme close-up of an open palm, fingers curling inward one segment at a time starting from the little finger, the thumb finally locking over a tight fist, cloth bandage creasing with the motion, dramatic side lighting, dust drifting`

### 135. 刀尖微颤（Tremor Transmitted to Blade Tip）

握刀的手极力稳持，颤抖却沿手臂一路传到刀尖，寒光在刃尖小幅高频地晃——恐惧瞒得过脸，瞒不过刀。出处：剑戟片对峙惯例（刀尖颤动=武士内心外化）；条目30"颤抖之手"的武器化变体。

- **揭示什么**：情绪=强撑的恐惧或透支；信息=体力见底（连刀都握不稳了）。颤抖由武器说出，比直拍手抖多一层物证。
- **AI提示词写法**：`extreme close-up of a sword blade tip quivering in small rapid shivers, cold light flickering along the edge, a straining grip barely visible at the frame edge, shallow depth of field, oppressive quiet`

### 136. 咬破拇指血契（Blood-Seal Thumb Bite）

牙齿咬破拇指指肚，血珠涌出，随即这只血手按向地面/卷轴/掌心画出血印——以血为钥匙的契约仪式。出处：《火影忍者》通灵之术（咬破拇指提供血祭，结印后按地成召唤阵）；东方歃血为盟原型。

- **揭示什么**：信息=召唤/血契类术式启动（耗血=代价可视化，呼应总纲资源可视化）；情绪=破釜沉舟。咬合与按压两个连续动作、单主体、无群演，一镜可完成。
- **AI提示词写法**：`extreme close-up of teeth biting the ball of a thumb, a bead of blood welling up, the bloodied thumb pressing firmly onto a marked surface, a crimson smear spreading under the print, dim atmospheric light`

### 137. 拳峰命中的面部涟漪（Hisashi Punch Cheek Ripple）

拳头陷进脸颊，以接触点为圆心，皮肉像水面一样荡开一圈圈同心波纹，嘴唇与眼睑被波峰推得变形外翻——慢速放大把打击翻译成流体力学。出处：日漫作画"久パンチ"（Hisashi Punch，命中强调型长顿拳，面部扭曲+效果线+黑白化为其标配，sakugabooru 列为署名技法）；写实来源为慢放拳击影像中面部压缩波的传播。

- **揭示什么**：信息=打击量级（波纹幅度与圈数=力量读数）；情绪=痛感的物理化转译。与条目107（负片白闪）联用：剪辑层与画面层双重痛感。
- **AI提示词写法**：`extreme close-up in extreme slow motion of a fist sinking into a cheek, concentric ripples of skin spreading outward from the knuckle contact point like rings on water, lips and eyelid pushed out of shape by the passing wave, dramatic side lighting`

### 138. 刀背拍击·峰打ち（Mine-uchi Flat Slap）

刀身翻转以宽面拍中目标：一声闷响，被拍处整片皮肉被宽面压扁、横向荡开，衣料与头发被风压掀起，目标踉跄而不流血——与刀刃切入"只留下一道延迟渗血的细红线"完全相反的反馈语言，拍=制服，切=杀伤。出处：剑戟片"峰打ち"（以刀背/刀面击倒而不杀）传统，逆刃刀原型（《浪客剑心》不杀之誓的物化）。

- **揭示什么**：信息=手下留情的意志（观众凭反馈形态读出"他本可以杀"）；情绪=克制的强者美学。提示词按"拍"写，切勿混入刃线。
- **AI提示词写法**：`slow-motion close-up of the flat side of a katana slapping into a shoulder, flesh compressing broadly under the wide steel surface, fabric and hair blasted outward by the air pressure, no blood, the victim staggering from the dull impact`

### 139. 皮肤凹陷与回弹（Skin Dent & Rebound）

接触点的皮肤先被压出一个深窝，施力物离开后凹陷回弹复原，余震让脸颊/腹部软组织轻轻颤动数下才静止——肉体的弹性复位是"真打到了"的签名，无此凹陷则打击像穿过纸片。出处：慢动作拳击实拍的面部压缩-复原全程；2D 打击动画 stagger-recoil 原理中 squash 峰值的弹性回落。

- **揭示什么**：信息=承力的物理证据（凹陷深度=力量，回弹速度=肉体年轻/老练）；情绪=痛感的前奏帧外叙事。
- **AI提示词写法**：`extreme close-up of skin dimpling deeply at the exact point of contact, the dent holding briefly then springing back as soft flesh rebounds and trembles into stillness, visible skin texture, harsh raking light`

### 140. 接触点同心冲击波（Contact-Point Shockwave Rings）

命中的刹那，一圈圈半透明环状气浪以接触点为圆心急速扩张，尘埃与碎屑被环面推离，空气出现热浪般的折射扭曲——日式作画把"力"画成看得见的同心圆。出处：anime shockwave/円形エフェクト 演出传统（手绘 2D 同心环是打击重音的标准符号）。

- **揭示什么**：信息=能量释放的方向与半径（环数与直径=威力档位）；情绪=轰击体感的放大器。单源扩张、无多体协同，WAN3 友好。
- **AI提示词写法**：`close-up of translucent concentric shockwave rings expanding rapidly outward from the exact point of impact, dust and small debris pushed away by each passing wave front, heat-haze air distortion, dark background, hand-drawn anime effect style`

### 141. X光透视骨骼受创（X-Ray Bone Impact）

整颗镜头以透视风格渲染：皮肉半透明化，露出内部骨骼，受力点裂出放射状纹路并在慢速推进中逐段蔓延——体外不可见的真实伤害被直接陈列。出处：《真人快打》（Mortal Kombat，2011 重启起）X-Ray Move 定式：动作减速、皮肉剥离、骨骼碎裂的内部解剖视角。

- **揭示什么**：信息=真实伤害等级（骨裂 vs 皮肉伤的官方判读）；情绪=残忍的解剖学凝视。一部作品用一次即定格战力差，滥用即麻木。
- **AI提示词写法**：`slow-motion x-ray style close-up, skin and muscle rendered translucent to reveal the bone beneath, radiating fracture lines spreading from the impact point across the bone surface, clinical blue-grey palette, dark background`

### 142. 击中瞬间汗与唾液飞溅（Sweat & Saliva Ejecta）

命中的刹那，积在皮肤上的汗珠与口中唾液被震离体表，以接触点为源呈放射状水雾喷出，逆光中每颗液滴被逐一点亮——体液的离弦是打击速度与人此前体力消耗的物证。出处：拳击慢放摄影的"汗雾"现象；《第一神拳》液体拖影（liquid smears）作画传统——汗与血珠在命中瞬间脱离身体飞行。

- **揭示什么**：信息=此前鏖战的存量证据（汗量=消耗时长）；情绪=暴力的美学化瞬间。逆光与暗背景是液滴可读的前提。
- **AI提示词写法**：`extreme slow-motion close-up of sweat beads and saliva bursting off a face from the point of impact, a radial spray of droplets each caught and lit by hard backlight, skin rippling beneath the ejecta, dark background`

### 143. 巨物角质层与旧疤年表（Hide Texture & Scar Chronicle）

低机位仰拍巨物躯干的一小块皮肤：龟裂的角质鳞片、层层叠压的旧疤与新生组织共存，侧逆光把每道棱线刻出深影，随呼吸缓缓起伏——战绩与年龄刻在皮上的年表，全貌始终不出画。出处：《真·哥斯拉》(2016) 焦黑表皮裂缝间透出熔红瘢痕组织的设定（"molten scar tissue glows blood red between the cracks in its charred hide"）；《哥斯拉 Minus One》(2023) 剥落鳞片近似辐射伤痕的质感；巨兽造型的 battle-worn 战损涂装传统。

- **揭示什么**：信息=这只巨物的战斗履历与自愈史（疤=杀不死的物证）；情绪=不可战胜的先验。与条目79（人类新伤叠旧疤）同源，本条为巨物尺度版本。
- **AI提示词写法**：`extreme close-up, ground-level low angle looking up at a colossal creature's hide filling the frame, cracked keratin scales layered with old pale scars and fresh dark tissue, raking side light carving deep shadows into every ridge, the skin slowly rising and falling with breath, battle-worn texture`

### 144. 巨物鼻息吹袭（Kaiju Nostril Blast）

巨物头颅不入画，只有两只黑洞般的鼻孔悬在画幅上方；一声闷响，滚烫鼻息喷下，主角的头发、衣摆、身周的尘与雾被同一股气流压向一侧，鼻孔边缘黏液被吹出细丝——它只是在呼吸，对主角已是风暴。出处：《侏罗纪公园》(1993) 霸王龙鼻口贴脸嗅探格兰特段落（原著："black flaring nostrils just inches away... startling hot breath on his face"）；音效师 Gary Rydstrom 录鲸豚喷气孔呼吸合成霸王龙吐息。

- **揭示什么**：信息=体量差（它的日常生理=你的灭顶之灾）；情绪=被当成猎物的生理性恐惧。气流单向、单一主体动作，WAN3 友好。
- **AI提示词写法**：`ground-level low-angle close-up, two huge dark nostrils of an unseen giant creature hanging at the top of frame, a sudden hot exhale blasting downward, the protagonist's hair and clothes whipped flat to one side, dust and mist blown away in one direction, moisture streaming from the nostril edges`

### 145. 阴影先行吞没（Shadow Swallows First）

巨物本体未至，投影先到：地面上的阳光被一道移动的阴影边界缓缓吞没，主角仰头看着自己整个人被罩进黑暗，随后才有巨物的局部（下颌线/趾爪/鳞缘）进入画幅——威胁按"影→局部→本体"逐层递进，本体始终不全露。出处：加里斯·爱德华斯《哥斯拉》(2014) "把怪兽当自然灾害拍"的街头人视低机位体系；本多猪四郎《哥斯拉》(1954) 人与怪兽永不同框的构图法则；AI 巨物提示词的标准锚定句式 "the shadow falling over a person"（Morphic 巨物视频库）。

- **揭示什么**：信息=体量超出画框（用光的变化量尺寸）；情绪=无处可逃的宣判。全程贴地人视，禁航拍禁俯视，呼应总纲法则39。
- **AI提示词写法**：`ground-level low-angle shot, sunlight on a street slowly consumed by the advancing edge of an enormous shadow, the protagonist looking up as darkness covers their body, then only the lower jawline and scaly edge of the giant creature entering the frame, the full body never shown`

### 146. 巨眼扫视锁定（Scanning Eye Lock-On）

巨物单眼占满画幅（呼应条目81的尺度宣告），但重点在状态切换：眼球缓缓扫过一片区域，虹膜掠过主角方位后退回、骤停、对焦，瞳孔微微收缩，眼底映出主角的渺小身影——从"没看见"到"看见了"的生理瞬间。出处：Weta 总监 Joe Letteri 谈《霍比特人》史矛革眼部设计（多层眼球几何结构，"永远要读得出它的焦点在哪"）；《The Secret of NIMH》(1982) 大猫头鹰巨眼倒映女主全身的反光眼传统；索伦之眼 "You cannot hide. I see you."

- **揭示什么**：信息=已被标记（逃跑窗口关闭）；情绪=猎物被点名。与条目81的分工：81 宣告体量，本条宣告猎杀关系成立。
- **AI提示词写法**：`extreme close-up of a colossal creature's single eye filling the frame, the eyeball slowly panning across, then halting, sliding back and locking focus, the pupil contracting as a tiny human figure reflects in its glossy surface, layered iris detail, wet highlights`

### 147. 巨足落地扬尘环（Footfall Dust Ring）

贴地机位拍巨物一只脚掌自画幅上方进入、落下：趾爪先触地，全掌压实的瞬间地面龟裂，一圈尘环以落点为心向外炸开，近处碎石被震起又落下，脚掌边缘占据画面一半以上——不拍全身，一只脚就是全部尺度信息。出处：本多猪四郎《哥斯拉》(1954) 反复低机位拍足/尾摧毁建筑（"人与哥斯拉无法同框即巨大"）；《哥斯拉 Minus One》(2023) 摄影柴崎幸三以低角度强调足下碾压的平民视角。

- **揭示什么**：信息=单脚面积=体量读数（局部即尺度）；情绪=随机降临的死亡。尘环单源扩散，与条目140同心冲击波同语法。
- **AI提示词写法**：`ground-level close-up, a colossal foot descending from the top of frame, claws touching down first, then the full sole slamming the ground, cracks spiderwebbing outward, a ring of dust blasting outward from the impact point, nearby rubble bouncing, the foot filling half the frame, full body never visible`

### 148. 巨口深处炉光（Maw Throat Glow）

仰角贴近巨物微张的下颌：獠牙根根如立柱，涎丝在齿间拉断，口腔深处喉管随吸气一明一暗地透出炉膛般的红光，热气上涌使画面边缘的空气产生折射扭曲——它还未吐息，膛内已在装填。出处：《真·哥斯拉》(2016) 原子吐息前口腔与背鳍渐亮的"炉心"演出；《霍比特人：史矛革之战》(2013) 史矛革喉底火光先亮于喷焰的蓄力节拍；《侏罗纪公园》原著霸王龙张口段（滚热气息、齿列刮擦）。

- **揭示什么**：信息=吐息读秒（观众先于角色拿到倒计时）；情绪=死刑宣告的前摇。单主体、单一蓄力动作、无多体协同，WAN3 友好。
- **AI提示词写法**：`low-angle extreme close-up of a giant creature's slightly parted maw, massive fangs like pillars, saliva strands stretching and snapping between teeth, deep in the throat a furnace-red glow pulsing brighter with each slow inhale, heat haze distorting the air at the frame edges, mouth interior lit from within`

### 149. 怒极反笑（Laughing Mad Dislocated Face）

愤怒越过临界点，喉咙里先漏出一声气音，随即笑声炸开：嘴在大笑，眉心仍紧锁，眼眶通红蓄泪，半张脸怒半张脸笑地错位抖动——情绪系统短路时，输出端接错了线。出处：Laughing Mad 演出传统（AllTheTropes 词条：崩溃边缘的角色爆发出歇斯底里的笑）；《反叛的鲁鲁修》鲁鲁修崩溃狂笑段、《寒蝉鸣泣之时》黑化笑的颜艺传统。

- **揭示什么**：情绪=愤怒/绝望过载后的表情系统崩坏；信息=精神防线断裂的官方宣告。与条目129（失控假笑，社交面具承压）区分：129 是压着演，本条是压不住地炸；与条目96（怒极反静）互为两极——一个归零，一个短路。
- **AI提示词写法**：`close-up of a face bursting into laughter at the peak of rage, mouth wide in a laugh while the brows stay knitted and the eyes redden and glisten, one half of the face laughing and the other half twisted in fury, shoulders jolting with each burst, harsh overhead light`

### 150. 战栗蔓延（Shiver Creeping Up）

颤抖从指尖开始：先是捏着的物件被磕出轻响，随即小臂、肩膀、下颌逐段失守，牙关开始打颤，最后整个人缩肩弓背止不住地抖——恐惧不是一击命中，是从肢体末端一路烧上来的。出处：漫画"震え線/揺れ線"（furue-sen，画在物体或角色周围表示打颤的抖动线）作画传统；《拯救大兵瑞恩》米勒上尉手颤的全身化版本。

- **揭示什么**：情绪=恐惧/虚脱的传导路径（指尖→躯干=防线逐段告破）；信息=镇定额度已耗尽。与条目30（颤抖之手）与条目135（刀尖微颤）区分：那两条把颤抖锁在局部物证上，本条拍颤抖传遍全身的蔓延过程，单主体、一镜连续完成。
- **AI提示词写法**：`close-up of trembling fingertips, the shiver visibly traveling up the forearm to the shoulders, the jaw beginning to chatter, the whole body hunching and shaking uncontrollably, ragged visible breath, dim cold light`

### 151. 后颈寒毛倒竖（Nape Hair Standing Warning）

后颈特写：发根处的汗毛齐刷刷竖起，细小鸡皮疙瘩沿颈侧一路铺向耳后，角色本人尚未回头、尚未看见任何威胁——身体比眼睛先 0.5 秒收到警报。出处：武侠"后颈一凉"的直觉预警传统；《全职猎人》西索杀气感知段的生理外化；恐怖片威胁入画前的标准前奏帧。

- **揭示什么**：信息=危险已在近处（观众先于角色确认威胁存在）；情绪=爬虫脑的原始报警。与条目2（瞳孔骤缩，已看见恐怖的反射）区分：本条是"还没看见"的预警，那条是"已看见"的反射。单主体、单一皮肤细节动作，WAN3 友好。
- **AI提示词写法**：`extreme close-up of the back of a neck, fine hairs slowly standing on end, goosebumps spreading up toward the hairline, skin texture crisp, cold side light, the person frozen mid-motion`

### 152. 高频眼震（Quivering Eyes Overload）

情绪过载到临界，整颗眼球开始高频小幅震颤：虹膜在眼眶里碎抖，下眼睑肌肉跟着抽动，高光乱晃，却始终没哭、没喊、没动——全身只剩眼睛在说实话。出处：Quivering Eyes 演出传统（AllTheTropes：情绪濒临崩溃时眼球或眼中高光可见地颤动，通常预示决堤）；《夏日重现》慎平遇刺段"惊恐大脸+瞳孔震颤"的主观视角处理。

- **揭示什么**：情绪=崩溃前最后一格缓冲（眼球=唯一失守的器官）。与条目3（瞳孔地震·信念动摇）区分：3 是听到颠覆真相时慢速不规则的晃动、"世界观在震"；本条是恐惧/愤怒/狂喜过载下的连续高频震颤，面部其余部分全部僵死。
- **AI提示词写法**：`extreme close-up of a single wide eye, the iris trembling in rapid fine vibrations, the lower eyelid twitching, highlights scattering and shaking, the rest of the face rigid and motionless, muted cold palette`

### 153. 太阳穴青筋咬起（Temple Vein Clench）

咬肌全力收紧，太阳穴处颞肌绷出硬棱，一条青筋自发际线凸起、随脉搏一下一下地搏动，皮肤被撑得发亮——怒吼被咽回去了，血压没咽回去。出处：《鬼灭之刃》蝴蝶忍质问童磨段"额头爆满青筋"的写实系愤怒作画；漫符 cross-popping veins（💢，AllTheTropes 词条）的写实化变体。

- **揭示什么**：情绪=被强行内化的暴怒（嘴不说，血管说）；信息=距离动手还剩最后一层皮。与条目61（颈部青筋，发力/变身的输出证明）区分：61 是力量向外输出的解剖学，本条是愤怒向内挤压的压力表；与条目125（咬牙/牙龈）联用——125 拍下颌，本条拍颞部。
- **AI提示词写法**：`extreme close-up of a clenched temple, the temporal muscle ridged hard, a vein bulging from the hairline and pulsing visibly with each heartbeat, skin stretched and sheened, the locked jaw at the frame edge, low-key dramatic side light`

### 154. 无意识流泪（Tears Before Knowing）

一张茫然的脸：眼神涣散没有焦点，泪却自顾自成串往下掉，本人毫无知觉，直到泪滴落在手背上，才低头怔怔看着那点湿、抬手摸脸，指腹沾到泪水时愣住——"咦，我在哭？"出处：悲剧演出"身体先于意识哭泣"的最高级写法；《紫罗兰永恒花园》薇尔莉特情绪迟滞系演出传统。

- **揭示什么**：情绪=意识还没追上的巨大悲恸（身体已签收，大脑未拆封）。与条目95（无表情+一行泪，知情压制下的失控）与条目128（含泪不落，主动瞪眼阻止）区分：那两条的主角知道自己在哭，本条的主角是全场最后知道的人。流泪→察觉两个连续微动作、单主体，一镜可完成。
- **AI提示词写法**：`close-up of a blank dazed face with unfocused eyes, tears streaming down unchecked, one tear dripping onto the back of the hand, the person glancing down at the wet spot and slowly touching their own cheek, staring at the damp fingertip in bewilderment, soft desaturated light`

### 155. 白手帕拭血（Calm Blood-Wiping）

杀戮刚结束，他不急着离场：掏出白手帕，一根手指一根手指地擦，指缝、甲缘都擦到，动作慢得像餐后拭唇；擦完垂眼看一下帕上那摊红，随手让它飘落在地——血是别人的，体面是自己的。出处：黑帮片/黑色电影"拭血手帕"的优雅暴力传统（《教父》谱系）与汉尼拔·莱克特的礼仪化杀戮美学；《死神》蓝染惣右介"杀人不沾血"的从容演出；与麦克白夫人"Out, damned spot!"（负罪者搓洗不净的幻血）构成镜像——那是擦不净，本条是擦得净。

- **揭示什么**：情绪=零内疚、零肾上腺素残留（心率根本没上来）；信息=这对他不是战斗，是日常公务。与条目118（缠带渗血再握紧，己方伤痛的忍耐）对立：一痛一净。单主体、单一手部慢动作，一镜完成。
- **AI提示词写法**：`close-up of pale hands unhurriedly wiping blood from between the fingers with a white handkerchief, cleaning each finger and nail edge one by one, then glancing at the red stain and letting the handkerchief flutter down, unhurried elegant motion, soft cold light`

### 156. 歪头打量（Inquisitive Head Tilt）

他盯着对手看了两秒，忽然把头向一侧缓缓倾斜十五度，下颌不动、眼不眨、瞳孔不移，像猫盯甲虫、像孩童俯身观察蚁穴——不是威压，是标本观察。出处：《全职猎人》伊尔迷·揍敌客无表情歪头的招牌演出；猫科与猛禽捕食前的好奇性侧头行为（动物行为学：侧头=调整视差、重新测距猎物）；AllTheTropes "Quizzical Tilt" 演出传统的反派化。

- **揭示什么**：情绪=不带敌意的好奇（比敌意更瘆人——你不在他的对等坐标系里）；信息=实力差已被对方目测完毕。与库布里克凝视（低头抬眼的威压锁定）区分：那是捕食者的锁定，本条是观察者的测距；与条目117（阴影抬眼，敌意的重量）区分：本条轻得像在看虫子。单主体、单一颈椎慢动作。
- **AI提示词写法**：`close-up of a man slowly tilting his head to one side like a cat watching an insect, chin steady, wide unblinking eyes fixed forward, long hair swaying slightly with the tilt, face flat and expressionless, cold even lighting`

### 157. 真心鼓掌（Sincere Applause for the Foe）

对手挣扎着撑起半身，阴影里忽然传出鼓掌声——不疾不徐、每一下都拍实，掌心相击的脆响在空场里荡开；他踱出暗处，脸上挂着货真价实的欣赏笑容，手掌都拍红了，像刚看完一场值回票价的演出。出处：《蝙蝠侠：黑暗骑士》(2008) 小丑在拘留所为戈登晋升鼓掌段（希斯·莱杰的真心式喝彩演出）；《Hellsing》少校为敌人的精彩抵抗真诚喝彩的传统；AllTheTropes "Sarcastic Clapping" 的镜像变体——本条的恐怖在于毫无讽刺。

- **揭示什么**：情绪=真诚的愉悦（你的垂死挣扎=他的余兴节目）；信息=一切仍在他的剧本之内。与讽刺性慢鼓掌区分：讽刺版嘴角下撇、掌声敷衍，本条掌声饱满、笑容到位——真心实意才是最深的居高临下。单主体、单一鼓掌节奏动作。
- **AI提示词写法**：`medium close-up of a man stepping out of shadow while clapping slowly and steadily, each clap full and deliberate, a broad genuine smile of appreciation, palms reddening slightly from the applause, dim theatrical light`

### 158. 整理袖口与手套（Pre-Fight Cuff Adjustment）

开打前最后一秒，他低头慢条斯理地抚平袖口褶皱，逐指拉正白手套的指根，再把领口抚平——整套动作像出席晚宴而非赴死斗，全程没抬眼看对手一眼。出处：《黑执事》塞巴斯蒂安·米卡利斯动手前整理白手套的执事美学（"我不过是一介执事罢了"）；《王牌特工》"manners maketh man"的礼服暴力传统；击剑与拳手赛前整理装备仪式的反派化挪用。

- **揭示什么**：情绪=绝对的从容（这场架不配让他失仪——他是在为自己保持体面，不是为你）；信息=此战在他的日程表里只是一场约会。与条目119（拔刀居合，兵器仪式、锋芒外放）区分：本条是服装仪式、锋芒内收——越整齐越危险。单主体、手部整理细节。
- **AI提示词写法**：`close-up of white-gloved hands meticulously smoothing a shirt cuff, then pulling each finger of the glove taut one by one and adjusting a cufflink, calm unhurried motions, crisp black formal attire, cool window light`

### 159. 踩影而过（Stepping Across the Shadow）

低角度贴地镜头：倒地者的长影摊在地面，一双皮鞋不疾不徐走入画，不踩人、不绕路，鞋尖径直从影子的咽喉处碾过，步伐节奏纹丝不乱——连半拍停顿都欠奉。出处：日本民俗"影を踏む"（影=魂的外延，踩影即践踏其魂；影踏み游戏与冈本绮堂《影を踏まれた女》的民俗背景）的反派化运用；武侠片"胜者不回顾"走位传统的极简化。

- **揭示什么**：情绪=不恨、不怒、不屑——纯粹的顺路碾压（恨还承认对等，踩影连对等都不承认）；信息=战斗已结算，败者已被移出他的世界坐标。与踩头/补刀式残暴区分：那是还在意的泄愤，本条是已翻篇的轻蔑。倒地者全程静止作环境、行走者单一线性动作，无协同交互，一镜完成。
- **AI提示词写法**：`low-angle ground-level close-up of a fallen fighter's long shadow stretched across the floor, polished leather shoes walking into frame and stepping unhurriedly across the shadow's throat, stride never breaking, the motionless fallen figure blurred at the frame edge, harsh side light`

### 160. 笑眼温差（Smile Without the Eyes）

嘴角标准上扬、弧度完美得像量过，眼轮匝肌却全程罢工：眼周皮肤纹丝不动，眼神冷而稳，瞳孔里没有一丝笑意的倒影——同一张脸，下半张在春天，上半张在冬天。出处：Duchenne 微笑心理学（真笑必牵动眼轮匝肌，假笑仅动颧大肌——眼周是测谎仪）；《权力的游戏》培提尔·贝里席官方设定"his eyes don't smile when his mouth does"（嘴笑眼不笑的衣冠禽兽原型）；《死亡笔记》夜神月"计划通"笑容的温差演出。

- **揭示什么**：情绪=恒温的假意（不是装不出真笑，是不屑为你消耗真笑）；信息=眼前一切都在他的计算之内。与条目94（假笑真哭，面具承压开裂）与条目129（失控假笑，肌肉抽搐漏馅）区分：那两条的面具在崩、在漏，本条的面具完好如新——崩溃的假笑可怜，完美的假笑可怕。单主体、面部静态+单一嘴角动作。
- **AI提示词写法**：`extreme close-up of a face with a perfectly curved polite smile, the skin around the eyes completely still and unmoved, cold steady gaze with no amusement in the eyes, the contrast between the warm mouth and the frozen upper face, soft even lighting`

---

## 第十一编 · 余波静物类（战后静场，6 条）

> 打戏的最后一镜不是胜负，而是静。余波特写拍的是"世界重新接管画面"的过程：尘落、火灭、花至、雨洗、声归、蝶栖——六个确认"结束了"的静物级证据。全编单主体、零协同、一镜到底，专为 10 秒文生视频的收束帧设计。

### 161. 落尘归位（Settling Dust Return）

爆风掀起的尘与灰不再升腾，开始以肉眼可见的速度缓缓沉降，落在倒伏的躯体、断裂的兵刃与翻起的焦土上，给一切盖上一层均匀的灰白——世界在自行掩埋现场。出处：《萤火虫之墓》空袭后的"灾难静止"（the stillness of disaster：画面无一物移动，观众却感到炮弹休克）——高畑勋证明"落尘+静"比爆炸本身更有冲击；战争片尘暴落定后揭示尸横遍野的揭示性沉降（revelatory settling）传统。

- **揭示什么**：信息=战斗已结束（噪音源消失，重力重新接管世界）；情绪=炮弹休克后的空白哀悼。尘落速度=安静的程度。与本库战斗中的扬尘动势条目区分：那是"打"的尘，本条是"停"的尘。
- **AI提示词写法**：`close-up of fine grey dust slowly settling out of still air onto a fallen figure and a broken blade, particles drifting down through a single shaft of pale light, everything else motionless, monochrome grey stillness`

### 162. 最后一缕火舌（The Last Flame Guttering）

战场余焰烧到最后一根燃料，火舌忽然缩成豆大一点、左右摇晃两下，熄灭，一缕细烟笔直升起——光从画面上被抽走一格。出处：《银翼杀手》Roy 与 Tyrell 烛光戏（"The light that burns twice as bright burns half as long"）的烛灭=寿命隐喻；巴赞评《天色破晓》：火焰熄灭的那一刻才是悲剧的终点——火是与生命相连的最后一件物。

- **揭示什么**：情绪=终结的正式盖章（火灭=不再有东西在挣扎）；信息=热源/意志的彻底撤离。烟的直线=无风=世界已静止。
- **AI提示词写法**：`extreme close-up of the last small flame on a battlefield ember shrinking to a pinprick, wavering twice, then snuffing out, a single thin thread of smoke rising perfectly straight, the frame dimming`

### 163. 落花上断刃（Petal on the Broken Blade）

一瓣山茶/樱被风送到，轻轻搁在断刀的豁口上，瓣尖还颤了一下——最软的东西落在了最硬之物的伤口上。出处：《浪客剑心 追忆篇》尸体之上整朵落下的红色山茶（断头花，武士决绝的象征）；物哀（mono no aware）与"武士道之花是樱"的传统：以最短命的美为最短命的武士送葬。

- **揭示什么**：情绪=天地的吊唁（自然不问胜负，只祭无常）；信息=凶器已被缴械为静物。花瓣与金属的质感反差=余韵的容器。
- **AI提示词写法**：`close-up of a single red camellia petal drifting down and landing gently on the nicked edge of a broken katana, the petal trembling once on contact, soft dewy texture against cold scratched steel, shallow focus`

### 164. 雨洗血迹（Rain Diluting the Blood）

雨点开始敲下来，积在瓦砾间的血洼被打出涟漪，红色一丝丝化开、顺着低处的水流蜿蜒流走，颜色一路变淡——世界在自行清洗现场。出处：《浪客剑心 追忆篇》剑心冒雨回到血流成河的杀人现场、雨帘中血水交融的幕末挽歌；《七武士》终战大雨冲走一切、只留四座坟茔的清洗式收尾。

- **揭示什么**：情绪=冲刷而非抚平（淡了，不是没了）；信息=时间重新流动（雨=自然复工）。红色稀释的程度=距离"重新开始"的距离。
- **AI提示词写法**：`close-up of raindrops stippling a shallow puddle tinged with blood, the red bleeding into thin threads that drift and pale as the water overflows and trickles away through a crack, desaturated grey light`

### 165. 晨钟与鸟鸣回归（First Birdsong, Distant Bell）

死寂中先是一只鸟试探性地叫了一声，停顿，再叫；极远处一记闷闷的晨钟，一小群鸟掠过画框上缘——声音回来了，意味着世界同意继续运转。出处：《细红线》（The Thin Red Line）马力克反复在战场间隙插入鸟与自然的漠然镜头（自然不站队，只在场）；《平家物语》开篇"祇园精舎の鐘の声、諸行無常の響きあり"——钟声=无常的听觉锚点。

- **揭示什么**：信息=战斗已结算（声景从人工噪音切回自然底噪）；情绪=不带安慰的重启。第一声鸟鸣的迟疑=连世界自己也不确定是否安全了。声音靠文字描述写进场景氛围，画面只拍可视锚点（鸟/惊飞/晨雾）。
- **AI提示词写法**：`static shot of a mist-shrouded battlefield at dawn, a small bird hopping onto a broken spear, tilting its head, beak opening in song, a distant flock rising across the pale sky at the top of the frame, hushed first light`

### 166. 蝴蝶停在凶器上（Butterfly on the Weapon）

硝烟未散，一只蝴蝶穿过画框，不慌不忙收翅停在那把刚杀过人的刀镡上，翅膀一张一合地做着深呼吸——生命对死亡毫无兴趣，只当它是一块晒太阳的石头。出处：《西线无战事》结尾保罗伸手去够战壕泥地上的蝴蝶——影史最著名的"蝴蝶×战场"镜头（美对战场的不设防=致命的天真）；"断剑上的蝴蝶=冲突止息"的定型图像符号。

- **揭示什么**：情绪=漠然的慈悲（生命继续，不因谁的死而改行程）；信息=危险解除（蝴蝶只落在静止的东西上）。翅膀的一张一合=全画面唯一的动作=静的标尺。
- **AI提示词写法**：`close-up of a butterfly gently landing on the guard of a bloodied katana lying on scorched ground, wings slowly opening and closing, the blade and the blurred fallen figure beneath it completely still, soft diffused light`

---

## 参考来源

**特写理论与电影史**

- [Story2Board: What is Extreme Close-Up (ECU)?](https://story2board.com/glossary/extreme-close-up) — ECU 定义、Psycho 排水口/眼睛叠化、Requiem for a Dream 瞳孔母题
- [Backstage: Get in Tight With This Guide to Extreme Close-ups](https://www.backstage.com/magazine/article/extreme-close-up-shot-example-advice-76973/) — 银翼杀手2049、无耻混蛋、埃德加·赖特节奏论、LOTR 魔戒
- [CineD: Extreme Close-Ups and Their Place in the Visual Story](https://www.cined.com/extreme-close-ups-and-their-place-in-the-visual-story-with-film-examples/) — 广角 vs 长焦 ECU 的不同体感、ECU 三种叙事节奏
- [Backstage: How to Use Insert Shots in Film and Television](https://www.backstage.com/magazine/article/what-is-an-insert-shot-film-examples-75545/) — 插入镜头的六种职能、诺兰物件叙事、Reisz 停留律
- [HARTS/PCC: Closer and Closer — On Close-Ups in Film](https://www.pcc.edu/harts/2020/05/03/closer-and-closer-on-close-ups-in-film/) — 巴拉兹《电影理论》特写职能详解、"好的特写是抒情诗"
- [豆丁: 电影的"微相学"——特写镜头](https://www.docin.com/touch_new/preview_new.do?id=314436508) — 巴拉兹微相学原始论述、爱浦斯坦/普多夫金特写论、《飞越疯人院》65 秒特写、《克莱默夫妇》
- [牛津大学出版社博客(外研社转载): 影片中的面部特写缘何夺目](https://iyc.unipus.cn/book/detail/2458) — 巴拉兹：脸特写区分电影与戏剧
- [StudioBinder: The Kuleshov Effect Explained](https://www.studiobinder.com/blog/kuleshov-effect-examples/) — 库里肖夫效应与斯皮尔伯格变体
- [NFI: Kuleshov Effect](https://www.nfi.edu/kuleshov-effect/5/) — 希区柯克"纯电影"三段式（close-up → POV → reaction）
- [Movies and Collections: Kuleshov Effect 10 Films](https://cinenoir.net/style/montage/the-kuleshov-effect-10-architectures-of-audience-perception/) — 《战舰波将金号》《后窗》《惊魂记》《黄金三镖客》拉片

**西部片/莱昂内与手部电影**

- [Slant Magazine: Once Upon a Time in the West](https://www.slantmagazine.com/film/once-upon-a-time-in-the-west/) — 莱昂内开场"汗湿三人组"特写与苍蝇
- [Mank's Movie Musings: Once Upon a Time in the West](https://manksjoint.home.blog/2019/07/31/once-upon-a-time-in-the-west-sergio-leones-postmodern-fairy-tale-about-the-old-west/) — "Leone time"、布朗森眼部大特写
- [Tom Gunning: A Hand for Hitchcock (PDF)](https://www.crisiscritique.org/storage/app/media/2020-07-22/gunning.pdf) — 触觉电影、《惊魂记》Marion 滑落的手
- [Far Out: Why do Tom Hanks' hands shake during Saving Private Ryan?](https://faroutmagazine.co.uk/why-do-tom-hanks-hands-shake-during-saving-private-ryan/) — 颤抖之手的 PTSD 叙事
- [Movies and Collections: Cinematic Hands](https://cinenoir.net/style/visual-symbol/the-palpable-unspoken-a-deciphering-of-hands-in-film/) — 《大都会》《奥拉克之手》《奇爱博士》的手部符号学
- [Movies and Collections: Hand-Holding in Cinema](https://cinenoir.net/emotions/romance/sweet/tactile-resonance-the-geometry-of-hand-holding-in-cinema/) — 《爱在黎明破晓前》将触未触、《花样年华》
- [Knock on Wood: Lessons from the Wasteland — Close-Ups](https://knockonwoodfilm.com/2025/10/26/lessons-from-the-wasteland-close-ups/) — 《圣女贞德蒙难记》《卡萨布兰卡》单泪

**动漫作画与日式演出**

- [SAKUGAART: Yoshihiko Umakoshi](https://www.sakugaart.com/yoshihiko-umakoshi/) — 马越嘉彦与 Umakoshi Eye 谱系（Casshern Sins 定型）
- [3DJuegos: ¿Qué es el Sakuga?](https://www.3djuegos.com/manga-anime/noticias/que-sakuga-que-importante-para-anime-cuando-animacion-se-convierte-espectaculo) — Umakoshi eye / Kutsuna Lightning / Hisashi Punch 等署名技法
- [Le Dévorêve: Les techniques hommages](https://ledevoreve.wordpress.com/2025/02/14/les-techniques-hommages/) — Obari Pose、Yutapon Cube、Dezaki Freeze Frame（harmony cell）、Umakoshi Eye 出处编年
- [Danbooru Wiki: cut-in](https://safebooru.donmai.us/wiki_pages/cut-in) — 日式 cut-in 构图定义
- [祭禍@saika\_aiart: 技能发动カットイン提示词](https://topicdigg.com/x/saika_aiart/2046426251414630548) — AI 生成 cut-in 构图的提示词工程
- [Tumblr: Levi's Eye Panel in Chapter 132](https://104cadetlauren.tumblr.com/post/785874392647450624/) — 兵长眼部特写与悲伤五阶段分析
- [Wakoku: How Anime Emotions Bring Characters to Life](https://wakokujp.com/anime-emotions/) — 汗滴/爆筋/猫眼/鼻血等漫符系统
- [Art and Popular Culture: Manga iconography](https://artandpopularculture.com/Face_fault) — manga iconography 符号体系（速度线/汗滴/抽象背景）
- [Japanese with Anime (2020/03)](https://www.japanesewithanime.com/2020/03/?m=1) — 汗滴符号学、灯泡顿悟等日式视觉记号
- [Dattebayo: How to Draw Anime Faces](https://dattebayo.me/en/blog/how-to-draw-anime-faces) — 漫符（manpu）作为"标点符号"、眼睛即演员

**AI 视频提示词工程**

- [Runway: AI Camera Prompts](https://runway.com/resources/ai-camera-prompts) — AI 相机提示词公式 [Shot size]+[Angle]+[Movement]+[Subject]+[Lens]+[Lighting]+[Reveal]
- [Runway: How to Use Camera Angles in AI Generation](https://runway.com/resources/ai-camera-angle-shot-type-tips) — ECU 在 AI 生成中的特性
- [Kling: AI Prompt Guide](https://kling.ai/blog/kling-ai-prompt-guide) — 自然语言相机指令
- [Pixara: Runway Gen-4 Prompt Guide](https://www.pixara.ai/blogs/the-ultimate-runway-gen-4-prompt-guide-master-ai-video-on-pixara) — "眼中倒映城市"宏特写提示词实例
- [AI Magicx: AI Video Prompt Engineering 2026](https://www.aimagicx.com/blog/ai-video-prompt-engineering-advanced-guide-2026) — 景别术语表与导演级提示词框架
- [StudyRaid: Storyboarding for Animation — Close-Ups and Extreme Close-Ups](https://app.studyraid.com/en/read/103627/4638202/close-ups-and-extreme-close-ups) — "特写揭示情绪，大特写揭示信息"、Cut-in 转场、动画特写作画要点

---

*与《对战编排总纲》法则 4/16/19/27/35/38/39/40 联用；本库为活文档，实战返工教训持续沉淀。*
