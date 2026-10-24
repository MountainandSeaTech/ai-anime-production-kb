# ai-anime-production-kb

面向 AI 智能体的**影视化生产知识库** —— 从提示词工程到剪辑合成的全流程实战沉淀，共 **14 大类 483 条目 + 16 个技法库（约 1400 条技法）**。

## 简介

本库为 AI 智能体提供可直接调用的「影视化生产知识」，覆盖从创意到成片的完整链路。不止用于动漫：同一套方法论同样适用于**写实短片、真人感分镜、广告级画面、剧情视频**。

无论是二次元演出，还是接近真人的镜头语言，本库给出的都是可复用的判断标准与参数级写法。内容基于 Wan、可灵等主流视频生成模型实测沉淀，涵盖提示词写法、角色一致性方案、张力构建、镜头语言、动作戏编排（含冲击帧/居合等专项拆解）、分镜连贯性、音频配音、剪辑合成规范与踩坑记录。

条目以编号 + 主题命名，按目录分类组织，便于智能体检索、引用与组合调用。智能体调用请先读 [INDEX.md](INDEX.md)（机器可读入口：分类清单 + 技法库目录 + 调用约定）。

## 作品预览

本库知识在实际成片中的效果，可参考以下作品：

- [终于把镜头的流畅感解决了](https://www.bilibili.com/video/BV1iWpd6CEmv/) —— 镜头衔接与流畅感处理
- [钟灵儿](https://www.bilibili.com/video/BV1xwJy6JEu8/) —— 角色表演与张力呈现

## 目录结构

共 **14 大类 483 条目 + 16 个技法库（约 1400 条技法）**。每个条目是独立的 Markdown 文件，按编号 + 主题命名，便于智能体定向检索、按需加载。

| 目录 | 覆盖内容 | 条目数 |
|---|---|---|
| **01-工具与模型** | 视频生成模型特性、工具编排、Skill 工程 | 17 |
| **02-提示词技巧** | 提示词结构、写法模式、参数控制 | 59 |
| **03-角色与表演** | 角色一致性、微表情、眼部表演、情绪库 | 71 |
| **04-张力与节奏** | 张力构建引擎、节奏曲线、动效参数 | 36 |
| **05-镜头与构图** | 景别、机位、运镜、构图语言 | 52 |
| **06-作画与光影** | 作画风格、光影设计、色彩控制 | 47 |
| **07-动作与战斗** | 打斗编排、冲击帧、居合、武器战 | 94 |
| **08-分镜与连贯性** | 分镜语法、镜头衔接、对话连贯性 | 31 |
| **09-音频与配音** | 音效设计、配音表演、音乐情绪 | 20 |
| **10-剪辑与合成** | 剪辑节奏、转场、合成规范 | 17 |
| **11-案例拆解** | 经典镜头逐帧拆解、张力案例库 | 21 |
| **12-规范与踩坑** | 制作规范、常见崩坏与规避 | 10 |
| **13-技能与流程** | 工作流、管线设计、资产表规范 | 8 |
| **14-技法词库** | 16 个 100+ 技法库：镜头/特写/打斗/群战/法术/特效/转场/声音/情绪/对话/喜剧/日常/场景/悬念 | 16 |

### 条目明细

<details>
<summary><b>01-工具与模型</b>（17 条） — 视频生成模型特性、工具编排、Skill 工程</summary>

- [001-runway-gen3](01-工具与模型/001-runway-gen3.md)
- [002-kling-ai](01-工具与模型/002-kling-ai.md)
- [084-runway-gen3-tension-shot](01-工具与模型/084-runway-gen3-tension-shot.md)
- [085-kling-tension-shot](01-工具与模型/085-kling-tension-shot.md)
- [086-jimeng-action-tension](01-工具与模型/086-jimeng-action-tension.md)
- [171-skill-anatomy](01-工具与模型/171-skill-anatomy.md)
- [172-skill-description-triggers](01-工具与模型/172-skill-description-triggers.md)
- [173-skill-body-instructions](01-工具与模型/173-skill-body-instructions.md)
- [174-skill-examples-antipatterns](01-工具与模型/174-skill-examples-antipatterns.md)
- [175-tool-orchestration](01-工具与模型/175-tool-orchestration.md)
- [176-knowledge-pipeline-skill](01-工具与模型/176-knowledge-pipeline-skill.md)
- [177-process-skill](01-工具与模型/177-process-skill.md)
- [178-skill-testing](01-工具与模型/178-skill-testing.md)
- [179-skill-maintenance](01-工具与模型/179-skill-maintenance.md)
- [180-skill-system-design](01-工具与模型/180-skill-system-design.md)
- [181-capability-map](01-工具与模型/181-capability-map.md)
- [447-wan3-calibration-baseline](01-工具与模型/447-wan3-calibration-baseline.md)

</details>

<details>
<summary><b>02-提示词技巧</b>（59 条） — 提示词结构、写法模式、参数控制</summary>

- [003-镜头运动提示词](02-提示词技巧/003-镜头运动提示词.md)
- [040-tension-prompt-templates](02-提示词技巧/040-tension-prompt-templates.md)
- [087-midjourney-tension-storyboard](02-提示词技巧/087-midjourney-tension-storyboard.md)
- [111-prompt-formula-structure](02-提示词技巧/111-prompt-formula-structure.md)
- [112-negative-prompt](02-提示词技巧/112-negative-prompt.md)
- [113-style-reference-lock](02-提示词技巧/113-style-reference-lock.md)
- [114-parameters-tuning](02-提示词技巧/114-parameters-tuning.md)
- [115-camera-vocabulary](02-提示词技巧/115-camera-vocabulary.md)
- [116-lighting-vocabulary](02-提示词技巧/116-lighting-vocabulary.md)
- [117-action-vocabulary](02-提示词技巧/117-action-vocabulary.md)
- [118-mood-atmosphere-vocabulary](02-提示词技巧/118-mood-atmosphere-vocabulary.md)
- [119-reference-image-tecunique](02-提示词技巧/119-reference-image-tecunique.md)
- [120-prompt-debugging-tips](02-提示词技巧/120-prompt-debugging-tips.md)
- [141-h3-camera-command-syntax](02-提示词技巧/141-h3-camera-command-syntax.md)
- [142-h3-prompt-structure](02-提示词技巧/142-h3-prompt-structure.md)
- [143-wan3-prompt-formula](02-提示词技巧/143-wan3-prompt-formula.md)
- [144-wan-first-last-frame](02-提示词技巧/144-wan-first-last-frame.md)
- [145-h3-vs-wan-selection](02-提示词技巧/145-h3-vs-wan-selection.md)
- [146-universal-prompt-principles](02-提示词技巧/146-universal-prompt-principles.md)
- [147-h3-command-combo-rhythm](02-提示词技巧/147-h3-command-combo-rhythm.md)
- [148-wan-multishot-prompt](02-提示词技巧/148-wan-multishot-prompt.md)
- [149-h3-wan-troubleshooting](02-提示词技巧/149-h3-wan-troubleshooting.md)
- [150-h3-wan-hybrid-workflow](02-提示词技巧/150-h3-wan-hybrid-workflow.md)
- [265-ai-creature-consistency](02-提示词技巧/265-ai-creature-consistency.md)
- [276-dragon-palms-vfx-styles](02-提示词技巧/276-dragon-palms-vfx-styles.md)
- [281-invisible-qi-blade](02-提示词技巧/281-invisible-qi-blade.md)
- [290-zhenqi-huaxing-levels](02-提示词技巧/290-zhenqi-huaxing-levels.md)
- [305-ai-video-impact-frame-prompts](02-提示词技巧/305-ai-video-impact-frame-prompts.md)
- [348-vfx-believability-overview](02-提示词技巧/348-vfx-believability-overview.md)
- [349-fire-explosion-vfx](02-提示词技巧/349-fire-explosion-vfx.md)
- [350-water-fluid-vfx](02-提示词技巧/350-water-fluid-vfx.md)
- [351-lightning-energy-beam-vfx](02-提示词技巧/351-lightning-energy-beam-vfx.md)
- [352-wind-smoke-dust-gas-vfx](02-提示词技巧/352-wind-smoke-dust-gas-vfx.md)
- [353-ice-earth-rbd-destruction](02-提示词技巧/353-ice-earth-rbd-destruction.md)
- [354-light-energy-volumetric-vfx](02-提示词技巧/354-light-energy-volumetric-vfx.md)
- [355-effect-character-interaction](02-提示词技巧/355-effect-character-interaction.md)
- [356-post-compositing-pipeline](02-提示词技巧/356-post-compositing-pipeline.md)
- [374-skill-visual-prompt-pipeline](02-提示词技巧/374-skill-visual-prompt-pipeline.md)
- [378-skill-magic-vfx-overview](02-提示词技巧/378-skill-magic-vfx-overview.md)
- [379-fire-explosion-vfx-prompts](02-提示词技巧/379-fire-explosion-vfx-prompts.md)
- [380-lightning-vfx-prompts](02-提示词技巧/380-lightning-vfx-prompts.md)
- [381-ice-frost-vfx-prompts](02-提示词技巧/381-ice-frost-vfx-prompts.md)
- [382-water-liquid-vfx-prompts](02-提示词技巧/382-water-liquid-vfx-prompts.md)
- [383-wind-air-vfx-prompts](02-提示词技巧/383-wind-air-vfx-prompts.md)
- [384-earth-rock-vfx-prompts](02-提示词技巧/384-earth-rock-vfx-prompts.md)
- [385-light-holy-beam-vfx-prompts](02-提示词技巧/385-light-holy-beam-vfx-prompts.md)
- [386-shadow-dark-mist-curse-vfx-prompts](02-提示词技巧/386-shadow-dark-mist-curse-vfx-prompts.md)
- [387-healing-life-magic-vfx-prompts](02-提示词技巧/387-healing-life-magic-vfx-prompts.md)
- [388-portal-space-magic-vfx-prompts](02-提示词技巧/388-portal-space-magic-vfx-prompts.md)
- [389-time-magic-vfx-prompts](02-提示词技巧/389-time-magic-vfx-prompts.md)
- [390-shield-barrier-ward-vfx-prompts](02-提示词技巧/390-shield-barrier-ward-vfx-prompts.md)
- [391-transformation-awakening-vfx-prompts](02-提示词技巧/391-transformation-awakening-vfx-prompts.md)
- [392-summoning-circle-rune-magic-vfx-prompts](02-提示词技巧/392-summoning-circle-rune-magic-vfx-prompts.md)
- [393-sword-energy-weapon-enchant-vfx-prompts](02-提示词技巧/393-sword-energy-weapon-enchant-vfx-prompts.md)
- [394-particle-system-concepts-ai-alternative](02-提示词技巧/394-particle-system-concepts-ai-alternative.md)
- [395-vfx-compositing-post-pipeline](02-提示词技巧/395-vfx-compositing-post-pipeline.md)
- [396-prompt-template-engineering](02-提示词技巧/396-prompt-template-engineering.md)
- [397-vfx-asset-library-and-bible](02-提示词技巧/397-vfx-asset-library-and-bible.md)
- [448-seedance25-30-commands](02-提示词技巧/448-seedance25-30-commands.md)

</details>

<details>
<summary><b>03-角色与表演</b>（71 条） — 角色一致性、微表情、眼部表演、情绪库</summary>

- [004-角色一致性方案](03-角色与表演/004-角色一致性方案.md)
- [024-microexpression-breathing](03-角色与表演/024-microexpression-breathing.md)
- [070-villain-design-oppression](03-角色与表演/070-villain-design-oppression.md)
- [071-underdog-protagonist-tension](03-角色与表演/071-underdog-protagonist-tension.md)
- [072-supporting-reaction-amplifier](03-角色与表演/072-supporting-reaction-amplifier.md)
- [073-size-difference-tension](03-角色与表演/073-size-difference-tension.md)
- [074-costume-prop-tension-signals](03-角色与表演/074-costume-prop-tension-signals.md)
- [075-expression-design-tension](03-角色与表演/075-expression-design-tension.md)
- [088-character-consistency-tension](03-角色与表演/088-character-consistency-tension.md)
- [161-facs-action-units](03-角色与表演/161-facs-action-units.md)
- [162-micro-expressions](03-角色与表演/162-micro-expressions.md)
- [163-eye-acting](03-角色与表演/163-eye-acting.md)
- [164-complex-expression-recipes](03-角色与表演/164-complex-expression-recipes.md)
- [165-ai-microexpression-prompts](03-角色与表演/165-ai-microexpression-prompts.md)
- [166-body-micro-movements](03-角色与表演/166-body-micro-movements.md)
- [167-breathing-performance](03-角色与表演/167-breathing-performance.md)
- [168-hand-acting](03-角色与表演/168-hand-acting.md)
- [169-posture-presence](03-角色与表演/169-posture-presence.md)
- [170-restrained-acting](03-角色与表演/170-restrained-acting.md)
- [200-production-design-artwork](03-角色与表演/200-production-design-artwork.md)
- [201-chubbuck-technique-overview](03-角色与表演/201-chubbuck-technique-overview.md)
- [202-objective-system-overall-scene](03-角色与表演/202-objective-system-overall-scene.md)
- [203-obstacles-tension](03-角色与表演/203-obstacles-tension.md)
- [204-substitution](03-角色与表演/204-substitution.md)
- [205-inner-objects](03-角色与表演/205-inner-objects.md)
- [206-beats-and-actions](03-角色与表演/206-beats-and-actions.md)
- [207-moment-before](03-角色与表演/207-moment-before.md)
- [208-place-fourth-wall](03-角色与表演/208-place-fourth-wall.md)
- [209-doings-prop-action](03-角色与表演/209-doings-prop-action.md)
- [210-inner-monologue](03-角色与表演/210-inner-monologue.md)
- [211-previous-circumstances](03-角色与表演/211-previous-circumstances.md)
- [212-let-it-go](03-角色与表演/212-let-it-go.md)
- [213-organic-fear-death-trauma](03-角色与表演/213-organic-fear-death-trauma.md)
- [214-substance-sex-killer](03-角色与表演/214-substance-sex-killer.md)
- [215-pregnancy-parenthood-occupation](03-角色与表演/215-pregnancy-parenthood-occupation.md)
- [233-silhouette-signature-anchor](03-角色与表演/233-silhouette-signature-anchor.md)
- [250-living-creature-interaction-overview](03-角色与表演/250-living-creature-interaction-overview.md)
- [251-carry-hold-biomechanics](03-角色与表演/251-carry-hold-biomechanics.md)
- [252-lead-rein-tension](03-角色与表演/252-lead-rein-tension.md)
- [253-riding-centaur-rhythm](03-角色与表演/253-riding-centaur-rhythm.md)
- [254-creature-idle-micro-library](03-角色与表演/254-creature-idle-micro-library.md)
- [255-creature-emotion-five-states](03-角色与表演/255-creature-emotion-five-states.md)
- [256-call-response-creature-dialogue](03-角色与表演/256-call-response-creature-dialogue.md)
- [257-petting-stroke-pairing](03-角色与表演/257-petting-stroke-pairing.md)
- [263-human-creature-eyeline](03-角色与表演/263-human-creature-eyeline.md)
- [264-realistic-anthropomorphism-limit](03-角色与表演/264-realistic-anthropomorphism-limit.md)
- [268-creature-as-supporting-actor](03-角色与表演/268-creature-as-supporting-actor.md)
- [364-power-personality-binding](03-角色与表演/364-power-personality-binding.md)
- [407-eye-movement-taxonomy](03-角色与表演/407-eye-movement-taxonomy.md)
- [408-gaze-trajectory-patterns](03-角色与表演/408-gaze-trajectory-patterns.md)
- [409-eyelid-acting](03-角色与表演/409-eyelid-acting.md)
- [410-tears-moisture-layer](03-角色与表演/410-tears-moisture-layer.md)
- [411-focus-defocus-gaze](03-角色与表演/411-focus-defocus-gaze.md)
- [412-pupil-physiology-performance](03-角色与表演/412-pupil-physiology-performance.md)
- [413-brow-eyelid-coordination](03-角色与表演/413-brow-eyelid-coordination.md)
- [414-abnormal-inhuman-eyes](03-角色与表演/414-abnormal-inhuman-eyes.md)
- [415-eye-ecu-shot-design](03-角色与表演/415-eye-ecu-shot-design.md)
- [416-anime-eye-symbol-system](03-角色与表演/416-anime-eye-symbol-system.md)
- [417-eye-micro-prompt-library](03-角色与表演/417-eye-micro-prompt-library.md)
- [418-eye-artifact-prevention](03-角色与表演/418-eye-artifact-prevention.md)
- [419-shot-size-eye-readability](03-角色与表演/419-shot-size-eye-readability.md)
- [420-seven-emotions-eye-recipes](03-角色与表演/420-seven-emotions-eye-recipes.md)
- [421-dialogue-eye-rhythm](03-角色与表演/421-dialogue-eye-rhythm.md)
- [422-combat-eye-focus](03-角色与表演/422-combat-eye-focus.md)
- [423-deadpan-psycho-eye-restraint](03-角色与表演/423-deadpan-psycho-eye-restraint.md)
- [424-moe-big-eye-micro-motion](03-角色与表演/424-moe-big-eye-micro-motion.md)
- [425-eye-micro-motion-frame-budget](03-角色与表演/425-eye-micro-motion-frame-budget.md)
- [426-eye-acting-breakdown-method](03-角色与表演/426-eye-acting-breakdown-method.md)
- [463-imbalance-exhaustion-poses](03-角色与表演/463-imbalance-exhaustion-poses.md)
- [472-lib-emotion-100](03-角色与表演/472-lib-emotion-100.md)
- [473-lib-dailylife-100](03-角色与表演/473-lib-dailylife-100.md)

</details>

<details>
<summary><b>04-张力与节奏</b>（36 条） — 张力构建引擎、节奏曲线、动效参数</summary>

- [011-tension-definition](04-张力与节奏/011-tension-definition.md)
- [012-static-vs-dynamic-tension](04-张力与节奏/012-static-vs-dynamic-tension.md)
- [013-tension-three-axes](04-张力与节奏/013-tension-three-axes.md)
- [014-tension-curve](04-张力与节奏/014-tension-curve.md)
- [015-tension-and-pacing](04-张力与节奏/015-tension-and-pacing.md)
- [021-slow-motion-tension](04-张力与节奏/021-slow-motion-tension.md)
- [023-cut-frequency-tension](04-张力与节奏/023-cut-frequency-tension.md)
- [029-pause-stillness](04-张力与节奏/029-pause-stillness.md)
- [076-opening-hook-tension](04-张力与节奏/076-opening-hook-tension.md)
- [077-info-drip-pacing](04-张力与节奏/077-info-drip-pacing.md)
- [078-foreshadow-callback](04-张力与节奏/078-foreshadow-callback.md)
- [079-expectation-violation](04-张力与节奏/079-expectation-violation.md)
- [080-segment-tension-curve](04-张力与节奏/080-segment-tension-curve.md)
- [081-pov-switch-tension](04-张力与节奏/081-pov-switch-tension.md)
- [082-timeline-dislocation](04-张力与节奏/082-timeline-dislocation.md)
- [083-ending-lingering-tension](04-张力与节奏/083-ending-lingering-tension.md)
- [239-theme-first-decision-filter](04-张力与节奏/239-theme-first-decision-filter.md)
- [259-creature-reacts-first](04-张力与节奏/259-creature-reacts-first.md)
- [261-tug-of-war-comedy-beats](04-张力与节奏/261-tug-of-war-comedy-beats.md)
- [296-impact-frame-timing](04-张力与节奏/296-impact-frame-timing.md)
- [333-story-structure-systems](04-张力与节奏/333-story-structure-systems.md)
- [334-scene-writing-expansion](04-张力与节奏/334-scene-writing-expansion.md)
- [335-character-building-want-need-flaw](04-张力与节奏/335-character-building-want-need-flaw.md)
- [336-dialogue-subtext-craft](04-张力与节奏/336-dialogue-subtext-craft.md)
- [337-conflict-stakes-tension](04-张力与节奏/337-conflict-stakes-tension.md)
- [338-worldbuilding-exposition-drip](04-张力与节奏/338-worldbuilding-exposition-drip.md)
- [339-battle-epic-writing-clarity](04-张力与节奏/339-battle-epic-writing-clarity.md)
- [340-sensory-cinematic-detail](04-张力与节奏/340-sensory-cinematic-detail.md)
- [341-outline-to-draft-expansion-workflow](04-张力与节奏/341-outline-to-draft-expansion-workflow.md)
- [342-revision-passes-kill-darlings](04-张力与节奏/342-revision-passes-kill-darlings.md)
- [347-character-not-drowned-narrative](04-张力与节奏/347-character-not-drowned-narrative.md)
- [357-vfx-narrative-restraint](04-张力与节奏/357-vfx-narrative-restraint.md)
- [372-magic-dialogue-jargon](04-张力与节奏/372-magic-dialogue-jargon.md)
- [453-product-promo-motion-parameters](04-张力与节奏/453-product-promo-motion-parameters.md)
- [470-lib-comedy-100](04-张力与节奏/470-lib-comedy-100.md)
- [471-lib-suspense-100](04-张力与节奏/471-lib-suspense-100.md)

</details>

<details>
<summary><b>05-镜头与构图</b>（52 条） — 景别、机位、运镜、构图语言</summary>

- [016-shot-scale-tension](05-镜头与构图/016-shot-scale-tension.md)
- [017-camera-angle-power](05-镜头与构图/017-camera-angle-power.md)
- [018-camera-movement-tension](05-镜头与构图/018-camera-movement-tension.md)
- [019-depth-of-field-focus](05-镜头与构图/019-depth-of-field-focus.md)
- [020-composition-tension](05-镜头与构图/020-composition-tension.md)
- [022-long-take-tension](05-镜头与构图/022-long-take-tension.md)
- [091-frame-within-frame](05-镜头与构图/091-frame-within-frame.md)
- [092-symmetry-one-point-perspective](05-镜头与构图/092-symmetry-one-point-perspective.md)
- [093-deep-focus-composition](05-镜头与构图/093-deep-focus-composition.md)
- [094-rule-of-thirds-negative-space](05-镜头与构图/094-rule-of-thirds-negative-space.md)
- [095-leading-lines-composition](05-镜头与构图/095-leading-lines-composition.md)
- [096-long-take-oner](05-镜头与构图/096-long-take-oner.md)
- [097-slow-push-pull](05-镜头与构图/097-slow-push-pull.md)
- [098-dolly-zoom-vertigo](05-镜头与构图/098-dolly-zoom-vertigo.md)
- [099-tracking-steadicam-shot](05-镜头与构图/099-tracking-steadicam-shot.md)
- [100-orbit-arc-shot](05-镜头与构图/100-orbit-arc-shot.md)
- [101-low-angle-shot](05-镜头与构图/101-low-angle-shot.md)
- [102-high-angle-birds-eye](05-镜头与构图/102-high-angle-birds-eye.md)
- [103-pov-subjective-shot](05-镜头与构图/103-pov-subjective-shot.md)
- [104-break-180-degree-rule](05-镜头与构图/104-break-180-degree-rule.md)
- [105-macro-close-up](05-镜头与构图/105-macro-close-up.md)
- [109-shadow-noir-composition](05-镜头与构图/109-shadow-noir-composition.md)
- [110-mirror-reflection-shot](05-镜头与构图/110-mirror-reflection-shot.md)
- [184-aspect-ratio-narrative](05-镜头与构图/184-aspect-ratio-narrative.md)
- [192-dramatic-action-range-depth](05-镜头与构图/192-dramatic-action-range-depth.md)
- [193-open-closed-composition](05-镜头与构图/193-open-closed-composition.md)
- [194-pov-identification](05-镜头与构图/194-pov-identification.md)
- [195-pan-six-uses](05-镜头与构图/195-pan-six-uses.md)
- [196-crane-shot-design](05-镜头与构图/196-crane-shot-design.md)
- [216-frame-playground-pressure-release](05-镜头与构图/216-frame-playground-pressure-release.md)
- [217-tension-lines-rubber-band](05-镜头与构图/217-tension-lines-rubber-band.md)
- [218-turning-point-momentum-shift](05-镜头与构图/218-turning-point-momentum-shift.md)
- [219-silhouette-guide-method](05-镜头与构图/219-silhouette-guide-method.md)
- [220-shape-language-composition](05-镜头与构图/220-shape-language-composition.md)
- [221-aspect-ratio-conversion-methods](05-镜头与构图/221-aspect-ratio-conversion-methods.md)
- [222-unconventional-composition](05-镜头与构图/222-unconventional-composition.md)
- [223-split-screen-halves-quarters](05-镜头与构图/223-split-screen-halves-quarters.md)
- [240-focal-length-psychology](05-镜头与构图/240-focal-length-psychology.md)
- [241-lens-plot-progression](05-镜头与构图/241-lens-plot-progression.md)
- [262-multi-creature-staging-depth](05-镜头与构图/262-multi-creature-staging-depth.md)
- [267-human-creature-framing](05-镜头与构图/267-human-creature-framing.md)
- [277-heavy-palm-cinematography](05-镜头与构图/277-heavy-palm-cinematography.md)
- [300-camera-shake-stacking](05-镜头与构图/300-camera-shake-stacking.md)
- [326-dance-cinematography-overview](05-镜头与构图/326-dance-cinematography-overview.md)
- [327-breaking-cinematography](05-镜头与构图/327-breaking-cinematography.md)
- [404-director-style-prompts-vol1-part1](05-镜头与构图/404-director-style-prompts-vol1-part1.md)
- [405-director-style-prompts-vol1-part2](05-镜头与构图/405-director-style-prompts-vol1-part2.md)
- [461-escape-pursuit-camera-language](05-镜头与构图/461-escape-pursuit-camera-language.md)
- [462-grip-resolve-closeups](05-镜头与构图/462-grip-resolve-closeups.md)
- [474-lib-scene-100](05-镜头与构图/474-lib-scene-100.md)
- [478-lib-camera-100](05-镜头与构图/478-lib-camera-100.md)
- [479-lib-closeup-100](05-镜头与构图/479-lib-closeup-100.md)

</details>

<details>
<summary><b>06-作画与光影</b>（47 条） — 作画风格、光影设计、色彩控制</summary>

- [056-limited-animation-tension](06-作画与光影/056-limited-animation-tension.md)
- [057-afterimage-tension](06-作画与光影/057-afterimage-tension.md)
- [058-speed-lines-tension](06-作画与光影/058-speed-lines-tension.md)
- [059-impact-frame](06-作画与光影/059-impact-frame.md)
- [060-deformation-tension](06-作画与光影/060-deformation-tension.md)
- [061-shadow-separation-tension](06-作画与光影/061-shadow-separation-tension.md)
- [062-line-weight-tension](06-作画与光影/062-line-weight-tension.md)
- [063-color-block-impact](06-作画与光影/063-color-block-impact.md)
- [064-high-contrast-lighting](06-作画与光影/064-high-contrast-lighting.md)
- [065-monochrome-two-color](06-作画与光影/065-monochrome-two-color.md)
- [066-shadow-gradient-approach](06-作画与光影/066-shadow-gradient-approach.md)
- [067-color-temperature-shift](06-作画与光影/067-color-temperature-shift.md)
- [068-backlight-silhouette](06-作画与光影/068-backlight-silhouette.md)
- [069-black-and-white-tension](06-作画与光影/069-black-and-white-tension.md)
- [225-line-direction-volume](06-作画与光影/225-line-direction-volume.md)
- [226-three-tone-zone-workflow](06-作画与光影/226-three-tone-zone-workflow.md)
- [227-four-value-zones-material](06-作画与光影/227-four-value-zones-material.md)
- [228-no-outline-value-blocking](06-作画与光影/228-no-outline-value-blocking.md)
- [229-weather-as-narrative](06-作画与光影/229-weather-as-narrative.md)
- [230-grayscale-value-buildup](06-作画与光影/230-grayscale-value-buildup.md)
- [231-depth-separation-atmospheric](06-作画与光影/231-depth-separation-atmospheric.md)
- [232-focus-and-detail-economy](06-作画与光影/232-focus-and-detail-economy.md)
- [242-color-plot-palette-first](06-作画与光影/242-color-plot-palette-first.md)
- [302-impact-frame-color-design](06-作画与光影/302-impact-frame-color-design.md)
- [331-dance-imaging-lighting](06-作画与光影/331-dance-imaging-lighting.md)
- [406-scene-alive-ambient-motion](06-作画与光影/406-scene-alive-ambient-motion.md)
- [427-fabric-material-dynamics](06-作画与光影/427-fabric-material-dynamics.md)
- [428-wind-on-clothing-model](06-作画与光影/428-wind-on-clothing-model.md)
- [429-action-fabric-tugging](06-作画与光影/429-action-fabric-tugging.md)
- [430-fitted-vs-loose-clothing](06-作画与光影/430-fitted-vs-loose-clothing.md)
- [431-skirts-and-special-structures](06-作画与光影/431-skirts-and-special-structures.md)
- [432-wet-fabric-and-moisture](06-作画与光影/432-wet-fabric-and-moisture.md)
- [433-tattered-cloth-and-rags](06-作画与光影/433-tattered-cloth-and-rags.md)
- [434-metal-armor-and-rigid-structures](06-作画与光影/434-metal-armor-and-rigid-structures.md)
- [435-layered-clothing-dynamics](06-作画与光影/435-layered-clothing-dynamics.md)
- [436-temperature-and-fabric-dynamics](06-作画与光影/436-temperature-and-fabric-dynamics.md)
- [437-cloth-motion-prompts-ai](06-作画与光影/437-cloth-motion-prompts-ai.md)
- [438-cloth-artifact-fixes-ai-video](06-作画与光影/438-cloth-artifact-fixes-ai-video.md)
- [439-cloth-frame-timing](06-作画与光影/439-cloth-frame-timing.md)
- [440-cloth-as-emotion-signal](06-作画与光影/440-cloth-as-emotion-signal.md)
- [441-cloth-battle-rhythm](06-作画与光影/441-cloth-battle-rhythm.md)
- [442-skirt-dynamics-walk-run](06-作画与光影/442-skirt-dynamics-walk-run.md)
- [443-cape-cloak-dynamics](06-作画与光影/443-cape-cloak-dynamics.md)
- [444-hair-physics-follow-through](06-作画与光影/444-hair-physics-follow-through.md)
- [445-accessories-small-objects-physics](06-作画与光影/445-accessories-small-objects-physics.md)
- [446-cloth-physics-breakdown-methodology](06-作画与光影/446-cloth-physics-breakdown-methodology.md)
- [464-lib-vfxshot-100](06-作画与光影/464-lib-vfxshot-100.md)

</details>

<details>
<summary><b>07-动作与战斗</b>（94 条） — 打斗编排、冲击帧、居合、武器战</summary>

- [025-ready-stance-tension](07-动作与战斗/025-ready-stance-tension.md)
- [026-action-windup](07-动作与战斗/026-action-windup.md)
- [027-gaze-line-crossing](07-动作与战斗/027-gaze-line-crossing.md)
- [028-footwork-distance](07-动作与战斗/028-footwork-distance.md)
- [030-hand-details](07-动作与战斗/030-hand-details.md)
- [031-ensemble-individual-action](07-动作与战斗/031-ensemble-individual-action.md)
- [121-battle-three-act-structure](07-动作与战斗/121-battle-three-act-structure.md)
- [122-duel-vs-group-battle](07-动作与战斗/122-duel-vs-group-battle.md)
- [123-weapon-style-rhythm](07-动作与战斗/123-weapon-style-rhythm.md)
- [124-momentum-shift](07-动作与战斗/124-momentum-shift.md)
- [125-boss-battle-stages](07-动作与战斗/125-boss-battle-stages.md)
- [126-fight-pacing-cut-frequency](07-动作与战斗/126-fight-pacing-cut-frequency.md)
- [127-fight-keyframe-selection](07-动作与战斗/127-fight-keyframe-selection.md)
- [128-weapon-clash-physics](07-动作与战斗/128-weapon-clash-physics.md)
- [129-fight-camera-movement](07-动作与战斗/129-fight-camera-movement.md)
- [130-fight-camera-angle](07-动作与战斗/130-fight-camera-angle.md)
- [182-action-scene-three-rules](07-动作与战斗/182-action-scene-three-rules.md)
- [183-weapon-persistence](07-动作与战斗/183-weapon-persistence.md)
- [234-action-four-phase-template](07-动作与战斗/234-action-four-phase-template.md)
- [235-unarmed-power-chain](07-动作与战斗/235-unarmed-power-chain.md)
- [236-weapon-action-discipline](07-动作与战斗/236-weapon-action-discipline.md)
- [237-female-combat-body-language](07-动作与战斗/237-female-combat-body-language.md)
- [238-action-camera-matrix](07-动作与战斗/238-action-camera-matrix.md)
- [258-escape-struggle-in-arms](07-动作与战斗/258-escape-struggle-in-arms.md)
- [260-large-animal-weight-inertia](07-动作与战斗/260-large-animal-weight-inertia.md)
- [270-dragon-palms-overview-yijing](07-动作与战斗/270-dragon-palms-overview-yijing.md)
- [271-dragon-palms-moves-1-6](07-动作与战斗/271-dragon-palms-moves-1-6.md)
- [272-dragon-palms-moves-7-12](07-动作与战斗/272-dragon-palms-moves-7-12.md)
- [273-dragon-palms-moves-13-18](07-动作与战斗/273-dragon-palms-moves-13-18.md)
- [274-kanglong-youhui-mechanics](07-动作与战斗/274-kanglong-youhui-mechanics.md)
- [275-dragon-palms-user-variants](07-动作与战斗/275-dragon-palms-user-variants.md)
- [278-dragon-palms-fight-choreography](07-动作与战斗/278-dragon-palms-fight-choreography.md)
- [279-yijing-move-design-method](07-动作与战斗/279-yijing-move-design-method.md)
- [280-six-meridian-sword](07-动作与战斗/280-six-meridian-sword.md)
- [282-lingbo-weibu-steps](07-动作与战斗/282-lingbo-weibu-steps.md)
- [283-dog-beating-staff-eight](07-动作与战斗/283-dog-beating-staff-eight.md)
- [284-douzhuan-xingyi-rebound](07-动作与战斗/284-douzhuan-xingyi-rebound.md)
- [285-beiming-absorb-three-systems](07-动作与战斗/285-beiming-absorb-three-systems.md)
- [286-tianshan-plum-sixyang](07-动作与战斗/286-tianshan-plum-sixyang.md)
- [287-shengsi-fu-ice-talisman](07-动作与战斗/287-shengsi-fu-ice-talisman.md)
- [288-huoyan-dao-jiumozhi](07-动作与战斗/288-huoyan-dao-jiumozhi.md)
- [289-qinlong-konghe-telekinesis](07-动作与战斗/289-qinlong-konghe-telekinesis.md)
- [291-skill-tension-four-principles](07-动作与战斗/291-skill-tension-four-principles.md)
- [292-impact-frame-overview](07-动作与战斗/292-impact-frame-overview.md)
- [293-impact-frame-history-kanada](07-动作与战斗/293-impact-frame-history-kanada.md)
- [294-black-white-flash-grammar](07-动作与战斗/294-black-white-flash-grammar.md)
- [295-impact-frame-five-types](07-动作与战斗/295-impact-frame-five-types.md)
- [297-hitstop-vs-impact-frame](07-动作与战斗/297-hitstop-vs-impact-frame.md)
- [298-hitstop-frame-budget](07-动作与战斗/298-hitstop-frame-budget.md)
- [299-smear-vs-impact-frame](07-动作与战斗/299-smear-vs-impact-frame.md)
- [308-impact-four-layer-combo](07-动作与战斗/308-impact-four-layer-combo.md)
- [313-street-dance-overview](07-动作与战斗/313-street-dance-overview.md)
- [314-breaking-toprock](07-动作与战斗/314-breaking-toprock.md)
- [315-breaking-footwork](07-动作与战斗/315-breaking-footwork.md)
- [316-breaking-freezes](07-动作与战斗/316-breaking-freezes.md)
- [317-breaking-powermoves-basic](07-动作与战斗/317-breaking-powermoves-basic.md)
- [318-breaking-powermoves-advanced](07-动作与战斗/318-breaking-powermoves-advanced.md)
- [319-popping-hit-wave-isolation](07-动作与战斗/319-popping-hit-wave-isolation.md)
- [320-popping-tutting-robot-glide](07-动作与战斗/320-popping-tutting-robot-glide.md)
- [321-locking-foundations](07-动作与战斗/321-locking-foundations.md)
- [322-hiphop-party-steps](07-动作与战斗/322-hiphop-party-steps.md)
- [323-house-dance-steps](07-动作与战斗/323-house-dance-steps.md)
- [324-krump](07-动作与战斗/324-krump.md)
- [325-waacking-voguing](07-动作与战斗/325-waacking-voguing.md)
- [358-skill-magic-writing-overview](07-动作与战斗/358-skill-magic-writing-overview.md)
- [359-hard-soft-magic-sanderson-laws](07-动作与战斗/359-hard-soft-magic-sanderson-laws.md)
- [360-skill-naming-craft](07-动作与战斗/360-skill-naming-craft.md)
- [361-mechanic-five-elements](07-动作与战斗/361-mechanic-five-elements.md)
- [362-power-cost-system](07-动作与战斗/362-power-cost-system.md)
- [363-power-scaling-ceiling](07-动作与战斗/363-power-scaling-ceiling.md)
- [365-power-debut-ritual](07-动作与战斗/365-power-debut-ritual.md)
- [366-writing-skills-in-combat](07-动作与战斗/366-writing-skills-in-combat.md)
- [367-combo-team-skills](07-动作与战斗/367-combo-team-skills.md)
- [368-counter-and-underdog](07-动作与战斗/368-counter-and-underdog.md)
- [369-power-loss-suppression](07-动作与战斗/369-power-loss-suppression.md)
- [370-powerup-awakening-transformation](07-动作与战斗/370-powerup-awakening-transformation.md)
- [371-original-skill-design](07-动作与战斗/371-original-skill-design.md)
- [373-team-ability-composition](07-动作与战斗/373-team-ability-composition.md)
- [375-modern-psychic-abilities](07-动作与战斗/375-modern-psychic-abilities.md)
- [376-summon-tame-companion](07-动作与战斗/376-summon-tame-companion.md)
- [398-fight-storyboard-50-index](07-动作与战斗/398-fight-storyboard-50-index.md)
- [399-fight-template-melee-burst](07-动作与战斗/399-fight-template-melee-burst.md)
- [400-fight-template-weapon-clash](07-动作与战斗/400-fight-template-weapon-clash.md)
- [401-fight-template-elemental-spell](07-动作与战斗/401-fight-template-elemental-spell.md)
- [402-fight-template-speed-blink](07-动作与战斗/402-fight-template-speed-blink.md)
- [403-fight-template-finisher](07-动作与战斗/403-fight-template-finisher.md)
- [456-collapse-destruction-vfx](07-动作与战斗/456-collapse-destruction-vfx.md)
- [457-hunt-pursuit-choreography](07-动作与战斗/457-hunt-pursuit-choreography.md)
- [458-fire-serpent-spell-anatomy](07-动作与战斗/458-fire-serpent-spell-anatomy.md)
- [459-chain-spell-anatomy](07-动作与战斗/459-chain-spell-anatomy.md)
- [460-terrain-collapse-spell-anatomy](07-动作与战斗/460-terrain-collapse-spell-anatomy.md)
- [465-lib-spell-100](07-动作与战斗/465-lib-spell-100.md)
- [466-lib-classfight-100](07-动作与战斗/466-lib-classfight-100.md)
- [477-lib-fight-100](07-动作与战斗/477-lib-fight-100.md)

</details>

<details>
<summary><b>08-分镜与连贯性</b>（31 条） — 分镜语法、镜头衔接、对话连贯性</summary>

- [005-分镜表标准字段](08-分镜与连贯性/005-分镜表标准字段.md)
- [131-axis-180-rule](08-分镜与连贯性/131-axis-180-rule.md)
- [132-match-on-action](08-分镜与连贯性/132-match-on-action.md)
- [133-eyeline-match](08-分镜与连贯性/133-eyeline-match.md)
- [134-match-cut](08-分镜与连贯性/134-match-cut.md)
- [135-causal-transition](08-分镜与连贯性/135-causal-transition.md)
- [136-visual-flow-line](08-分镜与连贯性/136-visual-flow-line.md)
- [137-j-cut-l-cut](08-分镜与连贯性/137-j-cut-l-cut.md)
- [138-ai-multishot-continuity](08-分镜与连贯性/138-ai-multishot-continuity.md)
- [139-time-ellipsis](08-分镜与连贯性/139-time-ellipsis.md)
- [140-continuity-checklist](08-分镜与连贯性/140-continuity-checklist.md)
- [185-shot-purpose-audit](08-分镜与连贯性/185-shot-purpose-audit.md)
- [186-triangle-system-axis](08-分镜与连贯性/186-triangle-system-axis.md)
- [189-dialogue-two-person-staging](08-分镜与连贯性/189-dialogue-two-person-staging.md)
- [190-dialogue-multi-person-staging](08-分镜与连贯性/190-dialogue-multi-person-staging.md)
- [191-shot-flow-scene-intro](08-分镜与连贯性/191-shot-flow-scene-intro.md)
- [197-dolly-staging-camera-path](08-分镜与连贯性/197-dolly-staging-camera-path.md)
- [199-storyboard-drawing-conventions](08-分镜与连贯性/199-storyboard-drawing-conventions.md)
- [224-graphic-novel-panel-language](08-分镜与连贯性/224-graphic-novel-panel-language.md)
- [243-rehearsal-to-previs-workflow](08-分镜与连贯性/243-rehearsal-to-previs-workflow.md)
- [311-impact-frame-acceptance-checklist](08-分镜与连贯性/311-impact-frame-acceptance-checklist.md)
- [328-cypher-battle-filming](08-分镜与连贯性/328-cypher-battle-filming.md)
- [329-mv-urban-choreography-filming](08-分镜与连贯性/329-mv-urban-choreography-filming.md)
- [332-anime-dance-storyboard-template](08-分镜与连贯性/332-anime-dance-storyboard-template.md)
- [343-character-drift-lock-overview](08-分镜与连贯性/343-character-drift-lock-overview.md)
- [344-wide-shot-crowd-identity](08-分镜与连贯性/344-wide-shot-crowd-identity.md)
- [345-motion-action-identity-stability](08-分镜与连贯性/345-motion-action-identity-stability.md)
- [346-multi-character-anti-swap](08-分镜与连贯性/346-multi-character-anti-swap.md)
- [467-lib-dialogue-100](08-分镜与连贯性/467-lib-dialogue-100.md)
- [468-lib-ensemble-100](08-分镜与连贯性/468-lib-ensemble-100.md)
- [469-lib-expand-100](08-分镜与连贯性/469-lib-expand-100.md)

</details>

<details>
<summary><b>09-音频与配音</b>（20 条） — 音效设计、配音表演、音乐情绪</summary>

- [006-TTS配音与口型同步](09-音频与配音/006-TTS配音与口型同步.md)
- [034-bgm-beat-sync](09-音频与配音/034-bgm-beat-sync.md)
- [035-sfx-pre-delay](09-音频与配音/035-sfx-pre-delay.md)
- [089-audio-tools-tension](09-音频与配音/089-audio-tools-tension.md)
- [151-sound-image-relationship](09-音频与配音/151-sound-image-relationship.md)
- [152-sfx-layering-design](09-音频与配音/152-sfx-layering-design.md)
- [153-audio-visual-counterpoint](09-音频与配音/153-audio-visual-counterpoint.md)
- [154-music-emotional-arc](09-音频与配音/154-music-emotional-arc.md)
- [155-power-of-silence](09-音频与配音/155-power-of-silence.md)
- [156-foley-action-sfx](09-音频与配音/156-foley-action-sfx.md)
- [157-sound-perspective-space](09-音频与配音/157-sound-perspective-space.md)
- [158-leitmotif-character-theme](09-音频与配音/158-leitmotif-character-theme.md)
- [159-ai-audio-tools-chain](09-音频与配音/159-ai-audio-tools-chain.md)
- [160-audio-visual-editing-rhythm](09-音频与配音/160-audio-visual-editing-rhythm.md)
- [246-score-spotting-dual-theme](09-音频与配音/246-score-spotting-dual-theme.md)
- [247-mix-layers-frequency-clash](09-音频与配音/247-mix-layers-frequency-clash.md)
- [269-creature-sound-layer](09-音频与配音/269-creature-sound-layer.md)
- [304-impact-frame-sound-sync](09-音频与配音/304-impact-frame-sound-sync.md)
- [455-product-promo-sound-beat-sync](09-音频与配音/455-product-promo-sound-beat-sync.md)
- [475-lib-sound-100](09-音频与配音/475-lib-sound-100.md)

</details>

<details>
<summary><b>10-剪辑与合成</b>（17 条） — 剪辑节奏、转场、合成规范</summary>

- [007-动漫转场与剪辑](10-剪辑与合成/007-动漫转场与剪辑.md)
- [032-hard-cut-impact](10-剪辑与合成/032-hard-cut-impact.md)
- [033-silence-negative-space](10-剪辑与合成/033-silence-negative-space.md)
- [036-flash-white-black](10-剪辑与合成/036-flash-white-black.md)
- [090-post-production-tension-flow](10-剪辑与合成/090-post-production-tension-flow.md)
- [106-jump-cut](10-剪辑与合成/106-jump-cut.md)
- [107-match-cut](10-剪辑与合成/107-match-cut.md)
- [108-montage](10-剪辑与合成/108-montage.md)
- [187-narrative-motion-qa-editing](10-剪辑与合成/187-narrative-motion-qa-editing.md)
- [188-action-editing-trio](10-剪辑与合成/188-action-editing-trio.md)
- [198-transition-toolbox-katz](10-剪辑与合成/198-transition-toolbox-katz.md)
- [244-subliminal-flashcut-escalation](10-剪辑与合成/244-subliminal-flashcut-escalation.md)
- [245-juxtaposition-tempo-editing](10-剪辑与合成/245-juxtaposition-tempo-editing.md)
- [303-chained-impact-frames](10-剪辑与合成/303-chained-impact-frames.md)
- [306-impact-frame-postproduction-pipeline](10-剪辑与合成/306-impact-frame-postproduction-pipeline.md)
- [330-dance-beat-editing](10-剪辑与合成/330-dance-beat-editing.md)
- [476-lib-transition-100](10-剪辑与合成/476-lib-transition-100.md)

</details>

<details>
<summary><b>11-案例拆解</b>（21 条） — 经典镜头逐帧拆解、张力案例库</summary>

- [008-案例拆解模板](11-案例拆解/008-案例拆解模板.md)
- [037-iaido-kill-fullflow](11-案例拆解/037-iaido-kill-fullflow.md)
- [038-confrontation-dialogue-tension](11-案例拆解/038-confrontation-dialogue-tension.md)
- [039-chase-escape-tension](11-案例拆解/039-chase-escape-tension.md)
- [041-weapon-fight-tension](11-案例拆解/041-weapon-fight-tension.md)
- [042-hand-to-hand-tension](11-案例拆解/042-hand-to-hand-tension.md)
- [043-superpower-magic-tension](11-案例拆解/043-superpower-magic-tension.md)
- [044-horror-tension-ma](11-案例拆解/044-horror-tension-ma.md)
- [045-mystery-suspense-tension](11-案例拆解/045-mystery-suspense-tension.md)
- [046-tragedy-farewell-tension](11-案例拆解/046-tragedy-farewell-tension.md)
- [047-comedy-rhythm-break](11-案例拆解/047-comedy-rhythm-break.md)
- [048-countdown-timer-tension](11-案例拆解/048-countdown-timer-tension.md)
- [049-siege-surround-tension](11-案例拆解/049-siege-surround-tension.md)
- [050-one-vs-many-tension](11-案例拆解/050-one-vs-many-tension.md)
- [051-twist-reversal-tension](11-案例拆解/051-twist-reversal-tension.md)
- [052-silent-standoff-tension](11-案例拆解/052-silent-standoff-tension.md)
- [053-betrayal-reveal-tension](11-案例拆解/053-betrayal-reveal-tension.md)
- [054-death-moment-tension](11-案例拆解/054-death-moment-tension.md)
- [055-transformation-rampage-tension](11-案例拆解/055-transformation-rampage-tension.md)
- [310-impact-frame-case-library](11-案例拆解/310-impact-frame-case-library.md)
- [312-whitehair-redhair-fight-breakdown](11-案例拆解/312-whitehair-redhair-fight-breakdown.md)

</details>

<details>
<summary><b>12-规范与踩坑</b>（10 条） — 制作规范、常见崩坏与规避</summary>

- [009-常见生成失败与修复](12-规范与踩坑/009-常见生成失败与修复.md)
- [010-项目文件命名规范](12-规范与踩坑/010-项目文件命名规范.md)
- [248-dailies-qa-four-rules](12-规范与踩坑/248-dailies-qa-four-rules.md)
- [249-wall-by-wall-batch-economy](12-规范与踩坑/249-wall-by-wall-batch-economy.md)
- [266-creature-contact-grounding](12-规范与踩坑/266-creature-contact-grounding.md)
- [301-impact-frame-devaluation-budget](12-规范与踩坑/301-impact-frame-devaluation-budget.md)
- [307-impact-frame-photoreal-boundary](12-规范与踩坑/307-impact-frame-photoreal-boundary.md)
- [309-impact-frame-forbidden-scenes](12-规范与踩坑/309-impact-frame-forbidden-scenes.md)
- [449-platform-compliance-redlines](12-规范与踩坑/449-platform-compliance-redlines.md)
- [451-subtitle-legibility-font-height](12-规范与踩坑/451-subtitle-legibility-font-height.md)

</details>

<details>
<summary><b>13-技能与流程</b>（8 条） — 工作流、管线设计、资产表规范</summary>

- [377-ability-bible-template](13-技能与流程/377-ability-bible-template.md)
- [452-product-promo-overview](13-技能与流程/452-product-promo-overview.md)
- [454-product-promo-pipeline-aesthetics](13-技能与流程/454-product-promo-pipeline-aesthetics.md)
- [Skill_单集制作本生成_episode-production-book](13-技能与流程/Skill_单集制作本生成_episode-production-book.md)
- [Skill_资产包生成_asset-pack](13-技能与流程/Skill_资产包生成_asset-pack.md)
- [Skill_逐镜资产核对_episode-shot-asset-audit](13-技能与流程/Skill_逐镜资产核对_episode-shot-asset-audit.md)
- [番剧制作四件套交付规范](13-技能与流程/番剧制作四件套交付规范.md)
- [逐镜资产清单模板](13-技能与流程/逐镜资产清单模板.md)

</details>

<details>
<summary><b>14-技法词库</b>（16 个库，约 1400 条技法） — 每条附可直接粘贴的英文提示词短语</summary>

- [lib_camera_100](14-技法词库/lib_camera_100.md)
- [lib_classfight_100](14-技法词库/lib_classfight_100.md)
- [lib_closeup_100](14-技法词库/lib_closeup_100.md)
- [lib_comedy_100](14-技法词库/lib_comedy_100.md)
- [lib_dailylife_100](14-技法词库/lib_dailylife_100.md)
- [lib_dialogue_100](14-技法词库/lib_dialogue_100.md)
- [lib_emotion_100](14-技法词库/lib_emotion_100.md)
- [lib_ensemble_100](14-技法词库/lib_ensemble_100.md)
- [lib_expand_100](14-技法词库/lib_expand_100.md)
- [lib_fight_100](14-技法词库/lib_fight_100.md)
- [lib_scene_100](14-技法词库/lib_scene_100.md)
- [lib_sound_100](14-技法词库/lib_sound_100.md)
- [lib_spell_100](14-技法词库/lib_spell_100.md)
- [lib_suspense_100](14-技法词库/lib_suspense_100.md)
- [lib_transition_100](14-技法词库/lib_transition_100.md)
- [lib_vfxshot_100](14-技法词库/lib_vfxshot_100.md)

</details>

## 交流与反馈

使用上有任何问题，欢迎加 QQ 群：**1131851799**

## 开源协议

[CC BY 4.0](LICENSE) —— 可自由使用、修改、分发（含商用），需署名原作者。

## 支持这个项目

如果这个知识库帮你省下了试错时间，欢迎请我喝杯咖啡。所有打赏用于服务器与模型调用开销，以及知识库的持续更新。

<table>
  <tr>
    <td align="center"><img src="assets/sponsor/wechat-pay.jpg" width="260" alt="微信支付"></td>
    <td align="center"><img src="assets/sponsor/alipay.jpg" width="260" alt="支付宝"></td>
  </tr>
  <tr>
    <td align="center"><b>微信支付</b></td>
    <td align="center"><b>支付宝</b></td>
  </tr>
</table>

