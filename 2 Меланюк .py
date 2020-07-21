check = int(input('Введіть число  :'))
fib = [0,1]
i=1
while fib[i]<= check:
    fib.append(fib[i]+fib[i-1])
    i+=1
if check in fib :
    print('Задача оцінена в ',i)
else :
    print('Таке число недопустиме!')
