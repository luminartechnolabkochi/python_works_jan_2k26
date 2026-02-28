"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""
lst=[1,2,3,4]
#    0 1 2 3 
#    p n

def missing_least_positive(arr):

    arr.sort()

    for prev  in range(0,len(arr)-1):

        next = prev+1

        difference = arr[next] - arr[prev]

        if difference!=1:

            print(arr[prev]+1,"is missing")

            break
    else:

        print(arr[-1]+1)


missing_least_positive([1,2,3,4])








# missing_least_positive([1,2,4])


