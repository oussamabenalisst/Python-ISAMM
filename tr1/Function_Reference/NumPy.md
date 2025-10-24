# Référence des fonctions NumPy (signatures et paramètres)

Ce document fournit, en français, les signatures, paramètres importants, valeurs de retour et remarques pour les fonctions NumPy demandées. L'objectif est une référence technique (pas d'exemples applicatifs détaillés).

---

## Table des matières

- Création et conversion de tableaux : `np.array`, `ndarray.astype`
- Vecteurs temps et échantillonnage : `np.arange`, `np.linspace`, `np.pi`
- Opérations élémentaires (ufuncs) : `np.sin`, `np.cos`, `np.exp`, `np.abs`
- Statistiques et agrégations : `np.sum`, `np.mean`, `np.std`, `np.var`, `np.min`, `np.max`, `np.argmin`, `np.argmax`
- Manipulation d'axes et produit matriciel : `.T`, `np.dot`
- Indexation, slicing et Boolean indexing
- Masquage : `numpy.ma.masked_array`
- Gestion des NaN : `np.isnan`, `np.nanmean`
- Génération aléatoire : `np.random.randn`
- Broadcasting (règles)
- Transformée de Fourier (FFT) : `np.fft.fft`, `np.fft.fftfreq`, `np.fft.rfft`

---

## Création et conversion de tableaux

- np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

  - object : iterable (liste, tuple, nested lists) ou autre array-like.
  - dtype : type souhaité (ex. `float`, `np.int16`, `np.complex64`). Si None, NumPy infère.
  - copy : bool, si True force la copie.
  - order : `'C'`, `'F'`, `'A'`, `'K'` (préférence d'ordre mémoire).
  - subok : si True et object est un ndarray sub-classé, on retourne la sous-classe.
  - ndmin : force un nombre minimal de dimensions.
  - Retour : un `ndarray` avec attributs `shape`, `dtype`, `strides`, `ndim`.

- ndarray.astype(dtype, order='K', casting='unsafe', subok=False, copy=True)
  - dtype : type cible (ex. `np.float64`).
  - order, casting, subok, copy : contrôlent le comportement de conversion.
  - Retour : un nouveau tableau (ou la même instance si conversion non nécessaire et `copy=False`).

---

## Vecteurs temps et échantillonnage

- np.arange([start,] stop[, step,], dtype=None)

  - start, stop, step : comme en Python, `step` peut être float.
  - dtype : type du résultat (optionnel).
  - Remarque : en floats, des erreurs d'arrondi rendent `arange` moins adapté quand on veut un nombre précis d'échantillons.

- np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

  - start, stop : bornes.
  - num : nombre entier d'échantillons (précis).
  - endpoint : inclure `stop` si True.
  - retstep : renvoyer aussi le pas réel.
  - dtype : type du résultat.

- np.pi
  - Constante scalaire représentant π (float).

---

## Opérations élémentaires (ufuncs)

Les ufuncs sont des fonctions vectorisées (implémentées en C). Elles acceptent en général :

- x (array_like) : entrée
- out (optionnel) : tableau de sortie
- where (optionnel) : masque booléen

- np.sin(x, /, out=None, where=True, \*\*kwargs)
- np.cos(x, /, out=None, where=True, \*\*kwargs)
- np.exp(x, /, out=None, where=True, \*\*kwargs)
- np.abs(x, /, out=None, where=True, \*\*kwargs)
  - x : array-like (float ou complex selon l'ufunc).
  - out : optionnel, écrire le résultat dans un tableau préalloué.
  - where : masque boolean pour appliquer l'opération partiellement.
  - Retour : ndarray de la même forme que `x`.

Remarque : ufuncs supportent le broadcasting et sont optimisées pour éviter les boucles Python.

---

## Statistiques et agrégations

- np.sum(a, axis=None, dtype=None, out=None, keepdims=False)
- np.mean(a, axis=None, dtype=None, out=None, keepdims=False)
- np.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)
- np.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)
- np.min(a, axis=None, out=None, keepdims=False)
- np.max(a, axis=None, out=None, keepdims=False)
- np.argmin(a, axis=None)
- np.argmax(a, axis=None)

Paramètres communs :

- a : array_like d'entrée.
- axis : int ou tuple d'int, dimension(s) sur lesquelles réduire.
- dtype : type du résultat (utile pour accumulation pour éviter overflow).
- out : emplacement pour écrire le résultat (gain mémoire).
- keepdims : conserve les axes réduites (taille 1) pour la compatibilité d'axes.
- ddof : degrés de liberté (pour variance/écart-type).

Retour : scalaire ou ndarray réduit selon `axis`.

---

## Manipulation d'axes et produit matriciel

- `.T` / `ndarray.transpose(*axes)`

  - `.T` : raccourci pour `transpose()` qui inverse l'ordre des axes.
  - `transpose(*axes)` : permute les axes selon l'ordre fourni.
  - Ceci renvoie souvent une vue (pas de copie) ; vérifier `arr.flags['C_CONTIGUOUS']`/`strides` si une copie est créée.

