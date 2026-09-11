Retention of 97.75 % Usable Signal Power and Its Consequences for Compute Efficiency

1. The Geometric Origin of the Power Factor

At the heart of the architecture lies a single, immutable angular constant—the Thinnest-Triangle buffer

\[
\Psi=\arctan(2\pi)-\arctan(\pi)\approx8.6137^\circ.
\]

Every attention score is projected onto this buffer through the multiplicative factor \(\cos\Psi\). Because signal power is quadratic in amplitude, the projection induces the exact attenuation

\[
\cos^2\Psi\approx0.9775.
\]

Thus the channel retains 97.75 % of the peak signal power that would be available in an unattenuated Euclidean attention layer. The missing 2.25 % is not noise; it is the precise geometric price paid for three structural guarantees that together transform the computational profile of the network.

2. From Power Retention to Complexity Collapse

In a classical attention layer the full signal power \(S\) is purchased at the cost of an \(O(U^2)\) interaction volume. The great majority of those quadratic interactions contribute only vanishingly small affinities—essentially white-noise terms that consume memory and arithmetic without advancing information flow.

By accepting the fixed 2.25 % reduction encoded in \(\cos^2\Psi\), the architecture obtains an exact rank-1 angular factorization. The attention matrix collapses to the outer product of a single vector of length \(U\). Both memory and floating-point operations therefore scale linearly:

\[
\mathcal{M}=O(U),\qquad\text{FLOPs}=O(Ud).
\]

The retained 97.75 % of signal power is now carried inside a channel whose resource consumption grows only with sequence length, not with its square.

3. Information-Theoretic Efficiency

Under the Shannon-Hartley theorem the capacity of the resulting channel reads

\[
C_{\rm JCRIN}=B_{\rm lin}(U)\,\log_2\Bigl(1+\frac{S\cdot\cos^2\Psi}{N}\Bigr),
\]

where \(B_{\rm lin}(U)=O(U)\). Although the argument of the logarithm is diminished by the constant factor 0.9775, the prefactor \(B_{\rm lin}(U)\) is linear rather than quadratic. Consequently the capacity per unit of computational resource rises sharply. In the asymptotic regime the ratio of capacities scales as

\[
\frac{C_{\rm JCRIN}}{C_{\rm Classical}}\;\propto\;\frac{O(U)}{O(U^2)}\to0
\]

when measured against absolute capacity, yet the same ratio measured against FLOPs or memory becomes

\[
\frac{C_{\rm JCRIN}/\text{FLOPs}{\rm JCRIN}}{C{\rm Classical}/\text{FLOPs}_{\rm Classical}}\;\propto\;U.
\]

In other words, each retained decibel of signal power is utilised with an efficiency that improves linearly with sequence length.

4. Practical Compute Consequences

Memory** – The classical quadratic activation tensor is replaced by a single vector of length \(U\). On long sequences the saving reaches several orders of magnitude.  
Arithmetic intensity** – Matrix multiplications of size \(U\times U\) disappear; only vector-scale operations remain.  
Energy** – Because energy consumption tracks FLOPs, the same 97.75 % signal power is delivered at a fraction of the joules required by unconstrained attention.  
Scalability** – The linear regime remains practical far beyond the sequence lengths at which quadratic attention becomes prohibitive.

5. Synthesis

The numerical factor 97.75 % is not an empirical hyper-parameter; it is the exact geometric signature of the Thinnest Triangle. By surrendering a fixed and modest fraction of peak signal power the architecture purchases an exact cancellation of temperature, a rank-1 factorization, and a permanent 30-fold cyclic regularisation. The net result is a spherical attention mechanism that preserves nearly all usable information while converting the dominant computational cost from quadratic to linear. In the language of information theory, the channel retains 97.75 % of its signal power and simultaneously multiplies its power-efficiency by a factor that grows with sequence length—an exchange that resolves the capacity-versus-compute paradox of continuous deep networks.

Estimated Energy Consumption (Joules)  
Assumption: ≈ 15 pJ per FLOP (typical modern accelerator)

| Sequence Length \(N\) | Classical Attention (J) | Thinnest-Triangle / 30-Fold (J) | Energy Saving Factor |
|-----------------------|--------------------------|----------------------------------|----------------------|
| 512                   | 0.001007                 | 0.000002                         | 512×                 |
| 1 024                 | 0.004027                 | 0.000004                         | 1 024×               |
| 2 048                 | 0.016106                 | 0.000008                         | 2 048×               |
| 4 096                 | 0.064425                 | 0.000016                         | 4 096×               |
| 8 192                 | 0.257698                 | 0.000031                         | 8 192×               |
| 16 384                | 1.030792                 | 0.000063                         | 16 384×              |
| 32 768                | 4.123169                 | 0.000126                         | 32 768×              |

The table shows that the 97.75 % signal-power retention of the Thinnest-Triangle architecture is delivered at an energy cost that scales only linearly with sequence length, producing energy savings that grow exactly with \(N\).
