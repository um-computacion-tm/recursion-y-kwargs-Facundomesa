def ver_datos(*word, **kword):
    count = 0
    for key, subdiccionario in kword.items():
        valores_subdiccionario = set(subdiccionario.values())
        
        if set(word).issubset(valores_subdiccionario): 
            count += 1
            id = key
    
    if count == 0:
        return 'no hay'
    elif count == 1:
        return id
    else:
        return f"Hay {count} ID con el mismo nombre"
    





