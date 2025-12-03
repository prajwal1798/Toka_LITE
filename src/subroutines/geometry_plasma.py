import math
from dataclasses import dataclass

import numpy as np

mu0 = 4.0 * math.pi * 1e-7
kB = 1.380649e-23
eV = 1.602176634e-19


@dataclass
class Shape:
    R: float
    a: float
    kappa: float
    delta: float

    @property
    def aspect_ratio(self) -> float:
        return self.R / self.a


def fq_PROCESS(shape: Shape) -> float:
    A = shape.aspect_ratio
    k = shape.kappa
    d = shape.delta
    num = 1.17 - 0.65 * A * A
    den = 1.0 - A * A
    if den <= 0.0:
        den = 1e-6
    f1 = num / den
    f2 = 0.5 * (1.0 + k * k)
    f3 = 1.0 + 2.0 * d * d - 1.2 * d * d * d
    return f1 * f2 * f3


def Ip_from_q95_PROCESS(Bt: float, q95: float, shape: Shape) -> float:
    fq = fq_PROCESS(shape)
    return 5.0 * shape.a * shape.a * Bt / (q95 * shape.R * fq)


def greenwald_density(Ip_MA: float, a: float, f_G: float = 0.4):
    nG = 1.0e20 * Ip_MA / (math.pi * a * a)
    ne = f_G * nG
    return nG, ne


def thermal_beta(Bt: float, ne: float, Te_eV: float, Ti_eV: float) -> float:
    Te_J = Te_eV * eV
    Ti_J = Ti_eV * eV
    p = ne * kB * (Te_J / kB + Ti_J / kB)
    return 2.0 * mu0 * p / (Bt * Bt)
