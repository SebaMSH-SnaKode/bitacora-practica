# Semana 3 — Desatorarse solo, y entender la web

**S5** Lun 5 oct · **S6** Mar 6 oct
**Objetivo:** que deje de depender del mentor para avanzar, y que entienda qué pasa realmente cuando se abre una página web.

> ⚠️ **Semana de valle.** La novedad se acabó y los errores aparecen. Nómbralo el lunes: *"esta semana te va a costar más que las anteriores, y eso significa que vas avanzando"*. Dicho antes, es normal; descubierto solo, es "no sirvo para esto".

---

## S5 — Lunes 5 de octubre · Depurar: la sesión más rentable de la práctica

Esta sesión decide si en la semana 6 avanza solo o sigue esperándote. Vale por tres de cualquier framework.

### 10:00 – 10:30 · **Presentación P2**

### 10:30 – 11:45 · Concepto

1. **Leer un error.** Abre un traceback de Python en pantalla y léelo **de abajo hacia arriba**, en voz alta, palabra por palabra. La mayoría de los principiantes no lee el error: lo ve, se asusta y vuelve al código. Romper ese reflejo es el objetivo del día.
2. **Los cinco errores que va a ver toda su vida:** `SyntaxError`, `NameError`, `TypeError`, `IndexError` / `KeyError`, `AttributeError`. Qué significa cada uno en castellano.
3. **`print()` como microscopio.** Antes del debugger, la técnica que más se usa en el mundo real.
4. **El debugger de VS Code.** Punto de interrupción, ejecutar paso a paso, mirar las variables. Que vea su programa avanzar línea por línea: es revelador.
5. **Bisección.** Cuando no sabes dónde está el error: cortar el programa por la mitad, ver de qué lado está, repetir. Es el método, y casi nadie se lo enseña.

### 11:45 – 13:00 · Buscar y preguntar

- **Orden de consulta:** documentación oficial → error textual en el buscador → IA → persona.
- **Cómo preguntarle a la IA:** dándole el error completo, el código y lo que esperabas. No "no me funciona".
- **La regla:** la IA explica, no resuelve. **No entra al repositorio ninguna línea que no pueda explicar.**
- **Cómo preguntar a una persona:** qué quiero lograr / qué intenté / qué pasó. Que escriba una pregunta así hoy, en serio, aunque no la necesite.

### 14:00 – 17:00 · Bug hunt *(ver ejercicios)*

---

## S6 — Martes 6 de octubre · La terminal y el viaje de un request

### 10:15 – 11:15 · La terminal

Su herramienta de todos los días. Solo lo que va a usar:

- `pwd`, `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `code .`
- Rutas absolutas y relativas; qué son `.` y `..`
- `--help` y cómo leer la ayuda de un comando
- Tab para autocompletar, flecha arriba para el historial
- **Procesos y puertos** — porque va a leer *"el puerto 3000 está ocupado"* mil veces y tiene que saber qué significa

### 11:15 – 13:00 · El viaje de un request

**El modelo mental más importante de toda la práctica.** Dibújalo en pizarra, no en diapositiva.

```
Navegador  →  DNS  →  Servidor  →  Base de datos
    ↑                                    │
    └────────── respuesta ───────────────┘
