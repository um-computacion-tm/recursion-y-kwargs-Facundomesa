def factorial(valor):
    if valor > 0:
        return valor * factorial(valor - 1)
    return 1
result = factorial(5)
print(result)

