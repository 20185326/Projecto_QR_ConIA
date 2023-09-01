from flask import Flask,render_template,request
import openai
import random
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
def obtener_respuesta(model, messages):
    respuesta = openai.ChatCompletion.create(model=model, messages=messages)
    return respuesta.choices[0].message['content']

def evaluarJuan(modelo,ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Juan y jusgas sobre sus acciones. 
    Si consideras que obra mal debes decir solo: "Juan es malo"
    Si consideras que obra bien debes decir solo: "Juan es bueno" """
    respuesta = obtener_respuesta(modelo, [
        {"role": "user", "content": observadorDescription},
        {"role": "user", "content": ultimaConversacion+ "Solo debes responder es malo o bueno. No te explayes."}
    ])
    return respuesta
def evaluarMaria(modelo,ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Maria y adivinaras su estado de animo. 
    Si consideras que Maria esta triste debes decir solo: "Maria esta triste"
    Si consideras que Maria esta feliz debes decir solo: "Maria esta feliz" """
    respuesta = obtener_respuesta(modelo, [
        {"role": "user", "content": observadorDescription},
        {"role": "user", "content": ultimaConversacion+ "Solo debes responder si esta feliz o triste. No te explayes."}
    ])
    return respuesta
def evaluarElena(modelo,ultimaConversacion):
    observadorDescription = """Eres una persona muy critica observa a Elena y adivinaras su estado de animo. 
    Si consideras que Elena esta Amarga debes decir solo: "Elena esta amarga"
    Si consideras que Elena esta feliz debes decir solo: "Elena esta feliz" """
    respuesta = obtener_respuesta(modelo, [
        {"role": "user", "content": observadorDescription},
        {"role": "user", "content": ultimaConversacion+ "Solo debes responder si esta amarga o feliz. No te explayes."}
    ])
    return respuesta

def conversacion_juan(modelo, historial_conversacion,opcionJuan):
    descripcionJuanBueno = """Eres Juan, un joven de 18 años.Tu mama se llama Elena.Te gustan los videojuegos y eres muy olvidadizo. Debido a tu personalidad las personas usualmente no se juntan contigo, pero tu valoras mucho a tus amigos y eres buena persona. Por eso amas mucho a tu mascota, al cual consideras como que es tu mejor amigo."""
    descripcionJuanMalo = """Eres Juan, un joven de 18 años.Te gusta hacerte el malo.Tu mama se llama Elena.Te gustan los videojuegos y eres muy olvidadizo. Eres una persona agresiva con todas las personas menos con tu mama, ademas a ella siempre le haces caso en todo. Debido a tu caracter las personas te tienen miedo y no se juntan contigo. Amas mucho a tu mascota, al cual consideras como que es tu mejor amigo."""
    respuesta_juan=""
    if opcionJuan=="Bueno":
        respuesta_juan = obtener_respuesta(modelo, [
            {"role": "system", "content": descripcionJuanBueno},
            {"role": "user", "content": historial_conversacion + """\n¿Qué diría Juan?.
            (sigue hilo de la conversación)\nSolo Juan debe dar una respuesta corta a la vez y esperar. No redactes mas de un parrafo \nJuan:"""}
        ])
    if opcionJuan=="Malo":
        respuesta_juan = obtener_respuesta(modelo, [
            {"role": "system", "content": descripcionJuanMalo},
            {"role": "user", "content": historial_conversacion + """\n¿Qué diría Juan?.
            (sigue hilo de la conversación)\nSolo Juan debe dar una respuesta corta a la vez y esperar. No redactes mas de un parrafo \nJuan:"""}
        ])
    return respuesta_juan
def conversacion_maria(modelo, historial_conversacion):
    descripcionMaria = """Eres Maria, una niña de 9 años que le gusta andar en 
    los parques limpios y te gustan  los animales. 
    Te disgusta mucho ver que la gente ensucia los parques de distintas maneras. 
    Cuando ves que ensucian los parques, siempre se lo haces saber. Pero no eres muy insistente , ya que tienes miedo cuando te tratan mal"""
    respuesta_maria = obtener_respuesta(modelo, [
        {"role": "system", "content": descripcionMaria},
        {"role": "user", "content": historial_conversacion + """\n¿Qué diría Maria?. 
        (sigue hilo de la conversación)\nSolo Maria debe dar una respuesta breve a la vez y esperar. No redactes mas de un parrafo \nMaria:"""}
    ])
    global historial
    historial=historial_conversacion+"\nMaria: "+ respuesta_maria
    return "\nMaria: " + respuesta_maria
def conversacion_mama_juan(modelo, historial_conversacion):
    descripcionMamaJuan = """Eres Elena,
    tienes 35 años y eres la mama de Juan.
    Eres una persona comprensiva.
    Te gusta respetas las normas.
    Te gusta pasear por los parques.
    Eres amiga de Maria.
    Si Juan no te hace caso lo reprendes.
    Si Juan te hace caso lo premiaras con algo que le guste.
    Sabes que a juan le gustan los videojuegos"""
    
    respuesta_mama_juan = obtener_respuesta(modelo, [
        {"role": "system", "content": descripcionMamaJuan},
        {"role": "user", "content": historial_conversacion + """"\n¿Qué diría Elena?. 
        (sigue hilo de la conversación)\nSolo Elena debe dar una respuesta corta a la vez y esperar. No redactes mas de un parrafo \nElena:"""}
    ])
    return "\nElena:" + respuesta_mama_juan

def conversacion_oraculo(modelo, historial_conversacion):
    descripcion_oraculo = """Eres el dios Oraculo que juzga
    a las personas por sus acciones. 
    Ademas que justificas siempre tu desicion con moralejas cortas"""
    respuesta_oraculo = obtener_respuesta(modelo, [
        {"role": "system", "content": descripcion_oraculo},
        {"role": "user", "content": historial_conversacion + """"
        ¿En base a la conducta de "Juan", qué diría el Oraculo?. 
        Solo El Oraculo debe dar una respuesta reflexiba."""}
    ])
    return("Oráculo: " + respuesta_oraculo)
# Aquí puedes usar el modelo de IA para generar respuestas de texto
def evaluaMensajeJuan(ultimaConversacion):
    modelo = 'gpt-3.5-turbo'
    response=evaluarJuan(modelo,ultimaConversacion)
    return response

def evaluaMensajeMaria(ultimaConversacion):
    modelo = 'gpt-3.5-turbo'
    response=evaluarMaria(modelo,ultimaConversacion)
    return response

def evaluaMensajeElena(ultimaConversacion):
    modelo = 'gpt-3.5-turbo'
    response=evaluarElena(modelo,ultimaConversacion)
    return response


def generate_response_juan(historial,evento):
    modelo = 'gpt-3.5-turbo'
    # Aquí iría tu lógica para generar respuestas basadas en el input del usuario
    response=conversacion_juan(modelo,historial,evento)
    return response
def generate_response_maria(user_input):
    modelo = 'gpt-3.5-turbo'
    # Aquí iría tu lógica para generar respuestas basadas en el input del usuario
    response=conversacion_maria(modelo,user_input)
    return response
def generate_response_elena(user_input):
    modelo = 'gpt-3.5-turbo'
    # Aquí iría tu lógica para generar respuestas basadas en el input del usuario
    response=conversacion_mama_juan(modelo,user_input)
    return response

def generate_response_oraculo(user_input):
    modelo = 'gpt-3.5-turbo'
    # Aquí iría tu lógica para generar respuestas basadas en el input del usuario
    response=conversacion_oraculo(modelo,user_input)
    return response

@app.route('/')
def principal():
    global situacionInicial
    global historial
    respuestaIA = generate_response_maria(situacionInicial)
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
