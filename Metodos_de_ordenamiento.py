import time, random

def numerosaleatorios():
    '''Genera una lista de diez mil numeros aleatorios'''
    v = []
    for i in range(1,1000):
           num = int(random.randint(1,500))
           v.append(num)
    return v
    
def calcularTiempo(metodo):
   def metodo_a_ejecutar(*argumentos):
       # Tiempo de inicio de ejecucion.
       t_inicial = time.time()
       # llamada al metodo a ejecutar.
       metodo(*argumentos)
       # Tiempo de fin de ejecucion.
       t_final = time.time()
       # Tiempo de ejecucion.
       tiempo_total = t_final - t_inicial
       # Devolvemos el tiempo de ejecucion.
       return tiempo_total
   # Devolvemos la funcion que se ejecuta.
   return metodo_a_ejecutar
    
def burbuja(v):
    """Metodo ordenamiento burbuja"""
    for i in range(len(v)-1):
        for j in range(len(v)-1):
            if(v[j] > v[j+1]):
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux


def ordenSeleccion(v):
    """Ordenamiento por seleccion"""
    for i in range(0,len(v)-1):
        min=i
        for j in range(i+1,len(v)):
            if v[min] > v[j]:
                min=j
        aux=v[min]
        v[min]=v[i]
        v[i]=aux


def quicksort(v,izq,der):
    """Metodo de ordenamiento QuickSort"""
    i=izq
    j=der
    x=v[(izq + der)/2]
    while( i <= j ):
        while v[i]<x and j<=der:
            i=i+1
        while x<v[j] and j>izq:
            j=j-1
        if i<=j:
            aux = v[i]; v[i] = v[j]; v[j] = aux;
            i=i+1;  j=j-1;
 
        if izq < j:
            quicksort( v, izq, j );
    if i < der:
        quicksort( v, i, der );


def HeapSort(A):
    def heapify(A):
        start = (len(A) - 2) / 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

    def siftDown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return
    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1


def shellSort(sample):
    """Metodo de ordenamiento shell"""
    length = len(sample)
    gap = int(length/2)
    while(gap >= 1):
     i = gap
     while(i < length):
      value = sample[i]
      j = i
      while(j-gap >= 0 and value < sample[j - gap]):
       sample[j] = sample[j - gap]
       j -= gap
      sample[j] = value
      i+=1
     gap = int(gap/2)
#     print("sorted sample=",sample)    
print("El tiempo en segundos de los metodos de ordenamiento es: \n")
t1 = calcularTiempo(burbuja)(numerosaleatorios())
print("Ordenamiento Burbuja: %10.5f" % t1)
t2 = calcularTiempo(shellSort)(numerosaleatorios())
print("Ordenamiento Shell: %15.5f" % t2)
t3 = calcularTiempo(ordenSeleccion)(numerosaleatorios())
print("Ordenamiento por Seleccion: %10.5f" % t3)
t5 = calcularTiempo(HeapSort)(numerosaleatorios())
print("Ordenamiento HeapSort: %10.5f" % t5)
t4 = calcularTiempo(quicksort)(numerosaleatorios(), 0, len(numerosaleatorios())-1)
print("Ordenamiento QuickSort: %10.5f" % t4)