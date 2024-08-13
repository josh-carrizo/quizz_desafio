import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    indices = ['a', 'b', 'c', 'd']

    # Verificar si la elección está en los índices permitidos
    if eleccion in indices:
        index = indices.index(eleccion)
        correcta = alternativas[index][1] == 1

        if correcta:
            print("¡Has Acertado!")
        else:
            print("Mejor Suerte para la próxima")

        return correcta
    else:
        print("Error en su elección")
        return False


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






