# 条目简介总表

按分类列出每个 Markdown 文件的一句话简介，用于快速定位该读哪个文件。文件级目录结构见 [INDEX.md](INDEX.md)，调用约定也在那里。

共 **499** 个文件。

## 01-工具与模型（17）

| 文件 | 标题 | 简介 |
|---|---|---|
| [001-runway-gen3](01-工具与模型/001-runway-gen3.md) | Runway Gen-3 视频生成使用要点 | Gen-3 图生视频的提示词结构、参数控制与动漫短剧适配要点 |
| [002-kling-ai](01-工具与模型/002-kling-ai.md) | 可灵 Kling AI 视频生成使用要点 | 可灵图生视频/视频延长的提示词写法与动漫人物一致性策略 |
| [084-runway-gen3-tension-shot](01-工具与模型/084-runway-gen3-tension-shot.md) | Runway Gen3 张力镜生成技巧 | Gen3 善运镜不擅动作；用运镜建张力而非堆动作；锁定机位+缓推拉+单主体=稳 |
| [085-kling-tension-shot](01-工具与模型/085-kling-tension-shot.md) | Kling（可灵）张力镜生成技巧 | Kling 强动作连贯与物理感；适合打戏/转身/奔跑；提示词写动作链而非单帧 |
| [086-jimeng-action-tension](01-工具与模型/086-jimeng-action-tension.md) | 即梦/豆包 动作张力生成技巧 | 即梦中文理解最深；动作幅度可控；适合国风/二次元短剧；用分镜脚本式提示词 |
| [171-skill-anatomy](01-工具与模型/171-skill-anatomy.md) | Skill解剖学——SKILL.md结构与frontmatter字段 | Skill就两块：frontmatter决定"会不会被触发"，正文决定"触发后干得好不好"；90%的翻车死在第一块 |
| [172-skill-description-triggers](01-工具与模型/172-skill-description-triggers.md) | Description触发条件写法——Skill的名片与门神 | description是Agent决定是否调用的唯一依据；写what+when+边界三段，写流程=模型跳过正文直接自由发挥 |
| [173-skill-body-instructions](01-工具与模型/173-skill-body-instructions.md) | Skill正文指令写法——祈使句、边界与防啰嗦 | 正文是触发后才加载的上岗培训；祈使句打头、步骤显式编号、约束写成" Only if"句式，示例比形容词管用十倍 |
| [174-skill-examples-antipatterns](01-工具与模型/174-skill-examples-antipatterns.md) | Skill示例与反模式——七大死法与对应解药 | 网上流传的skill尸体解剖报告：无规划直接干、单体巨兽、无验证、硬编码工具链、无护栏、无状态、只测顺境 |
| [175-tool-orchestration](01-工具与模型/175-tool-orchestration.md) | 工具编排与多Agent协同——workflows怎么不翻车 | 编排不是堆Agent——分解任务、最小化共享状态、工具目标导向、有回退有预算，五步经典模式覆盖90%场景 |
| [176-knowledge-pipeline-skill](01-工具与模型/176-knowledge-pipeline-skill.md) | 知识沉淀型Skill——从学到存的流水线 | 知识型skill不是搜索引擎——结构化输出、可复用模板、自动归档，把学到的东西变成下次能直接调用的资产 |
| [177-process-skill](01-工具与模型/177-process-skill.md) | 流程型Skill——确定性任务的执行引擎 | 流程型skill追求一次做对——入口校验、步骤编号、中间落盘、出口验证，每个状态点都可审计 |
| [178-skill-testing](01-工具与模型/178-skill-testing.md) | Skill测试与验证——不写测试的skill等于裸奔 | 测试不是"跑通就行"——触发测试、输入测试、输出验证、异常注入、回归测试，五层防线缺一不可 |
| [179-skill-maintenance](01-工具与模型/179-skill-maintenance.md) | Skill迭代与维护——版本不维护等于过期食品 | skill写完才是开始——翻车记录、用户反馈、能力扩展、定期体检，维护才是skill的生命线 |
| [180-skill-system-design](01-工具与模型/180-skill-system-design.md) | 个人Skill体系设计——从散装到编队 | 散装skill是消耗品，编队skill是资产——领域划分、命名规范、依赖图谱、调用地图，一次设计终身受益 |
| [181-capability-map](01-工具与模型/181-capability-map.md) | 能力总图——479条知识库调用地图 | 479条知识条目的导航地图——按任务场景查条目，按问题症状找修法，让知识库从仓库变成武器库 |
| [447-wan3-calibration-baseline](01-工具与模型/447-wan3-calibration-baseline.md) | WAN3.0 校准基线——全库对标基准（30秒/30fps/1080P/原生音画） | WAN3.0 是全库基准模型：30秒/30fps/1080P 单次生成、原生音画（对话+BGM+音效）、10图+5视频+5音频多模态参考、本地编辑；所有旧条目需按此校准 |

## 02-提示词技巧（59）

