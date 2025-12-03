from dataclasses import dataclass
import math
from .geometry_plasma import mu0


@dataclass
class TFCoils:
    N_tf: int
    N_turn: int
    I_max_coil: float

    def coil_current(self, Bt: float, R0: float) -> float:
        Itot = 2.0 * math.pi * R0 * Bt / mu0
        return Itot / (self.N_tf * self.N_turn)

    def feasible(self, Bt: float, R0: float) -> bool:
        return self.coil_current(Bt, R0) <= self.I_max_coil