- np.dot(a, b) / a.dot(b)
  - a, b : array_like. Comportement dépend des dimensions :
    - 1-D \* 1-D -> produit scalaire.
    - 2-D \* 2-D -> produit matriciel.
    - N-D : somme sur dernières dimensions compatibles.
  - Retour : ndarray résultant de la multiplication.
  - Note : l'opérateur `@` réalise la multiplication matricielle et est équivalent pour 2-D.

---

## Indexation, slicing et Boolean indexing

- Slicing standard : `arr[start:stop:step]` (vue si possible).
- Indexation multi-dimensionnelle : `A[i, j]`, `A[:, 1:3]`.
- Fancy indexing : `A[[0,2,5]]` retourne une copie (pas une vue).
- Boolean indexing : `A[A < 5]` sélectionne éléments ; l'affectation `A[A < 5] = val` modifie l'original.

Vue vs Copie :

- Slices -> vues quand c'est possible (partage de mémoire via `strides`).
- Fancy indexing et masques -> copies.

---

## Masquage : `numpy.ma.masked_array`

- numpy.ma.masked_array(data, mask=None, dtype=None, copy=True, fill_value=None)
  - data : array-like source.
  - mask : bool array-like ; True = valeur masquée.
  - dtype, copy : même sémantique que pour ndarray.
  - fill_value : valeur de remplissage pour affichage/écriture.
  - Retour : `MaskedArray` qui surchage les opérations pour ignorer les éléments masqués.

Remarque : utile pour représenter des données manquantes tout en conservant des types non-float (ex. entiers).

---

## Gestion des NaN

- np.isnan(x)

  - x : array_like.
  - Retour : mask booléen de même forme indiquant les NaN.

- np.nanmean(a, axis=None, dtype=None, out=None, keepdims=False)
  - Variante de mean qui ignore les NaN.
  - Il existe `np.nansum`, `np.nanstd`, `np.nanvar` pour opérations analogues.

Remarque : remplacer NaN (`a[np.isnan(a)] = valeur`) modifie l'array en place.

---

## Génération aléatoire

- np.random.randn(\*d0)
  - Paramètres : dimensions positionnelles (ex. `np.random.randn(3,4)` pour shape=(3,4)).
  - Retour : ndarray d'échantillons depuis une loi normale centrée réduite N(0,1).
  - Remarque : pour un usage moderne et reproductible, préférer `rng = np.random.default_rng(seed)` puis `rng.standard_normal(size)`.

---

## Broadcasting (règles principales)

1. Les formes sont alignées à droite.
2. Deux dimensions sont compatibles si elles sont égales ou si l'une d'elles vaut 1.
3. Si une dimension vaut 1, elle est étendue virtuellement pour correspondre à l'autre.

Conséquence : opérations élément-par-élément entre arrays de formes (m,n) et (n,) sont possibles sans copie.

---

## Transformée de Fourier (FFT)

- np.fft.fft(x, n=None, axis=-1, norm=None)

  - x : array_like (typ. float ou complex).
  - n : int (longueur de la FFT). Si fourni, effectue zero-pad ou tronque.
  - axis : axe le long duquel calculer la FFT.
  - norm : normalisation (`None` ou `'ortho'`).
  - Retour : ndarray complexe contenant les coefficients de la DFT.

- np.fft.fftfreq(n, d=1.0)

  - n : nombre de points (int).
  - d : intervalle d'échantillonnage (float), ex. 1/fs.
  - Retour : vecteur de fréquences (positives et négatives) correspondant aux indices de la FFT.

- np.fft.rfft(x, n=None, axis=-1, norm=None)
  - Optimisée pour signaux réels ; retourne uniquement la partie non redondante (fréquences >= 0).
  - Pour `x` réel de taille N, la sortie a taille `N//2 + 1`.

Remarques :

- Choisir `n` et appliquer une fenêtre modifie résolution/fréquence et leakage.
- Attention au scaling (multiplication par 1/N) selon convention d'analyse.

---

## Notes de performance et bonnes pratiques

- Vérifier `arr.dtype` avant opérations numériques coûteuses (prévenir overflow, choisir float32 vs float64).
- Minimiser les copies : utiliser vues, `out=` et `memmap` pour grands jeux de données.
- Pour l'algèbre linéaire lourde, NumPy délègue à BLAS/LAPACK ; la configuration du runtime (mkl/openBLAS) impacte la vitesse.

---

Fichier : `python/tr1/Function_Reference/NumPy.md` — cette version fournit les signatures et paramètres demandés. Dites-moi si vous voulez :

- ajouter un petit exemple minimal pour chaque entrée, ou
- une traduction en arabe, ou
- extraire cette documentation dans un PDF ou README plus concis.
