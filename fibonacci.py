n = int(input("enter the number of terms"))
a,b=0,2
for i in range(n):
  print(a,end=" ")
  a,b=b,a+b

output
enter the number of terms7
0 2 2 4 6 10 16 
