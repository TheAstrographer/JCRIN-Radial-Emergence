import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 6))

# --- Left: Full 360° Spherical Heatmap ---
ax1 = fig.add_subplot(121, projection='3d')

u = np.linspace(0, 2 * np.pi, 140)
v = np.linspace(0, np.pi, 70)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

phi = np.arctan2(y, x)
# Dense 64-fold modulation + equatorial concentration
intensity = np.exp(-((v - np.pi/2)**2) / 0.32) * (0.5 + 0.5 * np.cos(64 * phi))
intensity = np.clip(intensity, 0, 1)

ax1.plot_surface(x, y, z, facecolors=plt.cm.magma(intensity),
                 rstride=1, cstride=1, antialiased=True, shade=False, linewidth=0)

# Sample meridians (every 4th for clarity)
for k in range(0, 64, 4):
    theta = 2 * np.pi * k / 64
    ax1.plot(np.sin(v)*np.cos(theta), np.sin(v)*np.sin(theta), np.cos(v),
             color='cyan', alpha=0.3, linewidth=0.5)

ax1.set_title("64D Octonionic Chains / Pathions\n360° Spherical JCRIN τ-Temperature Attention Map", fontsize=12)
ax1.set_axis_off()
ax1.view_init(elev=18, azim=40)
ax1.set_box_aspect([1,1,1])

# --- Right: Aerial (Top-Down) View ---
ax2 = fig.add_subplot(122, projection='polar')

theta = np.linspace(0, 2*np.pi, 512)
r = np.linspace(0, 1, 80)
Theta, R = np.meshgrid(theta, r)

intensity_2d = np.exp(-((R - 0.72)**2)/0.12) * (0.45 + 0.55 * np.cos(64 * Theta))
pcm = ax2.pcolormesh(Theta, R, intensity_2d, cmap='magma', shading='auto')

# Mark Ψ buffer
psi = 0.150338
ax2.plot([0, psi], [0, 1.0], color='red', linewidth=2.5, label=r'$\Psi \approx 8.61^\circ$')
ax2.legend(loc='upper right', fontsize=9)

ax2.set_title("Aerial View — 64-fold Radial Structure\n+ Arcan(τ) Ψ Buffer", fontsize=12)
plt.colorbar(pcm, ax=ax2, shrink=0.7, label='Attention Intensity')

plt.suptitle("JCRIN τ-Temperature Attention Mapping  |  64D Fold\n"
             r"Arcan(τ)  $\Psi \approx 8.61^\circ$  |  $\cos\Psi \approx 0.9887$  |  Temperature-Invariant Softmax  |  Open Winding via $\delta$",
             fontsize=13, y=1.03)

plt.tight_layout() plt.savefig('/home/workdir/64d_jcrin_tau_attention_map.png', dpi=160, bbox_inches='tight', facecolor='white') print("Saved: /home/workdir/64d_jcrin_tau_attention_map.png")
