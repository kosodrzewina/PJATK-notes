# relations

A relation $R$ on a set $X$ is a subset of $X \times X$ ( $R \subseteq X \times X$)

$(a,b) \in R \equiv aRb \equiv a \sim b$

Defining the equality symbol as a set: $EQ = \{(x, x): x \in X\}$

$\leq LTE$

$\lt LT$

$= EQ$

$LTE = LT \cup EQ$

#### properties of relations

1. Reflexivity: $(\forall x \in X)(x \sim x)$
2. Symmetricity: $(\forall x,y \in X)(x \sim y \implies y \sim x)$
3. Transitivity: $(\forall x,y,z \in X)(x \sim y \land y \sim z \implies x \sim z)$
4. Antisymmetricity: $(\forall x,y \in X)(x \sim y \land y \sim x \implies x=y)$

#### equivalence relations

$R \subseteq X \times X$ is said to be an equivalence relation iff $R$ is reflexive, symmetric and transitive.

The equivalence class of an element $x \in X$ is the set $[x]_\sim = \{ y \in X: x \sim y\}$

1. Every $x \in X$ belongs to the equivalence class of some element $a$
2. $(\forall x, y \in X)([x] \cap [y] \neq \emptyset \iff [x] = [y])$

#### partitions

A partition is a set containing subsets of some set $X$ such that their collective symmetric difference equals to $X$. A partition of $X$ is a set $\{A_i: i \in I \land A_i \subseteq X\}$ such that:

1. $(\forall x \in X)(\exists j \in I)(x \in A_j)$
2. $(\forall i, j \in I)(i \neq j \implies A_i \cap A_j = \emptyset)$