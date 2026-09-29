# Semana 10 — El código real, y el cierre

**S18** Lun 23 nov · **S19** Mar 24 nov · **S20** Lun 30 nov
**Objetivo:** que entre a Datamédica, entienda cómo está construida, y cierre su primer pull request sobre el repositorio real.

> ⚠️ **Segundo valle, y el más duro.** Abrir un monorepo de producción después de nueve semanas se siente como volver a empezar. **Dilo antes de abrirlo:** *"esto le pasa a todos los que entran a un proyecto grande, incluido yo cuando entré. No se entiende entero, y no hace falta."*

---

## S18 — Lunes 23 de noviembre · Dentro de Datamédica

### 10:00 – 10:30 · **Presentación P9**

### 10:30 – 11:30 · Levantar el proyecto

- Clonar el repositorio, instalar dependencias, levantar con Docker.
- **Docker aquí es un comando, no un tema.** `docker compose up` y qué significa: *una caja con todo lo necesario para que el programa corra igual en cualquier máquina*. Nada más.
- Que lo vea corriendo en su máquina. Ese solo hecho ya es un logro.

### 11:30 – 13:00 · Recorrer el mapa

**Enséñale a navegar, no a entender.** La habilidad del día es encontrar cosas, no dominarlas.

- **El monorepo:** qué hay en `apps/`, qué hay en `packages/`, y por qué está así.
- **TypeScript a nivel lectura.** No se enseña como tema: se presenta como *"JavaScript con anotaciones que dicen qué tipo de dato es cada cosa"*. Con eso lee el 80%. Muéstrale una interfaz y una función tipada, y sigue adelante.
- **El mapeo con lo que él construyó** — esta es la tabla del día:

  | En mini-OT | En Datamédica |
  |---|---|
  | `index.html` + JavaScript | Next.js + React |
  | `estilos.css` | Tailwind CSS |
  | `servidor.js` con Express | NestJS (controladores y servicios) |
  | Consultas SQL a mano | Prisma sobre PostgreSQL |
  | `fetch()` suelto | React Query |
  | Sus `if` de validación | class-validator |
  | Su `.env` | Variables de entorno en Azure |

  **Dedícale tiempo.** Esta tabla es la razón por la que construyó mini-OT durante nueve semanas: todo lo que ve tiene un equivalente que él ya escribió con sus manos.

- **Trazar un request de punta a punta**, juntos, con el código a la vista: desde el clic en la interfaz hasta la fila en la base de datos y de vuelta.

### 14:00 – 17:00 · Ejercicios 1 y 2

---

## S19 — Martes 24 de noviembre · Ramas, pull requests y su primer ticket 🏁

### 10:15 – 11:15 · Git en equipo

Ahora sí, porque ahora hay un motivo real:

- **Ramas:** `git switch -c`, por qué no se trabaja sobre la principal.
- **Pull request:** para qué sirve la revisión, cómo se escribe una descripción útil.
- **Conflictos de merge:** provócale uno a propósito y resuélvanlo juntos. Es mucho menos aterrador cuando ya pasó una vez.
- **Cómo se revisa código:** qué mira un revisor, cómo se comenta sin ser desagradable, cómo se recibe una corrección sin tomársela a pecho.

### 11:15 – 13:00 · Que él revise

**Dale un pull request real del equipo y que lo revise.**

No tiene que aprobar nada: tiene que leerlo, entender qué cambia y **escribir tres preguntas**. Leer código ajeno es la mitad del trabajo de un desarrollador y casi nunca se practica.

### 14:00 – 16:45 · 🏁 Su primer ticket real

---

## S20 — Lunes 30 de noviembre · Cierre

**Sin materia nueva. Día completo de cierre.**

| Hora | Qué |
|---|---|
| 10:00 – 10:30 | Preparación final de la presentación |
| 10:30 – 11:15 | **Presentación final P10** ante el equipo y la jefatura (20 min + preguntas) |
| 11:15 – 13:00 | Dejar todo en orden: READMEs, repositorio limpio, documentación al día |
| 14:00 – 15:00 | **Retrospectiva** con el mentor (abajo) |
| 15:00 – 16:00 | Entrega del **mapa post-práctica** (`06-mapa-post-practica.md`) y plan de los próximos 6 meses |
| 16:00 – 17:00 | Portafolio y CV con lo que construyó. Cierre y agradecimiento |

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Mapa del repositorio
> Sin modificar una línea, recorre Datamédica y escribe un documento que responda:
> 1. ¿Dónde está el código de la web que ve el usuario? ¿Y el de la API?
> 2. ¿Dónde se define el modelo de datos? ¿Se parece al tuyo?
> 3. Encuentra el endpoint que lista órdenes de trabajo. ¿Cómo se llama el archivo?
> 4. Encuentra dónde se valida que una orden tenga los datos obligatorios.
> 5. ¿Qué hace `packages/shared-core` y por qué existe?
> 6. Nombra **tres cosas que el sistema real hace y el tuyo no**, y por qué crees que están.
>
> La 6 es la importante. Casi siempre la respuesta es "porque en producción pasa algo que uno no se imagina".

