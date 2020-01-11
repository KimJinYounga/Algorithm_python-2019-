numbers=[40,35,27,50,75]

def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        # print(pivot)
        less=[number for number in array[1:] if number < pivot]
        greater=[number for number in array[1:] if number >= pivot]
        # print(less)
        # print(greater)

    return quickSort(less)+[pivot]+quickSort(greater)

print(quickSort(numbers))