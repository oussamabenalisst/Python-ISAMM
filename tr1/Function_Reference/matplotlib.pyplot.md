# Référence des fonctions matplotlib.pyplot

Ce document donne une référence concise et orientée « signatures » pour les fonctions de `matplotlib.pyplot` couramment utilisées dans `son.ipynb`.

---

## Table des matières

- `plt.plot`
- `plt.scatter`
- `plt.grid`
- `plt.xlabel` / `plt.ylabel`
- `plt.title`
- `plt.legend`
- `plt.xlim` / `plt.ylim`
- `plt.show`
- `plt.figure` / `plt.subplots`
- `plt.colorbar`

---

## plt.plot(x, y=None, fmt='', \*\*kwargs)

- Signature simplifiée : `plot(*args, **kwargs)` — l'appel peut être : `plot(x, y, fmt, **kwargs)` ou `plot(y)`.
- Paramètres importants :
  - `x`, `y` : array-like. Si seul `y` est fourni, `x` est implicite `range(len(y))`.
  - `fmt` : chaîne de format pour couleur/linestyle/marker (ex. `'r--'`).
  - `color`, `linestyle`, `marker`, `linewidth`, `markersize`, `alpha`, `label`.
  - `drawstyle` : `'default'`, `'steps'`, etc.
- Retour : liste d'objets `Line2D`.
- Remarques : relie par défaut les points par segments ; `out` n'existe pas (utiliser `Line2D` pour modifications avancées).

---

## plt.scatter(x, y, s=None, c=None, cmap=None, marker=None, norm=None, vmin=None, vmax=None, \*\*kwargs)

- Paramètres clés :
  - `x`, `y` : coordonnées (array-like).
  - `s` : taille (float ou array-like) en points^2.
  - `c` : couleur ou valeurs numériques (array-like) mappées via `cmap`.
  - `cmap` : colormap si `c` est numérique.
  - `marker`, `alpha`, `edgecolors`, `linewidths`.
- Retour : `PathCollection`.
- Remarques : adapté pour color/taille par point ; coûteux pour très grands jeux de points.

---

## plt.grid(b=True, which='major', axis='both', \*\*kwargs)

- Paramètres :
  - `b` : bool ou None (toggle).
  - `which` : `'major'`, `'minor'`, `'both'`.
  - `axis` : `'both'`, `'x'`, `'y'`.
  - `linestyle`, `color`, `linewidth`, `alpha` transmis aux lignes de grille.
- Retour : None (modifie l'axe courant).

---

## plt.xlabel(s, **kwargs) / plt.ylabel(s, **kwargs)

- Paramètres :
  - `s` : chaîne (label).
  - `fontdict`, `labelpad`, `fontsize`, `color` parmi autres.
- Retour : `Text` (objet texte créé).

---

## plt.title(s, \*\*kwargs)

- Paramètres :
  - `s` : chaîne du titre.
  - `loc` : `'left'|'center'|'right'`.
  - `pad`, `fontsize`, `fontdict`.
- Retour : `Text`.

---

## plt.legend(\*\*kwargs)

- Paramètres courants :
  - `loc` : position (string ou tuple), ex. `'best'`, `'upper right'`.
  - `ncol`, `frameon`, `fontsize`, `title`, `bbox_to_anchor`.
- Retour : `Legend` (objet).

---

## plt.xlim(left=None, right=None) / plt.ylim(bottom=None, top=None)

- Usage :
  - `plt.xlim( xmin, xmax )` fixe les limites ; sans arguments retourne `(xmin, xmax)`.
  - `plt.ylim( bottom, top )` analogue.
- Retour : tuple de limites si appel en lecture.

---

## plt.show(block=None)

- Paramètres :
  - `block` : bool ou None. Contrôle le blocage dans les scripts (Jupyter gère l'affichage automatiquement).
- Retour : None (affiche les figures et, selon le backend, peut bloquer).

---

## plt.figure(**kwargs) / plt.subplots(nrows=1, ncols=1, **kwargs)

- `plt.figure(**kwargs)` : crée une nouvelle figure.
  - arguments clés : `figsize=(w,h)`, `dpi`, `facecolor`, `edgecolor`.
- `plt.subplots(nrows=1, ncols=1, **kwargs)` : crée figure et axes.
  - Retour : `(fig, ax)` ou `(fig, axs)` selon `nrows/ncols`.
  - `sharex`, `sharey`, `gridspec_kw` sont des options fréquentes.

---

## plt.colorbar(mappable=None, \*\*kwargs)

- Paramètres :
  - `mappable` : objet issu d'un `ScalarMappable` (ex. `PathCollection` retourné par `scatter` ou `AxesImage`).
  - `orientation` : `'vertical'` (par défaut) ou `'horizontal'`.
  - `shrink`, `pad`, `aspect`, `label`.
- Retour : `Colorbar`.

---

## Conseils synthétiques

- Préférer l'API orientée-objet (`fig, ax = plt.subplots()`) pour un contrôle fin.
- Pour de gros nuages de points, `plt.plot(x, y, '.')` peut être plus rapide que `scatter` si la coloration individuelle n'est pas nécessaire.
- Toujours préciser `label=` aux tracés et appeler `ax.legend()` ou `plt.legend()` quand plusieurs courbes existent.
- Pour export en haute qualité : `fig.savefig(..., dpi=300, bbox_inches='tight')`.

---

Fichier : `python/tr1/Function_Reference/matplotlib.pyplot.md` — version signaturée et centrée sur les paramètres. Si vous voulez que j'ajoute :

- courtes notes sur les types d'objets retournés (`Line2D`, `PathCollection`, `Text`, `Legend`, `Colorbar`),
- ou une version condensée en arabe, je peux l'ajouter.
