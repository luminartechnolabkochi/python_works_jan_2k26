

def find_duplicates(arr):

    arr.sort()

    for prev in range(0,len(arr)-1):

        next = prev+1

        difference = arr[next] - arr[prev]

        if difference==0:

            print(arr[prev])

find_duplicates([11,12,11,13,14,14])

    