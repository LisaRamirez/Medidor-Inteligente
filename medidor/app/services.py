# services.py

def obtener_respuesta(pregunta):
    q = pregunta.lower()

    # ----------------- Errores del Medidor -----------------
    errores = {
        "e-5": {"res": "E-5: Medidor cerrado por comando de cierre forzado.",
                 "keywords": ["e5", "error e5", "qué error es e5", "código e5", "fallo e5", "problema e5"]},
        "e-6": {"res": "E-6: Interferencia de imán detectada → Retire imanes cercanos.",
                 "keywords": ["e6", "error e6", "qué error es e6", "código e6", "fallo e6", "problema e6"]},
        "e-7": {"res": "E-7: Fallo de memoria → Apague y encienda el medidor, verifique baterías.",
                 "keywords": ["e7", "error e7", "qué error es e7", "código e7", "fallo e7", "problema e7"]},
        "e-8": {"res": "E-8: Fallo en válvula de corte.",
                 "keywords": ["e8", "error e8", "qué error es e8", "código e8", "fallo e8", "problema e8"]},
        "e-9": {"res": "E-9: Pérdida de agua o baja de presión (<10 PSI) → Verifique tuberías y sensor de presión.",
                 "keywords": ["e9", "error e9", "qué error es e9", "código e9", "fallo e9", "problema e9"]},
        "e-10": {"res": "E-10: Error de medición o al cerrar desde Hand-Held.",
                  "keywords": ["e10", "error e10", "qué error es e10", "código e10", "fallo e10", "problema e10"]}
    }

    for err in errores.values():
        for kw in err["keywords"]:
            if kw in q:
                return err["res"]

    # ----------------- Medidor Inteligente -----------------
    medidor_keywords = ["medidor inteligente", "lxsz-15", "caracteristicas medidor", "información medidor", "qué es medidor", "funcionamiento medidor"]
    for kw in medidor_keywords:
        if kw in q:
            return (
                "Medidor digital inteligente LXSZ-15 desarrollado en Chile, certificado por Dictuc – UC. "
                "Lecturas y cortes a 100+ metros mediante radiofrecuencia, sin necesidad de Internet. "
                "Detecta fugas, disminuye morosidad, ahorra tiempo y dinero. Funciona correctamente si se instala invertido. "
                "Ideal para cortes por sectores. | Especificaciones: Tipo: Eléctrico inalámbrico, Batería: Litio recargable 8500 mAh, "
                "Garantía: 1 año (solo cubre fallas de fábrica, no daños por temperatura extrema u otros accidentes), "
                "Material: Base plástica, esfera húmeda, Frecuencia: 470 MHz, Diámetro: ½” adaptable ¾”, "
                "Reloj: Análogo y digital, Certificación: ISO 4064, Caudal máximo: 2,5 m³/h, Temperatura soportada: 40°C"
            )

    # ----------------- Hand-Held A380 -----------------
    handheld_keywords = ["hand-held", "a380", "mando manual", "manual a380", "uso hand-held", "lector portátil", "como usar hand-held", "ingresar excel", "tomar lectura"]
    for kw in handheld_keywords:
        if kw in q:
            return (
                "Receptor manual inalámbrico A380 que recibe datos del medidor sin necesidad de Internet. "
                "Alcance de 1 a 500 metros. Permite corte de suministro a distancia y toma de lecturas. "
                "Para usarlo, mantenga presionado el botón rojo 3 segundos, luego ingrese a 'Task List' → 'ReadMeter', "
                "seleccione el archivo Excel enviado desde el PC, presione Enter y siga las indicaciones en pantalla para tomar lecturas. "
                "DoRead: cantidad de medidores listos, NoRead: medidores pendientes, FailRead: fallas en la lectura. "
                "Se carga por USB conectado al PC."
            )

    # ----------------- Software WaterMeterSystem -----------------
    wms_keywords = ["watermetersystem", "software wms", "software medidor", "funciones wms", "lecturas medidor", "ingresar excel", "crear sectores"]
    for kw in wms_keywords:
        if kw in q:
            return (
                "Software WaterMeterSystem gestiona la transferencia de datos entre PC y Hand-Held, organiza sectores y usuarios, "
                "toma lecturas de medidores y descarga revisiones en Excel. Para enviar archivos al Hand-Held se usa 'Test.exe' con 'PC → PDA', "
                "y para recibir lecturas 'PC ← PDA'. Se recomienda renombrar sectores con máximo 3 caracteres, ingresar datos de medidor y usuario sin espacios ni tildes."
            )

    # ----------------- Software APR SPA -----------------
    apr_keywords = ["software apr", "apr spa", "funciones apr", "plataforma apr", "gestión apr"]
    for kw in apr_keywords:
        if kw in q:
            return (
                "Software APR SPA es una plataforma 100% online para APR/SSR, que automatiza procesos administrativos, financieros y de control de agua. "
                "Funciones: gestión de clientes, consumos, subsidios y pagos; administración financiera completa; inventario de productos; "
                "emisión de boletas electrónicas o exentas; pago online vía Punto Blue / Transbank, presencial vía Caja Vecina; "
                "control de consumo por sector; facturación electrónica y notas de crédito. "
                "Permite acceso seguro desde cualquier dispositivo y ofrece capacitación y soporte 24/7."
            )

    # ----------------- Punto Blue -----------------
    puntoblue_keywords = ["punto blue", "pagos apr", "pagos puntoblue", "sistema de pagos", "modo de pago"]
    for kw in puntoblue_keywords:
        if kw in q:
            return (
                "Punto Blue es un sistema de pago para APR/SSR. Permite pagos online, registrados automáticamente en el Software APR, "
                "y pagos presenciales mediante Caja Vecina. Funciona integrado con Transbank y permite mayor flexibilidad en la gestión de cobros."
            )

    # ----------------- Videos y PDFs -----------------
    recursos = {
        "videos": [
            {"titulo": "Restablecer lectura analógica/digital", "archivo": "https://www.youtube.com/watch?v=bYpqIhpIfBo", "descripcion": "Video paso a paso para restablecer lectura analógica y digital."},
            {"titulo": "Toma de lectura manual", "archivo": "https://www.youtube.com/watch?v=bYpqIhpIfBo", "descripcion": "Cómo tomar lecturas manuales de medidores con Hand-Held."},
            {"titulo": "Abrir/Cerrar válvula", "archivo": "https://www.youtube.com/watch?v=bYpqIhpIfBo", "descripcion": "Tutorial para abrir y cerrar válvula a distancia desde Hand-Held."}
        ],
        "pdfs": [
            {"titulo": "CERTIFICADO-DITUC", "archivo": "/media/CERTIFICADO-DITUC.pdf", "descripcion": "Certificado de homologación Dictuc."},
            {"titulo": "FICHA-TECNICA", "archivo": "/media/FICHA-TECNICA.pdf", "descripcion": "Ficha técnica del medidor LXSZ-15."},
            {"titulo": "Manual de Uso Software HandHeld Parte 1", "archivo": "/media/Manual-de-Uso-Software-HandHeld-Parte-1.pdf", "descripcion": "Primer parte del manual de Hand-Held."},
            {"titulo": "Manual de Uso Software HandHeld Parte 2", "archivo": "/media/Manual-de-Uso-Software-HandHeld-Parte-2.pdf", "descripcion": "Segunda parte del manual de Hand-Held."},
            {"titulo": "Manual de Uso Software HandHeld Parte 3", "archivo": "/media/Manual-de-Uso-Software-HandHeld-Parte-3.pdf", "descripcion": "Tercera parte del manual de Hand-Held."},
            {"titulo": "medidas_heladas", "archivo": "/media/medidas_heladas.pdf", "descripcion": "Medidas preventivas contra heladas en sistemas de agua."},
            {"titulo": "Informe de ensayos", "archivo": "/media/Informe-de-ensayos.pdf", "descripcion": "Informe de ensayos técnicos de medidores."},
            {"titulo": "Informe sanitaria Interagua Ecuador", "archivo": "/media/INFORME-SANITARIA-INTERAGUA-ECUADOR.pdf", "descripcion": "Informe de análisis sanitaria Interagua Ecuador."}
        ]
    }

    ayuda_keywords = ["manual", "pdf", "video", "descargar", "tutorial"]
    for kw in ayuda_keywords:
        if kw in q:
            respuesta = "Panel de ayuda rápida:\n\nVideos:\n"
            for v in recursos["videos"]:
                respuesta += f"- {v['titulo']}: {v['descripcion']} (ver en {v['archivo']})\n"
            respuesta += "\nDocumentos PDF:\n"
            for p in recursos["pdfs"]:
                respuesta += f"- {p['titulo']}: {p['descripcion']} (descargar en {p['archivo']})\n"
            return respuesta

    # ----------------- Default -----------------
    return "Lo siento, no tengo información sobre eso. Por favor contacte a soporte para mayor asistencia."
