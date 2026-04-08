'''
inicio <=fim
cresc -> inicio |fim
inicio > fim 
dec > fim | inicio
'''

inicio = int(input('numero:'))
fim = int(input('fim'))

while inicio<=fim:
   print (f'x: {inicio}')
inicio=inicio+1
print('fora do while')

while inicio > fim:
  print(f'{inicio}')
  inicio -= 1
  if inicio < 0:
     break





