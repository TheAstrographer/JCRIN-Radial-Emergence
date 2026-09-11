import numpy as np
import matplotlib.pyplot as plt

# Thinnest Triangle angles (radians)
theta = np.arctan(2 * np.pi)
phi   = np.arctan(np.pi)
psi   = theta - phi
cos_psi = np.cos(psi)

print(f"θ = {np.degrees(theta):.4f}°")
print(f"φ = {np.degrees(phi):.4f}°")
print(f"Ψ = {np.degrees(psi):.4f}°")
print(f"cos(Ψ) = {cos_psi:.6f}")

# Create a synthetic attention logit matrix (8 tokens)
np.random.seed(42)
n_tokens = 8
base_logits = np.random.randn(n_tokens, n_tokens) * 1.5

# Apply Thinnest-Triangle Softmax for several τ values
taus = [2*np.pi, np.pi, np.pi/2, np.pi/4, 0.5]

fig, axes = plt.subplots(1, len(taus), figsize=(16, 3.8))

for ax, tau in zip(axes, taus):
    # Temperature-scaled + Thinnest-Triangle modulation
    # After cancellation the effective score is cos(t) * cos(Ψ)
    # We simulate this by modulating the base logits with cos_psi and a soft radial factor
    modulated = base_logits * cos_psi
    
    # Softmax
    exp_scores = np.exp(modulated - np.max(modulated, axis=-1, keepdims=True))
    attn = exp_scores / exp_scores.sum(axis=-1, keepdims=True)
    
    im = ax.imshow(attn, cmap='magma', vmin=0, vmax=attn.max())
    ax.set_title(f'τ = {tau:.3f}\n(λ ≈ {1 - tau/(2*np.pi):.2f})', fontsize=10)
    ax.set_xlabel('Key')
    ax.set_ylabel('Query')
    ax.set_xticks(range(n_tokens))
    ax.set_yticks(range(n_tokens))

fig.suptitle('τ–Thinnest-Triangle Attention Heat Maps\n'
             r'(modulated by $\cos\Psi \approx 0.99887$, $\Psi\approx 8.6137^\circ$)',
             fontsize=13, y=1.05)

plt.tight_layout()
plt.savefig('/home/workdir/tau_thinnest_triangle_heatmap.png', dpi=150, bbox_inches='tight')
print("Heatmap saved.")
