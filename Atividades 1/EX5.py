sal=float(input("Digite seu salário: "))
if sal<500:
    reajuste=sal+(sal*0.15)
    print(f"Salario reajustado {reajuste}")
if sal>=500 and sal<=1000:
    reajuste=sal+(sal*0.10)
    print(f"Salario reajustado {reajuste}")
if sal>1000:
    reajuste=sal+(sal*0.05)
    print(f"Salario reajustado {reajuste}")