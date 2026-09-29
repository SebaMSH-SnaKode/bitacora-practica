# Semana 5 — JavaScript: la pantalla cobra vida

**S8** Lun 19 oct · **S9** Mar 20 oct
**Objetivo:** que descubra que los conceptos son los mismos y solo cambia la sintaxis, y que mini-OT pase de ser un dibujo a responder.

> 💡 **La semana con la mejor lección de toda la práctica.** El lunes cambia de lenguaje en una mañana. Si se lo presentas bien, entiende algo que mucha gente tarda años: *no se aprende un lenguaje, se aprende a programar*. Dilo con esas palabras.

---

## S8 — Lunes 19 de octubre · El mismo cerebro, otra sintaxis

### 10:00 – 10:30 · **Presentación P4**

### 10:30 – 11:00 · Por qué cambiamos de lenguaje

Sé honesto con él, entiende más de lo que uno cree:

> *"Aprendiste con Python porque es el más limpio para empezar. Pero el navegador solo entiende JavaScript, y Datamédica —el sistema que vas a tocar— está escrito en JavaScript de punta a punta. Hoy vas a descubrir que todo lo que sabes se traslada; lo único que cambia es cómo se escribe."*

### 11:00 – 11:45 · La tabla de traducción

Constrúyela **con él en la pizarra**, no se la entregues hecha. Que él dicte la columna de Python.

| Concepto | Python | JavaScript |
|---|---|---|
| Variable | `nombre = "Ana"` | `const nombre = "Ana";` |
| Variable que cambia | `x = 1` | `let x = 1;` |
| Mostrar | `print(x)` | `console.log(x);` |
| Condicional | `if x > 5:` | `if (x > 5) { }` |
| Bucle sobre lista | `for e in equipos:` | `for (const e of equipos) { }` |
| Función | `def sumar(a, b):` | `function sumar(a, b) { }` |
| Lista | `[1, 2, 3]` | `[1, 2, 3]` |
| Diccionario / objeto | `{"marca": "Siemens"}` | `{ marca: "Siemens" }` |
| Largo | `len(lista)` | `lista.length` |
| Agregar | `lista.append(x)` | `lista.push(x)` |
| Verdadero | `True` | `true` |
| Nada | `None` | `null` |

**Las cuatro diferencias que sí duelen:**
1. **Llaves en vez de indentación.** En JavaScript la indentación es cosmética. Hay que acostumbrarse a cerrar.
2. **Punto y coma** al final de cada instrucción.
3. **`const` y `let`.** Regla simple: `const` siempre, `let` solo si de verdad va a cambiar. Que no use `var` nunca.
4. **`===` y no `==`.** Regla igual de simple: en JavaScript siempre tres iguales. El porqué se lo cuentas cuando lo pregunte.

### 11:45 – 13:00 · El DOM

- Qué es: **el HTML convertido en objetos que el código puede tocar.**
- `document.querySelector()` y `querySelectorAll()`.
- Cambiar contenido: `textContent`, `innerHTML` (y cuándo *no* usar `innerHTML`).
- Cambiar apariencia: `classList.add()`, `.remove()`, `.toggle()`.
- Crear elementos: `createElement()`, `appendChild()`.

### 14:00 – 17:00 · Ejercicios 1 y 2

---

## S9 — Martes 20 de octubre · Eventos: la página responde

### 10:15 – 11:30 · Concepto

- **Eventos:** `addEventListener('click', ...)`, `'submit'`, `'input'`, `'change'`.
- **Funciones flecha:** `() => {}`. Preséntala como "otra forma de escribir lo mismo", no como un tema nuevo.
- **Leer un formulario** desde JavaScript y `event.preventDefault()` — por qué la página se recargaba y ahora no.
- **Validar antes de guardar:** campos vacíos, descripción demasiado corta.
- **`localStorage`:** guardar en el navegador. Es el equivalente al `equipos.json` de la semana 2 — dile eso, le cierra el círculo.

### 11:30 – 13:00 · Juntos
Conectar el formulario de `nueva-orden.html` con la lista de `index.html`. Que cree una orden y aparezca.

