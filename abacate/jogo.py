import random

m = int(input("Digite um número: "))
n = random.randint(1, 11)

if m == n:
    print(f"O computador escolheu {n}")
    print(f"Você escolheu {m}")
    print("VOCÊ GANHOOOOOU!!!!!!!")
else:
    print(f"O computador escolheu {n}")
    print(f"Você escolheu {m}")
    print("VOCÊ PERDEU SE LIXO")