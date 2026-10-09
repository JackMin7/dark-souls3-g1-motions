# CSV format

One file per gesture, UTF-8 numeric CSV, comma-separated, no header, 36 columns, 30 FPS. Row i is at i / 30 seconds (zero-based). Duration is frame_count / 30 seconds. Root translation is in meters; root quaternion is XYZW; joint angles are radians. World Z is up. Root XY is retained, not centered in the distributed data.

| Zero-based column | Name |
|---:|---|
| 0 | root_x |
| 1 | root_y |
| 2 | root_z |
| 3 | root_qx |
| 4 | root_qy |
| 5 | root_qz |
| 6 | root_qw |
| 7 | left_hip_pitch_joint |
| 8 | left_hip_roll_joint |
| 9 | left_hip_yaw_joint |
| 10 | left_knee_joint |
| 11 | left_ankle_pitch_joint |
| 12 | left_ankle_roll_joint |
| 13 | right_hip_pitch_joint |
| 14 | right_hip_roll_joint |
| 15 | right_hip_yaw_joint |
| 16 | right_knee_joint |
| 17 | right_ankle_pitch_joint |
| 18 | right_ankle_roll_joint |
| 19 | waist_yaw_joint |
| 20 | waist_roll_joint |
| 21 | waist_pitch_joint |
| 22 | left_shoulder_pitch_joint |
| 23 | left_shoulder_roll_joint |
| 24 | left_shoulder_yaw_joint |
| 25 | left_elbow_joint |
| 26 | left_wrist_roll_joint |
| 27 | left_wrist_pitch_joint |
| 28 | left_wrist_yaw_joint |
| 29 | right_shoulder_pitch_joint |
| 30 | right_shoulder_roll_joint |
| 31 | right_shoulder_yaw_joint |
| 32 | right_elbow_joint |
| 33 | right_wrist_roll_joint |
| 34 | right_wrist_pitch_joint |
| 35 | right_wrist_yaw_joint |

Joint order is the kinematic qpos order of the G1 29-joint model used by robot_retargeter, not an actuator command order. Confirm against your own model. Finger joints are not included.

For MuJoCo, convert root XYZW to WXYZ before assigning qpos: root_xyz + [qw,qx,qy,qz] + joint_angles. Do not feed these rows directly to hardware. Do not interpret the CSV as BVH, SMPL, LAFAN1 skeleton data, degrees, or a timestamped table.

GIF looping is a presentation choice, not a claim of dynamically feasible cyclic motion. No contact forces, torques, velocity commands, balance controller, or finger articulation are supplied.
