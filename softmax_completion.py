import math

============================================================
Constants from the notes
============================================================
psi = 0.15033788                    # ≈ 8.61°
cos_psi = math.cos(psi)             # ≈ 0.98872053
cos2_psi = cos_psi ** 2             # ≈ 0.9775 (97.75%)
eta_psi = psi / (2 * math.pi)       # ≈ 0.02392

M = 30
B_effective_coeff = M * eta_psi     # ≈ 0.7177

============================================================
Helper: discrete angles t_k = 2πk / N
============================================================
def get_angles(N):
    return [2 * math.pi * k / N for k in range(N)]

============================================================
Probability distribution
P_i = exp(cos(t_i) * cosψ) / Σ exp(cos(t_j) * cosψ)
============================================================
def compute_P(N, cos_psi):
    angles = get_angles(N)
    logits = [math.exp(math.cos(t) * cos_psi) for t in angles]
    Z = sum(logits)
    return [x / Z for x in logits]

============================================================
Alternative form that appears in the notes
A_ij related to exp(cos(t_i) * cos²ψ)
============================================================
def compute_A(N, cos2_psi):
    angles = get_angles(N)
    logits = [math.exp(math.cos(t) * cos2_psi) for t in angles]
    Z = sum(logits)
    return [x / Z for x in logits]

============================================================
Capacity formulas
============================================================
def C_classical(B, S, N):
    return B * math.log2(1 + S / N)

def C_JCRIN(gamma, M, U, S, N, cos2_psi):
    B = gamma * M * U
    return B * math.log2(1 + (S * cos2_psi) / N)

def B_effective(U):
    return B_effective_coeff * U

============================================================
Demo / verification
============================================================
if name == "main":
    print("=== Basic constants ===")
    print(f"ψ          = {psi:.8f} rad ≈ {math.degrees(psi):.2f}°")
    print(f"cosψ       = {cos_psi:.8f}")
    print(f"cos²ψ      = {cos2_psi:.8f}  ({cos2_psi*100:.2f}%)")
    print(f"ηψ         = {eta_psi:.5f}")
    print(f"B_eff ≈    {B_effective_coeff:.4f} * U")

    print("\n=== Probability distributions ===")
    for N in [16, 32, 64]:
        P = compute_P(N, cos_psi)
        print(f"\nP^{N} (first 5 values):")
        print([round(p, 6) for p in P[:5]], "...")

    print("\n=== A version with cos²ψ ===")
    for N in [16, 32, 64]:
        A = compute_A(N, cos2_psi)
        print(f"\nA^{N} (first 5 values):")
        print([round(a, 6) for a in A[:5]], "...")

    print("\n=== Example capacity calculation ===")
You can change these values as needed
    gamma = 1.0
    U = 100.0
    S = 10.0
    N = 1.0

    c_j = C_JCRIN(gamma, M, U, S, N, cos2_psi)
    c_c = C_classical(gamma * M * U, S, N)

    print(f"C_JCRIN     = {c_j:.4f}")
    print(f"C_classical = {c_c:.4f}")
    print(f"B_effective = {B_effective(U):.4f}")
