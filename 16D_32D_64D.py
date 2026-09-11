import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(18, 6))

def create_sphere_heatmap(ax, n_fold, title, elev=20, azim=45):
    u = np.linspace(0, 2 * np.pi, 120)
    v = np.linspace(0, np.pi, 60)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Attention intensity: equatorial band modulated by n-fold symmetry
    phi = np.arctan2(y, x)
    intensity = np.exp(-((v - np.pi/2)**2) / 0.35) * (0.55 + 0.45 * np.cos(n_fold * phi))
    intensity = np.clip(intensity, 0, 1)
    
    ax.plot_surface(x, y, z, facecolors=plt.cm.magma(intensity),
                    rstride=1, cstride=1, antialiased=True, shade=False, linewidth=0)
    
    # Sample meridians for visibility
    step = max(1, n_fold // 16)
    for k in range(0, n_fold, step):
        theta = 2 * np.pi * k / n_fold
        ax.plot(np.sin(v)*np.cos(theta), np.sin(v)*np.sin(theta), np.cos(v),
                color='cyan', alpha=0.25, linewidth=0.6)
    
ax.set_title(title, fontsize=12, pad=10)
    ax.set_axis_off()
    ax.view_init(elev=elev, azim=azim)
    ax.set_box_aspect([1,1,1])

# 16D
ax1 = fig.add_subplot(131, projection='3d')
create_sphere_heatmap(ax1, 16, "16D Sedenion Fold\nJCRIN τ-Temperature Attention Map")

# 32D
ax2 = fig.add_subplot(132, projection='3d')
create_sphere_heatmap(ax2, 32, "32D Trigintaduonions\nJCRIN τ-Temperature Attention Map")

# 64D
ax3 = fig.add_subplot(133, projection='3d')
create_sphere_heatmap(ax3, 64, "64D Octonionic Chains / Pathions\nJCRIN τ-Temperature Attention Map")

# Colorbar
sm = plt.cm.ScalarMappable(cmap='magma')
sm.set_array([])
cbar = fig.colorbar(sm, ax=[ax1, ax2, ax3], shrink=0.6, aspect=20, pad=0.02)
cbar.set_label('Attention Intensity', fontsize=11)

plt.suptitle("JCRIN τ-Temperature Attention Maps — 16D · 32D · 64D Folds\n"
             "Arcan(τ) Ψ ≈ 8.61° | cosΨ ≈ 0.9887 | Temperature-Invariant Softmax",
             fontsize=14, y=1.02)

             fontsize=14, y=1.02)

plt.tight_layout()
plt.savefig('/home/workdir/16d_32d_64d_jcrin_tau_maps.png', dpi=160, bbox_inches='tight', facecolor='white')
print("Saved: /home/workdir/16d_32d_64d_jcrin_tau_maps.png")
