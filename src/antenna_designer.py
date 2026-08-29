import numpy as np
import matplotlib.pyplot as plt

class RectangularPatchAntenna:
    """
    Calculates rectangular microstrip patch antenna dimensions 
    and models far-field radiation patterns based on transmission line theory.
    """
    def __init__(self, freq_hz: float, er: float, h_m: float):
        self.c = 3e8  # Speed of light (m/s)
        self.freq = freq_hz
        self.er = er
        self.h = h_m

    def calculate_dimensions(self) -> dict:
        """Calculates patch width (W), effective permittivity, extended length (dL), and patch length (L)."""
        # Patch Width (W)
        W = (self.c / (2 * self.freq)) * np.sqrt(2 / (self.er + 1))
        
        # Effective Dielectric Constant (e_eff)
        e_eff = ((self.er + 1) / 2) + ((self.er - 1) / 2) * (1 / np.sqrt(1 + 12 * (self.h / W)))
        
        # Length Extension (dL)
        dL = 0.412 * self.h * ((e_eff + 0.3) * (W / self.h + 0.264)) / ((e_eff - 0.258) * (W / self.h + 0.8))
        
        # Effective Length & Actual Length (L)
        L_eff = self.c / (2 * self.freq * np.sqrt(e_eff))
        L = L_eff - 2 * dL
        
        return {
            "Width_mm": W * 1e3,
            "Length_mm": L * 1e3,
            "e_eff": e_eff,
            "Delta_L_mm": dL * 1e3
        }

    def plot_radiation_pattern(self, save_path: str = None):
        """Generates a 2D polar plot of E-plane and H-plane far-field radiation patterns."""
        theta = np.linspace(-np.pi, np.pi, 360)
        
        # Normalized array factor approximation for E-plane & H-plane
        e_plane = np.abs(np.cos(theta))
        h_plane = np.abs(np.cos(theta / 2))
        
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6))
        ax.plot(theta, 20 * np.log10(e_plane + 1e-3), label="E-Plane (dB)", color="#1A365D")
        ax.plot(theta, 20 * np.log10(h_plane + 1e-3), label="H-Plane (dB)", color="#2B6CB0", linestyle="--")
        
        ax.set_rticks([-30, -20, -10, 0])
        ax.set_rlabel_position(-22)
        ax.grid(True)
        ax.set_title(f"Far-Field Radiation Pattern ({self.freq/1e9:.2f} GHz)", va='bottom', pad=15)
        ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()

if __name__ == "__main__":
    # Example simulation: 2.4 GHz WiFi Antenna on FR4 Substrate (er=4.4, h=1.6mm)
    antenna = RectangularPatchAntenna(freq_hz=2.4e9, er=4.4, h_m=1.6e-3)
    dims = antenna.calculate_dimensions()
    
    print("--- Calculated Patch Dimensions ---")
    for key, val in dims.items():
        print(f"{key}: {val:.3f}")
        
    antenna.plot_radiation_pattern()
