# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:57:32 2017

@author: mkaesler
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:10:02 2017

@author: mkaesler
"""

import random
from time import time
import matplotlib.pyplot as plt



def sorted_merge(iterable, key = lambda x:x, reverse = False):
    merge_swaps = 0
    merge_comps = 0

    t0 = time()
    merged, merge_swaps1, merge_comps1 = mergesort(iterable, key, merge_swaps, merge_comps)
    t1 = round(time()-t0,3)
    
    if reverse == False:
        return (merged, t1, merge_swaps1, merge_comps1)
    elif reverse == True:
        return (list(reversed(merged)), t1, merge_swaps1, merge_comps1)
    else:
        print "you did not enter a boolean for reverse = argument"


def sorted_bubble(iterable, key = lambda x:x, reverse = False):
    bubble_swaps = 0
    bubble_comps = 0
    t0 = time()
    bubbled, bubble_swaps1, bubble_comps1 = bubble(iterable, key, bubble_swaps, bubble_comps)
    t1 = round(time()-t0, 3)
    
    if reverse == False:
        return (bubbled, t1, bubble_swaps1, bubble_comps1)
    elif reverse == True:
        return (list(reversed(bubbled)), t1, bubble_swaps1, bubble_comps1)
    else:
        print "you did not enter a boolean for reverse = argument"


def mergesort(array, key, merge_swaps, merge_comps):
    n = len(array)
    if n < 2:
        return (array, merge_swaps, merge_comps)
    else:
        l1 = array[:(n/2)]
        l2 = array[(n/2):]
    
        l1, merge_swaps1, merge_comps1 = mergesort(l1, key, merge_swaps, merge_comps)
        l2, merge_swaps2, merge_comps2 = mergesort(l2, key, merge_swaps, merge_comps)
    
    merge_swap_combined = merge_swaps1 + merge_swaps2
    merge_comp_combined = merge_comps1 + merge_comps2
    
    return merge(l1, l2, key, merge_swap_combined, merge_comp_combined)
    
    
def merge(array1, array2, key, merge_swaps, merge_comps):
    array3 = []
    
    while len(array1) > 0 and len(array2) > 0:
        if key(array1[0]) > key(array2[0]):
            array3.append(array2[0])
            del array2[0]
            merge_swaps += 1
            merge_comps += 1
        else:
            array3.append(array1[0])
            del array1[0]
            merge_comps += 1
    while len(array1) > 0:
        array3.append(array1[0])
        del array1[0]
    while len(array2) > 0:
        array3.append(array2[0])
        del array2[0]
        
    return (array3, merge_swaps, merge_comps)
    
    
def bubble(array, key, swaps, comps):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            comps += 1
            if key(array[j]) < key(array[i]):
                swaps += 1
                array[j], array[i] = array[i], array[j]
    return (array, swaps, comps)


def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst    
    

def main():
    times_bubble = []
    SOC_bS = []
    SOC_bC = []
    
    times_merge = []
    SOC_mS = []
    SOC_mC = []
    
    for i in range(5, 700, 5):
        n = generateRandomList(i)
        lst_m, time_m, swaps_m, comb_m = sorted_merge(n)
        SOC_mS.append(swaps_m)
        SOC_mC.append(comb_m)
        times_merge.append(time_m)
        
        lst_b, time_b, swaps_b, comb_b = sorted_bubble(n)
        SOC_bS.append(swaps_b)
        SOC_bC.append(comb_b)
        times_bubble.append(time_b)
        
    x = [y for y in range(5, 700, 5)]
    
    
    plt.subplot(211)
    plt.plot(x, times_merge, 'bs-', x, times_bubble, 'g^-')
    plt.legend('mb')
    
    print "# of swaps in merge, array len = 700:", SOC_mS[138]
    print "# of comps in merge, array len = 700:", SOC_mC[138]
    print "# of swaps in bubble, array len = 700:", SOC_bS[138]
    print "# of comps in bubble, array len = 700:", SOC_bC[138]
    
    
    
    plt.show()
    
    
    
    







if __name__ == '__main__':
    main()