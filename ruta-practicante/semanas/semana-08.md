# Semana 8 — El sistema completo 🏁

**S14** Lun 9 nov · **S15** Mar 10 nov
**Objetivo:** que mini-OT quede funcionando de punta a punta —interfaz, servidor y base de datos— y que entienda cómo se rompe un sistema por seguridad.

> 🏁 **La mejor semana de la práctica.** El martes 10 su aplicación funciona completa. Reserva media hora al final para que la muestre al equipo, aunque sea informal. Ese momento vale más que tres sesiones de contenido.

---

## S14 — Lunes 9 de noviembre · La API conversa con la base de datos

### 10:00 – 10:30 · **Presentación P7**

### 10:30 – 11:45 · Concepto

- **Conectar Express con SQLite.** Su API deja de leer de un arreglo y lee de la base de la semana 6.
- **CRUD completo:** cada endpoint contra su consulta SQL.
- **Consultas parametrizadas.** Enséñalas como la forma normal de escribir SQL desde código, sin explicar todavía por qué. Mañana descubre el motivo y le va a quedar grabado.
- **Validar en el servidor:** campos obligatorios, tipos, reglas de negocio.
- **Errores con sentido:** `400` distinto de `404` distinto de `500`. Nunca devolver el error crudo de la base de datos al cliente.
- **Variables de entorno:** archivo `.env`, `.gitignore`, y por qué las claves no van en el código.

### 11:45 – 13:00 · Juntos
Migrar `GET /api/ordenes` y `POST /api/ordenes` a la base de datos, incluido el `JOIN` que trae el nombre del equipo y del cliente.

### 14:00 – 17:00 · Ejercicio 1

---

## S15 — Martes 10 de noviembre · Seguridad, e integración final

### 10:15 – 11:45 · Seguridad básica

**La sesión que nadie le va a enseñar después.** Media hora de susto que le ahorra un incidente en su primer trabajo. Todo demostrado en vivo sobre **su propio código**, no en diapositivas.

1. **Inyección SQL.** Escribe un endpoint vulnerable delante de él, concatenando texto. Rómpelo en vivo. Después arréglalo con una consulta parametrizada y muestra el mismo ataque fallando. **Se acuerda para siempre.**
2. **XSS.** Guardar una orden cuya descripción contenga `<script>` y ver qué hace su `innerHTML` de la semana 5. Arreglarlo con `textContent`.
3. **Contraseñas.** Por qué jamás se guardan en texto plano. Qué es un hash, por qué no se puede revertir, y `bcrypt` en tres líneas.
4. **Autenticación, a nivel conceptual.** Qué es un token, por qué el servidor no confía en el cliente. Datamédica usa JWT con refresh rotativo y MFA: nómbraselo para que reconozca las palabras en la semana 10, sin entrar en detalle.
5. **Secretos.** `.env` fuera del repositorio. Qué hacer si subiste una clave por error (respuesta: rotarla, no basta con borrar el commit).

### 11:45 – 13:00 · Integración
Conectar el frontend a su API real. Adiós `localStorage`.

### 14:00 – 16:00 · Ejercicio 3: cerrar el sistema

### 16:00 – 17:00 · 🏁 **Demo al equipo** y cierre

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · La API sobre la base de datos ⭐
> Migra los 6 endpoints para que lean y escriban en tu base SQLite.
>
> **Requisitos:**
> 1. `GET /api/ordenes` devuelve las órdenes **con el nombre del equipo y del cliente** (`JOIN`).
> 2. `POST` inserta de verdad y devuelve la orden creada con su `id`.
> 3. `PATCH` actualiza el estado y respeta la regla: una orden cerrada no se reabre.
> 4. Todas las consultas **parametrizadas**. Ninguna construida pegando texto.
> 5. Las credenciales y la ruta de la base, en un `.env` que **no** está en el repositorio.
> 6. Si la base falla, el cliente recibe un `500` con un mensaje genérico — y el detalle real queda en el log del servidor, no en la respuesta.
>
> El punto 6 es una regla de seguridad: el mensaje de error de una base de datos le dice a un atacante cómo está construido tu sistema.

