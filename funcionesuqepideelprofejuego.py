
def modificar_puntaje(diccionario_jugador:dict, nuevo_puntaje:int)->bool:
    pass

def modificar_vidas(diccionario_jugador:dict, vida_nueva:int)->bool:
    pass

def modificar_estadistica_jugador(usuario_modificar:dict, clave:str, valor:any)->bool:
    pass

def generar_respuesta_aleatoria(minimo:int, maximo:int)->int:
    pass

def mezclar_lista(lista_elementos:list)->bool:
    pass

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    pass

def agregar_dato(diccionario:dict, clave:str, valor:any)->bool:
    pass

def mostrar_dato(diccionario:dict, clave:str, valor:any)->bool:
    pass

def obtener_dato(diccionario:dict, clave:str)->any:
    pass

def modificar_dato(diccionario:dict, clave:str, dato_nuevo:any)->bool:
    pass

def terminar_juego(mensaje_final:str)->None:
    pass

def guardar_puntuacion(lista_rankings:list, diccionario_jugador:int)->bool:
    pass

def ordenar_puntaciones(lista_rankings:list, criterio:str)->bool:
    pass

def mostrar_rankings(lista_rankings:list)->bool:
    pass

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->str:
    pass

def ingresar_numero(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    pass

def mostrar_menu(mensaje:str)->None:
    pass

def calcular_porcentaje(cantidad_aciertos:int, cantidad_partidas:int)->float:
    pass

def verificar_estado_juego(diccionario_juego:dict)->bool:
    pass

def jugar_juego(diccionario_juego:dict,lista_rankings:list)->None:
    #Arranca el juego
    #Aca creamos todas las variables temporales que necesite nuestro juego
    
    while verificar_estado_juego(diccionario_juego):
        #Jugamos
        #Verificamos si la partida sigue o no
        pass
    
    #Pido el nombre del jugador para guardar la puntuación
    guardar_puntuacion(lista_rankings,diccionario_jugador)
    terminar_juego("TERMINO EL JUEGO")
    