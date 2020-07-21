a = int(input('Vvedit livu mezhu :'))
b = int(input('Vvedit pravu mezhu :'))
if a>=b  :
    print('Error ')
else :
    fib = [0,1]

    for i in range(1,25):
        fib.append(fib[i]+fib[i-1])
    for i in fib :
        if i>=a and i<=b :
            print(i)


