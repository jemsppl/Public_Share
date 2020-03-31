# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:14:18 2020

@author: jemsp
"""

import pair_to_sum as pts

num_list = [2,4,3,5,6,3,8,2,4,4,6,4,6,8,8,6,5,4,3,23,34,56,23,34,56,67]
target = 13
positions = 3


final_combs = pts.pair_to_sum(num_list,target,positions)
print(final_combs)
print("Total number of pairs: "+str(len(final_combs)))