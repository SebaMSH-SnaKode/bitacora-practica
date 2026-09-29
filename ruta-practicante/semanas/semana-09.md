# Semana 9 — Producción, pruebas, y Python vuelve con la IA

**S16** Lun 16 nov · **S17** Mar 17 nov
**Objetivo:** que su aplicación esté publicada en internet, que sepa qué es una prueba automatizada, y que tenga criterio para decir dónde la IA aporta y dónde no.

---

## S16 — Lunes 16 de noviembre · Publicar 🏁

**El deploy va aquí, no al final.** Dos razones: la motivación está en su punto más alto justo después de que la app funciona, y quedan cuatro sesiones de colchón para cuando se rompa, que se va a romper.

### 10:00 – 10:30 · **Presentación P8** (demo de producto)

### 10:30 – 11:45 · Llevarlo a producción

- **Qué significa "producción"** y por qué "en mi máquina funciona" es una frase famosa.
- **Variables de entorno en el servidor.** Aquí entiende para qué servía el `.env`.
- **Desplegar el frontend y el backend.** Usa plataformas de nivel gratuito; lo que importa es el concepto, no el proveedor.
- **Lo que siempre se rompe**, y hay que verlo romperse: rutas fijas a `localhost`, CORS en el dominio nuevo, la base de datos que no existe allá, variables que faltan.
- **Logs.** Cuando no puedes ver la pantalla del usuario, los logs son tus ojos. Datamédica usa Application Insights: nómbralo.
- **Mapa mental de la infraestructura de Datamédica** —Docker, Azure, GitHub Actions— a nivel de *para qué sirve cada cosa*, sin instalar nada.

### 11:45 – 13:00 · Pruebas automatizadas

- **Por qué existen:** que no se rompa mañana lo que funciona hoy.
- **Prueba unitaria** con Jest: `describe`, `it`, `expect`.
- **Qué vale la pena probar:** la lógica de negocio y los casos borde. Qué no: que el framework funcione.
- Que pruebe **su** regla: *una orden cerrada no se reabre*.

### 14:00 – 17:00 · Ejercicios 1 y 2

---

## S17 — Martes 17 de noviembre · Python vuelve: automatización e IA

### 10:15 – 11:15 · Python como herramienta

Aquí Python reaparece con un trabajo que sí le corresponde: lo que no es la aplicación web.

- **Scripts de automatización:** leer la base de datos y generar un reporte.
- **Trabajar con archivos:** CSV y Excel desde Python.
- **Cuándo un script vale más que una funcionalidad:** lo que se corre una vez al mes no necesita una pantalla.

### 11:15 – 13:00 · IA aplicada, y criterio para usarla

Esta parte la conduce el responsable de IA. Son dos cosas distintas y hay que separarlas:

**a) Desarrollar con IA** — ya la usa desde la semana 1 con la regla de la calculadora. Hoy se formaliza: dónde acelera de verdad (código repetitivo, tests, explicar código ajeno, primer borrador de documentación) y dónde estorba (decisiones de arquitectura, código que no puede revisar, cualquier cosa que no sepa evaluar).

**b) Consultoría en IA** — el criterio que Snakode vende. Llamar a una API de un modelo desde Python, ver qué cuesta, qué tarda y en qué se equivoca. **El punto no es que aprenda a llamar una API: es que vea las limitaciones con sus ojos**, porque es lo que le van a preguntar los clientes.

**El marco de evaluación, que debe poder aplicar solo:**
1. ¿El problema tolera respuestas aproximadas? *(Si necesita exactitud garantizada, la IA generativa no es la herramienta.)*
2. ¿Existe el dato para resolverlo?
3. ¿Cuánto cuesta equivocarse, y quién revisa?
4. ¿Hay una solución más simple y determinista que funcione igual?
5. ¿El costo por consulta se sostiene al volumen real?

La pregunta 4 es la que separa a un consultor de un vendedor de humo.

