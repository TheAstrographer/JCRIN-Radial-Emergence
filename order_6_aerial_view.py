import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------
# Order-6 field
# -------------------------------------------------
n_phi, n_theta = 120, 60
phi = np.linspace(0, 2*np.pi, n_phi)
theta = np.linspace(0, np.pi, n_theta)
PHI, THETA = np.meshgrid(phi, theta)

X = np.sin(THETA) * np.cos(PHI)
Y = np.sin(THETA) * np.sin(PHI)
Z = np.cos(THETA)

order = 6
field = (0.5 + 0.5 * np.cos(order * PHI)) * np.exp(-((THETA - np.pi/2)**2) / 0.30)
field = (field - field.min()) / (field.max() - field.min())

# -------------------------------------------------
# Aerial (top-down) view
# -------------------------------------------------
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, facecolors=plt.cm.magma(field),
                rstride=1, cstride=1, linewidth=0, alpha=0.95)

# Draw the 6 symmetry axes clearly
for k in range(order):
    ang = k * 2 * np.pi / order
    ax.plot([0, 1.08*np.cos(ang)], [0, 1.08*np.sin(ang)], [0, 0],
            color='cyan', lw=2.5, alpha=0.9)

# Aerial viewpoint – looking almost straight down the z-axis
ax.view_init(elev=90, azim=-90)

ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)
ax.set_zlim(-1.15, 1.15)
ax.set_box_aspect([1,1,1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_title('Aerial View\nOrder-6 Radial Symmetry\n360° Spherical Attention Heatmap on $S^2$',
             fontsize=14, pad=10)

# Colorbar
mappable = plt.cm.ScalarMappable(cmap='magma')
mappable.set_array(field)
cbar = fig.colorbar(mappable, ax=ax, shrink=0.6, pad=0.08)
cbar.set_label('Attention Intensity', fontsize=10)

plt.tight_layout()
plt.savefig('/home/workdir/order6_aerial_view.png', dpi=150, bbox_inches='tight')
print("Aerial view saved.")
