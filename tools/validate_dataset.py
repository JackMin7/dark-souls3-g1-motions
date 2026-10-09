"""Integrity and numerical checks only; does not certify collision or hardware safety."""
from pathlib import Path
import csv
import hashlib
import json
import math

def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'manifest.json').read_text())
    assert len(manifest['clips']) == 33
    assert len(manifest['columns']) == 36
    assert manifest['fps'] == 30
    expected = {c['path'] for c in manifest['clips']}
    actual = {p.relative_to(root).as_posix() for p in (root / 'data/g1').glob('*.csv')}
    assert actual == expected, 'Unexpected or missing CSV'
    for clip in manifest['clips']:
        path = root / clip['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == clip['sha256'], path.name
        with path.open(newline='') as f: rows = list(csv.reader(f))
        assert len(rows) == clip['frames'], path.name
        for i, row in enumerate(rows):
            assert len(row) == 36, (path.name, i)
            values = [float(v) for v in row]
            assert all(math.isfinite(v) for v in values), (path.name, i)
            assert abs(math.sqrt(sum(v*v for v in values[3:7])) - 1) < 1e-4, (path.name, i)
    for line in (root / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    print('PASS: 33 CSVs, frame counts, 36 columns, finite values, XYZW quaternion norms and all package hashes.')
    print('Not a geometric collision, balance, contact-force or hardware-safety check.')

if __name__ == '__main__': main()
