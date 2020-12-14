def my_quicksort(lst):
    if len(lst) <= 1:
        sorted_list = lst
    else:
        pivot = lst[0]
        bigger = []
        smaller = []
        same = []
        for item in lst:
            if item > pivot:
                bigger.append(item)
            elif item < pivot:
                smaller.append(item)
            else:
                same.append(item)
         
        sorted_list = my_quicksort(smaller) + same + my_quicksort(bigger)
    return sorted_list

my_quicksort([2,1,3,5,6,3,8,10])
