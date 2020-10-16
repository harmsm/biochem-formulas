## Summary of formulas and constants used in biochemistry

### Constants

$$R=0.008314\ kJ\cdot mol^{-1}\cdot K^{-1}$$
$$T\ in\ K=T\ in\ ^{\circ}C+273.15$$

### Free energy

$$\Delta G = \Delta H - T \Delta S$$

### Free energy and concentration:

$$aA+bB\rightleftarrows cC+dD$$
$$\Delta G=\Delta G^{\circ\prime}+RTln\left(\frac{[C]^{c}[D]^{d}}{[A]^{a}[B]^{b}}\right)$$
$$\Delta G^{\circ\prime}=-RTln\left(K_{eq}\right)=-RTln\left(\frac{[C]_{eq}^{c}[D]_{eq}^{d}}{[A]_{eq}^{a}[B]_{eq}^{b}}\right)$$

The standard state condition is defined as all products and reactants at 1 M, 25C, 1 atm pressure, pH 7.0.  

### Binding

For the reaction:

$$M + X \rightleftarrows M \cdot X$$
$$K_{eq} = K_{association} = K_{a} = \frac{[M \cdot X]}{[M][X]}$$

You can write this reaction as a dissociation reaction as well (generally preferred by biochemists)

$$M \cdot X \rightleftarrows M + X$$
$$K_{eq} = K_{dissociation} = K_{D} = \frac{[M][X]}{[M \cdot X]}$$

Written this way, $K_{D}$ has units of concentration and thus measures the concentration at which the reaction will be 50% bound and 50% unbound.

$$\theta = \frac{[MX]}{[M] + [MX]} = \frac{1}{1 + K_{D}/[X]}$$

### pH:

Note: $K_{a}$ is an *acid* constant, and thus a $K_{D}$ (dissociation constant).

$$M\cdot H\stackrel{K_{a}}{\rightleftarrows}M+H^{+}$$
$$K_{a}=\frac{[M][H^{+}]}{[M\cdot H]}$$
$$pH=-log_{10}\left([H^{+}]\right);\ pK_{a}=-log_{10}\left(K_{a}\right)$$
$$\theta=\frac{[M\cdot H]}{[M]+[M\cdot H]}=\frac{1}{1+K_{a}/[H^{+}]}=\frac{1}{1+10^{\left(pH-pK_{a}\right)}}$$

### Cooperative binding

For the cooperative binding reaction:

$$MX_{n} \rightleftarrows [M] + n[X]$$

$$\theta_{n} = \frac{[MX_{n}]}{[M] + \Sigma_{i=1}^{i=n} [MX_{i}]}$$
$$\theta = \frac{1}{1 + \big ( \frac{K_{D}}{[X]} \big )^{n}}$$


where $n$ is the number of cooperating sites.

### Enzyme activity

For a reaction

$$aA + bB \rightleftarrows C$$

The rate of the forward reaction is given by:

$$d[C]/dt = k \times [A]^{a} \times [B]^{b}$$


### Michaelis-Menten kinetics

$$E+S\stackrel[k_{-1}]{k_{1}}{\rightleftarrows}ES\overset{k_{cat}}{\rightarrow}P$$
$$V_{0} = \Big ( \frac{1}{1 + \frac{K_{M}}{[S]_{0}}} \Big ) k_{cat} [E]_{tot}$$
$$V_{max} = k_{cat} [E]_{tot}$$
$$K_{M} = \frac{k_{-1}+k_{cat}}{k_{1}}$$

