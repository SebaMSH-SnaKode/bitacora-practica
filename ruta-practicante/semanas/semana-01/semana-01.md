# Semana 1 — Pensar en pasos ordenados

**S1** Lun 21 sep (✅ hecha) · **S2** Mar 22 sep
**Objetivo:** que entienda que programar es descomponer un problema en pasos ordenados, y que escriba su primer programa que funciona.

---

## S1 — Lunes 21 de septiembre · Pseudocódigo *(ya realizada)*

Los ejemplos que usaste —cómo cocinar un huevo y cómo llegar al colegio— son los correctos: cotidianos, y con la estructura de un programa escondida adentro.

### Antes de cerrar, sácale los tres conceptos que ya están ahí

La receta del huevo ya contiene lo que va a usar toda su carrera. Solo hay que **ponerle nombre** a lo que él ya escribió:

| En la receta | Se llama | Por qué importa |
|---|---|---|
| "Si el agua todavía no hierve, espera" | **Condicional** | El programa toma decisiones |
| "Revisa cada 30 segundos hasta que hierva" | **Bucle** | El programa repite sin que se lo escriban 100 veces |
| "¿Y si el huevo se rompe al echarlo?" | **Manejo de errores** | Lo que pasa cuando el mundo no coopera |
| "Sacar el huevo del agua" (paso reutilizable) | **Función** | Un pedazo con nombre que se usa muchas veces |

Que él mismo marque en su papel dónde está cada uno. Toma cinco minutos y vale por una clase entera.

### El ejercicio del robot *(cierre de la sesión)*

El momento más importante del día y dura 15 minutos.

1. Él escribe en papel los pasos para algo que elija: hacer un sándwich, amarrarse los zapatos, lo que sea.
2. **Tú ejecutas los pasos literalmente**, en voz alta, sin usar sentido común. "Pon el jamón sobre el pan" → pones el paquete cerrado de jamón encima.
3. Se ríe, corrige, vuelve a fallar.

Cuando por fin funciona, le dices la frase: **"eso que acabas de hacer cuatro veces se llama depurar, y es el 60% del trabajo".**

### Cerrar la sesión

- [X] Explicarle el objetivo real de la práctica y su fecha de término (ver `00-vision-general.md`). Sin humo.
- [X] Entregarle las **cinco reglas de oro**, impresas o por escrito.
- [X] Explicarle el formato: lunes y martes, presentación cada lunes, bitácora todos los días.
- [X] Que escriba su primera bitácora hoy mismo, aunque sean tres líneas.

---

## S2 — Martes 22 de septiembre · Del pseudocódigo a Python

**La sesión donde la programación deja de ser abstracta.** Hoy ve su propio huevo ejecutándose.

### 10:00 – 10:15 · Retomar
Que explique con sus palabras qué es un algoritmo. Sin apuntes.

### 10:15 – 11:00 · Entorno de trabajo

Instalar **juntos**, y que él escriba cada paso en su bitácora. Va a tener que volver a hacerlo en otra máquina algún día.

- **VS Code** + extensión de Python.
- **Python 3.12+**. Verificar con `python3 --version` en la terminal.
- Crear la carpeta `mini-ot/` en su Escritorio. Ahí vive todo de aquí en adelante.
- Primer archivo: `hola.py` con `print("Hola, soy el practicante de Snakode")`. Ejecutarlo.

> **Advertencia de mentor:** instalar entornos es donde mueren las primeras sesiones. Si algo se tuerce más de 20 minutos, usa un entorno en el navegador por hoy y arreglan la instalación mañana. No gastes la sesión 2 en un instalador.

### 11:00 – 13:00 · Los cuatro ladrillos

Enseñar en este orden, con el ejemplo del huevo abierto al lado:

1. **Variables** — una caja con nombre. `minutos_coccion = 7`
2. **Tipos** — texto (`str`), número entero (`int`), decimal (`float`), verdadero/falso (`bool`). Solo eso.
3. **Entrada y salida** — `print()` y `input()`. Que el programa le hable y él le responda.
4. **Condicionales** — `if` / `elif` / `else`, y los comparadores `==`, `!=`, `>`, `<`.

