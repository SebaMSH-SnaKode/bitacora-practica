# 03 — Las presentaciones semanales

Cada lunes, de 10:00 a 10:30, el practicante presenta en PowerPoint lo que hizo la semana anterior. **Ocho minutos de exposición, siete de preguntas.**

No es un adorno del programa. Es una de sus dos columnas, junto al código.

## Por qué pesa tanto

- **Es lo que más lo va a diferenciar.** Hay miles de juniors que programan parecido. Los que explican bien lo que hicieron son pocos, y son los que ascienden.
- **Explicar es la prueba de entender.** Si no puede explicar en voz alta lo que programó, no lo aprendió. Es el mejor detector que tiene el mentor y no cuesta nada.
- **Resuelve el problema del calendario.** Entre el martes y el lunes hay seis días de pausa. Armar la presentación lo obliga a volver sobre lo aprendido justo antes de volver. La presentación *es* el repaso.
- **Es material del informe de práctica.** Diez presentaciones más diez semanas de bitácora y el informe de noviembre se escribe solo.

## Formato fijo — cinco diapositivas

Siempre las mismas. La restricción es intencional: cuando el formato no cambia, el esfuerzo se va al contenido y no al diseño.

| # | Diapositiva | Qué va |
|---|---|---|
| 1 | **Qué construí** | Una captura de pantalla de lo que funciona. Nada de texto. |
| 2 | **Cómo funciona** | Un diagrama hecho por él. Cajas y flechas. Esta es la diapositiva difícil y la que más enseña. |
| 3 | **Qué me costó** | Un problema concreto, cómo lo diagnosticó, cómo lo resolvió. |
| 4 | **Qué aprendí que no sabía** | Dos o tres ideas, en sus palabras. Prohibido copiar definiciones. |
| 5 | **Qué viene** | Qué queda pendiente y qué sigue la próxima semana. |

### Reglas de las diapositivas

- **Máximo 15 palabras por diapositiva.** Una diapositiva no es un documento; si se puede leer sola, sobra el expositor.
- **Máximo una diapositiva con código, y de 10 líneas.** Capturas de código completo, nunca.
- **Prohibido leer.** Si necesita leer, es que no lo entiende todavía.
- **Termina con una pregunta al público**, no con "eso sería".
- **Si no sabe responder algo, dice "no sé, lo averiguo".** Se valora más que inventar. Esto hay que decírselo explícitamente el primer día, porque nadie se atreve la primera vez.

## Calendario de presentaciones

| # | Fecha | Tema | Audiencia |
|---|---|---|---|
| **P1** | Lun 28 sep | Qué es programar, y mi primer programa | Mentor |
| **P2** | Lun 5 oct | Qué es Git y por qué existe (cuenta la historia del `informe_final_v2_AHORA_SI.doc`) | Mentor |
| **P3** | Mar 13 oct* | El viaje de un request: qué pasa cuando escribo una URL | Mentor + 1 invitado |
| **P4** | Lun 19 oct | Cómo se construye una página web | Mentor + 1 invitado |
| **P5** | Lun 26 oct | Python y JavaScript: qué cambia y qué no | **Equipo** |
| **P6** | Lun 2 nov | Cómo se guardan los datos de Datamédica (su modelo, en diagrama) | **Equipo** |
| **P7** | Lun 9 nov | Qué es una API y por qué todo el mundo las usa | **Equipo** |
| **P8** | Lun 16 nov | **Demo de mini-OT** — presentación de producto, no técnica | **Equipo** |
| **P9** | Lun 23 nov | Dónde sí y dónde no conviene usar IA generativa | **Equipo** |
| **P10** | Lun 30 nov | **Presentación final** (20 min): qué construí, qué aprendí, qué me falta | **Equipo + jefatura** |

\* P3 se corre al martes 13 por el feriado del lunes 12.

**La progresión de audiencia es deliberada.** Empieza presentándole al mentor, que es seguro, y termina frente a la jefatura. Subir la exigencia de golpe en la semana 1 lo bloquea; subirla de a poco lo entrena.

### Dos presentaciones distintas a las demás

- **P8 (demo de mini-OT)** es una presentación *de producto*: qué problema resuelve y a quién le sirve, sin hablar de código. Es un género completamente distinto y es el que más le va a servir en consultoría.
- **P10 (final)** dura 20 minutos e incluye lo que **no** alcanzó a aprender. Que un junior sepa nombrar sus propios vacíos vale más que cualquier certificado.

## Rúbrica de comunicación

Se evalúa después de cada presentación, junto con él, en dos minutos. De 1 a 4.

| Criterio | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **Claridad** | No se entiende qué hizo | Se entiende con esfuerzo | Se entiende bien | Lo entendería alguien no técnico |
| **Estructura** | Salta de un tema a otro | Se pierde a ratos | Sigue el formato | Cuenta una historia con principio y final |
| **No leer** | Lee todo | Lee la mitad | Mira las notas de reojo | Habla mirando al público |
| **Diagrama** | No hay | Copiado de internet | Propio pero confuso | Propio y explica el sistema |
| **Preguntas** | Se bloquea | Responde a medias | Responde bien | Dice "no sé" cuando corresponde y ofrece averiguarlo |
| **Tiempo** | Se pasa o no llega | ±3 min | ±1 min | Justo |

**Meta:** llegar a P10 con promedio 3 o más. Empezar en 1 o 2 es completamente normal y hay que decírselo.

### Cómo dar el feedback

Tres cosas, siempre en este orden y nunca más de tres:

1. **Una cosa que hizo bien**, específica. No "estuvo bien": *"el diagrama de la diapositiva 2 explicó el problema mejor que diez minutos de texto"*.
2. **Una cosa concreta para mejorar**, accionable la próxima semana. No "más confianza": *"la próxima, cuando muestres código, dilo en una frase antes de mostrarlo"*.
3. **Una pregunta difícil**, para entrenar el aguante. Y si no sabe, recordarle que "no sé, lo averiguo" es una respuesta correcta.

## Dónde quedan guardadas

Todas en su repositorio `bitacora-practica`, carpeta `presentaciones/`, con nombre `P01-que-es-programar.pptx`. En noviembre las tiene todas juntas y son la mitad de su portafolio.