### Ejercicio 2 · La traza completa ⭐
> Elige **una** acción del sistema —por ejemplo, cambiar el estado de una orden— y sigue su recorrido completo por el código real. Documenta cada salto:
> 1. El componente de la interfaz donde se hace clic.
> 2. La función que dispara la llamada.
> 3. El endpoint de la API que la recibe.
> 4. El controlador, y el servicio que llama.
> 5. La consulta que llega a la base de datos.
> 6. El camino de vuelta hasta la pantalla.
>
> Hazlo con capturas o con las rutas de los archivos. **Si logras esto, puedes trabajar en el proyecto.** Es la habilidad que de verdad se necesita para dar soporte, mucho más que conocer todos los frameworks.

### Ejercicio 3 · Revisa un pull request ajeno
> Te vamos a dar un PR real. No lo apruebes ni lo rechaces. Léelo y escribe:
> 1. Qué cambia, en dos frases.
> 2. Tres preguntas honestas sobre cosas que no entendiste.
> 3. Una cosa que te pareció bien hecha.
>
> Preguntar bien es más valioso que opinar. Empieza por ahí.

### Ejercicio 4 · Tu primer ticket real 🏁
> *(El mentor elige un ticket **acotado y de bajo riesgo**: un texto mal escrito, una validación que falta, una fecha mal formateada, un estado vacío sin mensaje. Nada de lógica de negocio, nada que toque datos de producción.)*
>
> De principio a fin, tú a cargo:
> 1. Entender el ticket y **preguntar lo que no esté claro antes de empezar**. Esto se evalúa.
> 2. Crear la rama con el nombre que usa el equipo.
> 3. Hacer el cambio.
> 4. Probarlo localmente.
> 5. Commits con el formato de la empresa.
> 6. Abrir el pull request con una descripción que explique qué cambia y cómo se prueba.
> 7. Atender los comentarios de la revisión.
>
> El paso 1 y el paso 6 son los que más se evalúan. El código es la parte fácil.

### Ejercicio 5 · Presentación final
> 20 minutos ante el equipo y la jefatura:
> 1. **Qué construí** — demo de mini-OT en vivo.
> 2. **Cómo funciona** — su arquitectura, con el diagrama de la traza al lado del de su propio sistema.
> 3. **Qué aprendí** — las 3 cosas más importantes, en sus palabras.
> 4. **Qué me costó** — con honestidad.
> 5. **Qué me falta** — y cómo piensa aprenderlo.
>
> **El punto 5 es obligatorio.** Que un junior sepa nombrar sus propios vacíos vale más que cualquier certificado, y quien lo escuche lo va a notar.

---

## La retrospectiva (S20, 14:00)

Una hora, conversación de ida y vuelta, no evaluación de una sola dirección.

**Lo que el mentor le pregunta:**
- ¿Qué semana te sirvió más? ¿Cuál menos?
- ¿En qué momento pensaste que no ibas a poder?
- ¿Qué te habría gustado que hiciéramos distinto?
- ¿Qué parte del trabajo te gustó más? *(Orienta hacia dónde seguir: frontend, datos, consultoría.)*
- ¿Qué vas a seguir estudiando?

**Lo que el mentor le dice, con nombre y apellido:**
- Tres cosas concretas que hizo bien.
- Dos cosas concretas en las que tiene que trabajar.
- Dónde está parado de verdad, sin adornos y sin desanimarlo.
- Qué haría falta para trabajar en Snakode, si esa conversación corresponde.

**Y queda escrito** en `SEGUIMIENTO.md`, junto con los resultados de los checkpoints: es la base del informe de práctica y la mejora para el próximo practicante.

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Se abruma con el repositorio real | Esperado. Recuérdale que nadie entiende un proyecto grande entero, y que su trabajo es saber **dónde** buscar |
| Quiere entender todo antes de tocar nada | Ponle una tarea concreta. Se entiende navegando con un objetivo, no leyendo |
| El ticket es demasiado grande | Culpa del mentor, no de él. Achícalo hasta que quepa en una tarde |
| No pregunta nada sobre el ticket | Mala señal. Que las preguntas sean un requisito explícito de la entrega |
| Se pone nervioso con la jefatura en la sala | Ensáyalo el martes. Y recuérdale que ya presentó nueve veces: está preparado |
