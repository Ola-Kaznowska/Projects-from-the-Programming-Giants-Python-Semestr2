liczby = [1,4,4,56,11]

def bubble_sort(arr):
    n = len(arr)
# iterujemy przez wszystkie elementy listy
    for i in range(n):
# ostatnie i elementów są już posortowane
        for j in range(0, n-i-1):
# porównujemy sąsiednie elementy
            if arr[j] > arr[j+1]:
# zamieniamy miejscami, jeśli kolejność jest nieprawidłowa

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(liczby))