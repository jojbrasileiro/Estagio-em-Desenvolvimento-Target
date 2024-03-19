def fibonacci(num):
    n1 = 0
    n2 = 1
    n3 = 0
    if num == 0 or num == 1:
        return True
    while num > n3:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    if num == n3:
        return True
    else:
        return False

num = input("Forneça um numero: ")
if(fibonacci(int(num))):
    print("O numero fornecido pertence a sequencia")
else:
    print("O numero fornecido não pertence a sequencia")

