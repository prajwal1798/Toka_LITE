# Toka_LITE

Toka_LITE is a small Python code for 0D tokamak design studies developed by students of the
CDT Fusion Energy and is intended for university-scale,
non-neutronic tokamak devices.

The code implements a simplified subset of the physics used
in the UKAEA PROCESS systems code and is calibrated to the
parameter ranges of university tokamaks.

## Features

- 0D plasma current model based on the PROCESS q95–Ip–Bt relation
- Greenwald density estimate and thermal beta
- Simple TF coil model (Ampère’s law, coil current per coil)
- Parametric scan over aspect ratio and toroidal field
- 3D surface plots of:
  - plasma current Ip(A, Bt)
  - electron density ne(A, Bt)
  - TF coil current I_coil(A, Bt)
  - thermal beta(A, Bt)

## Installation

We recommend using a virtual environment.

```bash
# clone the repository
git clone https://github.com/<your-user>/Tokamak-0D-Calculator.git
cd Tokamak-0D-Calculator

# create and activate a virtual environment (example: venv)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

