# middleware/filtro_preguntas.py
import re
from django.http import JsonResponse

class FiltroPreguntasMiddleware:
    """
    Middleware que bloquea preguntas fuera de contexto del Medidor Inteligente y sistema APR.
    Si la pregunta no contiene palabras clave, corta la request antes de llamar a OpenAI.
    """

    ALLOWED_KEYWORDS = [
        "medidor", "agua", "consumo", "cañería", "cañerias", "lectura",
        "boleta", "pago", "fuga", "apr", "ssr", "presión", "telemetría",
        "torre", "radiofrecuencia", "válvula"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Solo filtramos si es una consulta al asistente
        if request.path.startswith("/asistente_ai") and request.method == "POST":
            pregunta = (
                request.POST.get("pregunta")
                or request.body.decode("utf-8").lower()
            )

            if not any(keyword in pregunta.lower() for keyword in self.ALLOWED_KEYWORDS):
                return JsonResponse({
                    "respuesta": "⚠️ Solo puedo responder dudas relacionadas con el Medidor Inteligente y el sistema APR."
                })

        return self.get_response(request)
