# Référence et analyse des fonctions NumPy utilisées

Ce document fournit une explication détaillée (en français) des fonctions NumPy employées dans les notebooks `son.ipynb` et `TP1_NumPy.ipynb`. Pour chaque fonction ou motif d'utilisation, vous trouverez : le rôle, les arguments importants, un exemple tiré des scripts, et des conseils pratiques.

---

## Table des matières

- Création et conversion de tableaux : `np.array`, `astype`
- Vecteurs temps et échantillonnage : `np.arange`, `np.linspace`, `np.pi`
- Opérations élémentaires et fonctions mathématiques : `np.sin`, `np.cos`, `np.exp`, `np.abs`
- Statistiques et agrégations : `np.sum`, `np.mean`, `np.std`, `np.var`, `np.min`, `np.max`, `np.argmin`, `np.argmax`
- Manipulation d'axes et produit matriciel : `.T`, `dot`
- Indexation, slicing et Boolean indexing
- Masquage : `numpy.ma.masked_array`
- Gestion des NaN : `np.isnan`, `np.nanmean`
- Génération aléatoire : `np.random.randn`
- Broadcasting
- Transformée de Fourier (FFT) : `np.fft.fft`, `np.fft.fftfreq` et `np.fft.rfft` (remarque)

---

## Création et conversion de tableaux

- np.array(obj, dtype=None)
  - Rôle : créer un tableau NumPy à partir d'une liste, liste de listes, etc.
  - Exemples des scripts :

```python
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
```

- Conseils : préciser dtype si nécessaire (ex. `np.array(..., dtype=float)`) pour éviter les conversions implicites.

- array.astype(dtype)
  - Rôle : convertir le type d'un tableau (ex. int16 -> float) avant calculs/FFT.
  - Exemple conseillé : `x = x.astype(float)` avant `np.fft` si `x` est entier.

---

## Vecteurs temps et échantillonnage

- np.arange(start, stop, step)
  - Rôle : génère une séquence start + n\*step tant que la valeur est < stop (stop exclu).
  - Usage dans `son.ipynb` :

```python
fs = 44100
Ts = 1 / fs
t = np.arange(0, 2, Ts)  # échantillons de 0 à (presque) 2s
```

- Piège : pour les floats, la borne supérieure peut ne pas être exactement incluse à cause des erreurs d'arrondi. Si vous voulez un nombre précis d'échantillons, préférez `np.linspace`.

- np.linspace(start, stop, num, endpoint=True/False)
  - Rôle : génère exactement `num` valeurs uniformes entre `start` et `stop`. `endpoint=False` exclut la dernière valeur.
  - Exemples :

```python
t = np.linspace(0, 2, int(2*fs), endpoint=False)  # exactement 2*fs échantillons
te = np.linspace(0, Durée, N)  # utilisé pour construire les instants d'échantillonnage
```

- np.pi
  - Constante π; utilisée dans toutes les formules trigonométriques : `2*np.pi*f*t`.

---

## Opérations élémentaires et fonctions mathématiques

- np.sin(x), np.cos(x), np.exp(x), np.abs(x)
  - Rôle : fonctions mathématiques élémentaires vectorisées. Elles acceptent scalaires ou tableaux et retournent un tableau de même forme.
  - Exemples tirés des notebooks :

```python
x = 0.5 * np.cos(2 * np.pi * 500 * t + np.pi/2)
def x(t):
    return np.sin(2*np.pi*t)
y = np.exp(A)
```

- Rappel : les fonctions trigonométriques attendent des angles en radians. Pour des degrés, utiliser `np.deg2rad()`.

---

## Statistiques et agrégations

- np.sum, np.mean, np.std, np.var, np.min, np.max
  - Rôle : calculs d'agrégats sur un tableau. Acceptent un argument `axis` pour réduire selon une dimension.
  - Exemples :

```python
total = A.sum()
col_sum = A.sum(axis=0)
row_mean = A.mean(axis=1)
stdev = A.std()
```

- np.argmin, np.argmax

  - Rôle : index du minimum / maximum. Avec `axis` on peut obtenir indices selon une dimension.
  - Exemples : `A.argmin()`, `A.argmax(axis=1)`

