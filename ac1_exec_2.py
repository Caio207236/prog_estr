
ano = int(input("Por favor, informe um ano inteiro: "))

bissexto = False

if (ano % 4 == 0 and ano % 100 != 0):
   
    bissexto = True

elif (ano % 400 == 0):
   
    bissexto = True

if bissexto:
    print("True")
else:
    print("False")