Y una advertencia temprana que ahorra dolores: **`=` guarda, `==` compara.**

### 14:00 – 16:15 · Los ejercicios

*(Abajo, listos para copiar y pegar.)*

### 16:15 – 17:00 · Revisión, primer commit local y bitácora

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · El huevo, ahora en Python
> Traduce a Python el pseudocódigo del huevo que escribiste ayer.
> El programa debe:
> 1. Preguntar cómo quiere el huevo: `blando`, `medio` o `duro`.
> 2. Decidir los minutos de cocción: blando 4, medio 7, duro 10.
> 3. Mostrar: *"Hierve el huevo durante 7 minutos"*.
> 4. Si escribe cualquier otra cosa, responder: *"No conozco ese tipo de huevo"*.
>
> **Pista:** son cuatro `print`, un `input` y un `if/elif/else`. Nada más.

### Ejercicio 2 · ¿Alcanzo a llegar al colegio?
> Segunda parte del pseudocódigo de ayer.
> El programa pregunta a qué hora se levantó (solo la hora, un número entero) y responde:
> - Antes de las 7 → *"Vas sobrado"*
> - A las 7 → *"Justo, apúrate"*
> - Después de las 7 → *"Llegaste atrasado"*
>
> **Pista:** `input()` siempre entrega texto. Para compararlo con un número hay que convertirlo: `hora = int(input("¿A qué hora te levantaste? "))`. Esto te va a costar y es normal.

### Ejercicio 3 · Primer ladrillo de mini-OT
> Un programa que pregunta los datos de **un** equipo médico y los muestra ordenados.
> Pide: tipo de equipo, marca, modelo y número de serie.
> Muestra:
> ```
> --- EQUIPO REGISTRADO ---
> Tipo:   Ecógrafo
> Marca:  Siemens
> Modelo: Acuson P500
> Serie:  SN-48821
> ```
> **Este archivo no se borra.** Es el primer ladrillo del proyecto que vas a construir durante toda la práctica.

### Ejercicio 4 · *(si sobra tiempo)* Calculadora de visitas
> Un técnico cobra $35.000 por visita y $12.000 por cada equipo adicional revisado en la misma visita.
> Pregunta cuántos equipos revisó y muestra cuánto cobrar.
> Ejemplo: 3 equipos → 35.000 + 12.000 × 2 = **$59.000**.
>
> **Ojo:** el segundo equipo es el primero *adicional*. Si tu programa cobra 12.000 por el primero, está mal. Lee de nuevo el enunciado — esto también es parte del oficio.

---

## Entregable de la semana

- [ ] Carpeta `mini-ot/` con los cuatro archivos `.py` funcionando.
- [ ] `bitacora/semana-01.md` con dos entradas (lunes y martes).
- [ ] Entorno instalado y documentado paso a paso.

## Presentación P1 — lunes 28 de septiembre

**"Qué es programar, y mi primer programa"**

- Diapositiva 2 (el diagrama): el pseudocódigo del huevo dibujado como diagrama de flujo, con los condicionales marcados.
- Diapositiva 3: que cuente un error real que tuvo y cómo lo descubrió.

## Tarea de mitad de semana *(1 hora)*

1. Armar la presentación P1 (30 min).
2. Leer: qué es un lenguaje de programación y por qué hay tantos (15 min) — mándale **un** enlace concreto, no una búsqueda abierta.
3. Escribir en pseudocódigo, en papel, cómo se saca dinero de un cajero automático. Incluir qué pasa si la clave está mala **dos** veces (15 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Confunde `=` con `==` | Dilo antes de que pase. Va a pasar igual, pero lo reconoce más rápido |
| Compara texto con número y no entiende el error | **Es el error más formativo de la semana.** Que lo lea completo en voz alta antes de que se lo expliques |
| Escribe todo en un solo `print` gigante | Déjalo. Se arregla solo en la semana 2 cuando conozca las funciones |
| Se frustra con la instalación | No es programar. Resuélvelo tú si pasan 20 minutos y sigue adelante |
| Copia el código de una IA y funciona | Primera vez: conversación, no reto. Que te lo explique línea por línea. Si no puede, se borra y se rehace juntos |
