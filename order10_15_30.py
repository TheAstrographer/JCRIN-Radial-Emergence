import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_e8_projection(n_points=800, seed=42):
    """Approximate a visually rich point cloud inspired by E8 root system projections."""
    np.random.seed(seed)
    # Generate points with high symmetry tendency (not exact roots, but visually E8-like)
    # Real E8 has 240 roots; we create a denser cloud for heatmap aesthetics
    pts = []
    
    # Classic E8 construction ingredients (simplified for visualization)
    # Even coordinates or odd with integers / half-integers style sampling
    for _ in range(n_points):
        v = np.random.randn(8)
        v = v / np.linalg.norm(v)
        # Project to 3D using three random but fixed orthogonal directions for consistency
        pts.append(v[:3])   # simple first-3 projection for speed + visual density
    pts = np.array(pts)
    pts = pts / np.linalg.norm(pts, axis=1, keepdims=True)  # push onto sphere
    return pts

def make_order_field(PHI, THETA, order):
    """Create an attention-like field with given rotational order."""
    return (0.5 + 0.5*np.cos(order * PHI)) * np.exp(-((THETA - np.pi/2)**2)/0.4)

# -------------------------------------------------
# Create figure with three orders
# -------------------------------------------------
orders = [10, 15, 30]
fig = plt.figure(figsize=(15, 5.5))

for idx, order in enumerate(orders):
    ax = fig.add_subplot(1, 3, idx+1, projection='3d')
    
    # Spherical grid
    n_phi, n_theta = 90, 45
    phi = np.linspace(0, 2*np.pi, n_phi)
    theta = np.linspace(0, np.pi, n_theta)
    PHI, THETA = np.meshgrid(phi, theta)
    
    X = np.sin(THETA) * np.cos(PHI)
    Y = np.sin(THETA) * np.sin(PHI)
    Z = np.cos(THETA)
    
    # Order-specific field
    field = make_order_field(PHI, THETA, order)
    field = (field - field.min()) / (field.max() - field.min())
    
    # Surface
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.magma(field),
                    rstride=1, cstride=1, linewidth=0, alpha=0.92)
    
# Mark symmetry axes
    for k in range(order):
        ang = k * 2*np.pi / order
        ax.plot([0, 1.05*np.cos(ang)], [0, 1.05*np.sin(ang)], [0, 0],
                color='cyan', lw=1.2, alpha=0.7)
    
    ax.set_title(f'E₈-inspired  •  Order {order}', fontsize=12)
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_zlim(-1.15, 1.15)
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=22, azim=30)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

fig.suptitle('E₈ Radial Symmetry Orders 10, 15, 30\nSpherical Attention Heatmaps on $S^2$',
             fontsize=14, y=1.02)

plt.tight_layout()
plt.savefig('/home/workdir/e8_orders_10_15_30.png', dpi=150, bbox_inches='tight')
print("E₈ orders 10, 15, 30 maps saved.")
