#сортировка

def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(0, length-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

unsorted = [7,1,3,4,2,4,6,5,5]
print ("Изначальный список:")
for i in range(len(unsorted)):
    print ("% d" % unsorted[i],end=" ")
print ("\n")
bubble_sort(unsorted)

print ("Отсортированный список:")
for i in range(len(unsorted)):
    print ("% d" % unsorted[i],end=" ")

#двоичный поиск

def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)

print ("\n")
print ('Введите искомое число')
my_element = int(input())
binary_search(unsorted, my_element, unsorted[0], unsorted[-1])
for i in range(len(unsorted)):
    if my_element==unsorted[i]:
        match='MATCH'
    else: match='NOT MATCH'
print (match)
