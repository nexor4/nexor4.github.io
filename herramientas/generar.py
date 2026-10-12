"""Genera las páginas legales de las apps de Nexora (GitHub Pages).

Uso:  python herramientas/generar.py      (desde la carpeta del repo)

Jumpix y Equira NO se generan acá: su texto vive dentro de cada app (para que
la app y la web digan lo mismo) y la página se copia desde su proyecto:
  - Jumpix:  dart run tool/gen_site.dart  ->  copiar site/index.html a jumpix/index.html
  - Equira:  dart run tool/export_privacy_policy.dart  ->  copiar docs/politica-de-privacidad.html a equira/index.html
"""
import html
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTACTO = "nexor4.uy@gmail.com"
FECHA = "12 de octubre de 2026"
SITIO = "https://nexor4.github.io"

GOOGLE_PRIV = "https://policies.google.com/privacy"
GOOGLE_PARTNERS = "https://policies.google.com/technologies/partner-sites"


def p(*textos):
    return [("p", t) for t in textos]


def lista(*items):
    return [("ul", list(items))]


def publicidad(nombre, donde_opciones):
    return [
        ("Publicidad (Google AdMob)", p(
            f"{nombre} muestra anuncios a través de Google AdMob (Google LLC). Para mostrarlos, medir su rendimiento "
            "y prevenir fraude, Google y sus socios pueden recolectar y usar identificadores del dispositivo "
            "(como el ID de publicidad), la dirección IP y datos de interacción con los anuncios. Esa recolección "
            f"la hace Google según su propia política, no {nombre} directamente.",
            f"Política de privacidad de Google: {GOOGLE_PRIV}",
            f"Cómo usa Google los datos de las apps que usan sus servicios: {GOOGLE_PARTNERS}",
            "Podés restablecer o desactivar el ID de publicidad desde los ajustes de Google de tu dispositivo.",
        )),
        ("Consentimiento (RGPD, Reino Unido y otras regiones)", p(
            "Antes de cargar el primer anuncio, la app consulta si en tu región hace falta tu consentimiento "
            "(Espacio Económico Europeo, Reino Unido, Suiza y otras) y, si corresponde, te muestra el formulario "
            "de Google (User Messaging Platform). Recién después de esa respuesta se cargan anuncios.",
            f"Podés revisar o cambiar tu elección en cualquier momento desde {donde_opciones} "
            "(la opción solo aparece en las regiones donde corresponde).",
        )),
    ]


def comunes(nombre, menores):
    return [
        ("Con quién compartimos datos", p(
            "No vendemos ni compartimos datos tuyos. Nexora no tiene servidores que reciban la información que "
            f"cargás en {nombre}: queda en tu dispositivo. Lo único que sale del dispositivo es lo que procesa "
            "el SDK de anuncios de Google, como se describe más arriba (si la app tiene anuncios).",
        )),
        ("Cuánto tiempo se guardan y cómo borrarlos", p(
            "Los datos quedan en tu dispositivo hasta que los borres desde la app, uses \"Borrar datos\" de la app "
            "en los ajustes del sistema o desinstales la app. Como no guardamos nada en servidores, no tenemos "
            "datos tuyos que eliminar.",
        )),
        ("Menores de edad", p(menores)),
        ("Cambios en esta política", p(
            "Si la app cambia lo que hace con los datos, vamos a actualizar esta página antes de publicar el cambio, "
            "con su nueva fecha.",
        )),
        ("Contacto", p(f"Por cualquier consulta sobre privacidad escribinos a {CONTACTO}.")),
    ]


MENORES_GENERAL = ("La app no está dirigida a menores de 13 años y no recolecta a sabiendas datos personales de "
                   "ellos, más allá de lo que hace el SDK de anuncios de Google bajo su propia configuración.")
MENORES_SIN_ADS = "La app no está dirigida a menores de 13 años y no recolecta datos personales de nadie."

