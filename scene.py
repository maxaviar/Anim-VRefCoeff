from manim import *
from dataclasses import dataclass

@dataclass
class Wavefront:
    launch_time: float
    amplitude: float
    direction: str

def build_wavefronts(n_trips, T, v_plus, gamma_l, gamma_g):
    """Return every wavefront launched on the line, in launch order."""
    fronts = []
    amplitude = v_plus

    for k in range(n_trips):
        direction = "forward" if k % 2 == 0 else "backward"
        fronts.append(Wavefront(k * T, amplitude, direction))

        # Each trip ends at a reflection that sets the next front's amplitude
        amplitude *= gamma_l if direction == "forward" else gamma_g

    return fronts

def v(z,t):
    pass

## USER INPUTS
V_g = 0           # Step voltage from generator at t = 0

Z_g = 0           # Generator's internal resistance, sets how much
                  # of a returning wave is re-reflected

Z_o = 0           # Characteristic impedance, determines how big   
                  # the first wave is and how strong it reflects

Z_l = 0           # Load resistance

l = 1             # Line length, set to 1 if normalizing

u_p = 1           # Propogation velocity, set to 1 if normalizing

t_max = 10        # Simulation runtime, 8 to 12T to see wave settle

max_bounces = 0   # Cutoff below which new wavefronts stop being generated

t_r = 0           # Rise time for source step

# Time Domain
T = l / u_p  # One way travel time down line
Vplus = (V_g * Z_o) / (Z_g + Z_o)  # Amplitude of first wave
gamma_l = (Z_l - Z_o) / (Z_l + Z_o) # Fraction of forward wave reflected
gamma_g = (Z_g - Z_o) / (Z_g + Z_o)  #Fraction of backward wave reflected
V_inf = (V_g * Z_l) / (Z_g + Z_l)  # Final settled voltage

fwd_waves_time = [0, 2*T, 4*T]
fwd_waves_amp = 0
bck_waves_time = [T, 3*T, 5*T]


class VRefCoeff(Scene):
    def construct(self):
        axes = Axes([0,1,],[-1,1])
        self.add(axes)
        self.wait(10)