### Ejercicio 2 · Rompe tu propio sistema ⭐
> **Con el mentor al lado, sobre una copia de tu proyecto.**
>
> 1. Escribe un endpoint que arme el SQL concatenando texto.
> 2. Rómpelo con una inyección. Que el mentor te muestre cómo si no te sale.
> 3. Arréglalo con una consulta parametrizada y comprueba que el mismo ataque ya no funciona.
> 4. Guarda una orden cuya descripción sea `<script>alert(1)</script>` y mira qué pasa en tu lista.
> 5. Arréglalo.
> 6. Documenta los dos ataques en `seguridad.md`: qué eran, cómo funcionaban, cómo los cerraste.
>
> Ese documento es una de las mejores cosas que vas a poder mostrar en una entrevista.

### Ejercicio 3 · mini-OT completa 🏁
> Cierra el sistema:
> 1. El frontend obtiene todo desde tu API. Nada de `localStorage`.
> 2. Crear una orden desde el formulario la guarda en la base de datos.
> 3. Cambiar un estado se refleja en la base.
> 4. Los filtros funcionan contra el servidor, no en el navegador.
> 5. Los tres estados —cargando, éxito, error— implementados en cada pantalla.
> 6. Recargas la página y todo sigue ahí, porque está en la base.
>
> **Prueba de aceptación, y la haces tú delante del mentor:**
> - [ ] Crear una orden nueva y verla en la lista.
> - [ ] Cerrarla y ver el cambio de color.
> - [ ] Intentar reabrirla y recibir el error correcto.
> - [ ] Filtrar por estado.
> - [ ] Recargar y comprobar que todo persiste.
> - [ ] Apagar el servidor y comprobar que el frontend avisa en vez de quedarse en blanco.
> - [ ] Mandar un `POST` inválido por Postman y recibir un `400` explicativo.

### Ejercicio 4 · *(ampliación)* Login
> Una pantalla de login con usuario y contraseña, contraseñas guardadas con `bcrypt`, y que no se pueda crear una orden sin haber entrado.

---

## Entregable de la semana

- [ ] 🏁 **mini-OT funcionando de punta a punta**, con la prueba de aceptación pasada.
- [ ] `seguridad.md` con los dos ataques documentados.
- [ ] `.env` fuera del repositorio y `.gitignore` correcto.
- [ ] Demo al equipo realizada.

## Presentación P8 — lunes 16 de noviembre · 🎤 **Demo de producto**

**"mini-OT: qué problema resuelve"**

**Esta presentación es distinta a todas las demás y hay que explicárselo.** No es técnica. No se menciona código, ni Express, ni SQL. Es la presentación que haría ante un cliente.

- Diapositiva 1: el problema. *"Un técnico va a una clínica, arregla un equipo, y hoy eso se anota en un cuaderno."*
- Diapositiva 2: la demo en vivo. Crear una orden de verdad, delante de todos.
- Diapositiva 3: a quién le sirve y qué le ahorra.
- Diapositiva 4: qué le falta para ser un producto real.
- Diapositiva 5: qué aprendió construyéndolo.

Este es el género que más le va a servir en consultoría, y es el más difícil: exige olvidarse de lo que le costó y hablar de lo que le sirve a otro.

## Tarea de mitad de semana *(1 hora)*

1. Armar P8 — la demo de producto merece más cuidado (35 min).
2. **Ensayar la demo en vivo tres veces.** Siempre se rompe algo; tener un plan B con capturas (25 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Devuelve el error de la base de datos al cliente | Corrígelo. Es un problema de seguridad real, no un detalle |
| Sube el `.env` al repositorio | Va a pasar. Que rote la credencial, no que solo borre el commit — la lección está ahí |
| Confía en la validación del frontend | Mándale un `POST` inválido por Postman delante de él. Se entiende en diez segundos |
| Quiere agregar funcionalidades nuevas | Frénalo. El objetivo del martes es **cerrar**, no ampliar. Aprender a cerrar es parte del oficio |
| Se bloquea en la demo | Normal. Plan B con capturas, y dile que a todos les pasa — porque es cierto |