APPS = {
    "buenos-habitos": dict(
        nombre="Buenos Hábitos",
        resumen="Buenos Hábitos es una app para crear hábitos, seguir tu progreso y mantener la racha. No pide "
                "cuenta ni datos personales: tus hábitos quedan guardados en tu teléfono, cifrados.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Los hábitos que creás (nombre, días, horario del recordatorio y plazo), tu historial de cumplimiento, "
                "las rachas y la mejor racha de cada hábito, y tus ajustes. No pedimos nombre, correo, ubicación, "
                "contactos ni ningún otro dato personal.",
            )),
            ("Dónde se guardan y cómo se protegen", p(
                "En el almacenamiento interno de la app, en tu dispositivo, cifrados con AES-256. La clave de cifrado "
                "se genera en tu teléfono y se guarda en el almacén seguro del sistema (Android Keystore); nunca sale "
                "del dispositivo.",
            )),
            ("Recordatorios y permisos", lista(
                "Notificaciones: para avisarte cuando toca cumplir un hábito. Se programan en tu dispositivo; en Android 13 "
                "o superior el sistema te pide permiso.",
                "Alarmas exactas: para que el aviso llegue a la hora justa. Android te pide permiso; si no lo das, "
                "el aviso puede llegar con algunos minutos de demora.",
                "Inicio del dispositivo: para volver a programar los recordatorios después de reiniciar el teléfono.",
                "Tarea en segundo plano: una revisión periódica, dentro del teléfono, de los plazos de tus hábitos.",
                "Vibración: para la celebración cuando tu mascota de racha evoluciona.",
                "Internet: solo lo usa el SDK de anuncios.",
            )),
        ] + publicidad("Buenos Hábitos", "la opción \"Opciones de privacidad\" de la app"),
        menores=MENORES_GENERAL,
    ),
    "medicinas-al-dia": dict(
        nombre="Medicinas al Día",
        resumen="Medicinas al Día es una app para registrar tus medicamentos y recibir recordatorios para tomarlos "
                "a tiempo. No pide cuenta ni datos personales: lo que cargás queda en tu teléfono.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Los medicamentos que cargás (nombre, dosis, horarios y frecuencia) y el registro de tomas. Esta "
                "información puede considerarse un dato de salud: por eso nunca sale de tu dispositivo y Nexora no "
                "tiene acceso a ella. No pedimos nombre, correo, ubicación ni ningún otro dato personal.",
            )),
            ("Dónde se guardan", p(
                "En el almacenamiento interno de la app, en tu dispositivo. Si tu teléfono tiene activada la copia de "
                "seguridad de Android, el sistema puede incluir esos datos en tu copia de Google; esa copia la "
                "administra Google según tu configuración.",
            )),
            ("Recordatorios y permisos", lista(
                "Notificaciones: para avisarte a la hora de cada toma. Se programan en tu dispositivo; en Android 13 o "
                "superior el sistema te pide permiso.",
                "Alarmas exactas: para que el aviso llegue a la hora justa. Android te pide permiso; si no lo das, "
                "el aviso puede llegar con algunos minutos de demora.",
                "Inicio del dispositivo: para volver a programar los avisos después de reiniciar el teléfono.",
                "Vibración: para los avisos.",
                "Internet: solo lo usa el SDK de anuncios.",
            )),
            ("Aviso importante", p(
                "Medicinas al Día es una ayuda para recordar. No da indicaciones médicas ni reemplaza la consulta con "
                "un profesional de la salud. Ante cualquier duda sobre tu tratamiento, consultá a tu médico.",
            )),
        ] + publicidad("Medicinas al Día", "la opción \"Opciones de privacidad\" de la app"),
        menores=MENORES_GENERAL,
    ),
    "paleta-de-colores": dict(
        nombre="Paleta de Colores",
        resumen="Paleta de Colores es una app para crear, explorar y guardar paletas de colores. No pide cuenta ni "
                "datos personales: tus paletas quedan guardadas en tu teléfono.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Las paletas que creás o guardás (nombres y colores) y tus preferencias. No pedimos nombre, correo, "
                "ubicación ni ningún otro dato personal. Si copiás un código de color, se copia al portapapeles de "
                "tu teléfono.",
            )),
            ("Dónde se guardan", p("En el almacenamiento interno de la app, en tu dispositivo.")),
            ("Permisos", lista("Internet: solo lo usa el SDK de anuncios.")),
        ] + publicidad("Paleta de Colores", "la opción \"Opciones de privacidad\" de la app"),
        menores=MENORES_GENERAL,
    ),
    "pomodoro": dict(
        nombre="Temporizador Pomodoro",
        resumen="Temporizador Pomodoro es una app para trabajar en bloques de tiempo con descansos. No pide cuenta "
                "ni datos personales y no envía tus ajustes a ningún servidor.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Solo tus ajustes (duración del trabajo, de los descansos y cantidad de módulos), guardados en tu "
                "dispositivo.",
            )),
            ("Permisos", lista(
                "Notificaciones: para avisarte cuando termina cada fase. Se programan en tu dispositivo; en Android 13 "
                "o superior el sistema te pide permiso.",
                "Alarmas exactas: para que el aviso llegue justo cuando termina la fase.",
                "Mantener la pantalla encendida mientras corre una sesión.",
                "Internet: solo lo usa el SDK de anuncios.",
            )),
        ] + publicidad("Temporizador Pomodoro", "\"Opciones de privacidad\" en la pantalla de configuración"),
        menores=MENORES_GENERAL,
    ),
    "gestor-de-contrasenas": dict(
        nombre="Gestor de Contraseñas",
        resumen="Gestor de Contraseñas genera contraseñas seguras y guarda tus cuentas en tu propio teléfono, "
                "cifradas. No tenemos servidores: nunca vemos tus contraseñas.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Las cuentas que guardás (servicio, usuario y contraseña) y el código de acceso que elegís para abrir "
                "la app. No pedimos nombre, correo, ubicación ni ningún otro dato personal.",
            )),
            ("Dónde se guardan y cómo se protegen", lista(
                "Las cuentas se guardan cifradas en tu dispositivo, con una clave protegida por el almacén seguro del "
                "sistema (Android Keystore). Nunca se envían a ningún lado.",
                "El código de acceso no se guarda: se guarda solo una huella criptográfica (hash con sal) para "
                "verificarlo. Después de varios intentos fallidos, la app se bloquea por un tiempo creciente.",
                "La copia de seguridad automática de Android está desactivada para esta app: tus contraseñas no se "
                "suben a Google Drive.",
                "La app impide capturas de pantalla y oculta su contenido en el selector de apps recientes.",
            )),
            ("Huella o rostro", p(
                "Si usás el desbloqueo con huella o rostro, la verificación la hace el sistema operativo. La app nunca "
                "accede a tus datos biométricos: solo recibe si la verificación salió bien o no.",
            )),
            ("Portapapeles", p(
                "Cuando tocás \"copiar\", la contraseña se copia al portapapeles de tu teléfono, donde otras apps "
                "podrían leerla. Copiá solo cuando lo necesites.",
            )),
            ("Permisos", lista(
                "Biometría: para el desbloqueo con huella o rostro.",
                "Internet: solo lo usa el SDK de anuncios. Tus contraseñas nunca salen del dispositivo.",
            )),
        ] + publicidad("Gestor de Contraseñas", "\"Privacidad de anuncios\" en el menú principal"),
        menores=MENORES_GENERAL,
    ),
    "partyx": dict(
        nombre="PartyX",
        resumen="PartyX es una app de minijuegos para jugar con amigos. No pide cuenta ni datos personales: lo que "
                "cargás queda en tu teléfono.",
        secciones=[
            ("Qué datos guarda la app", p(
                "Las opciones de la ruleta y su historial, los nombres de jugadores y grupos que cargás, las "
                "categorías propias, los mejores puntajes y tus ajustes. Todo se guarda en tu dispositivo. No pedimos "
                "correo, ubicación ni ningún otro dato personal.",
            )),
            ("Sensores y permisos", lista(
                "Acelerómetro: en \"Adivina la Palabra\", para detectar cuando inclinás el teléfono. Se usa en el "
                "momento y no se guarda.",
                "Internet: solo lo usa el SDK de anuncios.",
            )),
        ] + publicidad("PartyX", "\"Opciones de privacidad\" en la configuración de la Ruleta"),
        menores=MENORES_GENERAL,
    ),
    "aura-battle": dict(
        nombre="Aura Battle",
        resumen="Aura Battle es un juego de cartas que funciona sin conexión. No pide cuenta, no tiene publicidad, "
                "no usa analítica y no envía tu partida a ningún servidor.",
        secciones=[
            ("Qué datos guarda el juego", p(
                "Tu partida (nivel, cartas, equipo, cofres, monedas, gemas, trofeos y progreso de la historia) y tus "
                "ajustes (música, efectos, vibración y accesibilidad), solo en tu dispositivo. También guarda un "
                "registro local de errores para diagnóstico, que nunca se envía. No pedimos nombre, "
                "correo, ubicación ni ningún otro dato personal.",
                "Si tenés activada la copia de seguridad de Android, el sistema puede incluir tu partida en tu copia de "
                "Google para que no la pierdas al cambiar de teléfono. Esa copia la administra Google según tu "
                "configuración; el juego no accede a ella.",
            )),
            ("Compras dentro de la app", p(
                "Si el juego ofrece compras con dinero real, el pago lo procesa Google Play según sus propias "
                "condiciones y política de privacidad. El juego no recibe ni guarda datos de pago: solo recibe la "
                "confirmación de la compra y guarda en tu dispositivo el número de cada compra para no entregarla dos "
                "veces.",
            )),
            ("Permisos", lista(
                "Vibración: en los momentos fuertes del juego (se apaga en los ajustes).",
                "Facturación de Google Play e internet: solo para procesar compras dentro de la app. El juego no envía "
                "tu partida ni otros datos por internet.",
            )),
        ],
        menores=MENORES_SIN_ADS,
        borrar="Desde Perfil → \"Reiniciar progreso\" borrás tu partida. Desinstalar el juego borra todos sus datos del "
               "dispositivo.",
    ),
}

