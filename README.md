# rf-antenna-designer
# Microstrip Patch Antenna Designer & Far-Field Visualizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Domain](https://img.shields.io/badge/Domain-RF%20%26%20Electromagnetics-orange)

A Python tool for calculating rectangular microstrip patch antenna dimensions and modeling 2D polar far-field radiation patterns. Designed to demonstrate fundamental RF engineering workflow principles, high-frequency analytical modeling, and computational electromagnetics.

---

## Technical Features

* **Dimension Calculations:** Computes patch width ($W$), patch length ($L$), effective dielectric constant ($\epsilon_{eff}$), and fringing field length extension ($\Delta L$) using transmission line equations.
* **Far-Field Radiation Patterns:** Simulates E-plane and H-plane polar power distributions in dB.
* **Object-Oriented Design:** Modular Python architecture suitable for parametric integration or automated design sweeps.

---

## Analytical Results (2.4 GHz FR4 Example)

Target specs: $f = 2.4\text{ GHz}$, $\epsilon_r = 4.4$, Substrate height $h = 1.6\text{ mm}$.

| Parameter | Calculated Value |
| :--- | :---: |
| Patch Width ($W$) | 38.04 mm |
| Patch Length ($L$) | 29.44 mm |
| Effective Permittivity ($\epsilon_{eff}$) | 4.08 |
| Extended Length ($\Delta L$) | 0.73 mm |

---

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
