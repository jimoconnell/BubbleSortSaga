#!/usr/bin/env python3

import time
def bubblesort(list):
    swapped =  True
    while swapped:
        print()
        print ("New Iteration...")
        swapped = False
        for i in range(len(list) -1):
            if (list[i] > list[i + 1]):
                time.sleep(1)
                print ("Index: " + str(i) + " - Swap " + str(list[i]) + " with " + str(list[i + 1]))
                tmp = list[i]
                list[i] = list[i +1]
                list[i + 1] = tmp
                swapped = True
                print (list)
                print()
    print ("Nothing left to swap. Done.")
    return list

l = [7,3,1,1,6,8,4,2,5]
print (l)
l = bubblesort(l)
print (l)
