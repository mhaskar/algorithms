#!/usr/bin/python

array = [5,54,54,10,31,311,301,32,123,456,456,4,564,564,74,123,456,2,31,2,34,56,0,1,564,654,231,231,321,67,854,15,1456,4,10000,125213]

def Quick(lis):
 left = []
 right = []
 if len(lis) <= 1:
   return lis
 else:
   for i in lis[1:]:
    if i < lis[0]:
     left.append(i)
    else:
     right.append(i)
   return Quick(left) + [lis[0]] + Quick(right)


print Quick(array)
