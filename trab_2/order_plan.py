
def merge_x(lista_x,lista_y):
  if lista_x == []:
      return lista_y
  elif lista_y == []:
      return lista_x
  else:
      if lista_x[0][0] < lista_y[0][0]:
          return [lista_x[0]] + merge_x(lista_x[1:],lista_y)
      else:
          return [lista_y[0]] + merge_x(lista_x,lista_y[1:])
 
def order_by_x(lista):
  if len(lista) <= 1:
     return lista
  else:
      middle = len(lista) // 2
      return merge_x(order_by_x(lista[:middle]), order_by_x(lista[middle:]))


def merge_y(lista_x,lista_y):
  if lista_x == []:
      return lista_y
  elif lista_y == []:
      return lista_x
  else:
      if lista_x[0][0] < lista_y[0][0]:
          return [lista_x[0]] + merge_y(lista_x[1:],lista_y)
      else:
          return [lista_y[0]] + merge_y(lista_x,lista_y[1:])
 
def order_by_y(lista):
  if len(lista) <= 1:
     return lista
  else:
      middle = len(lista) // 2
      return merge_y(order_by_y(lista[:middle]), order_by_y(lista[middle:]))