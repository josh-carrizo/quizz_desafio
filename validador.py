
def validate(opciones, eleccion):
        # numeros = ['0','1']
        # letras = ['a','b','c','d']
        
        if eleccion not in opciones:
            print(f'Opción no válida, ingrese una de las opciones válidas: \n {opciones}')
            eleccion = input('Ingresa una Opción: ').lower()
        else:
            return eleccion

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
