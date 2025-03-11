#sum of even numbers
a=int(input("enter the starting range"))
b=int(input("entrer the ending range"))
sum=0
for i in range(a,b+1):
  if i%2==0:
    sum=sum+i
print(sum)

output
enter the starting range2
entrer the ending range6
12
