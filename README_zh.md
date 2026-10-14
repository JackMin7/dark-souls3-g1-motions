# 黑暗之魂 III 动作集：Unitree G1

[English](README.md) | **简体中文**

将《黑暗之魂 III》的 33 个主角收集类姿态重定向到 Unitree G1（29 关节）。数据包含手臂对齐、收尾姿态、地面高度修正，以及 13 个下蹲、坐下、跪地和躺卧动作的贴地支撑优化。


## 动作对比

**左侧：G1 机器人；右侧：原游戏角色。** 动图自动循环，按原速同步播放（源数据 30 FPS，动图 15 FPS）。机器人显示大小做了适配。画面为动画渲染，不是实机录像；不包含武器、杯子或布料物理。

全部 33 个动图直接显示在下方，无需点击展开。

### 01 Beckon

![01 Beckon](media/comparisons/01_Beckon.gif)


### 02 Praise the Sun

![02 Praise the Sun](media/comparisons/02_Praise_the_Sun.gif)


### 03 Point Up

![03 Point Up](media/comparisons/03_Point_Up.gif)


### 04 Point Down

![04 Point Down](media/comparisons/04_Point_Down.gif)


### 05 Duel Bow

![05 Duel Bow](media/comparisons/05_Duel_Bow.gif)


### 06 Point Forward

![06 Point Forward](media/comparisons/06_Point_Forward.gif)


### 07 Welcome

![07 Welcome](media/comparisons/07_Welcome.gif)


### 08 Prostration

![08 Prostration](media/comparisons/08_Prostration.gif)


### 09 Proper Bow

![09 Proper Bow](media/comparisons/09_Proper_Bow.gif)


### 10 Prayer

![10 Prayer](media/comparisons/10_Prayer.gif)


### 11 Bow

![11 Bow](media/comparisons/11_Bow.gif)


### 12 Wave

![12 Wave](media/comparisons/12_Wave.gif)


### 13 Hurrah

![13 Hurrah](media/comparisons/13_Hurrah.gif)


### 14 Jump for Joy

![14 Jump for Joy](media/comparisons/14_Jump_for_Joy.gif)


### 15 Joy

![15 Joy](media/comparisons/15_Joy.gif)


### 16 My Thanks

![16 My Thanks](media/comparisons/16_My_Thanks.gif)


### 17 Rejoice

![17 Rejoice](media/comparisons/17_Rejoice.gif)


### 18 Rest

![18 Rest](media/comparisons/18_Rest.gif)


### 19 By My Sword

![19 By My Sword](media/comparisons/19_By_My_Sword.gif)


### 20 Dignified Bow

![20 Dignified Bow](media/comparisons/20_Dignified_Bow.gif)


### 21 Curl Up

![21 Curl Up](media/comparisons/21_Curl_Up.gif)


### 22 Stretch Out

![22 Stretch Out](media/comparisons/22_Stretch_Out.gif)


### 23 Call Over

![23 Call Over](media/comparisons/23_Call_Over.gif)


### 24 Collapse

![24 Collapse](media/comparisons/24_Collapse.gif)


### 25 Quiet Resolve

![25 Quiet Resolve](media/comparisons/25_Quiet_Resolve.gif)


### 26 Patches Squat

![26 Patches Squat](media/comparisons/26_Patches_Squat.gif)


### 27 Applause

![27 Applause](media/comparisons/27_Applause.gif)


### 28 Path of the Dragon

![28 Path of the Dragon](media/comparisons/28_Path_of_the_Dragon.gif)


### 29 Legion Etiquette

![29 Legion Etiquette](media/comparisons/29_Legion_Etiquette.gif)


### 30 Darkmoon Loyalty

![30 Darkmoon Loyalty](media/comparisons/30_Darkmoon_Loyalty.gif)


### 31 Sleep

![31 Sleep](media/comparisons/31_Sleep.gif)


### 32 Toast

![32 Toast](media/comparisons/32_Toast.gif)


### 33 Silent Ally

![33 Silent Ally](media/comparisons/33_Silent_Ally.gif)


## 数据与使用

- `data/g1/`：33 个无表头 CSV，每行 36 列，30 FPS。
- `manifest.json`：列顺序、帧数、时长与 SHA-256 校验值。
- [格式说明](docs/FORMAT.md) · [动作清单](docs/MOTIONS.md) · [贴地检查报告](reports/contact_report.md)。
- `media/comparisons/`：全部 33 个原游戏角色与 G1 的对比动图。
- `media/`：另外三个仅含机器人的贴地优化前后对比动图。
- `tools/validate_dataset.py`：只使用 Python 标准库的完整性与基础数值检查工具。

```sh
python3 tools/validate_dataset.py
```

每行依次为根位置 XYZ（米）、根四元数 XYZW、29 个关节角（弧度），世界坐标 Z 轴向上。请先阅读 [FORMAT](docs/FORMAT.md) 中的准确关节顺序，再用兼容的 G1 查看器播放。包内不含播放器和机器人模型；其他机器人需要重新重定向。数据不是 BVH/LAFAN1 骨架格式，不能直接发送到实机。

## 验证与已知限制

已有记录覆盖全部 33 个文件的 float32 地面及帧间/首尾接缝检查；13 个贴地优化动作额外进行了连续自碰撞与关节限位检查。检查针对当时模型，不能保证任意模型或实机安全。附带的检查工具仅验证完整性和基础数值，不重新执行几何认证。

贴地优化联合调整根高度、腿部及必要的手臂关节，相对前一处理阶段保留根水平位置、根朝向与腰部关节。部分过渡帧仍有支撑间隙：Rest 的间隙中位数由 59.6 mm 降至 6.5 mm，报告保留了 95% 分位数和最大值。

未进行动态平衡、接触力、无滑移和实机安全认证。此包是处理后数据快照，不包含可独立重现的完整提取/重定向流水线。部分姿态可能超出真实机器人的能力。

