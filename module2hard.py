import random

n = random.choice(range(3,21))

result =''
for i in range(1,n):
    for j in range(i+1, n):
        if n % (i + j) == 0:

            result += f'{i}{j}'
            #result = str(i)+str(j)

print(f'{n} - {result}')














