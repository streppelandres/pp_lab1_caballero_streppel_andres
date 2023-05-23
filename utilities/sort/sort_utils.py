def bubble_sort(elements: list) -> list:
    for i in range(len(elements)):
        for j in range(0, len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements

def quick_sort(elements: list) -> list:
    if len(elements) <= 1: return elements
    
    pivot = elements[0]
    less, greater = [], []
    
    for i in range(1, len(elements)):
        if elements[i] <= pivot:
            less.append(elements[i])
        else:
            greater.append(elements[i])
    
    return quick_sort(less) + [pivot] + quick_sort(greater)