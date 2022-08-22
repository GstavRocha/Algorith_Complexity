import time

start = time.time()


def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[min_index] > lista[j]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    lst1 = [2, 2, 3, 4, 5, 6]
    lst2 = [2, 1, 3, 4, 6, 5, 9, 8, 10]
    selection_sort(lst)
    print("Sorted", lst)
end = time.time()
tempo = end - start
print('Tempo gasto', tempo)
