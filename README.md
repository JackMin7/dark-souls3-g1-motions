# Dark Souls III Motions for Unitree G1

**English** | [简体中文](README_zh.md)

33 collectible player gestures from Dark Souls III, retargeted to the 29-joint Unitree G1. Includes arm alignment, terminal-pose corrections, ground-height correction and support optimization for 13 crouching, seated, kneeling or lying motions.


## Motion comparisons

**Left: G1 robot. Right: original game character.** GIFs play automatically, synchronized at original speed (30 FPS source, 15 FPS GIF). Robot display scale is adjusted for comparison. These are rendered animations, not real-robot footage. Weapons, cups and cloth physics are not included.

All 33 GIFs are displayed directly below; no expansion or clicking is required.

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


## Data and usage

- `data/g1/`: 33 headerless CSV files, 36 columns, 30 FPS.
- `manifest.json`: column order, frame counts, durations and SHA-256 hashes.
- [Format](docs/FORMAT.md) · [Motion catalog](docs/MOTIONS.md) · [Support report](reports/contact_report.md).
- `media/comparisons/`: all 33 original-character/G1 comparison GIFs.
- `media/`: three additional robot-only before/after support comparisons.
- `tools/validate_dataset.py`: integrity and basic numerical validation; Python standard library only.

```sh
python3 tools/validate_dataset.py
```

Each row contains root XYZ in meters, root quaternion XYZW and 29 joint angles in radians. World Z is up. Read the exact joint order in [FORMAT](docs/FORMAT.md) before loading into a compatible G1 viewer. This package does not include a player or robot model. Other robot morphologies require retargeting. This is not BVH or a LAFAN1 skeleton format and must not be sent directly to hardware.

## Validation and known limitations

All 33 saved files passed the recorded model-specific float32 ground and continuous between-frame/loop-seam checks. The 13 support-adjusted motions additionally passed recorded self-collision and joint-limit checks. The portable validator only checks integrity and basic numerical properties, not geometric certification.

Support optimization adjusted root height, legs and necessary arm joints while retaining root XY, root orientation and waist joints relative to the predecessor. Some transition frames still have support gaps. Rest's reported median gap decreased from 59.6 mm to 6.5 mm; p95 and maximum gaps remain available in the report.

No contact-force, dynamic balance, no-slip or hardware-safety certification is claimed. This is a frozen processed-data snapshot, not an independently reproducible extraction/retargeting pipeline. Some poses may exceed real-robot capabilities.