ORDEN_INDICE = [
    ("jumpix", "Jumpix", "Juego"), ("aura-battle", "Aura Battle", "Juego"), ("partyx", "PartyX", "Juego"),
    ("equira", "Equira – Gestor de Gastos", "App"), ("buenos-habitos", "Buenos Hábitos", "App"),
    ("medicinas-al-dia", "Medicinas al Día", "App"), ("gestor-de-contrasenas", "Gestor de Contraseñas", "App"),
    ("paleta-de-colores", "Paleta de Colores", "App"), ("pomodoro", "Temporizador Pomodoro", "App"),
]

CSS_REL = "../estilo.css"


def linkificar(texto):
    out = []
    for parte in texto.split(" "):
        limpio = parte.rstrip(".,)")
        cola = parte[len(limpio):]
        if limpio.startswith("https://"):
            out.append(f'<a href="{html.escape(limpio)}">{html.escape(limpio)}</a>{html.escape(cola)}')
        elif "@" in limpio and limpio == CONTACTO:
            out.append(f'<a href="mailto:{limpio}">{limpio}</a>{html.escape(cola)}')
        else:
            out.append(html.escape(parte))
    return " ".join(out)


def bloque(item):
    tipo, contenido = item
    if tipo == "p":
        return f"<p>{linkificar(contenido)}</p>"
    return "<ul>" + "".join(f"<li>{linkificar(x)}</li>" for x in contenido) + "</ul>"


