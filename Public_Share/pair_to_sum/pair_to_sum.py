# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:14:18 2020

@author: jemsp
"""

from itertools import combinations
import math

def pair_to_sum(num_list,target,positions):
    ded_list = list(dict.fromkeys(num_list))
    list.sort(ded_list)
    
    
    target_list = []
    for i in ded_list:
        if i<target:
            target_list.append(i)
    
    combins = combinations(num_list,positions)       
    
    res_list = []
    final_combs = []
    
    for j in combins:
        s = math.fsum(j)
        if s == target:
            res_list.append(j)
            temp = list(j)
            list.sort(temp)
            #print(temp)
            if temp not in final_combs:
                final_combs.append(temp)

    return final_combs
