
def modificar_puntaje(diccionario_jugador:dict, nuevo_puntaje:int)->bool:
    pass 
# modificar el puntaje de un jugador.


def modificar_vidas(diccionario_jugador:dict, vida_nueva:int)->bool:
    pass 
# modificar las vidas de un jugador.


def modificar_estadistica_jugador(usuario_modificar:dict, clave:str, valor:any)->bool:
    pass 
#modificar cualquiera de las estadísticas del jugador

def generar_respuesta_aleatoria(minimo:int, maximo:int)->int:
    pass 
# generar un dato elegido al azar entre un rango minimo y maximo.

def mezclar_lista(lista_elementos:list)->bool:
    pass 
#alterar el orden de los elementos de una lista.
#está

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    pass 
#selecciona un elemento al azar a partir de una colección.

def agregar_dato(diccionario:dict, clave:str, valor:any)->bool:
    pass 
# agregar un dato específico de un diccionario.


def mostrar_dato(diccionario:dict, clave:str, valor:any)->bool:
    pass 
#mostrar un dato específico de un diccionario.


def obtener_dato(diccionario:dict, clave:str)->any:
    pass 
#obtener un dato específico de un diccionario.

def modificar_dato(diccionario:dict, clave:str, dato_nuevo:any)->bool:
    pass 
#modificar un dato específico de un diccionario.

def terminar_juego(mensaje_final:str)->None:
    pass 
#mostrar el mensaje final de mi juego cuando termina la partida.

def guardar_puntuacion(lista_rankings:list, diccionario_jugador:int)->bool:
    pass 
#guardar la puntuación final del juego en la lista de rankings.

def ordenar_puntaciones(lista_rankings:list, criterio:str)->bool:
    pass 
#ordenar la lista de rankings.

def mostrar_rankings(lista_rankings:list)->bool:
    pass
#está

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->str:
    pass 
#ingresar el nombre del usuario que va a jugar.

def ingresar_numero(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    pass 
#un número entero entre dos rangos.

def mostrar_menu(mensaje:str)->None:
    pass 
#mostrar el menú del juego.
#está 

def calcular_porcentaje(cantidad_aciertos:int, cantidad_partidas:int)->float:
    pass 
# calcular el porcentaje de partidas ganadas o perdidas dependiendo de lo que se necesite

def verificar_estado_juego(diccionario_juego:dict)->bool:
    pass

def jugar_juego(diccionario_juego:dict,lista_rankings:list)->None:  
    #Arranca el juego
    #Aca creamos todas las variables temporales que necesite nuestro juego
    # Función que se encarga de ejecutar toda la lógica de la partida, maneja todas 
    # las variables posibles en mi juego, y aplica la lógica del juego elegido, 
    # al final de la partida guarda la puntuación final.
    while verificar_estado_juego(diccionario_juego):
        #Jugamos
        #Verificamos si la partida sigue o no devolviendo un booleano   
        pass
    
    #Pido el nombre del jugador para guardar la puntuación
    guardar_puntuacion(lista_rankings,diccionario_jugador)
    terminar_juego("TERMINO EL JUEGO")
    