| 文件 | 标题 | 简介 |
|---|---|---|
| [003-镜头运动提示词](02-提示词技巧/003-镜头运动提示词.md) | 镜头运动提示词词库 | 推/拉/摇/移/跟/升降等镜头运动的英文提示词与适用场景 |
| [040-tension-prompt-templates](02-提示词技巧/040-tension-prompt-templates.md) | 张力构建提示词模板汇总 | 汇总前29条张力技法的可复用提示词模块，按蓄势/峰值/释放三段拼接即用 |
| [087-midjourney-tension-storyboard](02-提示词技巧/087-midjourney-tension-storyboard.md) | Midjourney 张力分镜图生成 | MJ 先出关键帧锁定构图光影，再喂视频AI动起来；分镜图是张力骨架 |
| [111-prompt-formula-structure](02-提示词技巧/111-prompt-formula-structure.md) | 提示词公式化结构（七段式） | 把散装脑洞压成公式=可控出图；场景+主体+动作+镜头+光影+风格+参数七段式 |
| [112-negative-prompt](02-提示词技巧/112-negative-prompt.md) | 负向提示词（negative prompt / --no） | 告诉AI别生成什么=主动排除崩坏；SD 用 negative 字段，MJ 用 --no |
| [113-style-reference-lock](02-提示词技巧/113-style-reference-lock.md) | 风格锁定（--sref / --cref / 参考图） | 全片统一=锁风格锁角色；MJ 用 --sref 锁色质纹理，--cref 锁人脸发型 |
| [114-parameters-tuning](02-提示词技巧/114-parameters-tuning.md) | 权重与参数调优（chaos/stylize/seed/权重） | 参数是提示词的旋钮；chaos 管变化，stylize 管风格化，seed 管可复现 |
| [115-camera-vocabulary](02-提示词技巧/115-camera-vocabulary.md) | 镜头词汇库（运镜/景别/角度/焦段） | 镜头词是提示词的肌肉；景别+运镜+角度+焦段四件套英文词库 |
| [116-lighting-vocabulary](02-提示词技巧/116-lighting-vocabulary.md) | 光影词汇库（布光/色调/对比/质感） | 光影是张力命脉；布光位置+色调+对比+质感四类英文词库 |
| [117-action-vocabulary](02-提示词技巧/117-action-vocabulary.md) | 动作词汇库（动作链/物理/惯性） | 动作是视频的灵魂；预备+主动作+余动+模糊四段动作链 |
| [118-mood-atmosphere-vocabulary](02-提示词技巧/118-mood-atmosphere-vocabulary.md) | 情绪氛围词汇库（意境/情绪/氛围） | 氛围词是镜头词之外的张力调味；按情绪族分类的英文词库 |
| [119-reference-image-tecunique](02-提示词技巧/119-reference-image-tecunique.md) | 参考图与垫图技法（图生视频/角色锁定/构图锁） | 参考图是控制AI最硬的手段；sref/cref/ControlNet/IP-Adapter/LoRA 分工 |
| [120-prompt-debugging-tips](02-提示词技巧/120-prompt-debugging-tips.md) | 提示词避坑与调试（迭代/seed抽选/单变量） | 出图崩别瞎改；定性失败改结构，随机失败换seed，一次一个变量 |
| [141-h3-camera-command-syntax](02-提示词技巧/141-h3-camera-command-syntax.md) | H3运镜指令语法（[指令]格式完全指南） | H3的运镜不靠自然语言祈祷，靠方括号指令系统；15种指令是精确制导 |
| [142-h3-prompt-structure](02-提示词技巧/142-h3-prompt-structure.md) | H3提示词结构（主体+动作+场景+运镜+光线+声音） | H3提示词六件套：主体/动作/场景/运镜/光线/声音；按序组装，缺一补一 |
| [143-wan3-prompt-formula](02-提示词技巧/143-wan3-prompt-formula.md) | Wan3.0提示词公式（官方结构与分镜写法） | Wan系公式=主体+场景+运动；进阶版加镜头/光影/氛围；3.0支持分镜式Shot写法 |
| [144-wan-first-last-frame](02-提示词技巧/144-wan-first-last-frame.md) | Wan首尾帧技法（图生视频的最高控制度） | 首帧定起点尾帧定终点，AI只负责走中间——首尾帧是把随机性关进走廊 |
| [145-h3-vs-wan-selection](02-提示词技巧/145-h3-vs-wan-selection.md) | H3 vs Wan选型指南（场景对照表） | 同一段提示词喂给两个模型，谁强用谁；先搞清楚各自的脾气 |
| [146-universal-prompt-principles](02-提示词技巧/146-universal-prompt-principles.md) | H3/Wan通用提示词铁律（单一动作/幅度控制/动词优先） | 一个镜头只干一件事，动作幅度写出来，动词比形容词值钱 |
| [147-h3-command-combo-rhythm](02-提示词技巧/147-h3-command-combo-rhythm.md) | H3指令组合与镜头节奏（并发/顺序的编排艺术） | 同括号是同时，分括号是先后；指令的排列组合就是镜头内部的剪辑 |
| [148-wan-multishot-prompt](02-提示词技巧/148-wan-multishot-prompt.md) | Wan3.0多镜头分镜提示词（Shot格式深入） | Wan3.0的Shot [时间码]格式=一条提示词生成整场戏；但每Shot仍要守单镜纪律 |
| [149-h3-wan-troubleshooting](02-提示词技巧/149-h3-wan-troubleshooting.md) | H3/Wan避坑速查（高频翻车与对症修法） | 脸崩/手崩/乱动/漂移/换人的对症处方；先查语法层再查语义层 |
| [150-h3-wan-hybrid-workflow](02-提示词技巧/150-h3-wan-hybrid-workflow.md) | H3+Wan混合工作流（短剧全链路实战） | 从剧本到成片的标准管线：Shot原型→逐镜精做→锚点接力→音画缝合→连贯QA |
| [265-ai-creature-consistency](02-提示词技巧/265-ai-creature-consistency.md) | AI视频动物一致性——种子/主参考图/锚词三重锁定 | 动物比人更容易"换脸"：固定种子＋唯一主参考图＋锚词三件套锁定；禁链式引用上一镜输出，禁锚词漂移 |
| [276-dragon-palms-vfx-styles](02-提示词技巧/276-dragon-palms-vfx-styles.md) | 降龙掌视觉表现——龙形气劲与写实掌风的AI生成双方案 | 降龙掌特效两条路线：97式金龙气劲 vs 03式写实掌风；各自提示词模板与混用禁忌 |
| [281-invisible-qi-blade](02-提示词技巧/281-invisible-qi-blade.md) | 无形气刃表现法——"看不见的剑"如何让观众看懂 | 无形攻击类武功的三锚点表现法：发招姿态/介质扰动/受击反馈，拒绝光剑化 |
| [290-zhenqi-huaxing-levels](02-提示词技巧/290-zhenqi-huaxing-levels.md) | 真气显形四级制——化形的高级与廉价分水岭 | 真气从无形到凝实的L1-L4分级法，高级化形四特征与页游感四禁忌，全剧特效口径决策表 |
| [305-ai-video-impact-frame-prompts](02-提示词技巧/305-ai-video-impact-frame-prompts.md) | AI视频冲击帧提示词法——能与不能 | 当前AI视频模型生成冲击帧的能力边界——提示词可诱导的类型、不可控的帧级精度、以及"生成端诱导+后期端保底"的双轨策略 |
| [348-vfx-believability-overview](02-提示词技巧/348-vfx-believability-overview.md) | AI视频特效十连①——特效可信度总纲：交互、尺度、摄影机反应（特效不是贴片） | AI视频的VFX是烤进像素的单条成片而非可分层合成；可信=周围世界承认特效存在（光溢出/重力/位移）+尺度词+摄影机受惊；三条用途边界 |
| [349-fire-explosion-vfx](02-提示词技巧/349-fire-explosion-vfx.md) | AI视频特效十连②——火焰与爆炸：交互照明、火星重量、热浪减法、爆炸节拍 | 火假是因为周围不承认它存在；写光照结果不写光源动作；热浪用减法次级修饰；爆炸=点火拍+压力波+尺度碎片+摄影机震+余烟 |
| [350-water-fluid-vfx](02-提示词技巧/350-water-fluid-vfx.md) | AI视频特效十连③——水与流体：皇冠水花结构、镜面高光、雨的五层、体积不守恒警告 | 流体是全门类天花板最低（无流体模拟、体积不守恒）；水花真实感70%由静帧镜面高光决定；先写主水片再写边缘水滴与折射；雨要写下落+湿面+前后景分层 |
| [351-lightning-energy-beam-vfx](02-提示词技巧/351-lightning-energy-beam-vfx.md) | AI视频特效十连④——雷电电弧与能量束：起止点锚定、瞬时节拍、体积光GI、霓虹管病 | 电弧必须给源点与终止点否则悬浮；三层公式源+路径+环境响应；瞬时(0.1-2s)/持续/闪烁核心三时态；均匀霓虹管病加内部湍流；能量束走持续连贯逻辑 |
| [352-wind-smoke-dust-gas-vfx](02-提示词技巧/352-wind-smoke-dust-gas-vfx.md) | AI视频特效十连⑤——风烟尘气：描述空气而非颗粒、电影形容词替代物理术语、60%运镜律 | 烟的体积靠密度衰减+被排开；引擎按整场隐含力算烟——写空气不写蒸汽；turbulence等物理词触发高频抖动噪点，用steady plume/lazy drift；风不可见须借载体 |
| [353-ice-earth-rbd-destruction](02-提示词技巧/353-ice-earth-rbd-destruction.md) | AI视频特效十连⑥——冰雪、岩土与刚体破碎：材质重量词、落序、地面冲击环、冻结生长 | 重力不是模拟是猜的——必须点名材质与重量，石膏板与钢梁落法不能相同；碎块最大先落尘缓落；冰戏写晶体折射/霜花生长/碎冰抛射/冰火蒸汽 |
| [354-light-energy-volumetric-vfx](02-提示词技巧/354-light-energy-volumetric-vfx.md) | AI视频特效十连⑦——体积光、魔法光与全息：光矢锁定、密度基准、廉价发光病 | 光束可见必须先有颗粒介质；跨镜用钟面法锁光矢+密度基准（约40%遮挡）；魔法光靠打脸/尘粒/电弧跳边才不假；廉价发光病=均匀亮+无暗部+bloom泛滥 |
| [355-effect-character-interaction](02-提示词技巧/355-effect-character-interaction.md) | AI视频特效十连⑧——特效×人物环境交互：接触科学、手持能量、变身中间态、分区运动笔刷 | 特效与人同框要把六种接触面写全（光/身/衣发/地/道具/空气）；手持能量写指缝透光与手臂受力；变身必须显式描述中间态；I2V首帧+运动笔刷分区+角色实体双挂 |
| [356-post-compositing-pipeline](02-提示词技巧/356-post-compositing-pipeline.md) | AI视频特效十连⑨——后期合成路线：元素板、混合模式、交互光伪造、跟踪与调色统一 | 交付级特效走"AI底板+元素合成"：黑底火板用screen/add、烟用亮度键、阴影multiply；跟踪→roto→放元素→光包裹/脸光伪造→投影→Lumetri+匹配颗粒；时机帧级可调 |
| [374-skill-visual-prompt-pipeline](02-提示词技巧/374-skill-visual-prompt-pipeline.md) | 技能魔法编写二十连⑰——技能视觉开发管线：从能力卡到提示词模块的七步翻译 | 机制文档→签名特效规格→色板声音档→正典关键帧→可复用提示词模块→元素板→分镜提示装配；每能力一套固定串全剧复用；招名禁入提示词 |
| [378-skill-magic-vfx-overview](02-提示词技巧/378-skill-magic-vfx-overview.md) | 技能魔法特效与提示词模板二十连①——总纲：特效制作全景与提示词五锁层结构 | 技能魔法特效的两条生产线（传统VFX概念→AI直接生成）；优质提示词=镜头/光效/运镜/元素色板/主体克制五锁层+方向速度次生交互物理词汇；一条咒语一个元素一个峰值帧 |
| [379-fire-explosion-vfx-prompts](02-提示词技巧/379-fire-explosion-vfx-prompts.md) | 技能魔法特效与提示词模板二十连②——火焰与爆炸：冲击波层级、热量光效与模板 | 火焰特效的核心不是"颜色"而是层级：核心→焰舌→余烬→热浪扭曲→地面烟尘；爆炸要写出冲击波速度曲线+次生尘雾；提供3套直接复制的英文提示词模板 |
| [380-lightning-vfx-prompts](02-提示词技巧/380-lightning-vfx-prompts.md) | 技能魔法特效与提示词模板二十连③——雷电与电弧：源-终点坐标、电流脉冲与湿面反光 | 雷电特效的命门是"起点和终点"：AI必须知道电弧从哪里来、打到哪里，否则只会画天空闪电；用蓝白等离子+环境湿面反光+闪烁硬阴影制造高能感；提供3套模板 |
| [381-ice-frost-vfx-prompts](02-提示词技巧/381-ice-frost-vfx-prompts.md) | 技能魔法特效与提示词模板二十连④——冰霜与寒气：冰晶层级、冻结冲击波与折射率 | 冰霜特效的核心是折射率与层级：冰晶必须透明折射光线而非发光；冻结冲击波要写出"霜纹扩散→冰层生长→蒸汽凝结"的时间顺序；提供3套模板 |
| [382-water-liquid-vfx-prompts](02-提示词技巧/382-water-liquid-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑤——水流与液体魔法：高光衰减、粘性控制与慢动作皇冠 | 液体特效真实度70%取决于静态帧的高光衰减而非运动提示词；水系魔法要区分清水/粘稠液/蒸汽三态；慢动作液体皇冠是最高性价比镜头；提供3套模板 |
| [383-wind-air-vfx-prompts](02-提示词技巧/383-wind-air-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑥——风与气流：无形之力的视觉代理、压缩空气与龙卷风分级 | 风是看不见的：必须选至少两个视觉代理（头发/布料/植被/碎片）锚定风的存在；先定风速风向再写提示词；压缩空气爆发与螺旋气流是AI可识别的魔法风；提供3套模板 |
| [384-earth-rock-vfx-prompts](02-提示词技巧/384-earth-rock-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑦——岩石与大地：裂纹路径、重量感与尘雾层级 | 大地魔法的核心是重量与裂纹：石柱必须缓慢升起+地面开裂+尘雾滚落，不能轻飘飘；裂纹要有方向性路径；提供3套模板 |
| [385-light-holy-beam-vfx-prompts](02-提示词技巧/385-light-holy-beam-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑧——光效/圣光/能量束：体积光三要素与光束分层结构 | 光效AI生成第一死因是"看起来像画上去的"——缺散射介质；体积光必须同时写光源+介质+遮挡三要素；光束分核心/光晕/内部粒子/环境影响四层；色温即情绪（2000K暖金=安全，6500K冷白=孤绝）；提供3套模板 |
| [386-shadow-dark-mist-curse-vfx-prompts](02-提示词技巧/386-shadow-dark-mist-curse-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑨——暗影/黑雾/诅咒：吸收光、触须活体感与腐败分层 | 暗影特效第一死因是"像黑色烟雾贴图"——必须写核心色（深紫靛而非纯黑）+内部纹理+行为动词（clinging/writhing/solidifying）；黑雾要分层（核心色/纹理/行为/内光/内部元素）；触须必须像活物（liquid smoke/resisting/writhing）；提供3套模板 |
| [387-healing-life-magic-vfx-prompts](02-提示词技巧/387-healing-life-magic-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑩——治疗/生命魔法：四阶段结构、暖流方向与复活物质重组 | 治疗特效必须用四阶段结构（起源→成形→高潮→余韵）否则像静态贴图；治疗光从施法者手中"流出"而非"射出"；绿色不等于治疗——金/翠绿/白/琥珀对应不同治疗流派；复活=物质重组（身体由元素编织成形）；提供3套模板 |
| [388-portal-space-magic-vfx-prompts](02-提示词技巧/388-portal-space-magic-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑪——传送门/空间魔法：分层结构、视界形态与空间扭曲 | 传送门必须写四层结构（外环→视界→喉管→另一端）否则像色板贴纸；视界形态决定传送门气质（球体=稳定、撕裂=危险、液态=神秘）；空间扭曲三件套（引力透镜/时空涟漪/边缘色差）让传送门"真实存在"于空间中；提供3套模板 |
| [389-time-magic-vfx-prompts](02-提示词技巧/389-time-magic-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑫——时间魔法：六种类型、冻结语法与回溯三步骤 | 时间特效第一死因是"写成慢动作"——冻结必须写all motion completely frozen including eyes hair clothing；时间回溯必须按三步骤写（什么逆转→回到哪里→什么改变）；六种时间类型各有独立视觉语法；提供3套模板 |
| [390-shield-barrier-ward-vfx-prompts](02-提示词技巧/390-shield-barrier-ward-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑬——护盾/结界/屏障：六段式结构、形态材质符文三选与冲击反应 | 护盾特效必须写六段（场景→形态→激活→冲击→环境→风格）否则像玻璃贴纸；护盾反应是灵魂（涟漪/裂纹自愈/符文变亮/局部崩解重组）；提供3套模板 |
| [391-transformation-awakening-vfx-prompts](02-提示词技巧/391-transformation-awakening-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑭——变身/觉醒：四段式结构、能量七要素与锚点锁定 | 变身特效必须写四段式（蓄力→变身→爆发→锁定）否则像瞬间换装；能量七要素（形状/类型/源头/气场/粒子/环境/大气）缺一不可；锚点锁定（面部/站姿）防角色漂移；提供3套模板 |
| [392-summoning-circle-rune-magic-vfx-prompts](02-提示词技巧/392-summoning-circle-rune-magic-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑮——召唤阵/符文魔法：阵法材质、符文样式与中心显现三层结构 | 召唤阵必须写三层结构（阵法材质→符文样式→中心显现）否则像地面涂鸦；符文逐个亮起（from center to edge）是动画关键；中心显现物必须有独立光源和形容词；提供3套模板 |
| [393-sword-energy-weapon-enchant-vfx-prompts](02-提示词技巧/393-sword-energy-weapon-enchant-vfx-prompts.md) | 技能魔法特效与提示词模板二十连⑯——剑气/武器附魔：五层结构、核心暗边缘亮与残留轨迹 | 剑气第一死因是"纯亮核心"——核心暗+边缘亮=高级质感（如obsidian black core+white-silver edge）；剑气必须写五层（形状/能量色/粒子/质感/动态）；残留轨迹是灵魂（lingering trail after the slash）；武器附魔=武器表面持续发光的状态；提供3套模板 |
| [394-particle-system-concepts-ai-alternative](02-提示词技巧/394-particle-system-concepts-ai-alternative.md) | 技能魔法特效与提示词模板二十连⑰——粒子系统概念→AI替代：从发射器思维到提示词翻译 | 粒子系统核心概念（发射器/生命周期/物理/父子级）可直接翻译为AI提示词；AI替代不是复制粒子系统而是翻译其思维；减法提示（Subtractive Prompting）一次只加1-2个粒子描述；提供粒子类型→提示词映射表与3套模板 |
| [395-vfx-compositing-post-pipeline](02-提示词技巧/395-vfx-compositing-post-pipeline.md) | 技能魔法特效与提示词模板二十连⑱——特效合成后期管线：混合模式、辉光、色差与颗粒统一 | AI视频特效后期管线六步：AI主料→AE补交互→色彩校正→颗粒统一→色差镜头→最终输出；混合模式是合成核心（Screen光效/Add光源/Multiply阴影/Overlay中间调）；辉光阈值控制、色差模拟镜头、颗粒统一质感；提供混合模式选择表与管线检查清单 |
| [396-prompt-template-engineering](02-提示词技巧/396-prompt-template-engineering.md) | 技能魔法特效与提示词模板二十连⑲——提示词模板工程：模块化结构、变量槽、负向词库与种子管理 | 提示词模板必须工程化：拆为六模块（镜头/角色/特效/环境/风格/负向）自由组合；变量槽用[大写占位符]标记，5秒替换；负向词库按14类分类整理，调用时只取相关类；种子管理=同一特效固定seed保一致性；提供模块化骨架与变量字典 |
| [397-vfx-asset-library-and-bible](02-提示词技巧/397-vfx-asset-library-and-bible.md) | 技能魔法特效与提示词模板二十连⑳——技能特效资产库+特效圣经模板：全剧视觉规范与弹药库结构 | 技能特效资产库=弹药库（378-396所有模板按14类归档，每资产唯一编号FX-XXX-NNN）；特效圣经=作战手册（全剧视觉规范+角色特效对应表+特效分级+一致性检查清单）；资产库与圣经咬合：圣经定规范，资产库供弹药；提供完整资产库结构与圣经模板 |
| [448-seedance25-30-commands](02-提示词技巧/448-seedance25-30-commands.md) | Seedance 2.5 三十条导演级命令（索引页） | 索引页——Seedance 2.5 来源的 30 条导演级命令已逐条并入本库既有条目，本页只保留六要素公式、六问自检与"命令→归属条目"索引 |

## 03-角色与表演（71）

| 文件 | 标题 | 简介 |
|---|---|---|
| [004-角色一致性方案](03-角色与表演/004-角色一致性方案.md) | 动漫短剧角色一致性方案 | 用角色卡 + image-to-video + 固定 seed 锁定角色外观的四层一致性策略 |
| [024-microexpression-breathing](03-角色与表演/024-microexpression-breathing.md) | 微表情与呼吸：张力信号源 | 微表情与呼吸是蓄势段的张力信号源：眼/眉/嘴角微变+呼吸节律=不动的揪心 |
| [070-villain-design-oppression](03-角色与表演/070-villain-design-oppression.md) | 反派设计的压迫感 | 反派压迫感靠体型/逆光/俯视/不动+微表情；越静越强越揪心，忌张牙舞爪 |
| [071-underdog-protagonist-tension](03-角色与表演/071-underdog-protagonist-tension.md) | 主角的弱者张力 | 弱者主角靠代价可见+差点失手+觉醒反转制造张力；无敌主角=零张力 |
| [072-supporting-reaction-amplifier](03-角色与表演/072-supporting-reaction-amplifier.md) | 配角反应放大张力 | 配角是张力放大镜：旁观惊愕/屏息/倒吸=把主角的张力放大给观众 |
| [073-size-difference-tension](03-角色与表演/073-size-difference-tension.md) | 体型差与张力 | 体型差=视觉权力差；大压小=压迫，小胜大=反差爽点；体型是权力的肉身化 |
| [074-costume-prop-tension-signals](03-角色与表演/074-costume-prop-tension-signals.md) | 服装/道具张力信号 | 服装道具是张力信号源：破损=代价，隐藏道具=伏笔，仪式服装=宿命 |
| [075-expression-design-tension](03-角色与表演/075-expression-design-tension.md) | 表情设计张力（面部结构） | 表情设计靠面部结构夸张+表情库分层；关键时刻用极端表情，日常用克制的反差 |
| [088-character-consistency-tension](03-角色与表演/088-character-consistency-tension.md) | 角色一致性下的张力（动起来不崩） | 张力建立在角色不崩之上；先定妆图锁角色再动；一致性是张力的地基 |
| [161-facs-action-units](03-角色与表演/161-facs-action-units.md) | FACS动作单元——面部表情的解剖学 | 表情不是玄学是43块肌肉的组合题；记住10个高频AU就能拆解90%的表演 |
| [162-micro-expressions](03-角色与表演/162-micro-expressions.md) | 微表情——半秒内泄露的真话 | 微表情是被压缩到0.5秒内的完整情绪——角色想说谎，脸不同意 |
| [163-eye-acting](03-角色与表演/163-eye-acting.md) | 眼神演技——瞳孔、眨眼与视线的三重奏 | 眼睛是表演的主战场：眨眼时机=思考节奏，眼跳方向=内心地图，瞳孔大小=情绪强度 |
| [164-complex-expression-recipes](03-角色与表演/164-complex-expression-recipes.md) | 复合表情配方——一种情绪一张脸是谎言 | 真人很少"纯"情绪——苦笑、含泪的笑、愤怒的悲悯，复合表情才是高级演技的配方表 |
| [165-ai-microexpression-prompts](03-角色与表演/165-ai-microexpression-prompts.md) | AI微表情提示词工程——从面瘫到演技派 | AI默认把"悲伤"画成嚎啕大哭；微表情提示词的核心是压低幅度、精确到肌肉、给足时间 |
| [166-body-micro-movements](03-角色与表演/166-body-micro-movements.md) | 肢体微动作——小动作泄露大性格 | 台词是角色想让你听的，小动作是角色藏不住的——玩戒指、摸后颈、抖腿，全是潜台词 |
| [167-breathing-performance](03-角色与表演/167-breathing-performance.md) | 呼吸表演——看不见的演技发动机 | 吸气是蓄力，呼气是执行；呼吸给每个动作装上发动机——没呼吸感的表演是僵尸在走路 |
| [168-hand-acting](03-角色与表演/168-hand-acting.md) | 手部表演——手是身体的标点符号 | 手不在身体外面独立活着，手是情绪的标点——句号、感叹号、省略号全在手指的弧度和力度里 |
| [169-posture-presence](03-角色与表演/169-posture-presence.md) | 姿态与气场——脊柱决定地位 | 角色的社会地位、心理状态、战斗能力全写在脊柱的弧度里；姿态是24小时不间断的无声独白 |
| [170-restrained-acting](03-角色与表演/170-restrained-acting.md) | 表演层次与克制——less is more的表演工程学 | 好演员做减法：演50%让观众补50%；全程满格的表演=全程没有重点 |
| [200-production-design-artwork](03-角色与表演/200-production-design-artwork.md) | 美术设计图种与流程 | 美术部门图种全景：概念/最后设计图、建筑图、效果图、模型、故事板，及四种应用与片厂流程 |
| [201-chubbuck-technique-overview](03-角色与表演/201-chubbuck-technique-overview.md) | 查伯克十二步骤表演法（总纲） | 情感是燃料不是结果；把「目标—阻碍—斗争」转译为可写进 AI 提示词的角色表演指令 |
| [202-objective-system-overall-scene](03-角色与表演/202-objective-system-overall-scene.md) | 目标体系——总目标与分场目标（工具1+2） | 总目标=全剧最想要的；分场目标要「让你怎样」而非「我要感受什么」，且必须支撑总目标 |
| [203-obstacles-tension](03-角色与表演/203-obstacles-tension.md) | 阻碍——把障碍变成燃料（工具3） | 阻碍=物质/情感/精神三类障碍；难度越大达成越满足，阻碍令人不顾一切而不顾一切产生喜剧 |
| [204-substitution](03-角色与表演/204-substitution.md) | 替代——用真实的人替换对手（工具4） | 用现实中的真实人物替换合作演员，让角色情感有真来源、表演有多层次 |
| [205-inner-objects](03-角色与表演/205-inner-objects.md) | 内心视像——说到什么脑中就有画面（工具5） | 说话与倾听时脑中浮现的具体画面，让台词像从你个人生活中直接浮现 |
| [206-beats-and-actions](03-角色与表演/206-beats-and-actions.md) | 节奏单元与行动——把对白拆成节拍与动作（工具6） | beat是想法的一次变化，action是动词化的微型小目标；逐句拆对白即得表演层次 |
| [207-moment-before](03-角色与表演/207-moment-before.md) | 背景事件——开拍前发生了什么（工具7） | 背景事件=开拍前刚发生、身体与情感双重的起点；给分场目标紧迫性，须一分钟内点燃 |
| [208-place-fourth-wall](03-角色与表演/208-place-fourth-wall.md) | 场所与第四堵墙——把布景换成人生的地方（工具8） | 借真实生活场所给布景赋特征、以第四堵墙造私密；消除被观看感，让场景真正产生意义 |
| [209-doings-prop-action](03-角色与表演/209-doings-prop-action.md) | 行为动作——用道具演出的真实（工具9） | 行为动作=用道具把意图落到实处；言语说谎、行为吐真，用来泄露潜台词、避免「只演情绪」 |
| [210-inner-monologue](03-角色与表演/210-inner-monologue.md) | 内心独白——不发声的对话（工具10） | 内心独白=不发声的内心对话；用"你"写、与潜台词/台词区分，含《麦克白》级逐句对照与AI落地 |
| [211-previous-circumstances](03-角色与表演/211-previous-circumstances.md) | 既往情境——角色过去的累积（工具11） | 既往情境=角色过去的累积、解释他何以成为今天；四步法+情感日记把历史个人化 |
| [212-let-it-go](03-角色与表演/212-let-it-go.md) | 顺其自然——放下理性、进入自发（工具12） | 顺其自然=信任前十一项工具、放手只盯分场目标，进入自发无意识状态；含七步排练与复盘清单 |
| [213-organic-fear-death-trauma](03-角色与表演/213-organic-fear-death-trauma.md) | 恐惧·死亡·创伤·伤残的有机表演 | 用"求生驱动"倒逼无意识信号，把恐惧/濒死/伤残/伤疤演成身心双重真实 |
| [214-substance-sex-killer](03-角色与表演/214-substance-sex-killer.md) | 药物滥用·性吸引力·危险人格的有机表演 | 用可观察的外显信号，演出醉酒/吸毒/化学反应/连环杀手的身心层次 |
| [215-pregnancy-parenthood-occupation](03-角色与表演/215-pregnancy-parenthood-occupation.md) | 怀孕·为人父母·职业身份的身体真实 | 用护腹姿态/平视护头/职业化身体习惯把身份演成可观察的身体本能；补现代日常职业标准动作速查（职业+制服+工具+标准动作+真实场景） |
| [233-silhouette-signature-anchor](03-角色与表演/233-silhouette-signature-anchor.md) | 剪影识别与符号特征锚定 | 用基本形+剪影创建角色并多角度保持一致；一个符号特征出现几秒即可在潜意识中锚定角色；眼睛当结构体塑造 |
| [250-living-creature-interaction-overview](03-角色与表演/250-living-creature-interaction-overview.md) | 活物互动总原则——抱/牵/骑/扛，活物不是摆件 | 凡角色怀抱/牵引/骑乘/肩负活物，活物必须有自主动作＋接触反馈双层运动；静止即死物，互动即生命 |
| [251-carry-hold-biomechanics](03-角色与表演/251-carry-hold-biomechanics.md) | 怀抱姿态生物力学——托抱支点与重量下沉 | 抱活物必须有重量：人体后仰代偿5-15°、动物腹部受压形变、四肢垂坠或抓握——无重量下沉＝捧空气 |
| [252-lead-rein-tension](03-角色与表演/252-lead-rein-tension.md) | 牵引互动——缰绳/绳索的张力系统与拉锯节拍 | 缰绳是弹性张力系统不是钢丝：静止轻接触、拉扯有垂弧、动物头颈随张力偏移；情绪沿绳子双向传递 |
| [253-riding-centaur-rhythm](03-角色与表演/253-riding-centaur-rhythm.md) | 骑乘互动——人马一体的重心与起止步节拍 | 骑手不是粘在马背上的雕像：骨盆随马背节律三维微动、起步前倾止步后仰、转向重心内倾——人马共一个重心 |
| [254-creature-idle-micro-library](03-角色与表演/254-creature-idle-micro-library.md) | 动物待机微动作库——呼吸/耳抖/尾摆/眨眼的频率参数 | 待机≠静止：呼吸/耳抖/尾摆/眨眼构成生命噪音层，频率随体型反相关；附常用物种频率表与防机械循环规则 |
| [255-creature-emotion-five-states](03-角色与表演/255-creature-emotion-five-states.md) | 动物情绪五态——耳/尾/瞳/姿/毛五通道体征清单 | 警觉/放松/亲昵/恐惧/攻击前五态，通过耳位、尾位、瞳孔、体姿高度、被毛状态五通道表达；情绪不靠表情靠体征 |
| [256-call-response-creature-dialogue](03-角色与表演/256-call-response-creature-dialogue.md) | 人宠对话感——call & response 动作回应节拍 | 人宠之间建立"呼唤-回应"动作节拍：回应延迟0.5-1.5秒为自然，共同注视≥1秒建立连接——动物没回应＝人物自说自话 |
| [257-petting-stroke-pairing](03-角色与表演/257-petting-stroke-pairing.md) | 抚摸/顺毛互动配对——手型与动物反应对照表 | 手型决定动物反应：顺毛流向→放松耳后贴，逆毛/突兀触碰→警觉皮抖；手必须真接触有压痕，悬空抚摸最假 |
| [263-human-creature-eyeline](03-角色与表演/263-human-creature-eyeline.md) | 人兽视线互动——eyeline match 与共同注视 | 对视建立情感、共同注视建立同盟：对视要高度平齐，共同注视夹角≤30°指向同一画外点——人看镜头兽看别处＝关系断裂 |
| [264-realistic-anthropomorphism-limit](03-角色与表演/264-realistic-anthropomorphism-limit.md) | 写实系拟人化边界——身体语言表达情绪，不借人脸肌肉 | 写实系动物砍掉人形眉毛/咧嘴笑/拟人皱眉三件套，情绪只用耳尾瞳姿毛五通道与行为链传递——表情载体是身体不是脸 |
| [268-creature-as-supporting-actor](03-角色与表演/268-creature-as-supporting-actor.md) | 动物当配角演员——给动物设总目标与行动动词 | 动物训练师的表演法：给动物一个总目标（守护/觅食/依附）＋每镜一个行动动词（蹭/盯/扑/挡）——动词驱动，形容词禁用 |
| [364-power-personality-binding](03-角色与表演/364-power-personality-binding.md) | 技能魔法编写二十连⑦——能力即性格：同源异用、缺陷内嵌与使用即自白 | 能力不是角色"会什么"而是角色"是谁"——源于身份/创伤/欲望/缺陷；同一能力两个人必须用出两种劲；超人一家式的心理映射；使用方式即角色自白 |
| [407-eye-movement-taxonomy](03-角色与表演/407-eye-movement-taxonomy.md) | 微眼动分类学——扫视/微扫视/注视/漂移/震颤 | 五类眼球运动的科学参数与AI提示词写法——扫视是思考，注视是锁定，微扫视是注意力泄露，漂移是放空，震颤不可演 |
| [408-gaze-trajectory-patterns](03-角色与表演/408-gaze-trajectory-patterns.md) | 视线游移轨迹——回避/扫视/定焦/游移的叙事语义 | 四种视线轨迹图案对应四种内心状态；"看方向识谎"被科学证伪但作为观众已内化的视觉符号依然有效 |
| [409-eyelid-acting](03-角色与表演/409-eyelid-acting.md) | 眼睑表演——半阖/颤动/沉重抬起/抽搐的情绪档位 | 眼睑高度是情绪的音量旋钮：全开=惊恐，收紧=愤怒，半阖=轻蔑/诱惑/疲惫三义，抽搐=崩溃前兆 |
| [410-tears-moisture-layer](03-角色与表演/410-tears-moisture-layer.md) | 泪光与湿润层——从泪膜反光到滑落的克制演法 | 哭戏的最高档是"盈满不落"：泪膜反光增强→积聚→盈眶→临界→滑落有分帧节奏，AI对glass感和single tear识别稳定 |
| [411-focus-defocus-gaze](03-角色与表演/411-focus-defocus-gaze.md) | 焦点与失焦——放空、解离与重新聚焦的表演力 | 失焦=角色"人不在眼里"：解离/崩溃/回忆杀共用放空配方，重新聚焦的2-4帧回神是全镜头最有戏的瞬间 |
| [412-pupil-physiology-performance](03-角色与表演/412-pupil-physiology-performance.md) | 瞳孔生理与表演——缩放速率、瞳孔地震与情绪瞳孔语言 | 光反射缩放是帧级快动作、情绪缩放是秒级慢动作；瞳孔地震是动漫独有的震惊符号；暗杀缩瞳、心动放瞳、恐惧先缩后放各有提示词 |
| [413-brow-eyelid-coordination](03-角色与表演/413-brow-eyelid-coordination.md) | 眉毛-眼睑联动——眉眼是一个系统的组合拳表演 | 眉与眼睑是同一套机械系统：眉压必带睑动；眉压眼瞪/眉挑眼瞪/眉垂眼柔三套组合拳覆盖80%眼部情绪；眉眼间距就是攻击性仪表盘 |
| [414-abnormal-inhuman-eyes](03-角色与表演/414-abnormal-inhuman-eyes.md) | 病态与非常态眼神——眼球震颤/疯批/黑化/附身/非人瞳 | 非常态眼神五件套：震颤是生理病、疯批是放瞳+失焦、黑化是高光五级熄灭、附身是失焦+异常平滑、非人感靠异形瞳孔 |
| [415-eye-ecu-shot-design](03-角色与表演/415-eye-ecu-shot-design.md) | 眼部特写分镜法（ECU）——什么节点切眼特写、怎么构图、给多少帧 | ECU是景别体系里的"重拳"：七个情绪节点才配切、三种眼特写构图各司其职、时长按1-4秒预算——切多了就不值钱 |
| [416-anime-eye-symbol-system](03-角色与表演/416-anime-eye-symbol-system.md) | 动漫眼神符号体系——高光/异形瞳/符号眼型与萌系大眼微动适配 | 动漫眼的三变量里高光是生命开关：数量位置定情绪、形状定语域；符号眼型是喜剧专属；萌系大圆眼必须用更小幅度微动 |
| [417-eye-micro-prompt-library](03-角色与表演/417-eye-micro-prompt-library.md) | AI 提示词眼部微动写法库——30+ 条情绪分组速查 | 眼部微动提示词按情绪分组的中英对照速查库：每条标注适用场景与 AI 生成稳定性评级，写物理动作不写情绪词 |
| [418-eye-artifact-prevention](03-角色与表演/418-eye-artifact-prevention.md) | AI 视频眼部崩坏防治——成因·负面提示词·图生视频参数 | 眼部崩坏五大型（斗鸡眼/双眼不同步/瞳孔漂移/眨眼卡半开/高光乱闪）的成因诊断、负面提示词写法与"运动越小越稳"的图生视频参数策略 |
| [419-shot-size-eye-readability](03-角色与表演/419-shot-size-eye-readability.md) | 景别与眼神可读性——从瞳孔到头部朝向的信息量预算 | 眼神信息量随景别递减：特写读瞳孔、近景读眼跳、中景读视线大转移、远景用头部朝向代替——AI 提示词按景别分配眼部笔墨 |
| [420-seven-emotions-eye-recipes](03-角色与表演/420-seven-emotions-eye-recipes.md) | 情绪七态眼神配方——眨眼×眼跳×瞳孔×眼睑四通道对照 | 喜/怒/哀/惧/惊/厌/蔑七种情绪在眨眼频率、眼跳方向、瞳孔、眼睑高度四个通道上的配方对照表，每态配一条可直接复制的整段提示词 |
| [421-dialogue-eye-rhythm](03-角色与表演/421-dialogue-eye-rhythm.md) | 对话戏眼神节奏——倾听节拍·抢话先动·回避时点·盯人张力 | 对话戏眼神的四套节拍系统：倾听者"长注视+短暂移开"、说话者"开讲移开·讲毕回看"、抢话前眼神先动、盯人不眨的张力边界 |
| [422-combat-eye-focus](03-角色与表演/422-combat-eye-focus.md) | 战斗中的眼神——锁定、读招与杀气的眼部工程学 | 高手战斗时眼球几乎不动——视觉锚点锁对方眼/头部、余光读全身；杀气=瞳孔收缩+不眨眼+高光压制；高速战斗中眼神必须简化 |
| [423-deadpan-psycho-eye-restraint](03-角色与表演/423-deadpan-psycho-eye-restraint.md) | 冷面与疯批角色的眼神克制——全部表演压在眼周 | 面瘫角色把全部表演预算压在眼周；疯批=眼神平静+行为离谱的反差；眼皮跳/单侧挑眉是毫米级泄压阀——用最稳的眼神说最疯的话 |
| [424-moe-big-eye-micro-motion](03-角色与表演/424-moe-big-eye-micro-motion.md) | 萌系大眼微动专篇——眼越大，动作越小 | 萌系大眼把表情符号化：微动幅度与眼睛尺寸反相关；高光有无/形状=情绪开关（高光消失=黑化）；虎牙只跟微笑眯眼同框 |
| [425-eye-micro-motion-frame-budget](03-角色与表演/425-eye-micro-motion-frame-budget.md) | 眼部微动帧级参数表——眨眼/转睛/瞳孔/失焦的帧数预算 | 全部眼部微动作的帧数预算双表（24fps/30fps）：眨眼3-5帧、转睛2-4帧、瞳孔缩放6-10帧、失焦8-12帧；附on twos拍摄下的眼部处理 |
| [426-eye-acting-breakdown-method](03-角色与表演/426-eye-acting-breakdown-method.md) | 眼神戏实片拆解方法论——逐帧偷师的标准流程 | 眼神戏拆解六步：取元数据→抽帧→标注→分类→提炼→产出；动画拆鬼灭/咒术名场面，真人拆梁朝伟/周迅；附专用记录模板 |
| [463-imbalance-exhaustion-poses](03-角色与表演/463-imbalance-exhaustion-poses.md) | 失衡与力竭姿势六条（踉跄稳身/跪滑急停/回眸疾奔/力竭扶膝/扶墙强撑/翻滚起身） | 逃亡与力竭段的六个身体语言姿势：重心写法、四肢位置、躯干头部关系与推荐机位，已入 animeposelibrary.js #272-277 |
| [472-lib-emotion-100](03-角色与表演/472-lib-emotion-100.md) | 情感戏分镜动作库（60条） | 情感戏60条：用可落到镜头的物理动作指令替代抽象情绪描述，覆盖十大情感场景。 |
| [473-lib-dailylife-100](03-角色与表演/473-lib-dailylife-100.md) | 日常生活动作描写库 | 日常动作扩写库：把干巴巴的动作原句补成有身体细节、重心逻辑、画面感的连续动作。 |

## 04-张力与节奏（36）

| 文件 | 标题 | 简介 |
|---|---|---|
| [011-tension-definition](04-张力与节奏/011-tension-definition.md) | 张力定义与构成要素 | 张力=对"将发未发"的预期紧张感，由威胁/不确定性/延迟/信息差/代价五要素构成 |
| [012-static-vs-dynamic-tension](04-张力与节奏/012-static-vs-dynamic-tension.md) | 静态张力 vs 动态张力 | 静态张力靠不动维持揪心（居合待机），动态张力靠动作进行中的速度差，静>动 |
| [013-tension-three-axes](04-张力与节奏/013-tension-three-axes.md) | 张力三轴：时间/空间/心理 | 张力沿三轴建立：时间轴拉长等待、空间轴压缩距离/负空间、心理轴制造信息差与代价 |
| [014-tension-curve](04-张力与节奏/014-tension-curve.md) | 张力曲线：Build-up / Peak / Release | 张力三段曲线：蓄势build-up铺垫延迟、峰值peak最短一瞬、释放release余韵收束，比例约6:1:3 |
| [015-tension-and-pacing](04-张力与节奏/015-tension-and-pacing.md) | 张力与节奏的关系 | 张力≠节奏，但节奏决定张力释放时机；快慢对比制造张力，节奏破坏即张力破坏 |
| [021-slow-motion-tension](04-张力与节奏/021-slow-motion-tension.md) | 慢镜头（升格）的张力用法 | 升格把峰值瞬间拉长成可凝视的揪心，专用于peak；忌滥用，升格越频效果越弱 |
| [023-cut-frequency-tension](04-张力与节奏/023-cut-frequency-tension.md) | 切换频率与张力 | 切换频率编码张力：慢切=蓄势累积，快切=爆发过载；切换频率骤变是张力峰值的信号 |
| [029-pause-stillness](04-张力与节奏/029-pause-stillness.md) | 停顿与静止的张力 | 停顿=动作中途的静止，制造延迟与重量感；停顿位置决定张力——出手前、中、后的停 |
| [076-opening-hook-tension](04-张力与节奏/076-opening-hook-tension.md) | 开篇钩子张力（前3秒抓人） | 开篇钩子用悬念/冲突/反差在前3秒抓人；附前3秒爆点动作库（雨夜抬头/废墟起身/推开铁门等10模板） |
| [077-info-drip-pacing](04-张力与节奏/077-info-drip-pacing.md) | 信息滴漏节奏 | 信息滴漏=一点给线索留新疑问；每次滴漏是小峰，维持持续好奇驱动 |
| [078-foreshadow-callback](04-张力与节奏/078-foreshadow-callback.md) | 伏笔与回调张力 | 伏笔提前藏线索，回调时回收=观众"原来如此"的满足感峰；草蛇灰线=高级 |
| [079-expectation-violation](04-张力与节奏/079-expectation-violation.md) | 期待与违背（反套路张力） | 期待违背=建立观众预期再打破=认知冲击峰；喜剧靠它造笑，正剧靠它造揪心 |
| [080-segment-tension-curve](04-张力与节奏/080-segment-tension-curve.md) | 段落张力曲线 | 一条短剧由多段张力曲线组成；段间有小谷，整剧有大峰；别全程高压也别全程平 |
| [081-pov-switch-tension](04-张力与节奏/081-pov-switch-tension.md) | 视角切换张力（POV） | POV切换=信息差视觉化；第一人称让观众同无知，第三人称给全知，切换瞬间=峰 |
| [082-timeline-dislocation](04-张力与节奏/082-timeline-dislocation.md) | 时间线错位张力 | 时间线错位=闪回/闪前打乱顺序；观众拼时间=认知峰，错位揭示=反转 |
| [083-ending-lingering-tension](04-张力与节奏/083-ending-lingering-tension.md) | 结尾余韵张力 | 结尾余韵用定格/拉远/留白让观众回甘；不爆而留，余味比爆更高级 |
| [239-theme-first-decision-filter](04-张力与节奏/239-theme-first-decision-filter.md) | 主题先行决策法（吕美特） | 一句话主题是所有创作决策的过滤器，逐场诊断表剔除不推进主题/人物的废戏 |
| [259-creature-reacts-first](04-张力与节奏/259-creature-reacts-first.md) | 动物反应先行——预警/喜剧/张力三类叙事用法 | 动物感官先于人：预警（僵直注视≥2s后人再反应）、喜剧（动物已滑稽人未察觉）、张力（后退呜咽）——先行反应必须有后续payoff |
| [261-tug-of-war-comedy-beats](04-张力与节奏/261-tug-of-war-comedy-beats.md) | 牵引拉锯的喜剧节拍——力量反转与节奏错位 | 拉锯喜剧=力量反转+节奏错位：3-5回合后动物突进或骤停，人被拖行2-5步或扑空；静止到暴起间隔≤0.5s |
| [296-impact-frame-timing](04-张力与节奏/296-impact-frame-timing.md) | 冲击帧时机学——命中帧·蓄力峰值·情绪爆点 | 冲击帧必须精确卡在接触点的帧级时机规则，三大类合法时机，以及"早晚一帧都失效"的帧位校准法 |
| [333-story-structure-systems](04-张力与节奏/333-story-structure-systems.md) | 故事结构四大体系——三幕式/英雄之旅/七点结构/救猫咪15节拍 | 四大主流故事结构横向对比＋15节拍百分比定位法，短片按比例压缩即可套用 |
| [334-scene-writing-expansion](04-张力与节奏/334-scene-writing-expansion.md) | 场景写作与扩写——场景六步法＋目标冲突结果＋"展示场景、告诉过渡 | 场景是故事的基本粒子；每场必须有变化，六步法搭建，扩写只放大关键瞬间不注水 |
| [335-character-building-want-need-flaw](04-张力与节奏/335-character-building-want-need-flaw.md) | 人物塑造——欲望/需要/幽灵/谎言链条与人物弧光设计 | 幽灵事件制造谎言信念，谎言产生缺陷，缺陷驱动外在欲望，内在需要与欲望的裂缝就是弧光 |
| [336-dialogue-subtext-craft](04-张力与节奏/336-dialogue-subtext-craft.md) | 对白工艺——潜台词重写七步法、直说病修法与信息武器化 | 好对白活在台词与意图的缝隙里；情绪不贴标签、主题不广播、信息只在被逼时作为武器流出 |
| [337-conflict-stakes-tension](04-张力与节奏/337-conflict-stakes-tension.md) | 冲突·赌注·张力——冲突分层叠加、希区柯克炸弹与倒计时工程 | 冲突是双方目标相撞（客观），张力是观众对后果的预期（主观）；最强戏＝外部冲突与内部伤口同时发作 |
| [338-worldbuilding-exposition-drip](04-张力与节奏/338-worldbuilding-exposition-drip.md) | 世界观呈现——冰山理论、信息滴灌与把说明埋进冲突 | 按100%建造只露10%，信息随用随取、埋进冲突与行动，先让观众好奇再给答案 |
| [339-battle-epic-writing-clarity](04-张力与节奏/339-battle-epic-writing-clarity.md) | 战争/史诗场面写作——将军的清晰度、分乐章结构与远景-近景语法 | 史诗感是感觉，清晰度是手艺：一句话战略目标＋2-3个POV锚点＋分乐章＋远景近景交替，规模靠暗示不靠花名册 |
| [340-sensory-cinematic-detail](04-张力与节奏/340-sensory-cinematic-detail.md) | 感官细节与画面感——精确名词、单一正确细节与电影化描写 | 画面感来自精确不来自堆砌；一个对的细节胜十个形容词，最好的细节一感双关——既给感官又给人物处境 |
| [341-outline-to-draft-expansion-workflow](04-张力与节奏/341-outline-to-draft-expansion-workflow.md) | 从大纲到初稿——雪球式多级扩写工作流（一句话→段落→节拍→场景卡→分镜） | 永远不在错误的抽象层写作：每一级只做本级决策，逐级膨胀，结构没压测通过不写下一级 |
| [342-revision-passes-kill-darlings](04-张力与节奏/342-revision-passes-kill-darlings.md) | 改写与节奏诊断——分层修订pass、杀死宠儿与篇幅节奏学 | 结构没修好之前绝不抛光台词；按结构→人物→场景/对白→连贯→精修分层过pass，不挣位置的最爱也要删 |
| [347-character-not-drowned-narrative](04-张力与节奏/347-character-not-drowned-narrative.md) | 大场面人物不漂移⑤——叙事层：人物不被规模淹没（POV回访/宽近交替/个人赌注） | 大场面三层窄化（一句话目标/1-3个POV/个人代价），宽近交替、地理教一次、节奏化回访；叙事回访镜头同时是技术身份再锚定镜头——防漂移与防淹没是同一组镜头 |
| [357-vfx-narrative-restraint](04-张力与节奏/357-vfx-narrative-restraint.md) | AI视频特效十连⑩——特效叙事与节制：不可见特效、奇观四激活法、特效预算分级 | 最好的特效是观众没察觉的特效；每个特效解决一个故事问题而非"酷不酷"；连续奇观必然贬值；叙事激活奇观四法：节点/悬念/独创构想/动作即叙事 |
| [372-magic-dialogue-jargon](04-张力与节奏/372-magic-dialogue-jargon.md) | 技能魔法编写二十连⑮——魔法对白与术语投放：圈内人说行话，观众靠情境跟上 | 角色必须像圈内人一样说行话而不是给观众讲课；术语靠使用情境自解释；说明只搭在冲突/失败/外行视角上；删"如你所知"句；术语密度随剧情推进递增 |
| [453-product-promo-motion-parameters](04-张力与节奏/453-product-promo-motion-parameters.md) | 品牌→动效参数推导表（产品宣传片视觉节奏） | 不凭手感挑 easing/时长——把品牌放到能量轴×调性轴两根轴上，从最近的预设起步；6 个品类预设含主时长/easing/过冲/squash |
| [470-lib-comedy-100](04-张力与节奏/470-lib-comedy-100.md) | 喜剧节奏基础库 | 喜剧节奏单元库：每条六字段格式，沉淀可直接复用的喜剧节奏弹药。 |
| [471-lib-suspense-100](04-张力与节奏/471-lib-suspense-100.md) | 悬念构建基础库 | 悬念场景构建库：六字段格式，把悬念展开成可画的物理行为，禁抽象情绪。 |

## 05-镜头与构图（52）

| 文件 | 标题 | 简介 |
|---|---|---|
| [016-shot-scale-tension](05-镜头与构图/016-shot-scale-tension.md) | 景别与张力 | 景别决定张力密度：特写最揪心（细节压缩），全景疏离（环境压迫），中景最弱慎用 |
| [017-camera-angle-power](05-镜头与构图/017-camera-angle-power.md) | 机位角度与权力关系 | 机位角度编码权力：仰视=压迫/强，俯视=弱势，平视=对等；高低切换制造张力反转 |
| [018-camera-movement-tension](05-镜头与构图/018-camera-movement-tension.md) | 镜头运动与张力 | 镜头运动控张力：推进=加压蓄势，拉远=泄压揭示；固定机位+主体动是爆发段最稳 |
| [019-depth-of-field-focus](05-镜头与构图/019-depth-of-field-focus.md) | 景深与焦点：隔离与揭示 | 景深控张力：浅景深隔离主体加压，焦点转移揭示隐藏威胁，rack focus是信息差神器 |
| [020-composition-tension](05-镜头与构图/020-composition-tension.md) | 构图张力：负空间/对称/失衡 | 构图是张力底座：负空间=孤立/威胁潜伏，对称=仪式压迫，失衡=不安，角色压角=被环境挤压 |
| [022-long-take-tension](05-镜头与构图/022-long-take-tension.md) | 长镜头的张力累积 | 长镜头靠"不切"累积揪心，观众无处逃逸；适合逼近/潜伏威胁，但节奏须内含起伏 |
| [091-frame-within-frame](05-镜头与构图/091-frame-within-frame.md) | 框中框构图（Frame within a Frame） | 用门框/窗/镜/柱在画面内再造一框；聚焦+纵深+困局感+偷窥视角四合一 |
| [092-symmetry-one-point-perspective](05-镜头与构图/092-symmetry-one-point-perspective.md) | 对称构图与一点透视（Symmetry & One-Point Perspective） | 主体居中+对称+一点透视=秩序压迫；Kubrick 标志技法；制造诡异秩序感 |
| [093-deep-focus-composition](05-镜头与构图/093-deep-focus-composition.md) | 大景深构图（Deep Focus） | 前中后三层全清晰；无处可逃的视觉；Welles《公民凯恩》标志技法 |
| [094-rule-of-thirds-negative-space](05-镜头与构图/094-rule-of-thirds-negative-space.md) | 三分法则与负空间留白（Rule of Thirds & Negative Space） | 主体压三分点+大片留白=失衡=孤独/压迫；留白比填满更会说话 |
| [095-leading-lines-composition](05-镜头与构图/095-leading-lines-composition.md) | 引导线构图（Leading Lines） | 用场景线条把观众视线逼向主体；走廊/柱列/铁轨=逼迫感=纵深张力 |
| [096-long-take-oner](05-镜头与构图/096-long-take-oner.md) | 长镜头/一镜到底（Long Take / Oner） | 一镜不切=不可逃的沉浸；时间连贯=压迫递增；Hitchcock/柯达李查斯基标志 |
| [097-slow-push-pull](05-镜头与构图/097-slow-push-pull.md) | 慢推与缓拉（Slow Push In / Pull Out） | 慢推=逼近=压迫递增；缓拉=抽离=孤独余韵；最简运镜最强张力 |
| [098-dolly-zoom-vertigo](05-镜头与构图/098-dolly-zoom-vertigo.md) | 变焦拉伸/眩晕效应（Dolly Zoom / Vertigo Effect） | 推拉+反向变焦=主体不变背景畸变=心理失衡；Vertigo/Jaws 标志技法 |
| [099-tracking-steadicam-shot](05-镜头与构图/099-tracking-steadicam-shot.md) | 跟拍与斯坦尼康（Tracking / Steadicam Shot） | 跟随角色移动=沉浸"在场"；斯坦尼康稳而滑=不可逃的陪伴 |
| [100-orbit-arc-shot](05-镜头与构图/100-orbit-arc-shot.md) | 环绕/弧形运镜（Orbit / Arc Shot） | 绕主体旋转=审视/包围/时间凝固；对峙与告白两极通用 |
| [101-low-angle-shot](05-镜头与构图/101-low-angle-shot.md) | 低角度仰拍（Low Angle Shot） | 仰视主体=放大=权力/威胁/英雄；Welles《公民凯恩》标志；天花板压迫 |
| [102-high-angle-birds-eye](05-镜头与构图/102-high-angle-birds-eye.md) | 高角度俯拍与鸟瞰（High Angle / Bird's Eye） | 俯视主体=缩小=弱势/孤绝/宿命；鸟瞰=上帝视角=渺小；与仰拍相反 |
| [103-pov-subjective-shot](05-镜头与构图/103-pov-subjective-shot.md) | 主观镜头/POV（Point-of-View Shot） | 镜头=角色眼睛=第一人称代入；悬疑/恐怖最强视点；经典三段式结构 |
| [104-break-180-degree-rule](05-镜头与构图/104-break-180-degree-rule.md) | 越轴/打破180度线（Breaking the 180° Rule） | 故意越过动作线=空间错位=失衡/混乱/转折信号；规则是工具不是法律 |
| [105-macro-close-up](05-镜头与构图/105-macro-close-up.md) | 微距特写（Macro Close-Up） | 极近拍微小细节=放大不可逃=压迫/悬疑/顿悟；一滴汗一双眼的宇宙 |
| [109-shadow-noir-composition](05-镜头与构图/109-shadow-noir-composition.md) | 阴影构图与黑色电影布光（Shadow / Noir Lighting） | 阴影比光更重要；低调布光+高对比=半明半暗=道德灰区/未明/压迫 |
| [110-mirror-reflection-shot](05-镜头与构图/110-mirror-reflection-shot.md) | 镜面反射镜头（Mirror Shot） | 镜中影=双重/分裂/真相；镜是第二画面=框中框变体；替身/双面镜技法 |
| [184-aspect-ratio-narrative](05-镜头与构图/184-aspect-ratio-narrative.md) | 画幅制式叙事法（宽高比） | 画幅是隐性叙事语法：越窄越亲密压抑，越宽越宏大疏离；同一片内可切画幅区分现实与梦境 |
| [192-dramatic-action-range-depth](05-镜头与构图/192-dramatic-action-range-depth.md) | 戏剧性动作范围与纵深调度 | 机位在动作范围之内还是之外，决定观众认同还是疏离；纵深调度用前后景大小差取代剪辑 |
| [193-open-closed-composition](05-镜头与构图/193-open-closed-composition.md) | 开放与封闭式构图 | 开放＝容纳观众、边缘切人、写实；封闭＝除去参与、精心安置、舞台化。核心是观众的参与度与亲密性 |
| [194-pov-identification](05-镜头与构图/194-pov-identification.md) | 视点三型与认同设计 | 视点＝叙述姿态；三型（第一人称/受限第三人称/全知）；认同度由视线角度与镜头贴近程度决定，须保持对象一致 |
| [195-pan-six-uses](05-镜头与构图/195-pan-six-uses.md) | 摇镜的六种用途 | 摇镜=轴心旋转不移位；六种用途操作各异；远摄加速运动感，交叉摇镜连两主体 |
| [196-crane-shot-design](05-镜头与构图/196-crane-shot-design.md) | 升降镜头的设计 | 升降镜头=垂直运动为核心；范围/视点/器材/影像化四要素，配透视效果图三步骤 |
| [216-frame-playground-pressure-release](05-镜头与构图/216-frame-playground-pressure-release.md) | 画格即游戏场——压力区与释放区 | 画格是承载叙事的游戏场；主体位置决定周围气囊被压缩或释放，居中显平衡，靠边生压迫。 |
| [217-tension-lines-rubber-band](05-镜头与构图/217-tension-lines-rubber-band.md) | 张力线与橡皮筋原理 | 张力线是关键叙事点间的虚拟连线；橡皮筋原理：点距越远张力越大，松开即释放。 |
| [218-turning-point-momentum-shift](05-镜头与构图/218-turning-point-momentum-shift.md) | 拐点——动势方向突变即戏剧 | 拐点是能量流动方向突变的位置；变化即戏剧，用投接球、之字形、过山车效应制造张力。 |
| [219-silhouette-guide-method](05-镜头与构图/219-silhouette-guide-method.md) | 剪影导览法——简化为剪影检验构图 | 把构图元素压成背光剪影，用尺寸与明暗锁定焦点，用主对角线+角色次级结构检验叙事性 |
| [220-shape-language-composition](05-镜头与构图/220-shape-language-composition.md) | 形状语言——几何形状作为构图骨架 | 用倒三角、垂直线、之字形、弧形、A形、9形等几何形状先定构图骨架，形状决定动势与叙事基调 |
| [221-aspect-ratio-conversion-methods](05-镜头与构图/221-aspect-ratio-conversion-methods.md) | 画幅转换三法——1.85:1 与 2.35:1 的微妙变化 | 画幅间转换三法：保高调宽、保宽调高、宽高折中；先问原始画幅哪部分最有价值再动手 |
| [222-unconventional-composition](05-镜头与构图/222-unconventional-composition.md) | 非常规构图——垂直主题×水平画幅与反之 | 主题方向与画幅方向相悖时，用对比、影子、极端角度、黑色裁边、透视篡改等手法扬长避短 |
| [223-split-screen-halves-quarters](05-镜头与构图/223-split-screen-halves-quarters.md) | 分屏与分区——二分法与四分法构图 | 把画格平均切成2/4份：二分冲击强但机械（闪回/痛苦记忆），四分优雅舒适（史诗/街景）；分区数量由叙事基调决定 |
| [240-focal-length-psychology](05-镜头与构图/240-focal-length-psychology.md) | 焦段空间心理学（吕美特） | 广角/中焦/长焦各有空间心理与景深特性，运动方向与焦段匹配决定速度感 |
| [241-lens-plot-progression](05-镜头与构图/241-lens-plot-progression.md) | 镜头情节：焦段渐变叙事法 | 焦段/机位/灯光随剧情弧光系统性渐变，观众不应察觉；单镜位是拼成马赛克的最小质控单位 |
| [262-multi-creature-staging-depth](05-镜头与构图/262-multi-creature-staging-depth.md) | 多动物同框层次——主角精细、中景留步态、远景剪影 | 多动物同框按景别分级给细节：主角动物微动作全保留、中景动物只留步态、远景动物剪影化循环——全精细＝视觉混乱 |
| [267-human-creature-framing](05-镜头与构图/267-human-creature-framing.md) | 人兽同框构图——双主体的高度差与景别选择 | 双主体同框：高度差>1米用仰拍显威胁/俯拍显亲昵；中景为互动默认景别；特写给情感、全景给关系——全景拍亲密＝丢表情 |
| [277-heavy-palm-cinematography](05-镜头与构图/277-heavy-palm-cinematography.md) | 刚猛掌法的镜头语言——降龙十八掌适配机位与节奏 | 刚猛系武功的镜头搭档规则：低角度、前景遮挡、慢-快-慢节奏、受力延迟帧、环境破坏刻度 |
| [300-camera-shake-stacking](05-镜头与构图/300-camera-shake-stacking.md) | 屏幕震动与冲击帧的叠加公式 | 屏幕震动的三参数模型（幅度/频率/衰减）、与冲击帧的时序叠加规则、以及"镜头不冻只震"的现代准则 |
| [326-dance-cinematography-overview](05-镜头与构图/326-dance-cinematography-overview.md) | 街舞拍摄总览——机位高度/焦段/鱼眼美学与舞种-镜头匹配表 | 街舞影像的四条构图铁律、六类机位与舞种匹配、焦段选择、鱼眼经典美学及帧率快门参数，拍摄类条目的总索引 |
| [327-breaking-cinematography](05-镜头与构图/327-breaking-cinematography.md) | Breaking拍摄专项——一套throw-down的五机位脚本与慢动作投放 | Breaking专属拍法：五机位配置、四段throw-down逐段机位切换表、慢动作/回放投放规则与鱼眼风格化机位 |
| [404-director-style-prompts-vol1-part1](05-镜头与构图/404-director-style-prompts-vol1-part1.md) | AI导演风格提示词手册·第一期（上）——六维方法论与王家卫/张艺谋/侯孝贤/姜文/杜琪峰 | 「电影感」要落到焦段/构图/光线/色彩/运动/节奏六维参数；上篇含方法论总纲与王家卫、张艺谋、侯孝贤、姜文、杜琪峰五位导演的六维拆解与整段提示词 |
| [405-director-style-prompts-vol1-part2](05-镜头与构图/405-director-style-prompts-vol1-part2.md) | AI导演风格提示词手册·第一期（下）——贾樟柯/诺兰/韦斯·安德森/昆汀/芬奇 | 第一期下篇：贾樟柯、诺兰、韦斯·安德森、昆汀·塔伦蒂诺、大卫·芬奇五位导演的六维拆解与整段可复制提示词，附漫剧落地建议 |
| [461-escape-pursuit-camera-language](05-镜头与构图/461-escape-pursuit-camera-language.md) | 逃生与逼近镜头语言四条（倒退跟拍/低机位贴地/后视镜逼近/恒速逼近） | 与逃生者同速后撤的倒退跟拍、贴脚踝高度的低机位追击、镜中匀速放大的后视镜逼近、永不停止的恒速逼近——四条英文提示词 |
| [462-grip-resolve-closeups](05-镜头与构图/462-grip-resolve-closeups.md) | 握紧与决意特写三条（指节发白握柄/阴影抬眼/缠带渗血再握紧） | 手比脸先下决心的指节发白握柄、犹豫结束的阴影抬眼、负伤续战的缠带再握紧——三个剧情转折点特写与英文提示词 |
| [474-lib-scene-100](05-镜头与构图/474-lib-scene-100.md) | 场景镜头库（定场镜头六大手法） | 定场镜头六大常用手法的可复用扩写模板，六字段格式，适用分镜与AI视频生成。 |
| [478-lib-camera-100](05-镜头与构图/478-lib-camera-100.md) | 镜头语言技法库（168条） | 运镜/景别/构图/剪辑168条参考，每条附可直接粘贴进视频生成提示词的英文短语。 |
| [479-lib-closeup-100](05-镜头与构图/479-lib-closeup-100.md) | 特写镜头技法库（166条） | 特写镜头166条：只管信息与情绪两种职能，附提示词短语与特写预算制对接。 |

## 06-作画与光影（47）

| 文件 | 标题 | 简介 |
|---|---|---|
| [056-limited-animation-tension](06-作画与光影/056-limited-animation-tension.md) | 限帧/抽帧的张力 | 限帧用"少画"制造静止蓄势，关键瞬间全帧爆发；少即是多的张力经济学 |
| [057-afterimage-tension](06-作画与光影/057-afterimage-tension.md) | 残影/Afterimage 张力 | 残影用拖影制造速度与"未消之动"的悬念；残影数量=速度=威胁，定格后残影消=确认 |
| [058-speed-lines-tension](06-作画与光影/058-speed-lines-tension.md) | 速度线/集中线 | 速度线/集中线把视线强制聚焦一点=注意力钉死=张力加压；集中线指向威胁源 |
| [059-impact-frame](06-作画与光影/059-impact-frame.md) | 冲击帧/Impact Frame | 冲击帧=接触瞬间用单张高细节图替换动画，让"打中"可凝视；峰值最强作画工具 |
| [060-deformation-tension](06-作画与光影/060-deformation-tension.md) | 形变夸张张力 | 形变用夸张变形视觉化力量=重量感；受击形变+出招拉伸=张力，但需快速恢复 |
| [061-shadow-separation-tension](06-作画与光影/061-shadow-separation-tension.md) | 影分离与影张力 | 影可独立成威胁源（影分离）或主体剪影化；影子是潜伏威胁与压迫的视觉工具 |
| [062-line-weight-tension](06-作画与光影/062-line-weight-tension.md) | 线条粗细与张力 | 线条粗细编码重量与锐利：粗线=重量压迫，细线=锐利精致；线粗骤变=张力信号 |
| [063-color-block-impact](06-作画与光影/063-color-block-impact.md) | 色块冲击与张力 | 色块用大面纯色制造视觉冲击；色块对比=张力骤变，单色压满=情绪瞬间 |
| [064-high-contrast-lighting](06-作画与光影/064-high-contrast-lighting.md) | 高对比光影张力 | 高对比光影用强明暗差制造压迫与隐藏；阴影藏威胁，强光揭示瞬间 |
| [065-monochrome-two-color](06-作画与光影/065-monochrome-two-color.md) | 单色/双色张力 | 单色/双色限制=情绪纯粹+对比锐利；单色压满=情绪凝固，双色对立=冲突可视 |
| [066-shadow-gradient-approach](06-作画与光影/066-shadow-gradient-approach.md) | 阴影渐变逼近 | 阴影渐变用逐渐扩大的暗区逼近主体=潜伏威胁的可视化；暗区覆盖=临界 |
| [067-color-temperature-shift](06-作画与光影/067-color-temperature-shift.md) | 色温突变张力 | 色温突变=情绪反转信号；暖转冷=信任崩塌，冷转暖=觉醒希望 |
| [068-backlight-silhouette](06-作画与光影/068-backlight-silhouette.md) | 逆光剪影张力 | 逆光把主体化剪影=神秘+压迫+不可读；Boss登场/决意/决别的共同光影 |
| [069-black-and-white-tension](06-作画与光影/069-black-and-white-tension.md) | 黑白与张力 | 黑白去掉色彩=情绪抽离+对比极致；用于回忆/死亡/决别的极致凝练 |
| [225-line-direction-volume](06-作画与光影/225-line-direction-volume.md) | 线条方向塑体积（布线即结构） | 线条不是轮廓的附属而是塑形手段——布线方向贴合物体表面＝立体感，交叉角度、渐变、压力共同决定质感 |
| [226-three-tone-zone-workflow](06-作画与光影/226-three-tone-zone-workflow.md) | 三色调区域分层推进法 | 动笔前先概括前景/中景/背景三大色调区，三步推进：规划主色调→拉开对比→细节自然浮现，先大关系后细节 |
| [227-four-value-zones-material](06-作画与光影/227-four-value-zones-material.md) | 明暗四区与材质语言 | 受光体积必有高光/中间调/明暗交界线/反射光四区，交界线锐利度＝材质语言，暗部必须留反射光呼吸 |
| [228-no-outline-value-blocking](06-作画与光影/228-no-outline-value-blocking.md) | 无轮廓线光影起稿法 | 现实中不存在轮廓线——物体的边由光影对比定义；起稿只用黑白两色铺大块明暗，第一印象优先于细节 |
| [229-weather-as-narrative](06-作画与光影/229-weather-as-narrative.md) | 天气作为叙事推手 | 天气不是布景而是故事引擎——反常天气自带张力（暴雨+泳池浮尸），雪图形化简洁、雨分层造纵深，换天气＝换含义 |
| [230-grayscale-value-buildup](06-作画与光影/230-grayscale-value-buildup.md) | 灰度渐变与分步渲染法 | 笔刷固定不透明度靠涂抹次数控制深浅；INK正片叠底+TONAL图层工作流；逆光风景四步渲染（打底→排明暗→强调暗部→渲染中间调） |
| [231-depth-separation-atmospheric](06-作画与光影/231-depth-separation-atmospheric.md) | 纵深分离与空气透视 | 相邻面明度必须拉开（前景暗vs远景亮）；越远的细节越小越松散对比越弱；灰度把角色与背景融合成有机整体 |
| [232-focus-and-detail-economy](06-作画与光影/232-focus-and-detail-economy.md) | 焦点制造与细节经济学 | 细节的价值只等于它对整体的贡献——焦点区精雕、次要区简笔；同一构图不同明暗处理＝不同故事点；黑白草图是最高效的构思工具 |
| [242-color-plot-palette-first](06-作画与光影/242-color-plot-palette-first.md) | 色彩情节与调色板先行 | 每部片先建统一色彩系统再拍摄，用调色板、滤镜参数与禁用色清单量化角色弧光。 |
| [302-impact-frame-color-design](06-作画与光影/302-impact-frame-color-design.md) | 冲击帧色彩学——黑底白闪·白底黑闪·单彩色 | 冲击帧的三种色彩方案及其情绪含义——黑白反色、单色剪影、主题色闪，以及色彩与作品调性的匹配原则 |
| [331-dance-imaging-lighting](06-作画与光影/331-dance-imaging-lighting.md) | 街舞影像美学——场景类型、逆光雾光束、色彩阵营与地面资产 | 街舞影像六大经典场景资产、逆光+雾+实用光源布光法、阵营配色与频闪音乐同步、反光地面的视觉证据 |
| [406-scene-alive-ambient-motion](06-作画与光影/406-scene-alive-ambient-motion.md) | 场景生机法则——环境不是死物：常态微动让镜头活起来 | 场景不是死物，必须带对应动作——有风树叶要晃、山里要有飞鸟；按"持续微动/周期变化/偶发生机"三级给环境配动作，根治AI视频的塑料静止感 |
| [427-fabric-material-dynamics](06-作画与光影/427-fabric-material-dynamics.md) | 布料材质×动态对照表：8 种材质的摆动参数与 AI 提示词 | 丝绸/棉布/麻布/皮革/金属甲/薄纱/绒毛/毛衣 8 种常见材质的密度、弯曲阻力、阻尼、沾水反应、提示词写法与稳定性评级速查表 |
| [428-wind-on-clothing-model](06-作画与光影/428-wind-on-clothing-model.md) | 风对衣服的作用模型：风向/风速/阵风/旋风的动态规则与延迟 | 风向与摆向相反、风速决定摆幅（微风15°/强风45°/暴风90°+抽打）、衣摆追风延迟0.1-0.3秒、阵风与旋风的特殊动态 |
| [429-action-fabric-tugging](06-作画与光影/429-action-fabric-tugging.md) | 动作拉扯：跑步/挥刀/摔倒/转身的衣料惯性与滞后动画 | 跑步衣摆后甩、挥刀袖管随臂、摔倒先绷后坠、转身衣角滞后 2-3 帧——4 类常见动作的布料惯性公式与提示词 |
| [430-fitted-vs-loose-clothing](06-作画与光影/430-fitted-vs-loose-clothing.md) | 贴身 vs 宽松：紧身衣不写布料动，宽松衣必须独立微动体 | 紧身衣是身体轮廓的第二层（零布料动态），宽松衣是独立微动体（必须写摆动）；战斗穿紧身/日常穿宽松的场景配置表 |
| [431-skirts-and-special-structures](06-作画与光影/431-skirts-and-special-structures.md) | 裙摆与特殊结构：长/中/短裙摆 + 披风/斗篷/燕尾/长袍的独立动态公式 | 裙摆按长度分三级响应、披风 5-8 段骨链公式、燕尾不对称下摆、长袍下摆拖地的摩擦规则；裙摆"掀角"vs"贴腿"两态切换阈值 |
| [432-wet-fabric-and-moisture](06-作画与光影/432-wet-fabric-and-moisture.md) | 沾水与潮湿布料物理 | 湿衣贴体、重心下坠、水痕分布与干燥过程的视觉与物理规律，以及湿布与风交互的摆幅差异。 |
| [433-tattered-cloth-and-rags](06-作画与光影/433-tattered-cloth-and-rags.md) | 破损与破布条动态 | 破边、撕裂、流苏、补丁的风动态规律，破布条摆动频率与风速长度的关系，战斗中布条脱落的帧级描写。 |
| [434-metal-armor-and-rigid-structures](06-作画与光影/434-metal-armor-and-rigid-structures.md) | 金属甲与硬质结构布料 | 铠甲关节处衬垫的运动规律、甲片碰撞声画同步、以及铠甲上披风摆幅小但周期长的特点。 |
| [435-layered-clothing-dynamics](06-作画与光影/435-layered-clothing-dynamics.md) | 层次叠穿布料动态 | 内衫/外袍/披风三层各自独立的动态规律，内层动小外层动大的阻尼梯度机制，叠穿时外层遮内层的节奏。 |
| [436-temperature-and-fabric-dynamics](06-作画与光影/436-temperature-and-fabric-dynamics.md) | 不同温度下的布料动态 | 温度通过纤维物理变化（热胀冷缩、刚度、摩擦系数）和场景因素（湿度、雪、沙）影响布料摆幅、贴体度和视觉质感。 |
| [437-cloth-motion-prompts-ai](06-作画与光影/437-cloth-motion-prompts-ai.md) | AI 提示词布料动态写法库——30+ 条中英对照按材质分组 | 按 7 种常见材质分组的 30+ 条 AI 视频布料动态提示词，每条附适用场景与稳定性评级，可直接复制进 Sora/MidRunway/Kling/Vidu 等模型 |
| [438-cloth-artifact-fixes-ai-video](06-作画与光影/438-cloth-artifact-fixes-ai-video.md) | AI 视频布料崩坏防治——5 大常见崩坏成因与对策 | AI 视频布料 5 大崩坏类型（穿模/飘向反风/帧数乱抖/布料粘身/手臂动袖子不动）的成因、正向修正与负面提示词、I2V 参数建议 |
| [439-cloth-frame-timing](06-作画与光影/439-cloth-frame-timing.md) | 布料帧级参数表——24fps/30fps 双帧率下的布料动作帧数预算 | 按 24fps 与 30fps 双帧率给出全部布料动作的帧数预算（衣角摆动周期/裙摆掀起/披风下落等），含 on twos 动画下的布料处理规则 |
| [440-cloth-as-emotion-signal](06-作画与光影/440-cloth-as-emotion-signal.md) | 布料作为情绪信号——除了脸，衣服也在说话 | 布料动态是继面部微表情之后的第二情绪通道——紧攥衣角=紧张、袖口扯皱=烦躁、披风甩一下=转身离开，AI 视频提示词可直接写情绪→布料动作映射 |
| [441-cloth-battle-rhythm](06-作画与光影/441-cloth-battle-rhythm.md) | 布料与战斗节奏——布料是无声的战斗节拍器 | 出拳前衣角先动 0.2 秒=预判信号、闪避时衣服滞后=视觉残影、必杀前披风大掀=蓄力信号——布料动态是战斗节奏的独立节拍层 |
| [442-skirt-dynamics-walk-run](06-作画与光影/442-skirt-dynamics-walk-run.md) | 裙摆动力学——走路/奔跑/转身的布料节奏 | 裙摆是走路/奔跑节奏的"节拍器"——走路时小摆（同步脚步）、奔跑时后甩（滞后身体 1-2 帧）、转身时滞后甩出再回摆；高跟鞋减小摆幅、平底鞋加大摆幅 |
| [443-cape-cloak-dynamics](06-作画与光影/443-cape-cloak-dynamics.md) | 披风/斗篷专篇——长度·姿态·镜头引导三重视角 | 披风/斗篷是角色的"第二动作系统"——短披肩硬挺角、中披风波浪 S、长大披风流体拖曳；还能引导视线、作为转场 |
| [444-hair-physics-follow-through](06-作画与光影/444-hair-physics-follow-through.md) | 头发物理——挂在头上的"第二披风"动力学 | 头发 = 挂在头上的独立微动体——长发软滞后、短发硬快摆、扎辫有独立摆动相位；转头滞后、奔跑后甩、长发飘肩过脸 |
| [445-accessories-small-objects-physics](06-作画与光影/445-accessories-small-objects-physics.md) | 配饰与小物件物理——低成本微动信号库 | 配饰是角色的"低成本微动信号"——耳环/项链/腰带/鞋带各有专属摆动规则；奔跑时统一往后、停下时再摆 1-2 帧才停 |
| [446-cloth-physics-breakdown-methodology](06-作画与光影/446-cloth-physics-breakdown-methodology.md) | 布料物理实片拆解方法论——六步从参考到提示词 | 六步拆解法：取元数据→抽帧→标注材质/风向/动作→分类→对照参数表→提示词产出；对鬼灭披风/进巨斗篷/死神队长袍/武侠披风等经典案例逐一拆解 |
| [464-lib-vfxshot-100](06-作画与光影/464-lib-vfxshot-100.md) | 特效镜头拍法库（141条） | 特效作画/拍法141条：管画面里的特效怎么画，对接冲击三级制与作画签名技法。 |

## 07-动作与战斗（94）

| 文件 | 标题 | 简介 |
|---|---|---|
| [025-ready-stance-tension](07-动作与战斗/025-ready-stance-tension.md) | 待机姿势张力：居合与对峙 | 待机姿势是静态张力的容器：居合拔刀姿、侧身对峙、低姿态蓄势，姿势本身即揪心 |
| [026-action-windup](07-动作与战斗/026-action-windup.md) | 动作前摇的累积 | 前摇=动作爆发前的预备动作，拉长前摇=延迟释放=张力加压；前摇越细节越揪心 |
| [027-gaze-line-crossing](07-动作与战斗/027-gaze-line-crossing.md) | 凝视与视线交错 | 凝视是静态张力的视线版：视线锁定=注意力锚定；视线交错/偏移=动摇信号 |
| [028-footwork-distance](07-动作与战斗/028-footwork-distance.md) | 步法与距离控制 | 步法控距离=空间轴加压：逼近=威胁累积，拉开=喘息；距离骤变是交锋信号 |
| [030-hand-details](07-动作与战斗/030-hand-details.md) | 手部细节：握刀与颤抖 | 手部是张力最浓缩的细节区：握刀松紧=心理，颤抖=压抑，指节发白=决意；大特写锁定 |
| [031-ensemble-individual-action](07-动作与战斗/031-ensemble-individual-action.md) | 群戏个体动作编织 | 群戏张力靠个体动作错位编织：主角蓄势+旁人微动+反派锁定，分层动避免糊成一团 |
| [121-battle-three-act-structure](07-动作与战斗/121-battle-three-act-structure.md) | 战斗三幕式（建压-爆点-释放） | 一场好打的仗就是一出小话剧；建压-爆点-释放三幕骨架不破 |
| [122-duel-vs-group-battle](07-动作与战斗/122-duel-vs-group-battle.md) | 单挑 vs 群战结构差异 | 单挑靠心理与势转换，群战靠空间调度与节奏切片 |
| [123-weapon-style-rhythm](07-动作与战斗/123-weapon-style-rhythm.md) | 武器流派与战斗节奏 | 一寸长一寸强，一寸短一寸险；武器决定战斗节奏与镜头分配 |
| [124-momentum-shift](07-动作与战斗/124-momentum-shift.md) | 战斗中的势转换（攻守易势） | 战斗的灵魂是势的来回；攻转守易，守转攻难，势转即剧情转 |
| [125-boss-battle-stages](07-动作与战斗/125-boss-battle-stages.md) | BOSS战编排套路 | BOSS战是叙事压舱石；多阶段+形态升级+主角认知破局三件套 |
| [126-fight-pacing-cut-frequency](07-动作与战斗/126-fight-pacing-cut-frequency.md) | 战斗分镜节奏（快慢切与切片频率） | 战斗节奏=切片时长组合；快切堆不出张力，长切才建情绪 |
| [127-fight-keyframe-selection](07-动作与战斗/127-fight-keyframe-selection.md) | 战斗关键帧选择（接触/蓄力/受击/反作用） | 一招四帧：蓄力+接触+变形+反作用；选对帧才有冲击感 |
| [128-weapon-clash-physics](07-动作与战斗/128-weapon-clash-physics.md) | 武器交锋的物理感呈现 | AI出图常飘——靠重量词+惯性词+冲击波让武器有分量 |
| [129-fight-camera-movement](07-动作与战斗/129-fight-camera-movement.md) | 战斗运镜手法（跟拍/环绕/甩拍/手持） | 战斗运镜四件套：跟拍追势、环绕表势、甩拍转场、手持加乱 |
| [130-fight-camera-angle](07-动作与战斗/130-fight-camera-angle.md) | 战斗角度选择（仰拍/俯拍/越肩/POV/倾斜） | 角度即权力——仰拍优势方、俯拍劣势方、倾斜表失衡 |
| [182-action-scene-three-rules](07-动作与战斗/182-action-scene-three-rules.md) | 动作戏三铁律——张力靠"按"、招式靠"换维"、相交靠"几何 | 三条从实战返工中提炼的动作戏铁律：张力靠延迟释放而非加动作；招式靠维度轮换而非加招数；写"相交/接触/压住"必须给全几何四要素否则武器共面穿模 |
| [183-weapon-persistence](07-动作与战斗/183-weapon-persistence.md) | 武器/道具持久性——别让手里的剑凭空消失 | 变招/切镜时武器忽隐忽现=道具持久性失败；根因三层（缺武器锚词/运镜出画入画/负向词只防穿模），修法是每Shot复写武器状态锚＋运镜把剑留在框内＋补消失类负向词 |
| [234-action-four-phase-template](07-动作与战斗/234-action-four-phase-template.md) | 动作四阶段拆解模板（起始-发力-顶点-收势） | 把任何格斗动作拆成起始-发力-顶点-收势四段写提示词，收势必须带残心 |
| [235-unarmed-power-chain](07-动作与战斗/235-unarmed-power-chain.md) | 徒手格斗发力链（踢/拳/防御） | 踢拳防三条发力链：力从地起经腰胯传导到末端，配17组对战动作速查表与架势距离逻辑 |
| [236-weapon-action-discipline](07-动作与战斗/236-weapon-action-discipline.md) | 持械动作纪律（枪/刀/钝器） | 武器是身体的延长线，持械动作需额外遵守器械纪律：枪口指向管理、刀架势含义、钝器惯性控制，翻滚跑酷中器械贴身不干扰团身。 |
| [237-female-combat-body-language](07-动作与战斗/237-female-combat-body-language.md) | 女子格斗体态语言 | 女性骨盆宽重心低、躯干短四肢长，踢技线条修长；柔韧优势可完成一字/过头幅度；发力靠全身协调链，动作流畅弹性；少女体态+凌厉动作形成反差感。 |
| [238-action-camera-matrix](07-动作与战斗/238-action-camera-matrix.md) | 动作戏视角×服装矩阵 | 九种视角各有叙事功能：全景交代全貌、斜侧展示纵深、近景捕捉击中瞬间、俯拍仰拍风格化强点；同一动作按全景→斜侧→近景→仰/俯拍排布分镜骨架。 |
| [258-escape-struggle-in-arms](07-动作与战斗/258-escape-struggle-in-arms.md) | 怀中挣扎/逃脱动作设计——支点扭转的挣脱逻辑 | 挣扎不是乱晃：动物以人手臂间隙为杠杆，C/S型扭转、四肢找支点、头先朝逃脱方向——无支点逻辑的挣扎＝木偶抖 |
| [260-large-animal-weight-inertia](07-动作与战斗/260-large-animal-weight-inertia.md) | 大型动物的重量与惯性——推拉拖拽的体态代偿 | 大型动物质量大惯性大：启动延迟0.5-2s、人拉时前倾15-30°推时后仰10-20°——直立轻松拉动巨兽＝物理穿帮 |
| [270-dragon-palms-overview-yijing](07-动作与战斗/270-dragon-palms-overview-yijing.md) | 降龙十八掌总纲——易经卦象武学体系与版本口径 | 降龙十八掌以易经卦象为骨、刚猛收发为魂；十八招名单、版本差异与AI改编口径总表 |
| [271-dragon-palms-moves-1-6](07-动作与战斗/271-dragon-palms-moves-1-6.md) | 降龙十八掌·上六招详解（亢龙有悔/飞龙在天/见龙在田/鸿渐于陆/潜龙勿用/利涉大川） | 降龙掌第1-6招逐招拆解：卦象、动作要领、用法场景与AI生成提示词对照 |
| [272-dragon-palms-moves-7-12](07-动作与战斗/272-dragon-palms-moves-7-12.md) | 降龙十八掌·中六招详解（突如其来/震惊百里/或跃在渊/双龙取水/鱼跃于渊/时乘六龙） | 降龙掌第7-12招逐招拆解：卦象、动作要领、用法场景与AI生成提示词对照 |
| [273-dragon-palms-moves-13-18](07-动作与战斗/273-dragon-palms-moves-13-18.md) | 降龙十八掌·下六招详解（密云不雨/损则有孚/龙战于野/履霜冰至/羝羊触藩/神龙摆尾） | 降龙掌第13-18招逐招拆解：卦象、动作要领、用法场景与AI生成提示词对照 |
| [274-kanglong-youhui-mechanics](07-动作与战斗/274-kanglong-youhui-mechanics.md) | 亢龙有悔专项——"盈不可久"的收发力学 | 降龙总纲招深度拆解：发十分留二十分的力学逻辑、为什么它是第一招、AI表现要点 |
| [275-dragon-palms-user-variants](07-动作与战斗/275-dragon-palms-user-variants.md) | 降龙十八掌使用者差异——萧峰/洪七公/郭靖三种劲路 | 同一套掌法三种气质：萧峰刚猛直出、洪七公七虚七实、郭靖刚柔互济；角色绑定劲路表 |
| [278-dragon-palms-fight-choreography](07-动作与战斗/278-dragon-palms-fight-choreography.md) | 降龙十八掌对打编排——刚猛掌法对阵三类对手的战术设计 | 降龙掌vs灵巧型/内力型/兵刃型三类对手的编排公式，含挫败感与压制感的镜头实现 |
| [279-yijing-move-design-method](07-动作与战斗/279-yijing-move-design-method.md) | 易经卦象动作设计法——从卦辞提取动作意象的通用方法论 | 卦辞→动作意象三要素（方位/劲路/节奏）的转译方法，可推广到一切易经系武功的原创设计 |
| [280-six-meridian-sword](07-动作与战斗/280-six-meridian-sword.md) | 六脉神剑六路剑诀——无形剑气的六指分工 | 六路剑气逐路拆解：指位/经络/特点/气质对照表，段誉时灵时不灵的叙事功能与表现 |
| [282-lingbo-weibu-steps](07-动作与战斗/282-lingbo-weibu-steps.md) | 凌波微步——六十四卦步法与"边跑边练功"的动功设计 | 凌波微步的卦象步法逻辑、动功练内力的独特设定、闪避美学与AI生成要点 |
| [283-dog-beating-staff-eight](07-动作与战斗/283-dog-beating-staff-eight.md) | 打狗棒法八诀三十六路——巧劲兵刃体系的招式库 | 打狗棒法绊劈缠戳挑引封转八诀详解，三十六路结构与招式名库，巧劲棒法的动作设计 |
| [284-douzhuan-xingyi-rebound](07-动作与战斗/284-douzhuan-xingyi-rebound.md) | 斗转星移——借力打力的"反弹"逻辑与镜头表现 | 慕容家绝技的反弹原理、"出手越高死法越巧"的叙事规则、镜像构图的镜头表现法 |
| [285-beiming-absorb-three-systems](07-动作与战斗/285-beiming-absorb-three-systems.md) | 北冥神功/吸星大法/化功大法——吸功三体系的区别与视觉化 | 三大吸功绝学的原理差异（负极引正极/空洞丹田/只化不吸）、等级关系与吸取过程的镜头表现 |
| [286-tianshan-plum-sixyang](07-动作与战斗/286-tianshan-plum-sixyang.md) | 天山折梅手与天山六阳掌——逍遥派"化尽天下武功"的包容性招式库 | 折梅手六路包容天下招式的"永远学不完"设定与六阳掌六式"阳"字诀，虚竹笨拙身负绝学的反差表现 |
| [287-shengsi-fu-ice-talisman](07-动作与战斗/287-shengsi-fu-ice-talisman.md) | 生死符——液体暗器与延迟生效的痛苦表现 | 以水成冰的暗器机制、入体即溶的隐蔽性、麻痒剧痛的延迟发作表现与镇痒丸控制体系 |
| [288-huoyan-dao-jiumozhi](07-动作与战斗/288-huoyan-dao-jiumozhi.md) | 火焰刀专项——鸠摩智的无形刀气，名刀实掌 | 名为刀法实为掌法的设定陷阱、掌缘气劲的三重效果（灼热/破罡/穿透）与高僧外观反差 |
| [289-qinlong-konghe-telekinesis](07-动作与战斗/289-qinlong-konghe-telekinesis.md) | 擒龙功与控鹤功——隔空取物的念力类武功表现 | 隔空取物类武功的力学视觉化：无形牵引的三段式（锁定/起物/归手）与震慑场面的群像反应 |
| [291-skill-tension-four-principles](07-动作与战斗/291-skill-tension-four-principles.md) | 技能张力四原则——招式不是放出去就完事 | 技能释放的四拍节奏法则、势大于形的表现原则、角色情绪与技能的共振关系、环境反馈的必要性 |
| [292-impact-frame-overview](07-动作与战斗/292-impact-frame-overview.md) | 冲击帧总纲——1-2帧的"视觉音效 | 冲击帧的定义、本质、与前后帧的反差原则，以及"看见的不是帧本身而是冲击"的心理机制 |
| [293-impact-frame-history-kanada](07-动作与战斗/293-impact-frame-history-kanada.md) | 冲击帧发展史——从金田伊功到中村丰 | 黑白闪的源流——金田伊功1970年代首创、EVA普及、Neo-Kanada复兴、中村丰集大成，以及各时代的形态演变 |
| [294-black-white-flash-grammar](07-动作与战斗/294-black-white-flash-grammar.md) | 黑白闪三段语法——小点·爆发·反色 | 标准黑白闪的"收缩-爆发-反色"三帧结构，以及连续闪、负片对仗等变体编排 |
| [295-impact-frame-five-types](07-动作与战斗/295-impact-frame-five-types.md) | 冲击帧五大类型——反色/剪影/抽象/插画/文字 | 冲击帧的五种形态分类与各自适用场景——颜色反转型、黑色剪影型、抽象图形型、精细插画型、文字拟声型 |
| [297-hitstop-vs-impact-frame](07-动作与战斗/297-hitstop-vs-impact-frame.md) | 顿帧Hitstop——冲击帧的时间孪生 | 顿帧的本质是"作用力与反作用力的短暂对抗"而非单纯"命中了"，与冲击帧的分工（时间vs画面），及联用公式 |
| [298-hitstop-frame-budget](07-动作与战斗/298-hitstop-frame-budget.md) | 顿帧数值配置表——轻重攻击的帧数手感 | 60fps基准下轻/中/重/破防各级攻击的顿帧帧数带宽、软冻结替代方案，及帧数与武器量级的映射表 |
| [299-smear-vs-impact-frame](07-动作与战斗/299-smear-vs-impact-frame.md) | 残影帧Smear与冲击帧的分工——速度vs冲击 | 残影帧与冲击帧的本质分工——前者表现"快"，后者表现"重"；拉长变形、多重残像两类残影语法与适用场景 |
| [308-impact-four-layer-combo](07-动作与战斗/308-impact-four-layer-combo.md) | 打击感四层组合拳——冲击帧·顿帧·震动·音效 | 打击感的完整四层模型——画面层（冲击帧）、时间层（顿帧）、空间层（震动）、听觉层（音效）的叠加公式与分级配置 |
| [313-street-dance-overview](07-动作与战斗/313-street-dance-overview.md) | 街舞体系总览——舞种分类、发力体系与节拍逻辑 | 街舞九大舞种一图分清，站姿/地面/电流三大发力体系，8拍逻辑与grove/bounce底层——所有街舞分镜的总索引 |
| [314-breaking-toprock](07-动作与战斗/314-breaking-toprock.md) | Breaking-Toprock完整基础步——站姿舞步全套拆解 | Breaking站姿段全套基础步：Indian/Salsa/Crossover/Kick&T Twist等动作要领、8拍组合套路与AI生成要点 |
| [315-breaking-footwork](07-动作与战斗/315-breaking-footwork.md) | Breaking-Footwork地面脚步——6步/CC/3步/12步体系拆解 | Breaking地面段核心：6步标准轨迹、CC内八弹步、3步快圈、12步双绕及直升机等变化，含俯拍走位图与AI防穿模要点 |
| [316-breaking-freezes](07-动作与战斗/316-breaking-freezes.md) | Breaking-Freezes定格体系——Baby/Chair/Air/Hollowback全级拆解 | Breaking定格收尾动作库：从肘撑支点原理到Baby/Chair/Air/Hollowback各级freeze造型、hold拍数与镜头选择 |
| [317-breaking-powermoves-basic](07-动作与战斗/317-breaking-powermoves-basic.md) | Breaking-PowerMoves基础篇——背旋/风车/Swipe三大惯性招 | Breaking地面旋转三大基础大招：背旋与风车的肩滚差异、风车V字腿循环、Swipe四点腾空换位，含起势/循环/收招镜头脚本 |
| [318-breaking-powermoves-advanced](07-动作与战斗/318-breaking-powermoves-advanced.md) | Breaking-PowerMoves高阶篇——托马斯/大回环/头转/1990/2000 | Breaking空中系五大旋转大招形态辨识与力学要点、连招衔接顺序、仰角机位与AI分段生成策略 |
| [319-popping-hit-wave-isolation](07-动作与战斗/319-popping-hit-wave-isolation.md) | Popping核心技术——Hit/Pop、Wave电流、Isolation隔离与Boogaloo | Popping四大原子技术：重拍肌肉pop的部位分解、手臂/全身电流的逐关节传导链、隔离定点与Boogaloo滚动，附逐拍动画锚点 |
| [320-popping-tutting-robot-glide](07-动作与战斗/320-popping-tutting-robot-glide.md) | Popping风格族——Tutting几何手/Robot机器人/Glide滑步三大错觉术 | Popping三大招牌错觉风格：直角几何的Tutting、伺服电机质感的Robot、反物理滑行的Glide/太空步，含手脚切换帧与机位要求 |
| [321-locking-foundations](07-动作与战斗/321-locking-foundations.md) | Locking锁舞完整基础——Lock/Point/Twirl/Scooby/Skeeter Rabbit动作体系 | Locking舞种全套基础动作与表演语法：锁姿、指、绕腕、踢换步等招牌动作拆解，Funk半蹲groove与笑容互动的镜头用法 |
| [322-hiphop-party-steps](07-动作与战斗/322-hiphop-party-steps.md) | Old School Hip-Hop派对舞步全套——Running Man到Reebok的基础词汇 | Hip-Hop舞种的派对舞步词汇表：10个最高辨识招牌步的动作拆解、统一bounce底层与群舞排列用法 |
| [323-house-dance-steps](07-动作与战斗/323-house-dance-steps.md) | House Dance脚步体系——Jack律动/Farmer/Pas de Bourrée/Loose Leg | House舞种核心：Jacking躯干律动与快而轻的脚步词汇，三步切分逻辑、流动走位与跟拍镜头适配 |
| [324-krump](07-动作与战斗/324-krump.md) | Krump狂派舞——Chest Pop/Arm Swing/Stomp/Jab四大元素与爆发语法 | Krump四大基础动作、buck质感与情绪叙事语法，适配动漫变身穿爆发、愤怒战斗、野兽化场面的动作库 |
| [325-waacking-voguing](07-动作与战斗/325-waacking-voguing.md) | Waacking与Voguing——甩臂重击与T台造型两大俱乐部舞种 | Waacking的快速绕臂重击语法与Voguing三派系五元素（手/猫步/鸭步/旋转dip/地面），造型线条与镜头机位适配 |
| [358-skill-magic-writing-overview](07-动作与战斗/358-skill-magic-writing-overview.md) | 技能魔法编写二十连①——编写总纲：四层模型与好能力的七条标准 | 技能不是一招画面而是跨四层的系统：设定层/叙事层/视觉层/提示词层；好能力=有规则有限制有代价有个性有成长有画面有区分度；系列导航358-377 |
| [359-hard-soft-magic-sanderson-laws](07-动作与战斗/359-hard-soft-magic-sanderson-laws.md) | 技能魔法编写二十连②——硬魔法与软魔法：桑德森三定律与规则透明度 | 第一定律理解度决定解决冲突的权限；第二定律限制>能力；第三定律深挖而非新增；硬魔法给满足感软魔法给敬畏感，同一部剧可分区混用 |
| [360-skill-naming-craft](07-动作与战斗/360-skill-naming-craft.md) | 技能魔法编写二十连③——能力命名学：名字的两个职能与五大命名范式 | 好名字同时描述画面与适合被喊出；日式式-形-名三段、格斗游戏白描复合词、日式解放令、JOJO文化借名、中式易经意象五范式；喊招是节拍不是义务 |
| [361-mechanic-five-elements](07-动作与战斗/361-mechanic-five-elements.md) | 技能魔法编写二十连④——机制五要素：触发/输入输出/代价/边界/失败模式（AALC扩展） | 一个能写戏的机制必须答清五件事：怎么触发、烧什么产什么、代价、边界与克制、失败时怎样；AALC（表象-能力-限制-代价）补上"长什么样 |
| [362-power-cost-system](07-动作与战斗/362-power-cost-system.md) | 技能魔法编写二十连⑤——代价体系：代价的五个去向、负担路径与腐蚀滑坡 | 好代价是改变下一步选择的支付；五类去向（身体/资源/地方/秘密/转嫁）；代价的戏剧价值在"负担路径"；腐蚀滑坡=持续把代价转嫁给他人；每个主角留一项不可逆代价 |
| [363-power-scaling-ceiling](07-动作与战斗/363-power-scaling-ceiling.md) | 技能魔法编写二十连⑥——战力曲线与天花板：战力通胀死循环的五条出路 | 每弧更强敌人→主角更强→数字失去意义；开局先定天花板；策略多样替代蛮力；明示数值杀死悬念；任何能力不得成为"自动胜利的叙事缩写 |
| [365-power-debut-ritual](07-动作与战斗/365-power-debut-ritual.md) | 技能魔法编写二十连⑧——首秀仪式：能力第一次登场的五拍结构与"一次定终身 | 首秀一次定终身——机制、代价、人设、视觉口径全部在首战建立；先立人再立世界；五拍：需求→挣扎→显形→定价→后果；危险逼出而非剧情赠送；首秀即视觉正典资产 |
| [366-writing-skills-in-combat](07-动作与战斗/366-writing-skills-in-combat.md) | 技能魔法编写二十连⑨——战斗中写技能：意图-出招-应对的回合棋与beat-breath-burst | 技能战是棋局不是烟花：每个回合=出意图题→出招→应对，攻防转换即信息交换；能力在战斗中以应用而非讲解出现；beat-breath-burst呼吸节律；首看者测试 |
| [367-combo-team-skills](07-动作与战斗/367-combo-team-skills.md) | 技能魔法编写二十连⑩——组合技与连携：分工先于合体、铺垫先于成功 | 好组合不是两个大招叠加而是清晰分工（控制-惩罚/前台-后排）；四型：铺垫扣杀/元素融合/接力传手/环境触发；首次组合必须先失败或有信任铺垫；AI生成拆开拍再合成 |
| [368-counter-and-underdog](07-动作与战斗/368-counter-and-underdog.md) | 技能魔法编写二十连⑪——克制与以弱胜强：规则差比数值差好看，JOJO式破题四步 | 智斗赢家不是更强而是更懂规则：识别规则→找自然弱点→改造赛场→把自己的限制当掩体；克制链要双向有解；弱者胜利四来源：知识/赛场/准备/信息差 |
| [369-power-loss-suppression](07-动作与战斗/369-power-loss-suppression.md) | 技能魔法编写二十连⑫——技能失效与受限：失能戏的五种来源与"失去力量才看见人 | 失能不是削弱角色是把镜头还给人；五种来源（条件/代价/外力压制/心理/过载）；好限制自带时限与可干预性；失能段证明英雄之所以是英雄不靠能力；恢复必须由人物选择挣回 |
| [370-powerup-awakening-transformation](07-动作与战斗/370-powerup-awakening-transformation.md) | 技能魔法编写二十连⑬——升级·觉醒·变身：相变而非换装、铺垫的兑现窗口 | 变身是机制相变（速度/打法/性格规则全换）不是换色服装；合理升级=远期伏笔+触发事件+首次失控+代价+后续掌握；每次升级改变解题方式而非加大数字 |
| [371-original-skill-design](07-动作与战斗/371-original-skill-design.md) | 技能魔法编写二十连⑭——原创技能设计法：母题转译管线与"搬移而非创造"约束 | 原创=熟悉母题+陌生约束：取物理/匠艺/领域母题→选能力动词→加一条守恒式约束（只搬移不创造）；五型分类（放出/变形/突变/蓄积/混合）；原创度检验看应用而非元素 |
| [373-team-ability-composition](07-动作与战斗/373-team-ability-composition.md) | 技能魔法编写二十连⑯——群像能力配置：职能位、覆盖测试与色板隔离 | 先按职能位填坑（领/副/盾/智/心＋侦查护持），再让性格与能力错位制造戏；覆盖测试：每个战场问题恰好一人主解；能力色板/距离/节奏三维度防撞；阵容3-5人为宜 |
| [375-modern-psychic-abilities](07-动作与战斗/375-modern-psychic-abilities.md) | 技能魔法编写二十连⑱——现代异能：时间/空间/心智类高抽象能力的边界与落地 | 越抽象越要立死规则且不许挪球门；时间三模型（闭环/分支/可变）必须早锁；读心/瞬移/概率系各有专属边界清单；抽象能力必须介质显影并处理日常后果 |
| [376-summon-tame-companion](07-动作与战斗/376-summon-tame-companion.md) | 技能魔法编写二十连⑲——召唤·驯驭·伙伴：契约双向性、生物意志与不可驯之物 | 驯驭不是收集卡片：契约必须双向约束与双向代价、生物保留自己的意志与行为逻辑、数量/时长/距离/命令精度全有限制；最强的生物必须不可驯；羁绊是关系不是技能开关 |
| [398-fight-storyboard-50-index](07-动作与战斗/398-fight-storyboard-50-index.md) | 高燃武打分镜 50 式·总索引与万能公式 | 50个高燃武打分镜模板总纲：8要素万能公式+场景反馈三层+节奏三件套+战斗宏观三段式（近身/交手/收尾）与连招组装原则+五大类索引与50条速查清单 |
| [399-fight-template-melee-burst](07-动作与战斗/399-fight-template-melee-burst.md) | 高燃武打分镜模板·近身爆发类（01-10） | 近身爆发类10条模板逐条转写：贴身缠斗靠冲击力和痛感抓人，每条含景别/机位/运镜/动作/场景反馈五要素 |
| [400-fight-template-weapon-clash](07-动作与战斗/400-fight-template-weapon-clash.md) | 高燃武打分镜模板·兵器交锋类（11-20） | 兵器交锋类10条模板逐条转写：刀剑枪戟胜负在一寸之间，每条含景别/机位/运镜/动作/场景反馈五要素 |
| [401-fight-template-elemental-spell](07-动作与战斗/401-fight-template-elemental-spell.md) | 高燃武打分镜模板·异能法术类（21-30） | 异能法术类10条模板逐条转写：元素出手画面爽点在于"形"，每条含景别/机位/运镜/动作/场景反馈五要素 |
| [402-fight-template-speed-blink](07-动作与战斗/402-fight-template-speed-blink.md) | 高燃武打分镜模板·高速瞬移类（31-38） | 高速瞬移类8条模板逐条转写：速度感的关键是让观众"追不上"，每条含景别/机位/运镜/动作/场景反馈五要素 |
| [403-fight-template-finisher](07-动作与战斗/403-fight-template-finisher.md) | 高燃武打分镜模板·必杀终结类（39-50） | 必杀终结类12条模板逐条转写：一锤定音把前面的压抑一次还清，每条含景别/机位/运镜/动作/场景反馈五要素 |
| [456-collapse-destruction-vfx](07-动作与战斗/456-collapse-destruction-vfx.md) | 坍塌·崩落特效拍法四条（建筑崩塌分层/尘浪推进/巨石追击/逐级崩解） | 建筑整体崩塌的重量分层写法、尘浪贴地推进、巨石滚落追击的遮挡-显露节奏、拉普达式逐级崩解——四条可直接粘贴的英文提示词 |
| [457-hunt-pursuit-choreography](07-动作与战斗/457-hunt-pursuit-choreography.md) | 追猎·猎杀战编排四参照（恒速逼近/盲区反杀/剪影数量感/间距量化） | 女巨人森林追击的恒速逼近、甚尔猎杀的安全瞬间反杀、蚀之刻的剪影数量感、邪魔神的间距量化——追猎戏四条可复用编排规律 |
| [458-fire-serpent-spell-anatomy](07-动作与战斗/458-fire-serpent-spell-anatomy.md) | 蛇形焰流法术视觉解剖（豪龙火 / 炎之呼吸玖之型·炼狱） | 火蛇有头有躯干、贴地S形游走扑咬而非直线喷射；绳状炎蛇盘刀甩出缠卷爆燃——两条火蛇系法术五段式解剖与英文提示词 |
| [459-chain-spell-anatomy](07-动作与战斗/459-chain-spell-anatomy.md) | 锁链系法术视觉解剖（天之锁 / 金刚封锁） | 锁链自金色涟漪射出、链节逐节甩直带金属惯性、螺旋缠绕绞紧迸火花——锁链系法术五段式解剖与英文提示词 |
| [460-terrain-collapse-spell-anatomy](07-动作与战斗/460-terrain-collapse-spell-anatomy.md) | 地形崩落法术视觉解剖（地动核·土遁崩落） | 掌心拍地为锚、放射裂纹隆起、巨岩-碎石-粉尘三层崩落有先后、尘浪过后地形永久改写——土遁崩落五段式解剖与英文提示词 |
| [465-lib-spell-100](07-动作与战斗/465-lib-spell-100.md) | 法术/技能特效描写库（129式） | 法术特效129式：锚定特效+法术解剖学五段式+消散美学，提示词可直接粘贴。 |
| [466-lib-classfight-100](07-动作与战斗/466-lib-classfight-100.md) | 职业对战编排库（154条） | 职业对战编排154条：33对战组合+99可拍桥段+16职业个性+6双人阵型组合技。 |
| [477-lib-fight-100](07-动作与战斗/477-lib-fight-100.md) | 传奇打戏拆解库 · 动漫史100+场经典战斗 | 动漫史100+场经典打戏的可复用技法库：共性十律+分门别类技法，每条附提示词写法。 |

## 08-分镜与连贯性（31）

| 文件 | 标题 | 简介 |
|---|---|---|
| [005-分镜表标准字段](08-分镜与连贯性/005-分镜表标准字段.md) | 动漫短剧分镜表标准字段 | 一镜一行的分镜表字段定义，用于 AI 视频分段生成调度 |
| [131-axis-180-rule](08-分镜与连贯性/131-axis-180-rule.md) | 轴线与180度规则（空间连续性的地基） | 摄影机别越过那条看不见的线；越轴=观众瞬间迷路 |
| [132-match-on-action](08-分镜与连贯性/132-match-on-action.md) | 动作匹配剪辑（Match on Action） | 在动作最动的那帧切开换角度——观众的注意力被动作吸走，剪辑点隐形 |
| [133-eyeline-match](08-分镜与连贯性/133-eyeline-match.md) | 视线匹配与正反打（Eyeline Match & Shot Reverse Shot） | 观众跟着角色的视线走；视线接对了，两个镜头就是同一个空间 |
| [134-match-cut](08-分镜与连贯性/134-match-cut.md) | 匹配剪辑（Match Cut：形状/运动/色彩的缝合术） | 用相似性把两个不相干的镜头缝起来；形状、运动、色彩皆可作针脚 |
| [135-causal-transition](08-分镜与连贯性/135-causal-transition.md) | 承接转场与因果链（剧情不跳跃的叙事逻辑） | 画面连贯靠技法，剧情连贯靠因果；每场戏必须回答"因为什么"和"所以什么 |
| [136-visual-flow-line](08-分镜与连贯性/136-visual-flow-line.md) | 视觉引导线与动线一致性（视线的轨道工程） | 观众的眼睛是被你牵着走的；动线顺=看得爽，动线乱=看得累 |
| [137-j-cut-l-cut](08-分镜与连贯性/137-j-cut-l-cut.md) | 声音先导与声画错位（J-cut / L-cut） | 声音比画面早到或晚走，两个场景就被听觉缝在一起 |
| [138-ai-multishot-continuity](08-分镜与连贯性/138-ai-multishot-continuity.md) | AI多镜头连续性（锚点接力工作流） | AI没有记忆，所以你要当它的记忆；每个镜头的状态靠锚点手工接力 |
| [139-time-ellipsis](08-分镜与连贯性/139-time-ellipsis.md) | 时间省略与压缩（叙事时间的剪辑工程学） | 观众不需要看全过程——只需要看懂"过了多久"和"期间变了什么 |
| [140-continuity-checklist](08-分镜与连贯性/140-continuity-checklist.md) | 分镜连贯性自检清单（连贯QA流程） | 把131-139的法则变成一张打勾表；生成前自查，剪辑前复查 |
| [185-shot-purpose-audit](08-分镜与连贯性/185-shot-purpose-audit.md) | 镜头存在理由自检（三功能）与组接三原则 | 每镜须承担叙事／情感／视觉引导至少一项，三项皆无即废镜该删；组接守连续性、节奏感、逻辑性 |
| [186-triangle-system-axis](08-分镜与连贯性/186-triangle-system-axis.md) | 三角机位系统与越轴六法 | 180°半圆内三点成三角互连机位，六种合法越轴各有专用过渡手段 |
| [189-dialogue-two-person-staging](08-分镜与连贯性/189-dialogue-two-person-staging.md) | 双人对话场面调度（机位方案库） | I 形态下位置一~十的双人机位库：从侧拍、过肩到低角度反拍，按亲疏对立取用；附双人情感互动公式（A动作+B反应+接触位置+距离+视线+镜头） |
| [190-dialogue-multi-person-staging](08-分镜与连贯性/190-dialogue-multi-person-staging.md) | 三人及多人对话调度：A/L/I 形态与字母模式 | 用 A/L/I 形态与字母模式拆解三人以上对话；多人先锁 2 人轴线再做合并简化 |
| [191-shot-flow-scene-intro](08-分镜与连贯性/191-shot-flow-scene-intro.md) | 镜流与用景别交代场景 | 镜流=镜头连接的流动观感；用景别递进、后拉揭示或特写蒙太奇来交代场景 |
| [197-dolly-staging-camera-path](08-分镜与连贯性/197-dolly-staging-camera-path.md) | 推轨调度：以控制摄影机路径取代人物路径 | 推轨基本型与室内外衔接，核心是动作受地形约束时用摄影机路径取代人物路径 |
| [199-storyboard-drawing-conventions](08-分镜与连贯性/199-storyboard-drawing-conventions.md) | 手绘故事板规范 | 手绘故事板的技巧、材料与画法规范：用简练线条图解摇镜、推轨、升降、变焦与景别变更 |
| [224-graphic-novel-panel-language](08-分镜与连贯性/224-graphic-novel-panel-language.md) | 图像小说画格组合语言 | 漫画画格本身是语言：窄=幽闭、宽=开阔、方=平静、不规则=动作；锯齿分界=战斗爆发，画中画=主次并置 |
| [243-rehearsal-to-previs-workflow](08-分镜与连贯性/243-rehearsal-to-previs-workflow.md) | 排演九日志→AI预演工作流 | 吕美特两周排演流程映射为AI预演五阶段工作流，用走位、冻结剧本与情绪接力降低正片返工成本。 |
| [311-impact-frame-acceptance-checklist](08-分镜与连贯性/311-impact-frame-acceptance-checklist.md) | 冲击帧逐镜验收清单 | 冲击帧的交付前逐镜核对表——帧位/帧数/类型/色彩/配套四层/预算六项逐行勾选，不过关即返工 |
| [328-cypher-battle-filming](08-分镜与连贯性/328-cypher-battle-filming.md) | Cypher与Battle拍摄法——圈的空间几何、攻防剪辑与反应镜头投放 | Cypher圆圈的机位几何、Battle双方攻防的拍摄与剪辑规则、观众反应镜头配额，含《热烈》手持广角实战经验 |
| [329-mv-urban-choreography-filming](08-分镜与连贯性/329-mv-urban-choreography-filming.md) | 舞蹈MV与Urban编舞拍摄——一镜到底、Point Dance与多机排练工作流 | 预设编舞的拍摄法：摄影机即舞者（一镜到底走位法）、招牌动作捕捉、单机多遍/多机一遍方案与排练-预演工作流 |
| [332-anime-dance-storyboard-template](08-分镜与连贯性/332-anime-dance-storyboard-template.md) | 动漫短剧街舞场面整合——分镜模板、逐镜资产清单与三大戏用方案 | 街舞知识系列收官：把313-331整合为可直接生产的三套戏用方案（对决/变身/群舞）、12镜分镜模板与逐镜资产核对表 |
| [343-character-drift-lock-overview](08-分镜与连贯性/343-character-drift-lock-overview.md) | 大场面人物不漂移①——角色漂移六病因与"唯一正典参考"锁定体系 | 漂移本质是逐帧去噪误差累积；唯一正典参考实体＋短镜头＋降运动档＋首尾帧QC，可消除六七成跨镜漂移 |
| [344-wide-shot-crowd-identity](08-分镜与连贯性/344-wide-shot-crowd-identity.md) | 大场面人物不漂移②——远景/广角/人群中的身份锚定（脸小靠什么认出人） | 远景里脸没有像素可用，身份靠发色/服装/比例/标志物/站姿传达；把一致性预算从脸转移到轮廓层 |
| [345-motion-action-identity-stability](08-分镜与连贯性/345-motion-action-identity-stability.md) | 大场面人物不漂移③——高速动作中的身份稳定（减法提示/材质锚/时间超频/锚帧链） | 运动矢量越大身份溶解越快；显式锚定刚性材质、上稳下动、慢速生成后期提速、末帧接首帧的证据链、3-5次多pass合成 |
| [346-multi-character-anti-swap](08-分镜与连贯性/346-multi-character-anti-swap.md) | 大场面人物不漂移④——多人同框身份互换/融合的五因五修与空间泳道 | 模型把"红衣女蓝衣男"当一个属性袋，遮挡后属性重新分配→换装换脸；每人独立参考实体＋空间泳道＋回避遮挡，终极方案分开生成合成 |
| [467-lib-dialogue-100](08-分镜与连贯性/467-lib-dialogue-100.md) | 对话镜头技法库 | 对话镜头标准件：正反打/越肩/双人中景/轴线/权力角度/视线匹配，拍关系不拍脸。 |
| [468-lib-ensemble-100](08-分镜与连贯性/468-lib-ensemble-100.md) | 群像文戏站位调度技法库（60条） | 群像站位60条：三角/纵深/围坐/行列/散聚，站位是关系的物理化石。 |
| [469-lib-expand-100](08-分镜与连贯性/469-lib-expand-100.md) | 扩写能力库（60条） | 把一行剧本扩写成模型能拍的标准镜头60条：补物理事件不加形容词，已过WAN3筛选。 |

## 09-音频与配音（20）

| 文件 | 标题 | 简介 |
|---|---|---|
| [006-TTS配音与口型同步](09-音频与配音/006-TTS配音与口型同步.md) | AI 配音工具与口型同步流程 | TTS 配音选型、音色克隆、口型同步工具与音视频合成顺序 |
| [034-bgm-beat-sync](09-音频与配音/034-bgm-beat-sync.md) | BGM节拍对齐峰值 | BGM节拍对齐剪辑峰值：蓄势段低频堆积，峰值重拍炸响；节拍与硬切对齐张力翻倍 |
| [035-sfx-pre-delay](09-音频与配音/035-sfx-pre-delay.md) | 音效前置与延迟 | 音效前置（声音先于画面）制造预期揪心；音效延迟（画面先于声）制造重量感与回响 |
| [089-audio-tools-tension](09-音频与配音/089-audio-tools-tension.md) | 音频工具叠加张力（TTS+音效+BGM） | 音频占张力50%；TTS控语调+音效控冲击+BGM控情绪三层叠加；静默也是音 |
| [151-sound-image-relationship](09-音频与配音/151-sound-image-relationship.md) | 音画关系总论——叙事内/外与同步对位坐标系 | 每个声音先回答"你在故事世界里吗"；同步是平行叙事，对位是反差叙事，选错坐标全盘皆输 |
| [152-sfx-layering-design](09-音频与配音/152-sfx-layering-design.md) | 音效层次设计——三层结构与频段分工 | 一记好拳头=瞬态+主体+尾音三层叠；好混音=前景/中景/背景各占频段互不打架 |
| [153-audio-visual-counterpoint](09-音频与配音/153-audio-visual-counterpoint.md) | 音画对位——用声音说画面没说的话 | 画面演悲剧，音乐放圆舞曲——对位不是贴错音轨，是让观众同时看见两件事 |
| [154-music-emotional-arc](09-音频与配音/154-music-emotional-arc.md) | 配乐情绪曲线——riser、sting、drop与呼吸感 | 配乐不是一条平线而是过山车：铺垫-推进-riser-顶点-释放；顶点可以是爆炸也可以是真空 |
| [155-power-of-silence](09-音频与配音/155-power-of-silence.md) | 静默的力量——无声作为声音设计 | 电影里的静默全是人造的；抽掉声音不是偷懒，是把观众的注意力拧到最大档 |
| [156-foley-action-sfx](09-音频与配音/156-foley-action-sfx.md) | 拟音与动作音效——打架戏的三层拳头 | 没有一个拳头是真的拳头声；打击感=瞬态拍+闷击+脆响+sub低频的层叠工程学 |
| [157-sound-perspective-space](09-音频与配音/157-sound-perspective-space.md) | 声音透视——用听觉画出画外空间 | 近的声音响干亮，远的声音轻闷混——声音景深比镜头景深便宜一百倍，画框装不下的世界让声音去装 |
| [158-leitmotif-character-theme](09-音频与配音/158-leitmotif-character-theme.md) | 主题音与动机——让每个角色自带BGM | 一串音符绑定一个人；动机可以在剧集中变形、背叛、回归，比任何台词都诚实地记录角色的命运线 |
| [159-ai-audio-tools-chain](09-音频与配音/159-ai-audio-tools-chain.md) | AI配音音效工具链——从画面到音轨的全套生成管线 | 画面有了但没声音？ElevenLabs做SFX，Stable Audio做长环境，分开生成再混，别指望AI一键出片音轨 |
| [160-audio-visual-editing-rhythm](09-音频与配音/160-audio-visual-editing-rhythm.md) | 音画剪辑节奏——切点不是画面的事，是声音的事 | 好切点往往不在画面上，在重拍/台词换气/静默的真空里；声音领先画面半步，观众就觉得片子会呼吸 |
| [246-score-spotting-dual-theme](09-音频与配音/246-score-spotting-dual-theme.md) | 配乐配置会与双主题大纲 | 配乐为电影服务而非反之；双主题按数学曲线此消彼长；配置会逐格定切入点，差几格定成败 |
| [247-mix-layers-frequency-clash](09-音频与配音/247-mix-layers-frequency-clash.md) | 混音分层与频率冲突排查 | 混音导演不能缺席；对白先行音乐最后进；人声被盖不推音量，回源头衰减冲突乐器2-3dB |
| [269-creature-sound-layer](09-音频与配音/269-creature-sound-layer.md) | 动物声音层——呼吸/鼻息/爪步/毛皮摩擦的音画同步 | 动物存在感一半靠声音：呼吸对胸腹起伏帧、爪步对落足帧、毛皮摩擦对身体接触帧；只有叫声无体音＝配音感 |
| [304-impact-frame-sound-sync](09-音频与配音/304-impact-frame-sound-sync.md) | 冲击帧声画对位——"视觉音效"的同步法则 | 冲击帧与打击音效的帧级同步规则、音效抽空法、低频延续技巧，以及"先声后画/先画后声"的两种情绪选择 |
| [455-product-promo-sound-beat-sync](09-音频与配音/455-product-promo-sound-beat-sync.md) | 产品宣传片声音设计与节拍同步方法论 | 强节奏 BGM 片的完整卡点流程（节拍网格测定→鼓点分类→拍号编排→渲后回测）+ 声音设计方法（BGM 选型、16 类 SFX 词汇表、钉帧管理、音量分层） |
| [475-lib-sound-100](09-音频与配音/475-lib-sound-100.md) | 环境声层设计库 | 环境声层六大类别：所有声音翻译成可见物理行为与介质扰动，禁抽象音效词。 |

## 10-剪辑与合成（17）

| 文件 | 标题 | 简介 |
|---|---|---|
| [007-动漫转场与剪辑](10-剪辑与合成/007-动漫转场与剪辑.md) | 动漫风格转场与剪辑节奏 | 硬切/叠化/光效转场在动漫短剧中的适用场景与剪辑节奏控制 |
| [032-hard-cut-impact](10-剪辑与合成/032-hard-cut-impact.md) | 硬切节奏与爆发 | 硬切（无过渡直切）制造爆发冲击；慢切蓄到顶转极快硬切=张力峰值信号 |
| [033-silence-negative-space](10-剪辑与合成/033-silence-negative-space.md) | 留白与静默的张力 | 留白=画面静止+静默无声，把延迟推到极致；爆发前的静默是揪心顶点，忌滥用 |
| [036-flash-white-black](10-剪辑与合成/036-flash-white-black.md) | 闪白闪黑与瞬爆 | 闪白=能量爆发/惊愕，闪黑=剧变/死亡；峰值瞬间用闪代替切=瞬爆感，忌滥用 |
| [090-post-production-tension-flow](10-剪辑与合成/090-post-production-tension-flow.md) | 剪映/达芬奇 张力后期流程 | 后期是张力的总装线；剪辑控节奏+调色控氛围+混音控情绪；6:1:3 比例编镜 |
| [106-jump-cut](10-剪辑与合成/106-jump-cut.md) | 跳切（Jump Cut） | 同主体同框位硬切=时间跳=失序/混乱/精神崩；Godard《精疲力尽》标志 |
| [107-match-cut](10-剪辑与合成/107-match-cut.md) | 匹配剪辑（Match Cut） | 用形状/动作/视线匹配连两镜=隐藏剪=时空跃迁+主题连；2001望月棒经典 |
| [108-montage](10-剪辑与合成/108-montage.md) | 蒙太奇（Montage） | 镜头并置产生新义=1+1>2；库里肖夫效应=两镜相加生第三义 |
| [187-narrative-motion-qa-editing](10-剪辑与合成/187-narrative-motion-qa-editing.md) | 叙事运动与问答模式 | 剪辑=提问+设置预期；答案前置造悬念，一镜多问多答塞入最大信息量 |
| [188-action-editing-trio](10-剪辑与合成/188-action-editing-trio.md) | 动作剪辑三件套：动接动·出镜入镜·清空画面 | 切在动作中隐剪辑点、切在仍在画内处加速流动、空镜1~2秒平滑换轴 |
| [198-transition-toolbox-katz](10-剪辑与合成/198-transition-toolbox-katz.md) | 转场手法库 | 12种转场的实现手法与适用场合——连接场景用剪切／叠化，分隔场景用淡接 |
| [244-subliminal-flashcut-escalation](10-剪辑与合成/244-subliminal-flashcut-escalation.md) | 潜意识闪切递进法（2→4→8→16格） | 被压抑记忆用2格闪现侵入、按2→4→8→16格递进直至接管意识 |
| [245-juxtaposition-tempo-editing](10-剪辑与合成/245-juxtaposition-tempo-editing.md) | 并置与节奏：剪辑两要素（吕美特） | 剪辑=并置画面+创造节奏；素材决定上限，冲击靠对比蓄势而非快剪 |
| [303-chained-impact-frames](10-剪辑与合成/303-chained-impact-frames.md) | 连锁冲击帧——连击与爆炸序列的帧编排 | 多段打击/连环爆炸中冲击帧的交替编排法——负片对仗、节奏递增、末击升格三段模型 |
| [306-impact-frame-postproduction-pipeline](10-剪辑与合成/306-impact-frame-postproduction-pipeline.md) | 冲击帧后期合成工作流——静帧制作与帧级插入 | AI视频时代冲击帧的后期落地管线——接触帧定位、三类冲击帧静帧制作法、帧级插入与震动/顿帧的同步合成 |
| [330-dance-beat-editing](10-剪辑与合成/330-dance-beat-editing.md) | 舞蹈节拍剪辑——切点网格、动作匹配切与冲击帧的舞蹈用法 | 街舞剪辑专用规则：8拍切点网格、动作端点切法、pop/freeze与切点同帧、反拍意外切、速度斜坡与冲击帧配额 |
| [476-lib-transition-100](10-剪辑与合成/476-lib-transition-100.md) | 转场动作库（100条） | 转场动作100条：镜头内可见的运动/形状/色彩/构图对位，禁帧级微操与抽象词。 |

## 11-案例拆解（21）

| 文件 | 标题 | 简介 |
|---|---|---|
| [008-案例拆解模板](11-案例拆解/008-案例拆解模板.md) | 动漫短剧案例拆解模板 | 拆解一部动漫短剧的标准字段与流程，从镜头/动作/音频逐层分析 |
| [037-iaido-kill-fullflow](11-案例拆解/037-iaido-kill-fullflow.md) | 居合斩杀全流程拆解 | 居合斩杀是张力工艺集大成者，从待机到收刀全流程串联前29条技法 |
| [038-confrontation-dialogue-tension](11-案例拆解/038-confrontation-dialogue-tension.md) | 对峙对白张力构建 | 对峙对白靠视线正反打+停顿+信息差构建张力，言语只是表层，沉默才是刀 |
| [039-chase-escape-tension](11-案例拆解/039-chase-escape-tension.md) | 追逐逃亡张力曲线 | 追逐张力靠距离反复拉近拉远+信息差（观众知追兵位置），比单向往近更折磨 |
| [041-weapon-fight-tension](11-案例拆解/041-weapon-fight-tension.md) | 冷兵器对战张力（剑/双刀/枪） | 冷兵器对战张力靠步法可读+节奏化交锋+一击几何线；鬼灭式"长镜读站姿呼吸，爆发快切 |
| [042-hand-to-hand-tension](11-案例拆解/042-hand-to-hand-tension.md) | 徒手格斗张力构建 | 徒手格斗张力靠重量感+近身缠斗呼吸+一击定格；比兵器更吃接触瞬间的凝固 |
| [043-superpower-magic-tension](11-案例拆解/043-superpower-magic-tension.md) | 超能力/魔法对轰张力 | 超能力对轰张力靠蓄能延迟+能量可视化+对冲僵持；忌特效堆满，留静默瞬间 |
| [044-horror-tension-ma](11-案例拆解/044-horror-tension-ma.md) | 恐怖张力：Jump Scare vs Slow Burn 与"间 | 恐怖两路：jump scare 瞬时惊吓 vs slow burn 持续不安；日式"间(Ma)"用负空间逼观众扫阴影 |
| [045-mystery-suspense-tension](11-案例拆解/045-mystery-suspense-tension.md) | 悬疑推理张力构建 | 悬疑张力靠信息滴漏+视角限制+误导反转；观众比角色多知一点=最强揪心 |
| [046-tragedy-farewell-tension](11-案例拆解/046-tragedy-farewell-tension.md) | 悲剧决别张力构建 | 悲剧决别用长释放曲线+凝固瞬间+静默余韵；峰值不爆而是凝固，让观众心沉 |
| [047-comedy-rhythm-break](11-案例拆解/047-comedy-rhythm-break.md) | 喜剧反差张力（节奏破坏造笑点） | 喜剧用张力反差造笑：把严肃蓄势引到顶，用节奏破坏/期待违背释放成笑点 |
| [048-countdown-timer-tension](11-案例拆解/048-countdown-timer-tension.md) | 倒计时/限时张力 | 倒计时张力靠不可逆时间+阶梯加速+数字/钟声逼近；时间轴的极致运用 |
| [049-siege-surround-tension](11-案例拆解/049-siege-surround-tension.md) | 围困/包围张力 | 围困张力靠逼仄空间+包围闭合+无路可逃；空间轴压缩到极致，出路逐个被封 |
| [050-one-vs-many-tension](11-案例拆解/050-one-vs-many-tension.md) | 单挑群战张力 | 一对多群战靠错峰进攻+分层动+逐个击破节奏；忌全员齐上糊一团 |
| [051-twist-reversal-tension](11-案例拆解/051-twist-reversal-tension.md) | 反转剧张力构建 | 反转张力靠铺垫让"以为的真相"成立，再推翻；反转瞬间用静默+特写+重新理解定格 |
| [052-silent-standoff-tension](11-案例拆解/052-silent-standoff-tension.md) | 静默对峙（无对白纯动作张力） | 无对白对峙靠视线+微动作+负空间+静默声音构建张力；台词越少张力越强 |
| [053-betrayal-reveal-tension](11-案例拆解/053-betrayal-reveal-tension.md) | 背叛揭露瞬间张力 | 背叛揭露用信任铺垫+背刺瞬间凝固+受害者反应特写；最揪心在"还以为并肩"被破 |
| [054-death-moment-tension](11-案例拆解/054-death-moment-tension.md) | 死亡瞬间张力处理 | 死亡瞬间用凝固+静默+不可逆确认；不爆而沉，让"不可挽回"被凝视 |
| [055-transformation-rampage-tension](11-案例拆解/055-transformation-rampage-tension.md) | 觉醒/暴走变身张力 | 变身张力靠压抑到极限+能量破体+失控边缘；前段越被压，爆发越揪心 |
| [310-impact-frame-case-library](11-案例拆解/310-impact-frame-case-library.md) | 冲击帧经典案例拆解坐标 | 六部作品的冲击帧名场面坐标与拆解要点——金田系起源帧、EVA情绪帧、龙珠战斗闪、一拳认真拳、咒术黑闪、鬼灭插画帧 |
| [312-whitehair-redhair-fight-breakdown](11-案例拆解/312-whitehair-redhair-fight-breakdown.md) | 82秒白发紫电vs红发红炎打戏逐帧拆解 | 82秒AI原创打戏短片全片连帧拉片——五幕攻防逆转结构、六个"只看单帧看不出"的连读要点、三条可直接抄的技法 |

## 12-规范与踩坑（10）

| 文件 | 标题 | 简介 |
|---|---|---|
| [009-常见生成失败与修复](12-规范与踩坑/009-常见生成失败与修复.md) | AI 视频生成常见失败与修复 | 融指/变脸/背景融化/闪烁等常见生成失败的成因与修复手段 |
| [010-项目文件命名规范](12-规范与踩坑/010-项目文件命名规范.md) | AI 视频项目文件命名与目录规范 | 项目根目录结构、镜号命名、版本号与资产分类的统一规范 |
| [248-dailies-qa-four-rules](12-规范与踩坑/248-dailies-qa-four-rules.md) | 看样片四规则与走神测试 | 吕美特看样片四规则与走神测试，迁移为AI生成镜头的验收标准与缺陷补救顺序。 |
| [249-wall-by-wall-batch-economy](12-规范与踩坑/249-wall-by-wall-batch-economy.md) | 按墙拍摄与批次生成经济学 | 吕美特按墙拍摄的布光经济学，迁移为AI同场景同角度的批次生成与通告单式任务管理。 |
| [266-creature-contact-grounding](12-规范与踩坑/266-creature-contact-grounding.md) | 动物接触面翻车与修法——漂浮/穿模/无影/无挤压四病 | AI视频动物四大翻车：漂浮/穿模/无影子/无挤压形变；修法是显式声明接触点＋物理结果，说结果不说过程 |
| [301-impact-frame-devaluation-budget](12-规范与踩坑/301-impact-frame-devaluation-budget.md) | 冲击帧贬值律——单集预算与滥用阈值 | 冲击帧的稀缺性原则——单场/单集/全剧的用量预算，滥用的三种症状，以及"删到心疼才对"的规划法；补充整画面级节拍冲击限额（全片≤3处、相邻≥16拍、卡拍管时机不管幅度） |
| [307-impact-frame-photoreal-boundary](12-规范与踩坑/307-impact-frame-photoreal-boundary.md) | 真人写实风的冲击帧边界——本剧应用口径 | 冲击帧在真人写实风番剧中的适配边界——可用类型、改造方案、禁用类型，以及与真气显形四级制的对齐 |
| [309-impact-frame-forbidden-scenes](12-规范与踩坑/309-impact-frame-forbidden-scenes.md) | 冲击帧禁用清单——什么时候绝对不能闪 | 冲击帧的反面教材——五类绝对禁用场景、三类谨慎使用场景，以及误用后的修复方案 |
| [449-platform-compliance-redlines](12-规范与踩坑/449-platform-compliance-redlines.md) | 平台审核红线与规避写法（AI短剧与网文合规清单） | 交付前的合规准入线——八类平台红线、十类高危题材的虚构化改写手法、上线前逐项勾选清单 |
| [451-subtitle-legibility-font-height](12-规范与踩坑/451-subtitle-legibility-font-height.md) | 字幕与画面文字的有效字高——可读性硬指标 | 画面文字只有"纹理"和"要读"两态——要读的文字有最低有效字高（1080p：对白字幕≥56px/≥5%帧高，辅助≥32px/≥3%），按最终像素量验收不按提示词字号；读不到的文字宁可删掉 |

## 13-技能与流程（8）

| 文件 | 标题 | 简介 |
|---|---|---|
| [377-ability-bible-template](13-技能与流程/377-ability-bible-template.md) | 技能魔法编写二十连⑳——全剧能力圣经：规则正典文档结构与变更治理 | 观众被告知为真的规则必须持续为真，除非故事明确演化；能力圣经=世界规则+能力卡+术语表+战力标尺+时间表+视觉资产索引；改动走登记-影响评估-版本号 |
| [452-product-promo-overview](13-技能与流程/452-product-promo-overview.md) | 产品宣传片制作总纲（支线入口） | 产品宣传片领域支线入口——与动漫短剧不同的制作范式（代码逐帧绘制 vs AI 生成），124 镜头卡 10 分类索引，核心方法论导航 |
| [454-product-promo-pipeline-aesthetics](13-技能与流程/454-product-promo-pipeline-aesthetics.md) | 产品宣传片制作流水线与判例式审美准则 | 八阶段制作流水线（方向性问题不进昂贵阶段）+ 判例式审美准则（R节奏/Q质感运镜构图/S声音/C文案/P流程） |
| [Skill_单集制作本生成_episode-production-book](13-技能与流程/Skill_单集制作本生成_episode-production-book.md) | Skill：单集制作本生成 episode-production-book | 番剧每集制作6步中的第1-4步流程Skill——精读压缩→分镜表→段提示词→首尾帧，沉淀自《天龙八部》S1E1 Wan/H3双版实践 |
| [Skill_资产包生成_asset-pack](13-技能与流程/Skill_资产包生成_asset-pack.md) | Skill：资产包生成 asset-pack | 四件套第2、3件的生成流程Skill——分镜中每个具名元素都有出图依据，角色/场景/道具提示词开箱即贴、跨镜跨集不漂移 |
| [Skill_逐镜资产核对_episode-shot-asset-audit](13-技能与流程/Skill_逐镜资产核对_episode-shot-asset-audit.md) | Skill：逐镜资产核对 episode-shot-asset-audit | 制作本生成前必跑的审计Skill——逐镜核对场景/角色（含状态）/道具有无出图资产，产出可勾选逐镜资产清单，缺口当场回填；正负提示词必须同块 |
| [番剧制作四件套交付规范](13-技能与流程/番剧制作四件套交付规范.md) | 番剧制作四件套交付规范 | 番剧制作铁律集——四件套（制作本/角色资产/场景道具资产/逐镜清单）同批交付，含平台选定、能力探测与本地资产库、完整vs压缩模式、交付前逐镜自检等创作启动铁律 |
| [逐镜资产清单模板](13-技能与流程/逐镜资产清单模板.md) | 逐镜资产清单模板（Shot × Assets） | 逐镜资产调用清单空白模板——逐镜标注场景｜角色（含伤妆等状态）｜道具（带seed）｜备注，生成前逐行勾选 |

## 14-技法词库（16）

| 文件 | 主题 | 技法条数 | 适用范围 |
|---|---|---|---|
| [lib_camera_100.md](14-技法词库/lib_camera_100.md) | 镜头语言技法库（168 条） | 168 | 动漫 AI 视频创作的运镜/景别/构图/剪辑参考。每条附可直接粘贴进视频生成提示词的英文短语。 |
| [lib_classfight_100.md](14-技法词库/lib_classfight_100.md) | 职业对战编排库（libclassfight100） | 55 |  |
| [lib_closeup_100.md](14-技法词库/lib_closeup_100.md) | 特写镜头技法库 · 166 条 | 166 |  |
| [lib_comedy_100.md](14-技法词库/lib_comedy_100.md) | 喜剧节奏基础库 libcomedy100 | 60 |  |
| [lib_dailylife_100.md](14-技法词库/lib_dailylife_100.md) | 日常生活动作描写库（libdailylife100） | 60 |  |
| [lib_dialogue_100.md](14-技法词库/lib_dialogue_100.md) | 对话镜头技法库 · 对话镜头基础（第1章 6 条） | 60 | 把"两人说话"这种最容易写虚的文戏，翻译成模型能拍、观众能看懂、剪辑能接的标准对话镜头。 |
| [lib_emotion_100.md](14-技法词库/lib_emotion_100.md) | 情感戏分镜动作库（libemotion100） | 60 |  |
| [lib_ensemble_100.md](14-技法词库/lib_ensemble_100.md) | 群像文戏站位调度技法库 · 全 10 章 60 条（G01–G60） | 60 | 把"一群人站着/坐着说话"这种最容易拍成合影或新闻发布会的文戏，翻译成模型能拍、观众能一眼读懂权力与关系的空间调度。 |
| [lib_expand_100.md](14-技法词库/lib_expand_100.md) | 扩写能力库（60 条）——把一行剧本翻译成标准可拍镜头 | 65 | 剧本只写"她拔刀，他后退半步"，生成时必须扩成模型能拍、观众能看懂、后期能接的镜头。 |
| [lib_fight_100.md](14-技法词库/lib_fight_100.md) | 传奇打戏拆解库 · 动漫史 100+ 场经典战斗的可复用技法 | 186 | 为 AI 视频分镜提示词提供可直接调用的"打戏技法弹药"。 |
| [lib_scene_100.md](14-技法词库/lib_scene_100.md) | 场景镜头库 libscene100 | 60 |  |
| [lib_sound_100.md](14-技法词库/lib_sound_100.md) | libsound100 — 环境声层设计知识条目库 | 60 |  |
| [lib_spell_100.md](14-技法词库/lib_spell_100.md) | 法术/技能特效描写库（129 式） | 124 |  |
| [lib_suspense_100.md](14-技法词库/lib_suspense_100.md) | 悬念构建基础库（第1章） | 0 |  |
| [lib_transition_100.md](14-技法词库/lib_transition_100.md) | 转场动作库 100 条（第 1 章） | 60 |  |
| [lib_vfxshot_100.md](14-技法词库/lib_vfxshot_100.md) | 特效镜头拍法库（141 条） | 141 | 动漫 AI 视频创作的特效作画/拍法参考。与《镜头语言技法库》互补——那库管"机位怎么动"，本库管"画面里的特效怎么画"。 |
