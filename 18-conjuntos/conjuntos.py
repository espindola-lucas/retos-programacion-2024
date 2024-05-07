my_list = [1, 2, 3, 4, 5]

# Añade un elemento al final.
my_list.append(6)
print(my_list)

# Añade un elemento al principio.
my_list.insert(0, 0)
print(my_list)

# Añade varios elementos en bloque al final.
my_list.extend([7, 8])
print(my_list)

# Añade varios elementos en bloque en una posicion especifica.
my_list[2:3] = ['x', 'y']
print(my_list)

# Eliminar un elemento de una posicion especifica.
del my_list[2]
print(my_list)

# Actualiza el valor en una posicion especifica.
my_list[2] = 'hola'
print(my_list)

# Comprueba si un elemento se encuentra en el conjunto.
print(1 in my_list)

# Elimina todo el contenido del conjunto.
my_list.clear()

#EXTRA
set1={1,2,3,4,5}
set2={1,3,5,7,9}

#Union
print(set1|set2)

#Interseccion
print(set1&set2)

#Diferencia
print(set1-set2)

#Diferencia simetrica
print(set1^set2)