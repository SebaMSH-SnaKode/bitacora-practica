# 00 — Visión General

## La cuenta real, antes que nada

| | |
|---|---|
| Período | 21 de septiembre — 30 de noviembre de 2026 |
| Días | Lunes y martes, 10:00 a 17:00 |
| Sesiones | **20** (21 slots menos el feriado del lunes 12 de octubre) |
| Horas útiles | ~6 por sesión descontando almuerzo → **~120 horas totales** |

El plan original apuntaba a 22 semanas a jornada completa: del orden de 660 horas. **Disponemos del 18% de eso.** Todo este documento existe para decidir en qué se gasta ese 18% sin engañarnos.

## Objetivo reformulado

El plan original prometía que el practicante terminara **dando soporte supervisado a Datamédica en producción**. Con 120 horas eso no es alcanzable, y sostenerlo solo garantiza una conversación incómoda en noviembre.

**Lo que sí es alcanzable, y es mucho:**

1. **Construir una aplicación completa con sus manos** — interfaz, servidor, base de datos, autenticación básica — y dejarla publicada en internet.
2. **Entender el viaje de un request de punta a punta** y poder dibujarlo en una pizarra sin ayuda.
3. **Levantar Datamédica en su máquina, navegar el monorepo y explicar cómo está construida**, aunque todavía no pueda modificarla con soltura.
4. **Cerrar un ticket acotado** —un bug de frontend, un texto, una validación— en una rama, con un pull request revisable.
5. **Comunicar lo que hace.** Diez presentaciones ante el equipo en diez semanas: esto lo va a diferenciar más que cualquier framework.

**Perfil de salida honesto:** un junior que sabe programar, entiende el oficio completo porque lo recorrió entero una vez, y necesita acompañamiento para trabajar sobre el código real. No un desarrollador autónomo. Eso toma entre uno y dos años y ningún programa de diez semanas lo cambia.

Esto hay que decírselo a él el primer día, y decírselo a la empresa. Expectativa clara arriba, motivación intacta abajo.

## El stack de la práctica

Tres lenguajes, cada uno con un trabajo específico. Nunca tiene que sostener dos en la cabeza al mismo tiempo.

| Lenguaje | Cuándo | Para qué |
|---|---|---|
| **Python** | Semanas 1–3 | Aprender a pensar. Es la sintaxis más limpia que existe para alguien que nunca programó: sin llaves, sin punto y coma, sin declaraciones de tipo. Todo el esfuerzo va al concepto, no a la puntuación. |
| **JavaScript** | Semanas 5–9 | El lenguaje del producto. El navegador no admite otra cosa, y Datamédica es JavaScript/TypeScript de punta a punta. |
| **SQL** | Semanas 6–8 | Los datos. Transversal y pequeño: se aprende en dos sesiones y no caduca nunca. |
| **Python otra vez** | Semana 9 | Automatización e IA aplicada, que es donde Python aporta valor real a Snakode. |

### Sobre la decisión de enseñar dos lenguajes

Vale la pena dejarlo escrito porque es la decisión más discutible del plan. **Datamédica no tiene una línea de Python**: es TypeScript en las dos puntas. Cada hora de Python es una hora que no transfiere directo al producto.

Se mantiene igual por dos razones que pesan más en este contexto:

- **La rampa de entrada.** Para alguien en su sesión 2, `for equipo in equipos:` es legible y `for (let i = 0; i < equipos.length; i++) {` es un muro. Perder dos sesiones porque se atoró con la sintaxis cuesta más que el cambio de lenguaje después.
- **El salto es la lección.** En la semana 5, cuando pase de Python a JavaScript, descubre en una tarde que los conceptos son los mismos y solo cambia la forma de escribirlos. Esa es exactamente la diferencia entre "sé React" y "sé programar", y se aprende una sola vez.

**El costo se contiene así:** el backend de *mini-OT* se construye en **JavaScript (Node/Express)**, no en Python, para que mapee directo contra NestJS cuando entre al repo real. Python no toca el proyecto web. Vuelve solo en la semana 9, para scripts y para el eje de IA.

Si en algún momento el tiempo aprieta, el recorte correcto es acortar Python a dos sesiones, nunca saltarse el paso a JavaScript.

## El hilo conductor: mini-OT

Todo se construye sobre **un solo proyecto que crece cada semana**: *mini-OT*, una versión en miniatura de Datamédica —clientes, equipos, órdenes de trabajo con estados—. Especificación completa en [`04-proyecto-mini-ot.md`](04-proyecto-mini-ot.md).

No hay 20 temas sueltos. Hay una aplicación que el lunes 30 de noviembre está en línea, con su nombre en los commits, y que es la prueba física de todo lo que aprendió.

## Reglas de oro (se le comunican la sesión 1)

1. **Regla de los 30 minutos.** Intenta solo —documentación, búsqueda, IA— durante 30 minutos. Si sigue trabado, pregunta mostrando qué intentó y qué esperaba que pasara.
2. **No hay preguntas tontas, hay preguntas sin contexto.** Toda pregunta llega con: qué quiero lograr, qué intenté, qué pasó.
3. **La IA es calculadora, no cerebro.** No entra al repositorio ninguna línea que no pueda explicar. En los checkpoints explica su código sin la IA delante.
4. **Todo queda escrito.** Bitácora al final de cada sesión, commits descriptivos en español (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`), presentación cada lunes.
5. **Producción se respeta.** No toca nada conectado a producción hasta la semana 10, y ahí solo con revisión previa del mentor.

## Roles

- **Mentor principal** — está presente las dos jornadas completas. Este formato es intensivo: no funciona con un mentor que pasa a ver cómo va.
- **Equipo** — audiencia de las presentaciones desde la semana 5. Rotar quién da el feedback para que conozca distintos estilos.
- **Responsable de IA** — conduce la sesión 17 (IA aplicada) y la evaluación del caso de factibilidad.

## Lo que el mentor debe tener presente

- **Prepara poco, corrige mucho.** No hacen falta clases magistrales; hace falta estar disponible y hacer buenas preguntas: *¿qué esperabas que pasara?*, *¿cómo lo verificarías?*
- **Déjalo equivocarse barato.** El error en desarrollo es el mejor profesor. Interviene antes solo si el error va a costar días o moral.
- **Narra tu proceso en voz alta.** Cuando resuelvas algo delante de él, di cómo lees el error, cómo buscas, cómo decides. Es la clase más valiosa que va a recibir y no está en ningún curso.
- **Cuida la moral.** Aprender a programar tiene valles profundos. En este calendario caen en la **semana 3** (cuando la novedad se acaba y aparecen los errores) y en la **semana 10** (cuando ve el repo real y se siente diminuto). Nómbralos antes de que lleguen: *"esto le pasa a todos, es señal de que estás aprendiendo"*.
- **El riesgo real es la frustración, no el aburrimiento.** Se ve parecido —se calla, se pone lento, dice que sí a todo—. El remedio es achicar la tarea, nunca bajar la exigencia.
