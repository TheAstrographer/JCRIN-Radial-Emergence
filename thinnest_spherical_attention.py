import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Angular gates in radians
theta = np.arctan(2 * np.pi)      # ≈ 80.9569°
phi   = np.arctan(np.pi)         # ≈ 72.3432°
psi   = theta - phi              # ≈ 8.6137°

print(f"θ = {np.degrees(theta):.4f}°")
print(f"φ = {np.degrees(phi):.4f}°")
print(f"Ψ = {np.degrees(psi):.4f}°")

# -------------------------------------------------
# Create a spherical grid (S²)
# -------------------------------------------------
n_phi = 60          # azimuthal
n_theta = 30        # polar

phi_grid = np.linspace(0, 2*np.pi, n_phi)
theta_grid = np.linspace(0, np.pi, n_theta)
PHI, THETA = np.meshgrid(phi_grid, theta_grid)

# Spherical coordinates → Cartesian
R = 1.0
X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

# Synthetic attention field on the sphere
# Higher attention near the thinnest-triangle sector
attn = np.exp(-((THETA - (theta+phi)/2)**2) / (0.15)**2) * np.exp(-((PHI - 0.3)**2)/(0.8)**2)
attn = (attn - attn.min()) / (attn.max() - attn.min())

# -------------------------------------------------
# Plot
# -------------------------------------------------
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface with attention colormap
surf = ax.plot_surface(X, Y, Z, facecolors=plt.cm.magma(attn),
                       rstride=1, cstride=1, alpha=0.92, linewidth=0)

# Draw the Thinnest Triangle rays on the sphere
def ray(angle, length=1.05, color='cyan', lw=2.5, label=None):
    # Place rays in the xz-plane for clarity (elevated slightly)
    x = length * np.sin(angle)
    z = length * np.cos(angle)
    ax.plot([0, x], [0, 0], [0, z], color=color, linewidth=lw, label=label)

ray(theta, color='lime', lw=3, label=fr'θ = arctan(2π) ≈ {np.degrees(theta):.1f}°')
ray(phi,   color='deepskyblue', lw=3, label=fr'φ = arctan(π) ≈ {np.degrees(phi):.1f}°')

# Draw the Ψ buffer arc (thinnest triangle)
arc_angles = np.linspace(phi, theta, 40)
arc_x = 1.03 * np.sin(arc_angles)
arc_z = 1.03 * np.cos(arc_angles)
ax.plot(arc_x, np.zeros_like(arc_x), arc_z, color='orange', linewidth=4,
        label=fr'Ψ (Thinnest Triangle) ≈ {np.degrees(psi):.2f}°')

# Origin
ax.scatter([0], [0], [0], color='white', s=40, zorder=5)

# Labels and styling
ax.set_title('360° Spherical Attention Map on $S^2$\nwith Thinnest Triangle Labelled',
             fontsize=14, pad=15)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Equal aspect
ax.set_box_aspect([1,1,1])
ax.view_init(elev=18, azim=35)

# Legend
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

# Colorbar
mappable = plt.cm.ScalarMappable(cmap='magma')
mappable.set_array(attn)
cbar = fig.colorbar(mappable, ax=ax, shrink=0.55, pad=0.08)
cbar.set_label('Attention Intensity', fontsize=10)

plt.tight_layout()
plt.savefig('/home/workdir/spherical_attention_thinnest_triangle.png', dpi=150, bbox_inches='tight')
print("Spherical attention map saved.")
