# Semana 7 — Asincronía y su primera API

**S12** Lun 2 nov · **S13** Mar 3 nov
**Objetivo:** que entienda cómo un programa le pide datos a otro, y que escriba el suyo propio del lado del servidor.

---

## S12 — Lunes 2 de noviembre · Pedirle datos a otro lado

### 10:00 – 10:30 · **Presentación P6**

### 10:30 – 11:45 · Concepto

- **Síncrono y asíncrono**, con una analogía y no con teoría: pedir algo en un mesón y esperar parado (bloquea) versus dejar el pedido y que te llamen (no bloquea). El navegador no puede quedarse parado: la página se congelaría.
- **`fetch()`** — hacer un request desde JavaScript.
- **Promesas** — qué es "algo que todavía no llegó".
- **`async` / `await`** — la forma legible de escribirlo. Enséñale directamente esta; `.then()` solo para que lo reconozca cuando lo vea.
- **`try / catch`** — el mismo concepto del `try/except` de Python. Dile que es lo mismo.
- **Los tres estados que existen siempre**, y que los principiantes programan como si fuera uno solo:
  1. **Cargando** — pidiendo
  2. **Éxito** — llegaron los datos
  3. **Error** — no llegaron, se cayó, o no hay internet

**La frase del día:** *"la red siempre falla; la pregunta no es si, es qué hace tu programa cuando pase."*

### 11:45 – 13:00 · Juntos
Consumir una API pública real y mostrar los datos en pantalla, con los tres estados implementados a la vista.

### 14:00 – 17:00 · Ejercicios 1 y 2

---

## S13 — Martes 3 de noviembre · Su primera API

### 10:15 – 11:30 · Concepto

Hasta hoy siempre estuvo del lado del cliente. Hoy cruza al otro lado.

- **Qué es un servidor**, de verdad: un programa que queda esperando requests. Nada más místico que eso.
- **Node.js** — JavaScript fuera del navegador. La misma sintaxis que ya sabe, otro lugar de ejecución.
- **Express** — rutas, `req`, `res`, `res.json()`.
- **Diseñar endpoints REST:**
  | Verbo | Ruta | Qué hace |
  |---|---|---|
  | `GET` | `/api/ordenes` | Lista todas |
  | `GET` | `/api/ordenes/:id` | Trae una |
  | `POST` | `/api/ordenes` | Crea una |
  | `PATCH` | `/api/ordenes/:id` | Cambia su estado |
- **Códigos de estado que sí debe usar:** `200`, `201`, `400`, `404`, `500`.
- **Postman** (o Thunder Client) para probar sin frontend. Datamédica tiene su propia colección; muéstrasela.
- **CORS** — le va a aparecer el error mañana. Explícalo hoy en una frase para que lo reconozca.

> **Nota de diseño del programa:** la API se hace en JavaScript, no en Python, a propósito. Así mapea directo contra NestJS cuando entre al repositorio real en la semana 10.

### 11:30 – 13:00 · Juntos
Levantar el servidor y ver el primer `GET /api/ordenes` respondiendo JSON en el navegador. Momento de celebrar.

### 14:00 – 16:45 · Ejercicios 3 y 4

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Consume una API real
> Elige una API pública y gratuita, y muestra sus datos en una página.
> **Obligatorio implementar los tres estados:**
> 1. Mientras carga, un mensaje o indicador.
> 2. Si responde bien, los datos.
> 3. Si falla, un mensaje útil **con un botón de reintentar**.
>
> **Prueba el estado de error de verdad:** apaga el wifi y recarga. Si tu página queda en blanco o congelada, no está terminada.

