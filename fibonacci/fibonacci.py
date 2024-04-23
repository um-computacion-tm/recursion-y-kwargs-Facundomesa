def fibonacci(value):
    if value < 2:
        return value
    values = [0, 1]
    for _ in range(value -1):
        values.append(values [-1] + values [-2])
    
    return values[value]

resultado = fibonacci(6)
print (resultado)