import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
from matplotlib.collections import LineCollection

# Angular gates
theta = np.arctan(2 * np.pi)
phi   = np.arctan(np.pi)
psi   = theta - phi
cos_psi = np.cos(psi)

print(f"θ = {np.degrees(theta):.4f}°")
print(f"φ = {np.degrees(phi):.4f}°")
print(f"Ψ = {np.degrees(psi):.4f}°")
print(f"cos(Ψ) = {cos_psi:.6f}")

# -------------------------------------------------
# 1. Generate polar (x, y) coordinates on the carrier
# -------------------------------------------------
n_points = 12
t_angles = np.linspace(0.2, np.pi - 0.2, n_points)   # upper half-plane angles

# Several radial temperatures
taus = [2*np.pi, np.pi, np.pi/2, 1.0]

fig = plt.figure(figsize=(14, 6))

# Left panel: Polar (x, y) mapping
ax1 = fig.add_subplot(121)
ax1.set_aspect('equal')
ax1.set_title(r'Polar Mapping: $x=\tau\cos t$, $y=\tau\sin t$' + '\n(Thinnest-Triangle Geometry)', fontsize=12)

# -------------------------------------------------
# 1. Generate polar (x, y) coordinates on the carrier
# -------------------------------------------------
n_points = 12
t_angles = np.linspace(0.2, np.pi - 0.2, n_points)   # upper half-plane angles

# Several radial temperatures
taus = [2*np.pi, np.pi, np.pi/2, 1.0]

fig = plt.figure(figsize=(14, 6))

# Left panel: Polar (x, y) mapping
ax1 = fig.add_subplot(121)
ax1.set_aspect('equal')
ax1.set_title(r'Polar Mapping: $x=\tau\cos t$, $y=\tau\sin t$' + '\n(Thinnest-Triangle Geometry)', fontsize=12)

colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(taus)))

for tau, color in zip(taus, colors):
    x = tau * np.cos(t_angles)
    y = tau * np.sin(t_angles)
    ax1.plot(x, y, 'o-', color=color, markersize=6, linewidth=1.5,
             label=fr'$\tau={tau:.2f}$')
    
    # Draw rays from origin
    for xi, yi in zip(x, y):
        ax1.plot([0, xi], [0, yi], color=color, alpha=0.25, linewidth=0.8)

# Mark the thinnest-triangle angular sector
r_max = 2*np.pi + 0.5
ax1.plot([0, r_max*np.cos(theta)], [0, r_max*np.sin(theta)], 'g--', lw=2, label=fr'$\theta\approx{np.degrees(theta):.1f}^\circ$')
ax1.plot([0, r_max*np.cos(phi)],  [0, r_max*np.sin(phi)],  'b--', lw=2, label=fr'$\phi\approx{np.degrees(phi):.1f}^\circ$')

# Shade the Ψ buffer
wedge_theta = np.linspace(phi, theta, 50)
ax1.fill_between(r_max*np.cos(wedge_theta), 0, r_max*np.sin(wedge_theta),
                 color='orange', alpha=0.15, label=fr'$\Psi\approx{np.degrees(psi):.2f}^\circ$ buffer')

ax1.set_xlabel(r'$x(\lambda)=\tau\cos t$')
ax1.set_ylabel(r'$y(\lambda)=\tau\sin t$')
ax1.legend(loc='upper right', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-1, 7)
ax1.set_ylim(-0.5, 7)

# -------------------------------------------------
# 2. Thinnest-Triangle Attention Heatmap
# -------------------------------------------------
ax2 = fig.add_subplot(122)

np.random.seed(42)
n_tokens = 8
base = np.random.randn(n_tokens, n_tokens) * 1.2

# Apply thinnest-triangle modulation
modulated = base * cos_psi
exp_scores = np.exp(modulated - np.max(modulated, axis=-1, keepdims=True))
attn = exp_scores / exp_scores.sum(axis=-1, keepdims=True)

im = ax2.imshow(attn, cmap='magma', vmin=0, vmax=attn.max())
ax2.set_title('Thinnest-Triangle Attention Map\n' + 
              r'(modulated by $\cos\Psi\approx 0.99887$)', fontsize=12)
ax2.set_xlabel('Key index')
ax2.set_ylabel('Query index')
ax2.set_xticks(range(n_tokens))
ax2.set_yticks(range(n_tokens))

# Colorbar
cbar = plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
cbar.set_label('Attention weight', fontsize=9)

plt.tight_layout()
plt.savefig('/home/workdir/xy_thinnest_triangle_attention.png', dpi=150, bbox_inches='tight')
print("Figure saved successfully.")
