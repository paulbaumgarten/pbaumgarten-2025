# Computia Island — Map

**Print at A3 if possible. One per pair.**

---

## The Towns

| Town | Code | Notes |
|------|------|-------|
| Port Alpha | α | Start/Port — southwest coast |
| Betaville | β | Northwest |
| Gammaford | γ | Central-west |
| Delta Bay | δ | South coast |
| Epsilon | ε | Central |
| Zeta Heights | ζ | High ground, central-north |
| Etaville | η | Southeast coast |
| Theta Cross | θ | East, crossroads town |
| Iota | ι | Northeast |
| Kappa End | κ | Far north — destination |

---

## The Roads (distances in km)

| From | To | Distance |
|------|----|:--------:|
| Alpha (α) | Betaville (β) | 8 |
| Alpha (α) | Gammaford (γ) | 15 |
| Alpha (α) | Delta Bay (δ) | 12 |
| Betaville (β) | Gammaford (γ) | 6 |
| Betaville (β) | Epsilon (ε) | 10 |
| Gammaford (γ) | Epsilon (ε) | 7 |
| Gammaford (γ) | Zeta Heights (ζ) | 9 |
| Delta Bay (δ) | Etaville (η) | 14 |
| Epsilon (ε) | Zeta Heights (ζ) | 5 |
| Epsilon (ε) | Theta Cross (θ) | 11 |
| Zeta Heights (ζ) | Iota (ι) | 8 |
| Etaville (η) | Theta Cross (θ) | 6 |
| Theta Cross (θ) | Iota (ι) | 9 |
| Theta Cross (θ) | Kappa End (κ) | 13 |
| Iota (ι) | Kappa End (κ) | 7 |

---

## Map Diagram (ASCII — draw your own cleaner version if needed)

```
                        κ (Kappa End)
                       /|
                     7/ |13
                     /  |
              ι (Iota)  |
             /|      \  |
           8/ |9       θ (Theta Cross)
           /  |       /|
     ζ (Zeta) |    11/ |6
      |  \    |    /   |
     9|   \8  |   /    η (Etaville)
      |    \  |  /         |
     γ(Gamma) ε (Epsilon)  |14
      |  \   7/             |
    15|  6\ /               δ (Delta Bay)
      |    β (Betaville)   /
      |   /         \    /12
      |  /8           \  /
      α (Port Alpha) ──┘
```

---

## Useful Totals (Teacher Reference — do not share)

Shortest path Alpha to Kappa End:
- Via β→γ→ε→ζ→ι→κ: 8+6+7+5+8+7 = 41 km ✓
- Via α→γ→ε→ζ→ι→κ: 15+7+5+8+7 = 42 km
- Via α→β→ε→ζ→ι→κ: 8+10+5+8+7 = 38 km ✓ (shorter!)
- Via α→β→ε→θ→κ: 8+10+11+13 = 42 km

**Actual shortest: α→β→ε→ζ→ι→κ = 38 km**
