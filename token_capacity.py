import math

print("=" * 70)
print("JCRIN τ-Temperature Attention Mapping")
print("Token Capacity Expansion from Quadratic Cost")
print("=" * 70)

# -------------------------------------------------
# 1. Classical reference length
# -------------------------------------------------
N_classical = 100_000          # 10^5
print(f"\n1. Classical sequence length (N_classical)")
print(f"   N_classical = {N_classical:,}")

# -------------------------------------------------
# 2. Leading-order JCRIN capacity (quadratic inversion)
# -------------------------------------------------
N_jcrin_leading = N_classical ** 2
print(f"\n2. Leading-order JCRIN capacity")
print(f"   N_JCRIN ≈ (N_classical)² = ({N_classical:,})² = {N_jcrin_leading:,}")

# -------------------------------------------------
# 3. Thinnest-Triangle power factor
# -------------------------------------------------
cos_Psi = 0.988721
cos2_Psi = cos_Psi ** 2
print(f"\n3. Thinnest-Triangle power factor")
print(f"   cos(Ψ)     ≈ {cos_Psi:.6f}")
print(f"   cos²(Ψ)    ≈ {cos2_Psi:.6f}  (97.75 % retention)")

# -------------------------------------------------
# 4. Corrected JCRIN capacity (marginal adjustment)
# -------------------------------------------------
# The power factor slightly reduces effective capacity,
# but does not change the leading-order scaling.
N_jcrin_corrected = int(N_jcrin_leading * cos2_Psi)
print(f"\n4. Corrected JCRIN capacity (with cos²Ψ)")
print(f"   N_JCRIN_corrected ≈ {N_jcrin_leading:,} × {cos2_Psi:.4f}")
print(f"                    ≈ {N_jcrin_corrected:,}")

# -------------------------------------------------
# 5. Token gain
# -------------------------------------------------
tokens_gained = N_jcrin_corrected - N_classical
multiplier = N_jcrin_corrected / N_classical

print(f"\n5. Expansion summary")
print(f"   Classical tokens : {N_classical:>15,}")
print(f"   JCRIN tokens     : {N_jcrin_corrected:>15,}")
print(f"   Tokens gained    : {tokens_gained:>15,}")
print(f"   Capacity multiplier ≈ {multiplier:,.0f}×")

# -------------------------------------------------
# 6. Quadratic cost illustration
# -------------------------------------------------
print(f"\n6. Quadratic cost relation")
print(f"   Classical cost ∝ N² = {N_classical:,}² = {N_classical**2:,}")
print(f"   JCRIN cost     ∝ N  = {N_jcrin_corrected:,}")
print(f"   Same budget therefore supports ~N² tokens under JCRIN")

print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)
print(f"{N_classical:,}  →  JCRIN  ≈  {N_jcrin_corrected:,}   ({multiplier:,.0f}×)")
print(f"Additional tokens ≈ {tokens_gained:,}")
print("=" * 70)
