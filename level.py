def choose_level(n_pregunta, p_level):

    if p_level == '1':
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        elif n_pregunta == 3:
            level = 'avanzadas'
        else:
            print(f"El nivel ingresado {n_pregunta} esta fuera del rango")
    
    elif p_level == 2:
        if 1 <= n_pregunta <= 2:
            level = 'basicas'
        elif 3 <= n_pregunta <= 4:
            level = 'intermedias'
        elif 5 <= n_pregunta <= 6:
            level = 'avanzadas'
        else:
            print(f"El nivel ingresado {n_pregunta} esta fuera del rango del nivel {p_level}")
    
    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            level = 'basicas'
        elif 4 <= n_pregunta <= 6:
            level = 'intermedias'
        elif 7 <= n_pregunta <= 9:
            level = 'avanzadas'
        else:
            print(f"El nivel ingresado {n_pregunta} esta fuera del rango del nivel {p_level}")
    
    else:
        print(f'El nivel ingresado no existe')
    # Construir lógica para escoger el nivel
    ##################################################
    print(level)
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias