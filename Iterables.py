dic = [1, 2, 3, 4]
iterador = dic
iterador = iter(iterador)
iterador.__next__()



print (iterador)
print (iterador.__next__())
print (iterador.__next__())