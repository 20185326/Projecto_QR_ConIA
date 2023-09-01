from flask import Flask,render_template,request
import openai
import asyncio
import random
from conversations import *

app=Flask(__name__)
contador=0
historial=" "
evento=""
situaciones = [
    "Maria ve a un niño llamado Juan pasear con su perro y este no lleva bozal y la mascota hace popo en el parque y el dueño no recoge sus desperdicios.",
    "Maria ve a a un niño llamado Juan jugando en la fuente del parque y salpicando agua por todas partes.",
    "Maria encuentra a un niño llamado Juan tirando basura en el suelo a pesar de que hay un bote de basura cerca.",
    "Maria observa a un niño llamado Juan montando su bicicleta en el camino peatonal y asustando a los peatones.",
    "Maria encuentra un banco del parque roto y dañado. Y a juan haciendo un graffiti en los alrededores del banco.",
    "Maria ve a un niño llamado Juan alimentando a las palomas en exceso y creando un desorden con migas de pan.",
    "Maria encuentra a un niño llamado Juan con  un perro sin correa corriendo libremente por el parque y persiguiendo a otros animales.",
    "Maria observa a un niño llamado Juan esuchando música fuerte en un altavoz sin usar audífonos.",
    "Maria ve a un niño llamado Juan pescando en el lago del parque y dejando restos de anzuelos y líneas de pesca en el suelo.",
    "Maria encuentra a un niño llamado Juan arrancando flores y plantas del jardín del parque sin permiso.",
    "Maria ve a un niño llamado Juan usando una bicicleta eléctrica a alta velocidad en un área designada para caminar."
]
situacionInicial = random.choice(situaciones)

openai.api_key = "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"


@app.route('/')
async def principal():
    global situacionInicial
    global historial
    respuestaIA = await generate_response_maria(situacionInicial)
    print(respuestaIA)
    respuestaIA=situacionInicial+"\n"+ respuestaIA 
    historial_dividido = historial.split('\n')
    historial=respuestaIA
    return render_template("index.html", historial=historial_dividido)

@app.route('/procesar', methods=['POST'])
def procesar():
    global historial
    global contador
    global evento
    juanAction=""
    mariaAction=""
    elenaAction=""
    contador=contador+1     
    print(contador)
    user_input = request.form.get('user_input', '')
    option_value = request.form.get('option_value', '')
    interaccion=""
    print(user_input)
    if(option_value=="Bueno" or option_value=="Malo"):
        if(contador>2 and contador<=4):
            mensaje_Elena=generate_response_elena(historial)
            historial = historial + "\n" + mensaje_Elena
            interaccion+="\n" + mensaje_Elena
        if(contador<=4):
            mensaje_juan = generate_response_juan(historial,option_value)
            interaccion=interaccion+"\nJuan: " + mensaje_juan
            historial_conversacion = historial + "\nJuan: " + mensaje_juan
            respuesta_maria = generate_response_maria(historial_conversacion)
            interaccion+=respuesta_maria
            # Actualizar el historial
            historial = historial_conversacion + "\n" + respuesta_maria
            # Dividir el historial en líneas para mostrarlo en el HTML
        if(contador==5):
            mensaje_oraculo=generate_response_oraculo(historial)
            historial_dividido = [mensaje for mensaje in historial.split('\n') if mensaje.strip() != ""]   
            historial_dividido.append(mensaje_oraculo)
            interaccion+="\n" + mensaje_oraculo
            juanAction=evaluaMensajeJuan(interaccion) 
            mariaAction=evaluaMensajeMaria(interaccion) 
            elenaAction=evaluaMensajeElena(interaccion) 
            interaccion = [mensaje for mensaje in interaccion.split('\n') if mensaje.strip() != ""] 
            return render_template("index.html",historial= (interaccion),juanAction=juanAction,mariaAction=mariaAction,elenaAction=elenaAction)
        historial_dividido = [mensaje for mensaje in historial.split('\n') if mensaje.strip() != ""]  
        juanAction=evaluaMensajeJuan(interaccion) 
        mariaAction=evaluaMensajeMaria(interaccion) 
        elenaAction=evaluaMensajeElena(interaccion) 
        interaccion = [mensaje for mensaje in interaccion.split('\n') if mensaje.strip() != ""]    
        return render_template("index.html",historial= (interaccion),juanAction=juanAction,mariaAction=mariaAction,elenaAction=elenaAction)
    else :
        if(contador>2 and contador<=4):
            mensaje_Elena=generate_response_elena(historial)
            historial = historial + "\n" + mensaje_Elena
            interaccion+="\n" + mensaje_Elena
        if(contador<=4):
            historial_conversacion = historial + "\nJuan: " + user_input
            interaccion=interaccion+"\nJuan: " + user_input
            respuesta_maria = generate_response_maria(historial_conversacion)
            interaccion+=respuesta_maria
            # Actualizar el historial
            historial = historial_conversacion + "\n" + respuesta_maria
            # Dividir el historial en líneas para mostrarlo en el HTML
        if(contador==5):
            mensaje_oraculo=generate_response_oraculo(historial)
            historial_dividido = [mensaje for mensaje in historial.split('\n') if mensaje.strip() != ""]   
            historial_dividido.append(mensaje_oraculo)
            interaccion+="\n" + mensaje_oraculo
            juanAction=evaluaMensajeJuan(interaccion) 
            mariaAction=evaluaMensajeMaria(interaccion) 
            elenaAction=evaluaMensajeElena(interaccion) 
            interaccion = [mensaje for mensaje in interaccion.split('\n') if mensaje.strip() != ""] 
            return render_template("index.html",historial= (interaccion),juanAction=juanAction,mariaAction=mariaAction,elenaAction=elenaAction)
        historial_dividido = [mensaje for mensaje in historial.split('\n') if mensaje.strip() != ""]  
        juanAction=evaluaMensajeJuan(interaccion) 
        mariaAction=evaluaMensajeMaria(interaccion) 
        elenaAction=evaluaMensajeElena(interaccion) 
        interaccion = [mensaje for mensaje in interaccion.split('\n') if mensaje.strip() != ""]    
        return render_template("index.html",historial= (interaccion),juanAction=juanAction,mariaAction=mariaAction,elenaAction=elenaAction)


if __name__=='__main__':
    app.run(debug=True,port=5501)
