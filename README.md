# Sitio legal de Nexora

Se publica con GitHub Pages en **https://nexor4.github.io/**. Tiene lo que piden Google Play y AdMob para las apps de Nexora.

| URL | Qué es |
|---|---|
| `/` | Índice con todas las apps |
| `/<app>/` | Política de privacidad de cada app (es la URL que va en Play Console) |
| `/terminos/` | Términos de uso comunes a todas las apps |
| `/app-ads.txt` | Verificación de AdMob. Tiene que estar en la **raíz** del sitio que figura como "sitio web" del desarrollador en Play Console |

Apps: `jumpix`, `equira`, `buenos-habitos`, `medicinas-al-dia`, `paleta-de-colores`, `pomodoro`, `gestor-de-contrasenas`, `partyx`, `aura-battle`.

## Cómo actualizar

- **Jumpix y Equira**: su texto vive dentro de cada app, para que la app y la web digan lo mismo. Se edita allá y se copia la página:
  - Jumpix: editar `lib/legal/privacy_policy.dart`, correr `dart run tool/gen_site.dart` y copiar `site/index.html` a `jumpix/index.html`.
  - Equira: editar `gestor_gastos/lib/legal/privacy_policy.dart`, correr `dart run tool/export_privacy_policy.dart` y copiar `docs/politica-de-privacidad.html` a `equira/index.html`.
- **El resto, el índice y los términos**: editar `herramientas/generar.py` y correr `python herramientas/generar.py`.

Si una app cambia lo que hace con los datos (por ejemplo, si agrega analítica, inicio de sesión o anuncios), hay que actualizar su política **antes** de publicar esa versión.