### Ejercicio 2 · Rompe tu propia página
> Con DevTools, en la pestaña Network, simula una conexión lenta (*Slow 3G*) y recarga.
> 1. ¿Qué ve el usuario durante esos segundos?
> 2. ¿Se puede apretar el botón dos veces y mandar dos pedidos?
> 3. Arregla lo que encuentres: deshabilita el botón mientras carga.
>
> Acabas de hacer tu primera prueba de condiciones reales. Los usuarios de Datamédica trabajan en hospitales con señal mala: esto no es teórico.

### Ejercicio 3 · La API de mini-OT ⭐
> Crea `servidor.js` con Express y estos endpoints, leyendo por ahora desde un arreglo en memoria:
>
> | Verbo | Ruta | Respuesta |
> |---|---|---|
> | `GET` | `/api/ordenes` | Todas las órdenes |
> | `GET` | `/api/ordenes?estado=abierta` | Filtradas por estado |
> | `GET` | `/api/ordenes/:id` | Una orden, o `404` si no existe |
> | `POST` | `/api/ordenes` | Crea y devuelve `201` |
> | `PATCH` | `/api/ordenes/:id` | Cambia el estado |
> | `GET` | `/api/equipos` | Todos los equipos |
>
> **Requisitos:**
> - Si el `id` no existe → `404` con un mensaje claro, no un error del servidor.
> - Si el `POST` viene sin descripción o con menos de 10 caracteres → `400` explicando qué falta.
> - Si intenta reabrir una orden cerrada → `400` con el motivo.
> - Probar todo en Postman **antes** de tocar el frontend.

### Ejercicio 4 · Documenta tu API
> Escribe `API.md` con cada endpoint: qué hace, qué recibe, qué devuelve, y un ejemplo de respuesta.
>
> Entrégaselo al mentor y pídele que intente usar tu API **solo con ese documento**, sin preguntarte nada. Lo que no logre hacer, está mal documentado.
>
> *(Mentor: hazlo en serio y sé literal. Es la mejor lección de documentación que va a recibir.)*

### Ejercicio 5 · *(ampliación)* Conecta el front
> Cambia tu mini-OT para que las órdenes vengan de tu API en vez del arreglo local. Aquí te va a aparecer CORS — investígalo antes de preguntar.

---

## Entregable de la semana

- [ ] Página consumiendo una API pública con los tres estados.
- [ ] `servidor.js` con los 6 endpoints funcionando y probados en Postman.
- [ ] `API.md` que permita usar la API sin explicaciones.
- [ ] Bitácora.

## Presentación P7 — lunes 9 de noviembre

**"Qué es una API y por qué todo el mundo las usa"**

- Diapositiva 2: el diagrama navegador → API → datos, y dónde encaja su `servidor.js`.
- Diapositiva 3: la demo. Que muestre **Postman en vivo** haciendo un `POST` y la orden apareciendo. Presentar algo funcionando en vivo es una habilidad aparte y hay que empezar a entrenarla.
- Buena pregunta para hacerle: *¿por qué la validación va en el servidor si ya la hiciste en el formulario?*

## Tarea de mitad de semana *(1 hora)*

1. Armar P7 y ensayar la demo en vivo dos veces — siempre falla la primera (35 min).
2. Leer sobre códigos de estado HTTP, y anotar cuándo se usa `400` y cuándo `422` (25 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Olvida el `await` y le llega una promesa | El error más común de la semana. Que aprenda a reconocer `Promise { <pending> }` en la consola |
| Solo programa el caso feliz | Insiste con los tres estados. Es el hábito que más lo va a diferenciar |
| Devuelve `200` para todo, incluso errores | Explícale por qué al cliente le importa el código: es cómo el programa sabe qué pasó |
| Valida solo en el frontend | **Concepto clave:** el frontend se puede saltar. La validación del servidor es la que manda. Enséñaselo mandando un `POST` inválido por Postman |
| Se pelea con CORS | Que lea el error completo. Está bien explicado y es su oportunidad de practicar lo de la semana 3 |
| Pone claves o rutas fijas en el código | Anótalo. Se resuelve la próxima semana con variables de entorno |
