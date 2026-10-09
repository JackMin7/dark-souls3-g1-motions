# Provenance and third-party materials

Source: Dark Souls III collectible player gestures, processed locally into motion skeletons and retargeted to Unitree G1. Gesture names refer to the game; source reference: https://darksouls3.wikidot.com/gestures . This reference is not a redistribution license.

Target: robot_retargeter G1 29-joint kinematic model. Model XML SHA-256: `e3aca57d6e6ce493b25454b4da26ae495eb300ad35e32be62dfb8bbefbaecf42`.

Processing stages: game motion extraction → skeleton/BVH conversion → G1 retargeting → arm/terminal-pose corrections → ground-height correction stage → ground-support optimization. This package includes only the final CSV snapshot, metadata and recorded reports. The source pipeline has local environment dependencies and is not distributed here; no end-to-end reproducibility claim is made.

Game assets and animations have third-party provenance. G1 names/model visuals have separate third-party provenance. Rights clearance for derived motion data and rendered previews has not been supplied. No rights are granted on behalf of those owners. Attribution alone does not establish permission.

Excluded: game installation files, extracted meshes/textures/animation archives, original BVH, Blender scene, robot geometry, external retargeter source, local caches and logs. Original-game comparison GIFs are included in this local repository candidate for review; public redistribution permissions remain unresolved.

Recorded validation uses the model and collision approximations of the local processing workflow. `source_sha256` in the verification report identifies the ground-height correction stage predecessor, not the raw game source; `sha256` identifies the released CSV.
