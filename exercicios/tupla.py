
''''
student = ('bro', 21, "male")


print(student.count('bro'))
print(student.index('male'))

for x in student:
    print(x)


if 'bro' in student:
    print("bro is here!")
'''
'''
gloceries = [('orange', 'apple', 'punapple', 'banana'),
            ( 'celery', 'carrots'),
            ('chicken', 'fish', 'turkey')]

 
for collection in gloceries:
    for food in collection:
        print(food, end= ' ')
    print()
'''
'''
num_pad = ((1, 2, 3,),
               (4, 5, 6),
               (7, 8, 9),
               ('*', 0, '#'))
    
for row in num_pad:
        for num in row:
            print(num, end='')
            print()
'''

#produto = 'iphone'
#quantidade_estoque = 200

#print("O produto ", produto, "tem", quantidade_estoque, "unidades no estoque", sep=";")

#mport time
#print("contagem")
#for i in range(5):
    #print(5 - i, end="\r")
    #time.sleep(1)
    #print("Acabou")

salarios = [1000, 5000, 7000, 850]

# 1. Define a function that handles ONE salary
def calcular_aumento(valor):
    if valor > 3000:
        return valor * 1.08
    else:
        return valor * 1.1

# 2. Use map to apply that function to the whole list
# We wrap it in list() to see the results immediately
novos_salarios = list(map(calcular_aumento, salarios))

print(f"Salários antigos: {salarios}")
print(f"Salários com aumento: {novos_salarios}")

