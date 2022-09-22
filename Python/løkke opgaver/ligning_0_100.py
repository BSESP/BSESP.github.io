
print('')
print('Dette program beregner y værdien i følgende ligning y=3x^2+6x+9 indenfor intervallet af x=0 til x=100 hvor den gør det for titabellen')
for x in range(0,101,10):
    y=3*x**2+6*x+9
    print('')
    print('når x= '+ str(x)+' er:')
    print('y= '+ str(y))
