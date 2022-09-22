print('Hello and welcome to the Bank')
print('Do you want to convert?')
response=input()
if response == 'yes':
    print('Nice, is it EUR to DKK, or DKK to EUR')
    print('For EUR to DKK press 1')
    print('For DKK to EUR press 2')
    value=input()
    if value == '1':
        print('Good choice. Note that at this bank we have 2% commition')
        print('The exchange rate for EUR to DKK is 7,44')
        print('How many EUR would you like to convert')
        EUR=input()
        EUR=float(EUR)
        print('You would like to convert ' +str(EUR)+ ' EUR')
        EUR=EUR*7.44
        EUR=EUR-EUR*0.02
        if EUR >= 3.65:
            print('Your exhange will then be '+str(EUR) + ' DKK')
            print('Thanks for using this program')
        else:
            print('Sorry we can not exhange lower than 3.65 DKK ')
    
         

    if value== '2':
        print('Good choice. Note that at this bank we have 2% commition')
        print('The exchange rate for DKK to EUR is 7,44')
        print('How many DKK would you like to convert')
        DKK=input()
        DKK=float(DKK)
        print('You would like to convert ' +str(DKK)+ ' DKK')
        DKK=DKK-DKK*0.02
        DKK=DKK*0.13
        if DKK >= 0.5:
            print('Your exhange will then be '+str(DKK) + 'EUR')
            print('Thanks for using this program')
        else:
            print('Sorry we can not exhange lower than 0,5 EUR ')
else:
     print('Sorry, this program cant help you')