- np.corrcoef
  - Rôle : matrice de corrélation. Exemple : `np.corrcoef(A)`.

---

## Manipulation d'axes et produit matriciel

- `.T` (transpose)

  - Exemple : `A2.T` retourne la matrice transposée.

- dot / np.dot
  - Rôle : produit matriciel. Exemple : `A2.dot(B2)` ou `np.dot(A2, B2)`.

---

## Indexation, slicing et Boolean indexing

- Slicing : `arr[start:stop:step]` et multi-dimension : `A[0:2, 1:3]`, `A[:,1]`
  - Exemples dans TP1 :

```python
A[0:2, 1:3]
A[:, -1]
A[:, 1:2]
```

- Boolean indexing : `A[A < 5] = 10` remplace les éléments satisfaisant la condition.
  - Exemple :

```python
A_bool = A.copy()
A_bool[A_bool < 5] = 10
```

Conseil : les opérations de masquage/modification sont in-place sur la copie uniquement si vous faites `.copy()`.

---

## Masquage avec numpy.ma

- numpy.ma.masked_array(data, mask=...)
  - Rôle : créer un tableau masqué pour ignorer certaines valeurs lors des calculs (somme, moyenne, etc.).
  - Exemple :

```python
import numpy.ma as ma
arr = np.array([1,2,3,4,5,6,7,8])
ma_arr = ma.masked_array(arr, mask=[False,False,False,True,True,True,False,False])
ma_arr.sum()  # somme en ignorant les valeurs masquées
```

---

## Gestion des NaN

- np.isnan(x) : renvoie un masque booléen des NaN.
- np.nanmean(x) : calcul de la moyenne en ignorant les NaN (idem pour `nanstd`, `nansum`, ...).
- Remarque : remplacer les NaN par une valeur (ex. `x[np.isnan(x)] = 0.5`) si vous voulez poursuivre les calculs sans NaN.

---

## Génération aléatoire

- np.random.randn(m, n)
  - Rôle : génère des échantillons depuis une loi normale standard (m x n).
  - Exemple dans TP1 : `B = np.random.randn(5,5)` puis insertion de NaN et traitement.

---

## Broadcasting

- Rôle : mécanisme qui permet d'appliquer des opérations entre tableaux de formes différentes sans copie explicite si les dimensions sont compatibles.
  - Exemple simple : `A + 2` ajoute 2 à toutes les entrées de `A`.
  - Conseil : connaître les règles de broadcasting (une dimension de taille 1 peut être étendue pour correspondre à l'autre).

---

## Transformée de Fourier (FFT)

- numpy.fft.fft(x) et numpy.fft.fftfreq(n, d)
  - Rôle : calculer la transformée de Fourier discrète et le vecteur de fréquences associé.
  - Exemple dans `son.ipynb` :

```python
from numpy.fft import fft, fftfreq
X = fft(x)
freq = fftfreq(x.size, d=1/rate)
N = x.size
X_abs = np.abs(X[:N//2]) * 2.0 / N
freq_pos = freq[:N//2]
```

- Remarques pratiques :
  - Si `x` est réel, on affiche seulement `[:N//2]` (fréquences positives).
  - Pour signaux réels, `np.fft.rfft` et `np.fft.rfftfreq` sont plus efficients et évitent le slicing manuel.
  - Avant la FFT, convertir `x` en float et envisager l'application d'une fenêtre (Hann/Hamming) pour réduire la fuite spectrale.

---

## Conseils généraux et bonnes pratiques

- Toujours vérifier le dtype des tableaux (`arr.dtype`) surtout avant la FFT ou des divs.
- Préférer `np.linspace(..., endpoint=False)` quand vous comptez un nombre fixe d'échantillons (audio), pour éviter des imprécisions d'arange.
- Documenter `fs`, `Ts`, `N`, `t` dans vos scripts pour garder la cohérence des unités (Hz, s, échantillons).
- Utiliser l'API orientée-objet de Matplotlib (`fig, ax = plt.subplots()`) conjointement avec NumPy pour des figures reproductibles.