```

- **Cliente y servidor.** Qué corre en cada lado y por qué.
- **URL:** protocolo, dominio, ruta, parámetros de consulta.
- **HTTP:** verbos `GET`, `POST`, `PUT`/`PATCH`, `DELETE`. Códigos `200`, `201`, `400`, `401`, `403`, `404`, `500`. Headers y body.
- **JSON:** el idioma en que hablan las APIs. Ya lo conoce de la semana 2 — dile que es el mismo.
- **DevTools del navegador:** pestaña Network. Abrir un sitio real y mirar los requests volando.
- **Mapear a Datamédica:** *"la web que ve el cliente, el cerebro que decide, la memoria que guarda"*. Que se quede con esos tres nombres.

### 14:00 – 16:45 · Ejercicios 3 y 4

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Bug hunt ⭐
> **El mentor prepara esto antes de la sesión:** toma el inventario que el practicante escribió la semana pasada y plántale 6 errores. Sugerencia de mezcla:
> 1. Un `SyntaxError` obvio (falta un paréntesis).
> 2. Un `NameError` (una variable mal escrita).
> 3. Un `TypeError` (comparar texto con número).
> 4. Un error lógico **sin excepción**: el contador arranca en 1 en vez de 0. El programa corre y da mal.
> 5. Un `KeyError` que solo aparece con cierto dato.
> 6. Un error que solo se cae cuando la lista está vacía.
>
> **Enunciado para él:**
> > Este programa tiene 6 errores. Encuéntralos y arréglalos. Por cada uno, anota en un archivo `bugs.md`: qué error era, cómo te diste cuenta y cómo lo arreglaste.
> > **No arregles nada que no entiendas.** Si no sabes por qué tu cambio funcionó, todavía no está arreglado.
>
> Los errores 4 y 6 son los importantes: no avisan. Que descubra que **un programa que corre no es un programa correcto.**

### Ejercicio 2 · La pregunta bien hecha
> Escribe una pregunta técnica real sobre algo que te trabó, con esta estructura:
> - **Qué quiero lograr:**
> - **Qué intenté:** (con el código)
> - **Qué esperaba que pasara:**
> - **Qué pasó:** (con el error completo)
>
> Mándasela al mentor por escrito. Esta estructura te va a servir el resto de tu carrera, y la mitad de las veces vas a encontrar la respuesta mientras la escribes.

### Ejercicio 3 · Arqueología de un sitio web
> Abre DevTools en un sitio que uses a diario y responde en un documento:
> 1. ¿Cuántos requests hace al cargar?
> 2. Encuentra uno que devuelva JSON. Pega un pedazo.
> 3. ¿Qué verbo y qué código de estado tiene?
> 4. Encuentra un request que **falle** (rojo). ¿Qué código devuelve y qué significa?
> 5. ¿Cuánto pesa la página completa?

### Ejercicio 4 · Tu diagrama del request
> Dibuja —a mano en papel o en una herramienta, da lo mismo— qué pasa desde que escribes una dirección hasta que ves la página.
> Tiene que incluir: navegador, DNS, servidor, base de datos, y la respuesta de vuelta.
>
> **Este dibujo es la diapositiva 2 de tu presentación del martes 13.** Que se entienda solo.

### Ejercicio 5 · Solo con la terminal
> Sin usar el mouse ni el explorador de archivos, crea esta estructura, escribe algo en cada archivo y muéstrala con `ls -R`:
> ```
> practica-terminal/
> ├── documentos/notas.txt
> ├── codigo/hola.py
> └── README.md
> ```

---

## Entregable de la semana

- [ ] Inventario reparado + `bugs.md` con los 6 errores documentados.
- [ ] Una pregunta técnica bien estructurada.
- [ ] Documento de arqueología web.
- [ ] Diagrama del request, hecho por él.

## Presentación P3 — martes 13 de octubre *(corrida por el feriado)*

**"El viaje de un request: qué pasa cuando escribo una URL"**

Primera presentación con un invitado del equipo. Avísale antes, no el mismo día.
- Diapositiva 2: su diagrama del Ejercicio 4.
- Diapositiva 3: uno de los bugs del bug hunt — cuál era, cómo lo cazó.

## Tarea de mitad de semana *(1 hora)*

1. Armar P3 (30 min).
2. Terminar el diagrama del request en limpio (15 min).
3. Leer sobre códigos de estado HTTP y anotar qué significan 401 y 403, que **no** son lo mismo (15 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| No lee el error, solo lo mira | Obligarlo a leerlo en voz alta. Todas las veces, hasta que sea reflejo |
| Cambia cosas al azar hasta que funciona | El peor hábito posible. Detenlo: *"¿por qué crees que eso lo arreglaría?"* antes de dejarlo ejecutar |
| Pide ayuda a los 3 minutos | Recordar la regla de los 30. Si aun así pregunta, responde con una pregunta |
| No pide ayuda en toda la tarde y no avanza | El opuesto y más peligroso. Pasa a preguntarle cada 30 minutos |
| Confunde cliente y servidor | Normalísimo. Vuelve a la pizarra las veces que haga falta |
