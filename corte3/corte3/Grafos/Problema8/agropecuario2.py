from os import system


# Una clase para representar un conjunto disjunto
class DisjointSet:
    parent = {}
 
    # realiza la operación MakeSet
    def makeSet(self, n):
        # crear `n` conjuntos disjuntos (uno para cada vértice)
        for i in range(n):
            self.parent[i] = i
 
    # Encuentra la raíz del conjunto al que pertenece el elemento `k`
    def find(self, k):
        # si `k` es root
        if self.parent[k] == k:
            return k
 
        # recurre para el padre hasta que encontramos la raíz
        return self.find(self.parent[k])
 
    # Realizar unión de dos subconjuntos
    def union(self, a, b):
        # encontrar la raíz de los conjuntos a los que pertenecen los elementos `x` e `y`
        x = self.find(a)
        y = self.find(b)
 
        self.parent[x] = y
 
 
# Función # para construir MST usando el algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
 
    # almacena los bordes presentes en MST
    MST = []
 
    # Inicializa la clase `DisjointSet`.
    # Crea un conjunto singleton para cada elemento del universo.
    ds = DisjointSet()
    ds.makeSet(n)
 
    index = 0
 
    # ordena los bordes aumentando el peso
    edges.sort(key=lambda x: x[2])
 
    # MST contiene exactamente aristas `V-1`
    while len(MST) != n - 1:
 
        # considerar el borde siguiente con peso mínimo del graph
        (src, dest, weight) = edges[index]
        index = index + 1
 
        # encontrar la raíz de los conjuntos a los que se unen dos extremos
        # vértices de la siguiente arista pertenecen
        x = ds.find(src)
        y = ds.find(dest)
 
        # si ambos extremos tienen diferentes padres, pertenecen a
        # diferentes componentes conectados y se pueden incluir en MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)
 
    return MST
 
 

 
# (u, v, w) el triplete representa un borde no dirigido desde
# vértice `u` a vértice `v` con peso `w`
edges = [(0, 1, 150), (0, 4, 150), (0, 5, 300), (1, 2, 250), (2, 5, 200), (2, 3, 150), (3, 5, 400), (3, 6, 300), (4, 5, 250), (6, 5, 250)]

nodos = ["A", "B", "C", "D", "E", "F", "G"]
animales = [20, 10, 5, 10, 30, 25, 50]

#número total de nodos en el graph (etiquetados de 0 a 6)
n = 7
 
# arbol de recorrido minimo
arbol_aristas = runKruskalAlgorithm(edges, n)


while(True):
    system("clear")
    print("               Sistema de control de potreros")
    print("1) Mostrar ruta mínima.")
    print("2) Calcular suministro total.")
    print("3) Calcular suministro por potrero.")
    print("4) Salir")

    opcion = int(input("Elija una opción: "))

    print()

    while(opcion < 0 or opcion > 4):
        print("Ingrese una opcion correcta")
        opcion = int(input("Elija una opción: "))

    if(opcion == 1):
        for arista in arbol_aristas:
            print("Puedes ir desde el potreto", nodos[arista[0]], "hasta", nodos[arista[1]], "que tiene una distancia de", arista[2])
        opcion = input("Presione enter para continuar")
    
    if(opcion == 2):
        suministro_total = 0
        for animal in animales:
            suministro_total += animal * 120
        
        print("El suministro total es de " + str(suministro_total) + "gr")
        opcion = input("Presione enter para continuar")
    
    if(opcion == 3):
        for potrero in range(len(nodos)):
            print("Potrero " + str(nodos[potrero]) + ": " + str(animales[potrero]*120) + "gr")
        
        opcion = input("Presione enter para continuar")

    if(opcion == 4):
        break;