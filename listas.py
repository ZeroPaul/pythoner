import random

lista = ['Karen', 'Mariana', 'Daniela', 'Yarette', 'Deny']

print lista

lista += ['Zero', 'Infinity', 'Paul']

print lista

p = "PYTHON"

lista += p
#otra funcion seria lista.extend(p)

print lista


for nombres in lista:
    print (nombres)

a = "ABCDEFGJIJKLMNOPQRSTUWXYZ"

for letra in a:
    if letra in 'AEIOU':
        print (letra, "es vocal")
    else:
        print (letra, "es consonante")

z = random.choice(lista)

print z


c=lista.count('Paul')

print 'Paul se repite %s'%c

print lista.pop(0)

print sorted(lista)
print lista[::-1]
l=lista[::-1]
for nombres in l:
    print nombres[::-1]
