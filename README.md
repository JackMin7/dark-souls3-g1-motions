# Dark Souls III Motions for Unitree G1

**English** | [简体中文](README_zh.md)

33 collectible player gestures from Dark Souls III, retargeted to the 29-joint Unitree G1. Includes arm alignment, terminal-pose corrections, ground-height correction and support optimization for 13 crouching, seated, kneeling or lying motions.


## Motion comparisons

**Left: G1 robot. Right: original game character.** GIFs play automatically, synchronized at original speed (30 FPS source, 15 FPS GIF). Robot display scale is adjusted for comparison. These are rendered animations, not real-robot footage. Weapons, cups and cloth physics are not included.

All 33 GIFs are embedded below. The full gallery is image-heavy; expand the list as needed.

<details>
<summary>01 Beckon</summary>

![01 Beckon](media/comparisons/01_Beckon.gif)

</details>

<details>
<summary>02 Praise the Sun</summary>

![02 Praise the Sun](media/comparisons/02_Praise_the_Sun.gif)

</details>

<details>
<summary>03 Point Up</summary>

![03 Point Up](media/comparisons/03_Point_Up.gif)

</details>

<details>
<summary>04 Point Down</summary>

![04 Point Down](media/comparisons/04_Point_Down.gif)

</details>

<details>
<summary>05 Duel Bow</summary>

![05 Duel Bow](media/comparisons/05_Duel_Bow.gif)

</details>

<details>
<summary>06 Point Forward</summary>

![06 Point Forward](media/comparisons/06_Point_Forward.gif)

</details>

<details>
<summary>07 Welcome</summary>

![07 Welcome](media/comparisons/07_Welcome.gif)

</details>

<details>
<summary>08 Prostration</summary>

![08 Prostration](media/comparisons/08_Prostration.gif)

</details>

<details>
<summary>09 Proper Bow</summary>

![09 Proper Bow](media/comparisons/09_Proper_Bow.gif)

</details>

<details>
<summary>10 Prayer</summary>

![10 Prayer](media/comparisons/10_Prayer.gif)

</details>

<details>
<summary>11 Bow</summary>

![11 Bow](media/comparisons/11_Bow.gif)

</details>

<details>
<summary>12 Wave</summary>

![12 Wave](media/comparisons/12_Wave.gif)

</details>

<details>
<summary>13 Hurrah</summary>

![13 Hurrah](media/comparisons/13_Hurrah.gif)

</details>

<details>
<summary>14 Jump for Joy</summary>

![14 Jump for Joy](media/comparisons/14_Jump_for_Joy.gif)

</details>

<details>
<summary>15 Joy</summary>

![15 Joy](media/comparisons/15_Joy.gif)

</details>

<details>
<summary>16 My Thanks</summary>

![16 My Thanks](media/comparisons/16_My_Thanks.gif)

</details>

<details>
<summary>17 Rejoice</summary>

![17 Rejoice](media/comparisons/17_Rejoice.gif)

</details>

<details>
<summary>18 Rest</summary>

![18 Rest](media/comparisons/18_Rest.gif)

</details>

<details>
<summary>19 By My Sword</summary>

![19 By My Sword](media/comparisons/19_By_My_Sword.gif)

</details>

<details>
<summary>20 Dignified Bow</summary>

![20 Dignified Bow](media/comparisons/20_Dignified_Bow.gif)

</details>

<details>
<summary>21 Curl Up</summary>

![21 Curl Up](media/comparisons/21_Curl_Up.gif)

</details>

<details>
<summary>22 Stretch Out</summary>

![22 Stretch Out](media/comparisons/22_Stretch_Out.gif)

</details>

<details>
<summary>23 Call Over</summary>

![23 Call Over](media/comparisons/23_Call_Over.gif)

</details>

<details>
<summary>24 Collapse</summary>

![24 Collapse](media/comparisons/24_Collapse.gif)

</details>

<details>
<summary>25 Quiet Resolve</summary>

![25 Quiet Resolve](media/comparisons/25_Quiet_Resolve.gif)

</details>

<details>
<summary>26 Patches Squat</summary>

![26 Patches Squat](media/comparisons/26_Patches_Squat.gif)

</details>

<details>
<summary>27 Applause</summary>

![27 Applause](media/comparisons/27_Applause.gif)

</details>

<details>
<summary>28 Path of the Dragon</summary>

![28 Path of the Dragon](media/comparisons/28_Path_of_the_Dragon.gif)

</details>

<details>
<summary>29 Legion Etiquette</summary>

![29 Legion Etiquette](media/comparisons/29_Legion_Etiquette.gif)

</details>

<details>
<summary>30 Darkmoon Loyalty</summary>

![30 Darkmoon Loyalty](media/comparisons/30_Darkmoon_Loyalty.gif)

</details>

<details>
<summary>31 Sleep</summary>

![31 Sleep](media/comparisons/31_Sleep.gif)

</details>

<details>
<summary>32 Toast</summary>

![32 Toast](media/comparisons/32_Toast.gif)

</details>

<details>
<summary>33 Silent Ally</summary>

![33 Silent Ally](media/comparisons/33_Silent_Ally.gif)

</details>

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

