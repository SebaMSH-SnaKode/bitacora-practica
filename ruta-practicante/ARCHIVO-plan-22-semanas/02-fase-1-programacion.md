# 02 — Fase 1: Programación desde cero (Semanas 3–6)

**Objetivo**: aprender a **pensar en lógica** y programar con JavaScript y luego TypeScript — el lenguaje de todo el stack de Datamédica. Esta es la fase más importante del programa: aquí se decide si el practicante será un programador o un copiador de código.

**Regla de esta fase**: la IA se usa como *tutor* (pedir explicaciones, ejemplos alternativos) pero **no como generador** de las soluciones de los ejercicios. Ver documento 07, etapa 1.

---

## Semana 3 — Lógica y JavaScript básico

- Variables (`let`, `const`), tipos primitivos (string, number, boolean, null/undefined).
- Operadores, condicionales (`if/else`, ternario), comparación (`===` vs `==`).
- Bucles (`for`, `while`, `for...of`).
- Funciones: declaración, parámetros, retorno, arrow functions.
- Ejecutar todo con `node archivo.js` — nada de navegador todavía; foco puro en lógica.

**Práctica diaria** (mínimo 3–5 ejercicios/día, dificultad creciente): FizzBuzz, conversores de unidades, validador de RUT chileno (¡lo usará en serio: Datamédica valida RUT en `rut.validator.ts`!), cajero automático, juego de adivinar el número.

## Semana 4 — Estructuras de datos y funciones sobre colecciones

- Arrays: `push`, `map`, `filter`, `find`, `reduce`, `some`, `every`, `sort`.
- Objetos: propiedades, anidamiento, destructuring, spread (`...`).
- JSON: `JSON.parse` / `JSON.stringify` — conectar con lo visto de APIs.
- Manejo de errores: `try/catch`, `throw`.
- Funciones como valores; callbacks.

**Proyecto de la semana — arranca el "mini-OT" (versión consola)**: un programa Node que gestiona órdenes de trabajo en memoria: crear OT (cliente, equipo, prioridad), listarlas, cambiar estado (`pendiente → asignada → en_proceso → completada`), filtrar por estado. Los estados son **los mismos de Datamédica real** — se le dice explícitamente.

## Semana 5 — Asincronía y módulos

- Por qué existe la asincronía (el modelo mental: "pedir una pizza y seguir viendo la tele").
- Promesas, `async/await`, `fetch` desde Node para consumir una API pública real (ej: una API de países o de feriados de Chile).
- Módulos: `import`/`export`, separar el mini-OT en archivos.
- npm en serio: `npm init`, instalar dependencias, `package.json`, scripts, `node_modules` (y por qué se ignora en Git).

**Proyecto**: mini-OT v2 — persistencia en archivo JSON (leer/escribir con `fs`), separado en módulos, y un comando que consume una API externa (ej: obtiene la fecha/feriados para agendar OTs).

## Semana 6 — TypeScript + HTML/CSS esencial

### TypeScript (3 días)
- Qué problema resuelve: errores en tiempo de compilación vs en producción.
- Tipos básicos, interfaces, type aliases, unions (`'pendiente' | 'asignada' | ...` — exactamente como los estados de OT), genéricos a nivel lectura, `tsconfig.json` básico.
- Migrar el mini-OT a TypeScript. Sentir cómo el editor ahora "sabe" cosas.

### HTML/CSS esencial (2 días)
- HTML semántico: estructura, formularios, tablas, listas.
- CSS: selectores, box model, flexbox, grid a nivel básico.
- **No profundizar en CSS puro**: en fase 2 usará Tailwind. El objetivo es entender qué hace Tailwind por debajo.
- Ejercicio: maquetar una tarjeta de "orden de trabajo" (código, cliente, equipo, estado con color, prioridad) en HTML/CSS puro.

---

## Entregables de la fase

- [ ] Repo `mini-ot` con historial de commits limpio mostrando la evolución (consola → JSON → módulos → TypeScript).
- [ ] Carpeta `ejercicios/` con todos los ejercicios diarios resueltos.
- [ ] Investigaciones I-02 e I-03 presentadas (ver documento 08).
- [ ] Bitácoras semanales al día.

## Recursos recomendados

- JavaScript: [javascript.info](https://es.javascript.info) (en español, excelente y gratis) — módulos 1 al 11 aprox.
- Práctica: [Exercism](https://exercism.org) (track JavaScript) o freeCodeCamp.
- TypeScript: documentación oficial "TS for the New Programmer" + [typescript-exercises.github.io](https://typescript-exercises.github.io).
- HTML/CSS: MDN + [flexboxfroggy.com](https://flexboxfroggy.com) y [cssgridgarden.com](https://cssgridgarden.com).

## Señales de alerta para el mentor

- Resuelve ejercicios pero no puede explicarlos → probablemente los generó con IA; volver a la regla de esta fase y rehacer sin IA.
- Se frustra con errores → enseñar a **leer** el error completo, en voz alta, línea por línea. Leer errores es una habilidad, no un talento.
- Avanza rápido en sintaxis pero mal en lógica → más ejercicios de lógica, menos material nuevo.

## Checkpoint de salida (ver documento 09)

Resuelve un ejercicio nuevo de lógica en vivo sin IA; el mini-OT en TypeScript funciona y puede explicar cualquier línea; entiende async/await y lo demuestra consumiendo una API.
