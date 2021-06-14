
import re
import math

while (True):
    print('Info:')
    print('\ta(x) = 3x ^ 2 + 4x\n\tb(x) = x + 1/x\n')
    print('\tf1(x) = (a + b) ^ 0.5\n\tf2(x) = (1 - a) / 10 + b\n\n\tC = a < 10\n')
    print('Padoms: a < 10, ja x = (-2.611; 1.277)\n')    
    
    xs = ''
    while (xs == ''):
        xs = input('Ievadiet x vērtību:\nx = ')
    
    if not re.search('^[-+]?\d*\.?\d*$',xs):
        print('Nepareiza ievade! Jāievada skaitlis!')
    else:
        x = float(xs)
        if x == 0:
            print('Kļūda - dalīšana ar 0!')
        else:
            a = x * (3 * x + 4)
            b = 1 / x + x
            if a < 10:
                if (a + b) < 0:
                    print('Y = f1(x) = {:.3f}i'.format(math.sqrt(abs(a + b))))
                else:
                    print('Y = f1(x) = {:.3f}'.format(math.sqrt(a + b)))
            else:
                print('Y = f2(x) = {:.3f}'.format(0.1 - 0.1 * a + b))
   
    C = input("\nVai vēlaties turpināt? ('Y' vai 'y', lai turpinātu!)\n")
    if C != 'y' and C != 'Y':
        break

print('Programma izbeigta!')
