from django.shortcuts import render, redirect
from .models import MensajeBot
from .forms import BotForm
from django.contrib.auth.decorators import login_required



RESPUESTAS = {

    "para que sirve python": "Python se utiliza en desarrollo web, ciencia de datos, inteligencia artificial y más.",
    "python que es": "Python es un lenguaje de programación de alto nivel, claro y legible.",
    "que es python": "Python es un lenguaje de programación usado en múltiples áreas tecnológicas.",

    "que utilidad tiene": "Puedo ayudarte si me indicas el tema concreto.",
    "como funciona": "Puedo explicarte el funcionamiento si me das contexto.",
    "como estas": "Estoy bien, listo para ayudarte en lo que necesites.",
    "como te llamas": "Puedes llamarme BotJuan, tu asistente virtual.",
    "necesito ayuda": "Claro, ¿con qué puedo ayudarte?",
    "me ayudas": "Por supuesto, dime qué necesitas.",
    "cuentame algo": "Puedo contarte datos curiosos o ayudarte con tus contactos.",
    "que puedes hacer": "Puedo responder preguntas y ayudarte con contactos básicas.",
    "que haces": "Estoy aquí esperando tus instrucciones.",
    "estas disponible": "Siempre disponible para ayudarte.",
    "estas ahi": "Sí, aquí estoy, listo para ayudarte.",

    "informame": "Claro, ¿sobre qué tema deseas información?",
    "actualizacion": "Puedo darte una actualización si me dices sobre qué.",
    "progreso": "Puedo indicarte el progreso si me dices qué estás siguiendo.",
    "estado": "Puedo revisar el estado si me das más detalles.",
    "instrucciones": "Puedo guiarte paso a paso si lo necesitas.",
    "detalles": "Puedo darte más detalles si me indicas qué parte te interesa.",
    "explicacion": "Con gusto, ¿qué parte deseas entender mejor?",
    "orientacion": "Puedo orientarte en la dirección correcta.",
    "sugerencia": "Puedo darte sugerencias si me explicas tu objetivo.",
    "recomendacion": "Puedo recomendarte opciones según lo que necesites.",
    "opinion": "Puedo darte información objetiva si lo deseas.",
    "problema": "Puedo ayudarte a resolverlo si me das más detalles.",
    "duda": "Estoy aquí para aclarar cualquier duda.",
    "consulta": "Estoy listo para atender tu consulta.",
    "urgente": "Entiendo, procederé lo más rápido posible.",
    "urgencia": "Comprendido, actuaré con rapidez.",
    "importante": "Comprendido, trataré tu mensaje con prioridad.",
    "solucion": "Buscaré la mejor solución posible.",
    "mostrar": "Con gusto, ¿qué deseas que muestre?",
    "buscar": "Puedo ayudarte a buscar lo que necesites.",
    "ver": "Puedo mostrarte información si me dices qué quieres ver.",
    "expresar": "Puedo ayudarte a formularlo si me das contexto.",
    "confirmar": "Confirmado, procedo.",
    "aceptar": "Perfecto, aceptado.",
    "rechazar": "De acuerdo, lo rechazo.",
    "opcion": "Puedo ayudarte a elegir la mejor opción.",
    "preferencia": "Puedo adaptarme a tus preferencias.",
    "configurar": "Puedo ayudarte a configurarlo si me das detalles.",
    "ajustar": "De acuerdo, haré los ajustes necesarios.",
    "modificar": "Puedo ayudarte a modificar lo que necesites.",
    "actualizar": "Procedo a actualizarlo.",
    "revisar": "Puedo revisarlo si me das más información.",
    "analizar": "Puedo analizarlo si me explicas el contexto.",
    "evaluar": "Puedo evaluar la situación si me das detalles.",
    "comprobar": "Puedo comprobarlo por ti.",
    "verificar": "Procedo a verificarlo.",
    "confirmado": "Perfecto, queda confirmado.",

    "python": "Python es un lenguaje de programación muy versátil y fácil de aprender.",
    "hola": "Muy buenas, ¿en qué puedo ayudarte hoy?",
    "buenas": "Buenas, un placer atenderte.",
    "saludos": "Saludos, ¿qué necesitas?",
    "buenos dias": "Buenos días, espero que estés teniendo una buena jornada.",
    "buenas tardes": "Buenas tardes, ¿cómo puedo ayudarte?",
    "buenas noches": "Buenas noches, ¿en qué puedo asistirte?",
    "que tal": "Estoy funcionando correctamente, gracias por preguntar.",
    "gracias": "No hay de qué, estoy para ayudarte.",
    "muchas gracias": "Con gusto, para eso estoy.",
    "te lo agradezco": "Me alegra ser de ayuda.",
    "perdon": "No te preocupes, todo está bien.",
    "disculpa": "No pasa nada, dime qué necesitas.",
    "ayuda": "Claro, ¿qué necesitas exactamente?",
    "informacion": "Puedo darte información sobre varios temas, ¿qué buscas?",
    "perfecto": "Me alegra que te parezca bien.",
    "entendido": "Perfecto, procedo con ello.",
    "correcto": "De acuerdo, tomo nota.",
    "muy bien": "Excelente, seguimos adelante.",
    "de acuerdo": "Perfecto, seguimos.",
    "vale": "Perfecto, continuemos.",
    "listo": "Perfecto, procedamos.",
    "hecho": "Excelente, continuemos.",
    "terminado": "Perfecto, ¿algo más en lo que pueda ayudarte?",
    "continuar": "De acuerdo, seguimos.",
    "sigue": "Perfecto, continúo.",
    "adelante": "Muy bien, procedo.",
    "espera": "Claro, tómate tu tiempo.",
    "un momento": "Sin problema, aquí estaré.",
    "vuelvo": "Perfecto, te espero.",
    "estoy aqui": "Bienvenido de nuevo, ¿en qué seguimos?",
    "empezar": "Muy bien, comencemos.",
    "iniciar": "De acuerdo, iniciemos el proceso.",
    "comenzar": "Perfecto, empezamos.",
    "finalizar": "De acuerdo, doy por finalizado el proceso.",
    "cerrar": "Perfecto, cierro lo que indiques.",
    "abrir": "De acuerdo, abro lo solicitado.",
    "ok": "De acuerdo, seguimos adelante."
}


@login_required
def chat(request):

    if request.method == "POST":
        form = BotForm(request.POST)
        if form.is_valid():
            mensaje_usuario = form.save(commit=False)
            mensaje_usuario.autor = "usuario"
            mensaje_usuario.save()

            texto = mensaje_usuario.texto.lower()

            for palabra, respuesta in RESPUESTAS.items():
                if palabra in texto:
                    MensajeBot.objects.create(
                        texto=respuesta,
                        autor="bot"
                    )
                    break

            return redirect('/bot/')

    else:
        form = BotForm()

    mensajes = MensajeBot.objects.all().order_by('fecha')

    return render(request, "bot/chat.html", {"form": form, "mensajes": mensajes})

@login_required
def borrar_chat(request):
    MensajeBot.objects.all().delete()
    return redirect('/bot/')
