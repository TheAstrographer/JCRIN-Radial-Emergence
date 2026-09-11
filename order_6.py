import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------
# Order-6 Radial Symmetry on S²
# -------------------------------------------------
n_phi = 120
n_theta = 60

phi = np.linspace(0, 2*np.pi, n_phi)
theta = np.linspace(0, np.pi, n_theta)
PHI, THETA = np.meshgrid(phi, theta)

# Cartesian coordinates
X = np.sin(THETA) * np.cos(PHI)
Y = np.sin(THETA) * np.sin(PHI)
Z = np.cos(THETA)

# Order-6 radial symmetry attention field
# 6 equally spaced lobes in azimuth + radial modulation
order = 6
attn = (
    0.55 * (1 + np.cos(order * PHI)) *          # 6-fold azimuthal symmetry
    np.exp( -((THETA - np.pi/2)**2) / 0.35 ) *  # concentration near equator
    (0.4 + 0.6 * np.sin(THETA)**2)              # mild radial weighting
)
attn = (attn - attn.min()) / (attn.max() - attn.min())

# -------------------------------------------------
# Plot
# -------------------------------------------------
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(
    X, Y, Z,
    facecolors=plt.cm.magma(attn),
    rstride=1, cstride=1,
    linewidth=0, antialiased=True, alpha=0.93
)

# Light wireframe for structure
ax.plot_wireframe(X, Y, Z, color='gray', alpha=0.08, linewidth=0.2)

# Mark the 6 symmetry axes on the equator
for k in range(order):
    angle = k * 2*np.pi / order
    ax.plot(
        [0, 1.08*np.cos(angle)],
        [0, 1.08*np.sin(angle)],
        [0, 0],
        color='cyan', linewidth=2.0, alpha=0.9
    )

ax.set_title('Order-6 Radial Symmetry\n360° Spherical Attention Heatmap on $S^2$',
             fontsize=14, pad=12)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_box_aspect([1,1,1])
ax.view_init(elev=25, azim=40)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Colorbar
mappable = plt.cm.ScalarMappable(cmap='magma')
mappable.set_array(attn)
cbar = fig.colorbar(mappable, ax=ax, shrink=0.55, pad=0.06)
cbar.set_label('Attention Intensity', fontsize=10)

plt.tight_layout()
plt.savefig('/home/workdir/order6_radial_symmetry_sphere.png', dpi=150, bbox_inches='tight')
print("Order-6 radial symmetry spherical attention map saved.")
