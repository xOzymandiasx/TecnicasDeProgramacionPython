divisores = 0;

for numeros in range(1,25):
  print(numeros);
  if (24 % numeros == 0):
    divisores += 1;
    
print(divisores);