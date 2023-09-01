import openai
from ..Auxiliares.apiKeys import obtenerApiKey, obtenerModelo
from ..Auxiliares.AuxiliaresRespuestas import  obtener_respuesta
openai.api_key = obtenerApiKey("openai")
model = obtenerModelo("openai")

def evaluaMensajeJuan(ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Juan y jusgas sobre sus acciones. 
    Si consideras que obra mal debes decir solo: "Juan es malo"
    Si consideras que obra bien debes decir solo: "Juan es bueno" """
    response = obtener_respuesta(
        [
            {"role": "user", "content": observadorDescription},
            {"role": "user", "content": ultimaConversacion+ "Solo debes responder es malo o bueno. No te explayes."}
        ]
    )   
    return response

def evaluaMensajeMaria(ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Maria y adivinaras su estado de animo. 
    Si consideras que Maria esta triste debes decir solo: "Maria esta triste"
    Si consideras que Maria esta feliz debes decir solo: "Maria esta feliz" """
    response = obtener_respuesta(
        [
            {"role": "user", "content": observadorDescription},
            {"role": "user", "content": ultimaConversacion+ "Solo debes responder si esta feliz o triste. No te explayes."}
        ]
    )
    return response

def evaluaMensajeElena(ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Elena y adivinaras su estado de animo. 
    Si consideras que Elena esta Amarga debes decir solo: "Elena esta amarga"
    Si consideras que Elena esta feliz debes decir solo: "Elena esta feliz" """
    response = obtener_respuesta(
        [
            {"role": "user", "content": observadorDescription},
            {"role": "user", "content": ultimaConversacion+ "Solo debes responder si esta amarga o feliz. No te explayes."}
        ]
    )
    return response

