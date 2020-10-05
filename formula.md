## Summary of formulas and constants used in biochemistry

[link to prettier pdf version](https://github.com/harmsm/biochem-formulas/raw/main/formula.pdf)

### Constants

$$R=0.008314\ kJ\cdot mol^{-1}\cdot K^{-1}$$
$$T\ in\ K=T\ in\ ^{\circ}C+273.15$$

### Free energy

$$\Delta G = \Delta H - T \Delta S$$

### Free energy and concentration:

$$aA+bB\rightleftarrows cC+dD$$
$$\Delta G^{\circ\prime}=-RTln\left(K_{eq}\right)=-RTln\left(\frac{[A]_{eq}^{a}[B]_{eq}^{b}}{[C]_{eq}^{c}[D]_{eq}^{d}}\right)$$
$$\Delta G=\Delta G^{\circ\prime}+RTln\left(\frac{[A]^{a}[B]^{b}}{[C]^{c}[D]^{d}}\right)$$

The standard state condition is defined as all products and reactants at 1 M, 25C, 1 atm pressure, pH 7.0.  

### Binding

For the reaction:

$$A + B \rightleftarrows A \cdot B$$
$$K_{eq} = K_{association} = K_{a} = \frac{[A \cdot B]}{[A][B]}$$

You can write this reaction as a dissociation reaction as well (generally preferred by biochemists)

$$A \cdot B \rightleftarrows A + B$$
$$K_{eq} = K_{dissociation} = K_{D} = \frac{[A][B]}{[A \cdot B]}$$

Written this way, $K_{D}$ has units of concentration and thus measures the concentration at which the reaction will be 50% bound and 50% unbound.


### pH:

$$M\cdot H\stackrel{K_{a}}{\rightleftarrows}M+H^{+}$$
$$K_{a}=\frac{[M][H^{+}]}{[M\cdot H]}$$
$$pH=-log_{10}\left([H^{+}]\right);\ pK_{a}=-log_{10}\left(K_{a}\right)$$
$$\theta=\frac{[M\cdot H]}{[M]+[M\cdot H]}=\frac{1}{1+K_{a}/[H^{+}]}=\frac{1}{1+10^{\left(pH-pK_{a}\right)}}$$

