#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:19:42 2024

@author: mjd
"""
# Time complexity is linear 
# Space complexity is linear
def merge (list1, list2):
  i, j = 0 , 0
  merged = []
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged.append(list1[i])
      i= i + 1
    else:
      merged.append(list2[j])
      j= j + 1
  # Try to see if the original lists have remaining data sets that is not in the 
  # merged data set
  while i < len(list1):
    merged.append(list1[i])
    i= i + 1
  while j < len(list2):
    merged.append(list2[j])
    j = j + 1
    """
  if i == len(list1):
    for k in range (j, len(list2)):
        merged.append(list2[k])
  else:
    for k in range (i, len(list1)):
        merged.append(list2[k])
        """
  return merged
print (merge([1, 3, 5, 10], [2, 4, 6, 7, 8, 9]))

# Time complexity is n log (n)
def sortmerge (ls):
  subls = []
  for i in ls:
    subls.append([i])
  while len(subls) > 1:
    newls = []
    i = 0
    while i < len(subls) - 1:
      merged = merge((subls[i]),(subls[i + 1]))
      newls.append(merged)
      i = i + 2    
    subls = newls
  return subls



def merge_sort(data):
  result = []

  for x in data:
    result.append([x])

  while len(result) > 1:
    newlist = []
    i = 0
    while i <= len(result) - 1:
      if i+1 == len(result): 
        newlist.append(result[i])
      else:
        list1 = result[i]
        list2 = result[i+1]
        merged = merge(list1, list2)
        newlist.append(merged)
      i = i + 2

    result = newlist

  return result[0]

def merged_sort(data):
    newlist = []

    for x in data:
      newlist.append([x])
    
    while len(newlist) > 1:
        merged = merge(newlist[0], newlist[1]) 
        newlist.append(merged)
        newlist=newlist[2:]
        
    return newlist[0]
        
print (merged_sort([9, 1, 5, 4, 6, 8]))