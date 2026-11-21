# vibration-lib

Vibration signal processing and bearing diagnostics in Python. Pure functions on NumPy arrays, verified against synthetic signals with known results.

> **Status:** early development (pre-0.1). The API may change.

## Installation

```bash
pip install vibration-lib
```

Requires Python 3.14 or newer. From source:

```bash
git clone https://github.com/<user>/vibration-lib
cd vibration-lib
uv sync
```

## Quick start

```python
from vibration_lib.kinematics import Bearing

# CWRU 6205 drive-end bearing (dimensions in mm)
bearing = Bearing(n_balls=9, ball_d=7.94, pitch_d=39.04, contact_angle=0)

bearing.bpfo(speed_hz=29.95)   # 107.36 Hz, outer race fault frequency
```

## Features

- **Kinematics:** characteristic bearing fault frequencies (BPFO, BPFI, BSF, FTF).
- **Planned:** spectral analysis, envelope spectrum, spectral kurtosis and kurtogram, cepstrum, order tracking, time-synchronous averaging, feature extraction.

## Conventions

- Every function takes the signal `x` and the sampling rate `fs` explicitly.
- Units are stated in docstrings and in argument names (`speed_hz`, not `speed`).
- Base dependencies: NumPy and SciPy only.

## Development

```bash
uv sync
uv run pytest
uv run ruff check
uv run mypy --strict src
```

## References

Randall, R. B., & Antoni, J. (2011). Rolling element bearing diagnostics: a tutorial. *Mechanical Systems and Signal Processing*, 25(2), 485-520. https://doi.org/10.1016/j.ymssp.2010.07.017

## License

MIT.