### 14:00 – 16:45 · Ejercicio 3 y cierre de la semana

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Traduce tu propio código
> Toma el inventario de equipos que escribiste en Python en la semana 2 y reescríbelo en JavaScript. Mismas funciones, misma lógica, `console.log` en vez de `print`.
>
> **Regla:** no lo copies de una IA ni de internet. Tradúcelo tú, mirando la tabla. El objetivo no es tener el archivo: es que compruebes con tus manos que ya sabes hacerlo.
>
> Anota en tu bitácora las **tres** diferencias que más te costaron.

### Ejercicio 2 · Las órdenes salen de los datos ⭐
> Hasta ahora las órdenes de tu pantalla están escritas a mano en el HTML. Ahora tienen que generarse desde JavaScript.
>
> 1. Crea un arreglo `ordenes` con al menos 6 órdenes, cada una un objeto con: `id`, `equipo`, `cliente`, `fecha`, `tecnico`, `estado`.
> 2. Escribe una función `mostrarOrdenes(ordenes)` que las dibuje en la pantalla.
> 3. Que los tres botones de filtro funcionen de verdad: *Todas*, *Abiertas*, *Cerradas*.
> 4. Que muestre cuántas está viendo: *"Mostrando 4 de 6 órdenes"*.
> 5. Si el filtro no deja ninguna, que diga *"No hay órdenes en este estado"* en vez de quedar en blanco.
>
> Ese punto 5 se llama **estado vacío** y es lo que separa una app hecha con cuidado de una hecha a medias. Casi nadie lo hace la primera vez.

### Ejercicio 3 · Crear órdenes de verdad
> 1. Que el formulario de nueva orden cree la orden y la muestre en la lista.
> 2. **Validaciones:** descripción mínimo 10 caracteres, equipo obligatorio, fecha no puede ser futura.
> 3. Si algo está mal, mostrar el mensaje **al lado del campo**, no un `alert`.
> 4. Que se pueda cambiar el estado de una orden desde la lista.
> 5. Una orden `cerrada` no puede volver a `abierta` — bloquéalo.
> 6. Que todo se guarde en `localStorage` y siga ahí al recargar.
>
> **El punto 5 es una regla de negocio**, no un detalle técnico. Los sistemas reales están llenos de reglas así y hay que respetarlas aunque el código funcione igual sin ellas.

### Ejercicio 4 · *(ampliación)* Buscador
> Un campo de búsqueda que filtre las órdenes por texto mientras escribe, sin apretar ningún botón. Debe buscar en equipo, cliente y descripción, y funcionar junto con los filtros de estado.

---

## Entregable de la semana

- [ ] mini-OT interactiva: lista, filtros, crear, cambiar estado, validaciones, estado vacío.
- [ ] Datos que sobreviven al recargar la página.
- [ ] El inventario traducido a JavaScript.
- [ ] Bitácora con las tres diferencias Python/JavaScript que más le costaron.

## Presentación P5 — lunes 26 de octubre · 🔴 **Primera vez ante el equipo**

**"Python y JavaScript: qué cambia y qué no"**

Avísale el martes, no el lunes. Que se prepare.

- Diapositiva 2: su tabla de traducción, pero **en sus palabras**, no copiada.
- La idea que tiene que dejar instalada: *los conceptos son los mismos, la sintaxis es ropa*.
- Diapositiva 4: qué le costó más del cambio.

Antes de que presente, recuérdale las dos reglas: **no leer**, y **"no sé, lo averiguo" es una respuesta correcta**.

## Tarea de mitad de semana *(1 hora)*

1. Armar P5 — la primera ante el equipo, merece un ensayo en voz alta (35 min).
2. Ensayarla cronometrada una vez, solo, en voz alta (10 min). Insiste: cambia todo.
3. Leer sobre `const` vs `let` (15 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Olvida las llaves o el punto y coma | Se pasa solo en dos sesiones. Instálale un formateador automático y no gastes energía ahí |
| Usa `var` porque lo vio en un tutorial viejo | Corrígelo apenas aparezca: `const` por defecto, `let` si cambia |
| `innerHTML` con datos que escribe el usuario | **Ojo:** esto es exactamente XSS. Márcalo hoy y dile que lo van a ver en detalle en la semana 8 |
| Repite el código de dibujar la lista en tres lugares | Buen momento para refactorizar juntos: una sola función `mostrarOrdenes()` |
| La página se recarga al enviar el formulario y no entiende por qué | Excelente. Que investigue `preventDefault()` él antes de que le des la respuesta |
| Cree que ya "sabe JavaScript" | Bien por la confianza. Aterrízalo en la semana 10, no ahora |
