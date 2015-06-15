import sys
 
def order_by_x(lista):
  return mergesort(lista, lambda pt1,pt2: pt1.x < pt2.x)
 
def order_by_y(lista):
  return mergesort(lista, lambda pt1,pt2: pt1.y < pt2.y)

def mergesort(array, compare):
  if len(array) <= 1:
    return array
  else:
    first_half = mergesort(array[:len(array)/2], compare)
    second_half = mergesort(array[len(array)/2:], compare)
    return merge(first_half, second_half, compare)

def merge(array1, array2, compare):
  merged = []
  i = 0
  j = 0
  while len(array1) > i and len(array2) > j:
    # se verdadeiro pega da primeira array
    if compare(array1[i], array2[j]):
      merged.append(array1[i])
      i += 1
    else:
      merged.append(array2[j])
      j += 1

  merged = merged + (array1[i:] if len(array2) == j else array2[j:])
  return merged
