import matplotlib.pyplot as plt

from subroutines.tf_coils import TFCoils
from subroutines.scanning import scan_A_Bt_grid
from subroutines.plotting import plot_surface


def make_all_surfaces():
    a = 0.25
    kappa = 1.6
    delta = 0.0
    q95 = 4.0
    f_G = 0.4
    Te_eV = 100.0
    Ti_eV = 50.0

    tf = TFCoils(N_tf=12, N_turn=4, I_max_coil=15e3)

    grids = scan_A_Bt_grid(
        A_min=1.5,
        A_max=3.0,
        Bt_min=0.25,
        Bt_max=0.75,
        n_A=60,
        n_Bt=60,
        a=a,
        kappa=kappa,
        delta=delta,
        q95=q95,
        f_G=f_G,
        Te_eV=Te_eV,
        Ti_e_V=Ti_eV,
        tf=tf,
    )

    A = grids["A"]
    Bt = grids["Bt"]
    Ip_kA = grids["Ip_MA"] * 1e3
    ne = grids["ne"]
    Icoil_kA = grids["Icoil"] * 1e-3
    beta = grids["beta"]

    mask = grids["feasible"]
    Ip_kA = Ip_kA * mask
    ne = ne * mask
    Icoil_kA = Icoil_kA * mask
    beta = beta * mask

    plot_surface(A, Bt, Ip_kA, "Aspect ratio A", "Bt [T]", "Ip [kA]",
                 "Plasma current vs A,Bt")
    plot_surface(A, Bt, ne, "Aspect ratio A", "Bt [T]", "ne [m$^{-3}$]",
                 "Electron density vs A,Bt")
    plot_surface(A, Bt, Icoil_kA, "Aspect ratio A", "Bt [T]", "I_coil [kA]",
                 "TF coil current vs A,Bt")
    plot_surface(A, Bt, beta, "Aspect ratio A", "Bt [T]", "beta",
                 "Thermal beta vs A,Bt")

    plt.show()


if __name__ == "__main__":
    make_all_surfaces()
