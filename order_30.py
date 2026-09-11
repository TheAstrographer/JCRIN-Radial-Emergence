import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Thinnest Triangle measurements
theta = np.arctan(2 * np.pi)
phi   = np.arctan(np.pi)
psi   = theta - phi
alpha = theta / 2
cos_psi = np.cos(psi)

# -------------------------------------------------
# Order-30 field on S²
# -------------------------------------------------
n_phi, n_theta = 120, 60
phi_g = np.linspace(0, 2*np.pi, n_phi)
theta_g = np.linspace(0, np.pi, n_theta)
PHI, THETA = np.meshgrid(phi_g, theta_g)

X = np.sin(THETA) * np.cos(PHI)
Y = np.sin(THETA) * np.sin(PHI)
Z = np.cos(THETA)

order = 30
field = (0.5 + 0.5 * np.cos(order * PHI)) * np.exp(-((THETA - np.pi/2)**2) / 0.35)
field = (field - field.min()) / (field.max() - field.min())

# -------------------------------------------------
# Figure
# -------------------------------------------------
fig = plt.figure(figsize=(13, 7))

# Left: Sphere
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=plt.cm.magma(field),
                rstride=1, cstride=1, linewidth=0, alpha=0.93)

# Mark a subset of the 30 axes for clarity
for k in range(order):
    ang = k * 2 * np.pi / order
    ax.plot([0, 1.05*np.cos(ang)], [0, 1.05*np.sin(ang)], [0, 0],
            color='cyan', lw=0.9, alpha=0.6)

ax.set_title('Order-30 Radial Symmetry\nSpherical Attention Heatmap on $S^2$', fontsize=12)
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)
ax.set_zlim(-1.15, 1.15)
ax.set_box_aspect([1,1,1])
ax.view_init(elev=24, azim=35)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Right: Thinnest Triangle table
ax2 = fig.add_subplot(122)
ax2.axis('off')

table_data = [
    ['Symbol', 'Expression', 'Radians', 'Degrees'],
    [r'θ', r'arctan(2π)', f'{theta:.8f}', f'{np.degrees(theta):.4f}°'],
    [r'φ', r'arctan(π)',  f'{phi:.8f}',  f'{np.degrees(phi):.4f}°'],
    [r'Ψ', r'θ − φ',      f'{psi:.8f}',  f'{np.degrees(psi):.4f}°'],
    [r'α', r'θ / 2',      f'{alpha:.8f}',f'{np.degrees(alpha):.4f}°'],
    [r'cos(Ψ)', r'cos(θ−φ)', f'{cos_psi:.8f}', '—'],
]

table = ax2.table(cellText=table_data, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.25, 2.0)

# Style header
for j in range(4):
    table[(0, j)].set_facecolor('#2c3e50')
    table[(0, j)].set_text_props(color='white', weight='bold')

# Highlight Ψ row
for j in range(4):
    table[(3, j)].set_facecolor('#f39c12')
    table[(3, j)].set_text_props(weight='bold')

ax2.set_title('Thinnest Triangle Measurements\n(ArcanTau Angular Gates)', fontsize=12, pad=20)

plt.tight_layout()
plt.savefig('/home/workdir/order30_thinnest_triangle.png', dpi=150, bbox_inches='tight')
print("Order-30 map with Thinnest Triangle table saved.")
