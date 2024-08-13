import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):

    pool=p.pool_preguntas[dificultad]
    posibles_preguntas = list(pool.keys())
    
    if not posibles_preguntas:
        print('No existen mas preguntas')
    
    n_elegido = random.choice(posibles_preguntas)
    pregunta = pool.get(n_elegido)
    if pregunta is None:
        raise ValueError(f"La pregunta '{n_elegido}' no está disponible.")
    
    del pool[n_elegido]
    
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas
    


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')