# Algorithmes de Kruskal et de Borůvka

## Code source
Le code source est disponible dans le répertoire `source`.
Le fichier `UnionFind.py` implémente une structure de donnée utilisée pour les algorithmes.
Le fichier `MST.py` contient le code des algorithmes de Kruskal et de Borůvka.

## Rapport
Le rapport est disponible sous format pdf, il s'agit du fichier `Rapport.pdf`.

## Exemple et comparaison
Le dossier `example` contient deux notebook.
Le premier, `Comparaison.ipynb`, est utilisé pour générer le tableau disponible dans le rapport (ses sorties sont les fichiers `k_time.txt` et `b_time.txt`).
Le second, `Brussels.ipynb`, est un exemple d'utilisation où les algorithmes sont appliqués à un graphe généré à partir des stations de métro bruxelloises.
Pour cet exemple, il est nécessaire d'installer les packages listés dans le fichier `requirements.txt`.
Cela peut être fait avec la commande 
```sh
pip install -r requirements.txt
```

## Utilisation

Pour appliquer l'algorithme de Kruskal a un objet `g` de type `networkx.Graph`, il suffit d'utiliser la commande
```python
kruskal_sg(g)
```
du module `MST.py`. Pour appliquer l'algorithme de Borůvka, on peut utiliser
```python
boruvka_sg(g)
```
Si on travaille avec un objet de type `networkx.MiultiGraph`, on utilisera les commandes
```python
kruskal_mg(g)
```
et
```python
boruvka_mg(g)
```
Dans tous les cas, la fonction ne renvoie rien mais va attribuer à chaque arête une valeur booléenne qui indique si oui ou non l'arête fait partie du sous-arbre couvrant.
On peut accéder à la valeur de l'arête (u, v) avec la commande
```python
g[u][v]["spanning"]
```
dans le cas d'un graphe simple.
Pour un multigraphe, la commande
```python
g[u][v][m]["spanning"]
```
donne la valeur de l'arête (u, v, m).

## Clustering
Le dossier `clustering` contient une implémentation d'un algorithme de classement automatique, vu au cours de statistique.
Cet algorithme est très similaire à l'algorithme de Kruskal.
