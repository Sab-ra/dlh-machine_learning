# ✍️ Logical & Set Operators

> The symbols below use standard LaTeX & KaTeX math formatting (e.g., `$\land$` for $\land$ **( ∧ )**), meaning you don't need to memorize difficult Alt codes or Hex inputs to type them!

---

#### 🧾 QUICK CHEAT SHEET

| LaTeX | Symbol | Concept | Meaning |
|:---:|:---:|:---|:---|
|`$\neg$`| $\neg$ | NOT | Flip the truth value |
|`$\land$`| $\land$ | AND or CONJUNCTION | Both must be true |
|`$\lor$`| $\lor$ | OR or DISJUNCTION | At least one is true |
|`$\oplus$`| $\oplus$ | XOR | Exactly one is true |
|`$\rightarrow$`| $\rightarrow$ | IMPLIES or IF | If A, then B |
|`$\leftrightarrow$`| $\leftrightarrow$ | BICONDITIONAL or IFF | Both match (if and only if) |
|`$\forall$`| $\forall$ | FOR ALL | Everything satisfies |
|`$\exists$`| $\exists$ | EXISTS | At least one satisfies |
|`$\exists!$`| $\exists!$ | UNIQUE | Exactly one satisfies |
|`$\in$ / $\notin$`| $\in$ / $\notin$ | BELONGS | Is / is not inside the group |
|`$\cup$`| $\cup$ | UNION | Combine everything |
|`$\cap$`| $\cap$ | INTERSECTION | Common elements |
|`$-$`| $-$ | DIFFERENCE | In A but not in B |
|`$\subseteq$ / $\subset$`| $\subseteq$ / $\subset$| SUBSET | A is inside B / strict subset |
|`$A^c$`| $A^c$ | COMPLEMENT | Everything outside A |
|`$\emptyset$`| $\emptyset$ | EMPTY SET | A set with no elements |
|`$U$`| $U$ | UNIVERSAL | The set of all possible elements |

---

## 🔷 PART 1: LOGIC MASTER TRUTH TABLE

Instead of separate tables, use this to compare all logical operators at a glance:

| $A$ | $B$ | $\neg A$ (NOT) | $A \land B$ (AND) | $A \lor B$ (OR) | $A \oplus B$ (XOR) | $A \rightarrow B$ (IMPLIES) | $A \leftrightarrow B$ (XNOR) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| F | F | ✅ | F | F | F | ✅ | ✅ |
| F | ✅ | ✅ | F | ✅ | ✅ | ✅ | F |
| ✅ | F | F | F | ✅ | ✅ | F | F |
| ✅ | ✅ | F | ✅ | ✅ | F | ✅ | ✅ |

**💡 De Morgan's Laws**
How NOT interacts with AND / OR:
- $\neg(A \land B) \equiv \neg A \lor \neg B$
- $\neg(A \lor B) \equiv \neg A \land \neg B$

---

## 🔷 PART 2: QUANTIFIERS

Quantifiers describe how many elements satisfy a property.

### FOR ALL ( $\forall$ )
Everything must satisfy the condition.
**🧠 Example:** $\forall x \in \mathbb{N}: x \ge 0$

### EXISTS ( $\exists$ )
At least one satisfies the condition.
**🧠 Example:** $\exists x \in \mathbb{N}: x = 2$

### UNIQUE EXISTENTIAL ( $\exists!$ ) *(New)*
Exactly one element satisfies the condition.
**🧠 Example:** $\exists! x \in \mathbb{N}: x + 5 = 6$ (Only $x = 1$ works).

---

## 🔷 PART 3: SET (GROUP) OPERATORS

Sets = groups of elements 📦

### FOUNDATIONS
- **Empty Set ( $\emptyset$ ):** The set containing nothing: `{}`.
- **Universal Set ( $U$ ):** Every possible element in the current context.

### BELONGING ( $\in$ and $\notin$ )
Is the element inside the group?
```text
A = {1, 2, 3}
2 ∈ A  (True)
5 ∉ A  (True)
```

### UNION ( $\cup$ )

Combine everything $+$ (NO duplicates)

```text
A = {1, 2}, B = {2, 3}
A ∪ B = {1, 2, 3}
```

### INTERSECTION ( $\cap$ )

Common elements 🤝.

```text
A = {1, 2}, B = {2, 3}
A ∩ B = {2}
```

### DIFFERENCE ( $-$ )

Elements in A but NOT in B.

```text
A = {1, 2, 3}, B = {2}
A - B = {1, 3}
```

### COMPLEMENT ( $A^c$ or $\lnot A$ )

Everything NOT in A (everything in $U$ except $A$).

```text
U = {1, 2, 3, 4}, A = {1, 2}
A^c = {3, 4}
```

### SUBSET ( $\subseteq$ ) & STRICT SUBSET ( $\subset$ )

- $A \subseteq B$: All of $A$ is in $B$ (they can be equal).
- $A \subset B$: All of $A$ is in $B$, but $B$ is strictly larger.

```text
A = {1, 2}, B = {1, 2, 3}
A ⊂ B (True)
```


---

# ✏️ FINAL MEMORY TRICK

- **Logic = truth values T (✅) or F**
- **Sets = groups 📦**
- **∧ = strict**
- **∨ = flexible**
- **∩ = overlap**
- **∪ = merge**