### 14:00 – 16:45 · Ejercicios 3 y 4

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Publica mini-OT 🏁
> Deja tu aplicación funcionando en internet, con una URL que puedas compartir.
> 1. Backend desplegado, con sus variables de entorno configuradas en la plataforma.
> 2. Frontend desplegado y apuntando al backend real, no a `localhost`.
> 3. Base de datos accesible desde producción.
> 4. **Ábrela desde tu teléfono, con datos móviles.** Si funciona ahí, está desplegada de verdad.
>
> Documenta en `DEPLOY.md` cada paso y **cada cosa que se te rompió**. Ese documento es el que vas a agradecer la próxima vez.

### Ejercicio 2 · Las primeras pruebas
> Escribe pruebas con Jest para la lógica de tu API:
> 1. Una orden nueva se crea con estado `abierta`.
> 2. Una orden cerrada **no** se puede reabrir.
> 3. Una descripción de menos de 10 caracteres se rechaza.
> 4. Pedir una orden que no existe devuelve `404`.
> 5. El filtro por estado devuelve solo las de ese estado.
>
> Después: **rompe tu código a propósito** —invierte una condición— y comprueba que la prueba falla. Una prueba que nunca falló no sirve de nada.

### Ejercicio 3 · Un script que ahorra trabajo
> Escribe un script en Python que lea tu base de datos y genere un reporte mensual en Excel o CSV con:
> - Total de órdenes del mes, y cuántas por estado.
> - Órdenes por técnico.
> - Equipos con más de 2 órdenes en el mes (podrían estar fallando).
> - Órdenes abiertas hace más de 15 días.
>
> **El último punto es el valioso**: no es un dato, es una alerta. Aprender a convertir datos en algo accionable es lo que distingue un reporte útil de una planilla.

### Ejercicio 4 · Comité de factibilidad ⭐
> Te llega esta petición de un cliente:
>
> > *"Queremos que el sistema lea las fotos que saca el técnico en terreno y complete solo la descripción de la orden de trabajo."*
>
> Escribe un análisis de una página aplicando el marco de las cinco preguntas, y termina con una recomendación clara: **hacerlo, no hacerlo, o hacer una prueba acotada primero**, y por qué.
>
> Se evalúa el razonamiento, no la respuesta. Un "no, y esta es la alternativa más simple" bien fundado vale más que un "sí" entusiasta.
>
> **Esto lo presentas el lunes.**

---

## Entregable de la semana

- [ ] 🏁 mini-OT con URL pública, probada desde el teléfono.
- [ ] `DEPLOY.md` con los pasos y los tropiezos.
- [ ] 5 pruebas automatizadas pasando, y comprobadas fallando.
- [ ] Script de reportes en Python.
- [ ] Análisis de factibilidad de IA, una página.

## Presentación P9 — lunes 23 de noviembre

**"Dónde sí y dónde no conviene usar IA generativa"**

- Estructura: el caso del cliente → el marco de evaluación → su recomendación.
- Diapositiva 2: el marco de las cinco preguntas, en sus palabras.
- Diapositiva 3: qué limitación descubrió probando la API con sus manos.
- **Que defienda su recomendación.** Que alguien del equipo le lleve la contra a propósito: es el primer entrenamiento de una conversación de consultoría real.

## Tarea de mitad de semana *(1 hora)*

1. Armar P9 (30 min).
2. Terminar el análisis de factibilidad (30 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| El deploy se rompe y se desanima | **Avísale el lunes por la mañana que se va a romper.** Esperado deja de ser fracaso |
| Rutas a `localhost` en el código desplegado | Es el error clásico. Que lo diagnostique con la consola del navegador |
| Escribe pruebas que nunca podrían fallar | Por eso el ejercicio pide romper el código. Insiste |
| Cree que la IA resuelve cualquier cosa | Para eso está el Ejercicio 4. Que se choque con el límite él mismo |
| Cree que la IA no sirve para nada | El extremo opuesto y también es un problema. El criterio es el objetivo, no la postura |