def pagina(titulo, cuerpo, css=CSS_REL, volver=True):
    nav = '<p class="volver"><a href="../">← Todas las apps de Nexora</a></p>' if volver else ""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{nav}
{cuerpo}
</main>
</body>
</html>
"""


def politica(slug, app):
    nombre = app["nombre"]
    secciones = [("Resumen", p(app["resumen"]))] + app["secciones"] + comunes(nombre, app["menores"])
    if "borrar" in app:
        secciones = [(t, p(app["borrar"]) if t.startswith("Cuánto tiempo") else c) for t, c in secciones]
    cuerpo = [f"<h1>Política de privacidad de {html.escape(nombre)}</h1>",
              f'<p class="fecha">Vigente desde el {FECHA}. Responsable: Nexora (desarrollador independiente, '
              f'Uruguay) · <a href="mailto:{CONTACTO}">{CONTACTO}</a></p>']
    for titulo, items in secciones:
        cuerpo.append(f"<h2>{html.escape(titulo)}</h2>")
        cuerpo.extend(bloque(i) for i in items)
    cuerpo.append('<p class="pie">Ver también los <a href="../terminos/">términos de uso</a> de las apps de Nexora.</p>')
    return pagina(f"{nombre} — Política de privacidad", "\n".join(cuerpo))


TERMINOS = [
    ("Aceptación", p(
        "Estos términos se aplican a todas las apps y juegos publicados por Nexora en Google Play (en adelante, "
        "\"las apps\"). Al descargar o usar una app aceptás estos términos. Si no estás de acuerdo, no la uses.",
    )),
    ("Licencia de uso", p(
        "Nexora te da una licencia personal, no exclusiva, intransferible y revocable para usar las apps en tus "
        "dispositivos, con fines personales y no comerciales. No podés copiar, modificar, descompilar, revender ni "
        "distribuir las apps o sus contenidos, salvo lo que permita la ley aplicable.",
    )),
    ("Tus datos y tus copias", p(
        "Las apps guardan la información que cargás en tu propio dispositivo (ver la política de privacidad de cada "
        "app). Sos responsable de esa información y de hacer copias de seguridad cuando la app lo permita: si "
        "desinstalás la app, borrás sus datos o perdés el dispositivo, Nexora no puede recuperarlos.",
    )),
    ("Uso responsable", lista(
        "Medicinas al Día es una ayuda para recordar y no da indicaciones médicas ni reemplaza la consulta con un "
        "profesional de la salud.",
        "Equira es una herramienta de registro personal y no constituye asesoramiento financiero.",
        "Gestor de Contraseñas guarda tus contraseñas en el dispositivo: cuidá tu código de acceso y el acceso a tu "
        "teléfono.",
        "Usá las apps de acuerdo con la ley y sin intentar afectar su funcionamiento ni el de los servicios de "
        "terceros que integran.",
    )),
    ("Publicidad", p(
        "Algunas apps son gratuitas y se financian con anuncios de Google AdMob. Los anuncios son de terceros: Nexora "
        "no controla su contenido ni se responsabiliza por los productos o servicios que ofrecen.",
    )),
    ("Compras dentro de las apps", p(
        "Algunas apps pueden ofrecer compras opcionales (por ejemplo, gemas o monedas de un juego). Los pagos los "
        "procesa Google Play con sus propias condiciones. Los objetos virtuales no tienen valor monetario fuera de la "
        "app, no son canjeables por dinero y pueden perderse si desinstalás la app o borrás sus datos. Los reembolsos "
        f"se rigen por la política de Google Play: https://support.google.com/googleplay/answer/2479637",
    )),
    ("Propiedad intelectual", p(
        "Las apps, su código, diseño, nombres, logos y contenidos son de Nexora o de sus respectivos titulares y se "
        "usan con permiso o bajo licencias libres (los créditos se indican dentro de cada app cuando corresponde).",
    )),
    ("Disponibilidad y cambios", p(
        "Las apps se ofrecen \"tal cual\". Podemos actualizarlas, cambiar funciones o dejar de ofrecerlas. Hacemos lo "
        "posible para que funcionen bien, pero no garantizamos que estén libres de errores o interrupciones.",
    )),
    ("Limitación de responsabilidad", p(
        "En la medida en que lo permita la ley, Nexora no es responsable por daños indirectos, pérdida de datos o "
        "lucro cesante derivados del uso o la imposibilidad de uso de las apps. Nada de esto limita los derechos que "
        "te reconozca la ley de defensa del consumidor aplicable.",
    )),
    ("Cambios en estos términos", p(
        "Si cambiamos estos términos vamos a publicar la nueva versión en esta página con su fecha. Seguir usando las "
        "apps después de un cambio implica aceptarlo.",
    )),
    ("Ley aplicable y contacto", p(
        "Estos términos se rigen por las leyes de la República Oriental del Uruguay. Por cualquier consulta escribinos "
        f"a {CONTACTO}.",
    )),
]


def terminos():
    cuerpo = ["<h1>Términos de uso de las apps de Nexora</h1>",
              f'<p class="fecha">Vigentes desde el {FECHA} · <a href="mailto:{CONTACTO}">{CONTACTO}</a></p>']
    for titulo, items in TERMINOS:
        cuerpo.append(f"<h2>{html.escape(titulo)}</h2>")
        cuerpo.extend(bloque(i) for i in items)
    return pagina("Nexora — Términos de uso", "\n".join(cuerpo))


def indice():
    filas = "\n".join(
        f'<li><a href="{slug}/"><strong>{html.escape(nombre)}</strong></a> <span class="tipo">{tipo}</span>'
        f'<br><span class="sub">Política de privacidad</span></li>'
        for slug, nombre, tipo in ORDEN_INDICE)
    cuerpo = f"""<h1>Nexora</h1>
