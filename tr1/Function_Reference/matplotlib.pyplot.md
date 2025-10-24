# Référence des fonctions matplotlib.pyplot

Ce document explique les fonctions de `matplotlib.pyplot` employées dans `son.ipynb` : usage, arguments importants, retours et exemples courts.

---

## plt.plot(x, y, fmt=None, \*\*kwargs)

- But : tracer une courbe (ligne) reliant les points (x, y).
- Arguments importants :
  - `x`, `y` : arrays (ou scalars broadcastables).
  - `fmt` (optionnel) : chaîne de format (ex. `'r--'`, `'ok'`, `'-'`, `'.'`).
  - `color`, `linestyle`, `marker`, `linewidth`, `alpha`, `label`.
- Valeur de retour : liste d'objets `Line2D`.
- Remarques :
  - Par défaut relie les points par des segments droits.
  - Pour tracer uniquement des points densément, `plt.plot(x, y, '.')` est souvent plus rapide que `plt.scatter`.
- Exemple :
  ```python
  plt.plot(t, x, '--', color='C0', linewidth=1, label='Signal réel')
  ```

---

## plt.scatter(x, y, \*\*kwargs)

- But : diagramme de dispersion — chaque point indépendant, adapté pour colorer/taille par point.
- Arguments clés :
  - `s` : taille en area (points²), ex. `s=20`.
  - `c` : couleur (nom, code, ou tableau numérique pour colormap).
  - `cmap` : colormap si `c` est numérique, ex. `'viridis'`.
  - `marker`, `alpha`, `edgecolors`, `linewidths`.
- Valeur de retour : `PathCollection`.
- Remarques :
  - Permet carte de couleurs et échelle (`plt.colorbar()`).
  - Moins performant pour très grand nombre de points que `plt.plot(..., '.')`.
- Exemple :
  ```python
  plt.scatter(te, x_e, color='orange', label='Signal échantillonné', s=25, alpha=0.9)
  ```

---

## plt.grid(b=True, which='major', axis='both', \*\*kwargs)

- But : afficher ou masquer la grille sur la figure.
- Arguments utiles :
  - `b` : True/False pour activer/désactiver.
  - `which` : `'major'` / `'minor'` / `'both'`.
  - `axis` : `'both'` / `'x'` / `'y'`.
  - `linestyle`, `color`, `linewidth`, `alpha` possibles.
- Exemple :
  ```python
  plt.grid(True, linestyle='--', alpha=0.5)
  ```

---

## plt.xlabel(label, **kwargs) / plt.ylabel(label, **kwargs)

- But : définir l'étiquette de l'axe x / y.
- Arguments fréquents : `fontsize`, `labelpad`, `fontdict`.
- Exemple :
  ```python
  plt.xlabel("Temps (s)", fontsize=12)
  plt.ylabel("Amplitude", fontsize=12)
  ```

---

## plt.title(label, \*\*kwargs)

- But : ajouter un titre à la figure.
- Arguments utiles : `fontsize`, `loc` (`'left'|'center'|'right'`), `pad`.
- Exemple :
  ```python
  plt.title("Signal cosinus", fontsize=14)
  ```

---

## plt.legend(\*\*kwargs)

- But : afficher la légende (à partir de `label=` dans `plot`/`scatter`).
- Arguments courants :
  - `loc` : position (`'upper right'`, `'best'`, tuple, etc.).
  - `ncol`, `frameon`, `fontsize`, `title`, `bbox_to_anchor`.
- Exemple :
  ```python
  plt.legend(loc='upper right')
  ```

---

## plt.xlim(left, right) / plt.ylim(bottom, top)

- But : fixer (ou lire) les limites d'un axe.
- Usage :
  - Pour fixer : `plt.xlim(0, 6000)`.
  - Pour lire : `xmin, xmax = plt.xlim()`.
- Remarque : utile pour zoomer sur une plage de fréquences/temporelle.

---

## plt.show(block=None)

- But : afficher la/les figure(s) à l'écran.
- Notes :
  - Dans Jupyter, l'affichage est souvent automatique ; `plt.show()` force l'affichage et termine la figure courante.
  - `block` contrôlé dans scripts (bloquant/non-bloquant).
- Exemple :
  ```python
  plt.show()
  ```

---

## plt.figure(**kwargs) et plt.subplots(nrows=1, ncols=1, **kwargs)

- But : créer explicitement une figure (`plt.figure`) ou une figure+axes (`plt.subplots`) — meilleure pratique pour contrôle fin.
- Arguments utiles :
  - `figsize=(w,h)` en pouces, `dpi`.
  - Pour `subplots` : renvoie `(fig, ax)` ; on peut appeler `ax.plot(...)`, `ax.set_xlabel(...)`, `ax.grid(...)`.
- Avantage : API orientée-objet (réglages par ax) meilleure pour figures multiples ou exports.
- Exemple :
  ```python
  fig, ax = plt.subplots(figsize=(8,4))
  ax.plot(t, x)
  ax.set_xlabel("Temps (s)")
  ax.grid(True)
  ```

---

## plt.colorbar(mappable, \*\*kwargs)

- But : afficher une échelle des couleurs associée à un scatter ou image.
- Usage : `sc = plt.scatter(x, y, c=vals, cmap='viridis'); plt.colorbar(sc)`
- Arguments : `orientation`, `label`, `shrink`, `pad`.

---

## Conseils pratiques et bonnes pratiques

- Pour des signaux échantillonnés, utiliser `plt.plot(t, x, '.', markersize=...)` ou `plt.scatter` selon besoin de colormap.
- Pour publications, régler `plt.figure(figsize=(w,h), dpi=300)` et `ax.tick_params`.
- Préférer l'API orientée-objet (`fig, ax = plt.subplots()`) quand on manipule plusieurs axes ou veut réutiliser la figure.
- Pour grosses séries de points : `plt.plot(..., '.')` est plus performant que `plt.scatter`.
- Toujours ajouter `label=` et `plt.legend()` si plusieurs courbes doivent être distinguées.
- Pour gérer l'affichage du texte mathématique, utiliser des raw-strings LaTeX : `r"$x(t)$"`.

---

## Exemples courts rassemblés

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(t_dense, x_dense, '--', label='Signal réel', color='C0')
ax.scatter(te, x_e, color='orange', s=30, label='Échantillons')
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Échantillonnage d'un signal")
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
plt.xlim(0, 1)
plt.show()
```
