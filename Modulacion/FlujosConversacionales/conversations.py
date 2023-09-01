import openai
from ..Auxiliares.apiKeys import obtenerApiKey,obtenerModelo
from ..Auxiliares.AuxiliaresRespuestas import obtener_respuesta,obtenerAgregado,obtenerPersonalidad 

openai.api_key = obtenerApiKey("openai")
model = obtenerModelo("openai")

def generate_response_juan(historial_conversacion,opcionJuan):
    descripcionJuanBueno = obtenerPersonalidad("JuanBueno")
    descripcionJuanMalo = obtenerPersonalidad("JuanMalo")
    agregadoPersonaje=obtenerAgregado("Juan")
    if opcionJuan=="Bueno":
        return obtener_respuesta(
            [
                {"role": "system", "content": descripcionJuanBueno},
                {"role": "user", "content": historial_conversacion + agregadoPersonaje}
            ]
        )
    if opcionJuan=="Malo":
        return obtener_respuesta(
            [
                {"role": "system", "content": descripcionJuanMalo},
                {"role": "user", "content": historial_conversacion + agregadoPersonaje}
            ]
        )


def generate_response_maria(historial_conversacion):
    descripcionMaria = obtenerPersonalidad("Maria")
    agregadoPersonaje=obtenerAgregado("Maria")
    respuesta_maria = obtener_respuesta(
        [
            {"role": "system", "content": descripcionMaria},
            {"role": "user", "content": historial_conversacion + agregadoPersonaje}
        ]
    )
    return "\nMaria: " + respuesta_maria

def generate_response_elena(historial_conversacion):
    descripcionMamaJuan = obtenerPersonalidad("Elena")  
    agregadoPersonaje=obtenerAgregado("Elena")  
    respuesta_mama_juan = obtener_respuesta(
        [
            {"role": "system", "content": descripcionMamaJuan},
            {"role": "user", "content": historial_conversacion +agregadoPersonaje}
        ]
    )
    return "\nElena:" + respuesta_mama_juan

def generate_response_oraculo(historial_conversacion):
    descripcion_oraculo =obtenerPersonalidad("Oraculo")
    respuesta_oraculo = obtener_respuesta(
        [
            {"role": "system", "content": descripcion_oraculo},
            {"role": "user", "content": historial_conversacion + """"
            ¿En base a la conducta de "Juan", qué diría el Oraculo?. 
            Solo El Oraculo debe dar una respuesta reflexiba."""}
        ]
    )
    return("Oráculo: " + respuesta_oraculo)