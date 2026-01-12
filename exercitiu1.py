a = int(input('Primul numar este: '))
b = int(input ('Al doilea numar este: '))

print('Alege operatiunea: + - * /')
op = input('Operatiunea aleasa este: ')

if op == '+':
    rezultatul = a + b
    print('Rezultatul adunarei este: ', rezultatul)
elif op == '-':
    rezultatul = a - b
    print('Rezultatul scaderei este: ', rezultatul)

elif op == '*':
    rezultatul  = a * b
    print('Rezultatul la inmultire este: ', rezultatul)

elif op == "/":
    if b == 0:
        print("Eroare: împărțirea la zero nu este permisă.")
    else:
        rezultat = a / b
        print("Rezultatul împărțirii este:", rezultat)

else:
    print("Operație invalidă.")
