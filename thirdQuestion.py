import math

yearAge = int(input("Digite a idade do cachorro:\n"))
monthAge = int(input("Digite quantos meses se passaram desde o último aniversário:\n"))
dogAge = yearAge + (monthAge/12)
humanAge = math.log(dogAge)*16 + 31
print(f"Seu cão teria {humanAge:.2f} anos")