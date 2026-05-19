# 📖 Human-to-Logic Dictionary

A quick translation guide from everyday English requirements into formal logic and set theory.

| Human Expression / Requirement | Concept | Logical / Set Translation |
|:---|:---|:---|
| **"A happens if and only if B happens"** | Biconditional | $A \leftrightarrow B$ |
| **"A is a sub-category of B"** | Subset | $A \subseteq B$ |
| **"All items / Every item must..."** | For All | $\forall x$ |
| **"At least one item..."** | Exists | $\exists x$ |
| **"Both A and B must be true"** | AND | $A \land B$ |
| **"Combine groups A and B"** | Union | $A \cup B$ |
| **"Either A or B (can be both)"** | OR (Inclusive) | $A \lor B$ |
| **"Either A or B (strictly one, not both)"** | XOR (Exclusive) | $A \oplus B$ |
| **"Everything except A"** | Complement / NOT | $A^c$ or $\neg A$ |
| **"Exactly one item..."** | Unique Existential | $\exists! x$ |
| **"If A happens, then B must happen"** | Implication | $A \rightarrow B$ |
| **"Is a member of / belongs to category A"** | Element of | $x \in A$ |
| **"Is NOT a member of category A"** | Not Element of | $x \notin A$ |
| **"Items in A, but exclude items in B"** | Difference | $A - B$ |
| **"Neither A nor B"** | NOR | $\neg(A \lor B)$ which is $\neg A \land \neg B$ |
| **"Not A / The opposite of A"** | NOT | $\neg A$ |
| **"Only items common to both A and B"** | Intersection | $A \cap B$ |

---

### 💡 Complex Translation Examples 

Sometimes humans combine these requirements. Here is how they break down:

* **"If a user is an Admin, they can Edit or Delete, but not both at the same time."**
  * $Admin \rightarrow (Edit \oplus Delete)$
* **"All items in the cart must be either Digital or Physical."**
  * $\forall x \in Cart: x \in Digital \lor x \in Physical$
* **"At least one user has Administrator rights."**
  * $\exists x: x \in Administrators$