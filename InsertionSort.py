def insertionSort(vetor):
    n = len(vetor)
    for i in range(1, n):
        chave =vetor[i]
        j=i-1
        while j>=0 and vetor[j]>chave:
            vetor[j+1] = vetor[j]
            j-=1
        vetor[j+1] = chave

vetor = [1, 3, 5, 4, 2, 6, 8, 7, 10, 9]
insertionSort(vetor)
print(vetor)