<p class="lema">Ideas · Tech · Futuro</p>
<p>Apps y juegos para Android hechos por Nexora, desarrollador independiente de Uruguay.</p>
<h2>Políticas de privacidad</h2>
<ul class="apps">
{filas}
</ul>
<h2>Términos de uso</h2>
<p><a href="terminos/">Términos de uso de las apps de Nexora</a></p>
<h2>Contacto</h2>
<p><a href="mailto:{CONTACTO}">{CONTACTO}</a></p>"""
    return pagina("Nexora — Apps y juegos", cuerpo, css="estilo.css", volver=False)


ESTILO = """:root { --tinta: #1d1d1f; --suave: #5f6577; --acento: #6d4aff; --fondo: #ffffff; --linea: #e6e8f0; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--fondo); color: var(--tinta);
       font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; line-height: 1.6; }
main { max-width: 720px; margin: 0 auto; padding: 24px 16px 64px; }
h1 { font-size: 1.7rem; line-height: 1.25; margin: 8px 0 0; }
h2 { font-size: 1.12rem; margin-top: 1.9rem; }
a { color: var(--acento); word-break: break-word; }
.fecha, .sub, .lema { color: var(--suave); }
.lema { letter-spacing: .25em; text-transform: uppercase; font-size: .85rem; margin-top: 0; }
.volver { font-size: .9rem; margin: 0 0 12px; }
.pie { margin-top: 2.4rem; padding-top: 1rem; border-top: 1px solid var(--linea); color: var(--suave); }
ul.apps { list-style: none; padding: 0; }
ul.apps li { padding: 12px 0; border-bottom: 1px solid var(--linea); }
.tipo { font-size: .75rem; color: var(--suave); border: 1px solid var(--linea); border-radius: 99px; padding: 1px 8px; margin-left: 6px; }
"""


def escribir(ruta, contenido):
    ruta = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)
    print("escrito", os.path.relpath(ruta, RAIZ))


def main():
    escribir("estilo.css", ESTILO)
    escribir("index.html", indice())
    escribir("terminos/index.html", terminos())
    for slug, app in APPS.items():
        escribir(f"{slug}/index.html", politica(slug, app))
    for slug in ("jumpix", "equira"):
        if not os.path.exists(os.path.join(RAIZ, slug, "index.html")):
            print(f"FALTA {slug}/index.html: copialo desde su proyecto (ver docstring).")


if __name__ == "__main__":
    main()
