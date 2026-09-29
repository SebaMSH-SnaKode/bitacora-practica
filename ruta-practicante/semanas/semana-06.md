# Semana 6 — SQL: dónde viven los datos de verdad

**S10** Lun 26 oct · **S11** Mar 27 oct
**Objetivo:** que sepa modelar datos en tablas relacionadas y consultarlos, que es la habilidad más duradera de toda la práctica.

> 💡 **Lo que aprenda esta semana no caduca.** Los frameworks cambian cada tres años; SQL lleva cincuenta y sigue igual. Díselo: es una de las pocas cosas que va a usar toda su carrera tal como la aprende hoy.

---

## S10 — Lunes 26 de octubre · Modelar y consultar

### 10:00 – 10:30 · **Presentación P5** *(primera ante el equipo)*

### 10:30 – 11:15 · Por qué `localStorage` no alcanza

Empieza por el dolor, no por la teoría. Preguntas que él mismo puede responder mirando su mini-OT:

- ¿Qué pasa si el técnico abre el sistema en otro computador?
- ¿Qué pasa si son 50 técnicos?
- ¿Cómo sacas "todas las órdenes abiertas de la Clínica Alemana en octubre" sin recorrer todo a mano?

**Conclusión que llega solo:** los datos tienen que vivir en un lugar compartido, y ese lugar sabe buscar.

### 11:15 – 13:00 · El modelo relacional

- **Tabla, fila, columna.** La analogía honesta: una planilla Excel muy estricta.
- **Tipos de columna:** `INTEGER`, `TEXT`, `DATE`, `BOOLEAN`.
- **Clave primaria** — cómo se identifica una fila sin ambigüedad. Por qué no sirve el nombre.
- **Clave foránea** — cómo una tabla apunta a otra. **Este es el concepto del día.**
- **Relaciones:** uno a muchos (un cliente, muchos equipos). Dibújalo.
- **Diseñar el modelo de mini-OT juntos**, en pizarra: `clientes`, `equipos`, `ordenes` (ver `04-proyecto-mini-ot.md`).
- **`SELECT`:** columnas, `WHERE`, `ORDER BY`, `LIMIT`, `COUNT`.

Herramienta: **SQLite** (un archivo, cero instalación) con la extensión de SQLite en VS Code. PostgreSQL —el de Datamédica— se nombra, no se instala: gastaría media sesión.

### 14:00 – 17:00 · Ejercicios 1 y 2

---

## S11 — Martes 27 de octubre · Escribir, relacionar y usarlo desde código

### 10:15 – 11:30 · Concepto

- **`INSERT`, `UPDATE`, `DELETE`.** Y la advertencia que hay que dar hoy: **un `UPDATE` sin `WHERE` cambia todas las filas.** Que le pase en su base de práctica, hoy, a propósito.
- **`JOIN`** — traer datos de dos tablas a la vez. Es lo que hace útil a una base de datos; dedícale tiempo.
- **`GROUP BY` + `COUNT`** — responder "cuántas órdenes por técnico".
- **SQL desde Python** — módulo `sqlite3`: conectar, ejecutar, leer resultados. Aquí Python reaparece y le muestra que sirve como pegamento.

### 11:30 – 13:00 · Juntos
Migrar los datos de mini-OT desde `localStorage` a una base SQLite, con un script en Python que la crea y la puebla.

### 14:00 – 16:45 · Ejercicios 3 y 4

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Diseña el modelo ⭐
> **Antes de escribir una línea de SQL**, dibuja en papel las tres tablas de mini-OT: `clientes`, `equipos`, `ordenes`.
> Para cada una: qué columnas tiene, de qué tipo, cuál es la clave primaria y cuáles son las claves foráneas.
>
> Después responde por escrito:
> 1. ¿Por qué el número de serie del equipo no sirve como clave primaria, aunque sea único?
> 2. ¿Qué pasaría si guardáramos el nombre del cliente dentro de la tabla de órdenes, en vez de apuntar al equipo?
> 3. Si un cliente cambia de nombre, ¿cuántas filas hay que modificar en tu diseño?
>
> **La pregunta 2 es la importante.** La respuesta —que el dato quedaría repetido y podría contradecirse— es la razón por la que existen las bases de datos relacionales.

### Ejercicio 2 · Crea y puebla la base
> 1. Escribe el `CREATE TABLE` de las tres tablas, con sus claves.
> 2. Inserta 5 clientes (clínicas ficticias chilenas), 12 equipos repartidos entre ellos, y 20 órdenes de trabajo con estados variados y fechas de los últimos 3 meses.
>
> **Los datos deben ser verosímiles:** equipos de imagenología reales —rayos X, ecógrafo, mamógrafo, resonador, tomógrafo—, marcas reales, órdenes con descripciones que un técnico escribiría de verdad.
>
> Inventar datos creíbles te obliga a entender el negocio, y entender el negocio es la mitad del trabajo.

### Ejercicio 3 · Las diez consultas
> Escribe una consulta para cada pregunta. Guárdalas en `consultas.sql` con la pregunta como comentario arriba.
>
> 1. Todas las órdenes abiertas.
> 2. Las órdenes ordenadas de la más reciente a la más antigua.
> 3. Cuántas órdenes hay de cada estado.
> 4. Los equipos de un cliente específico.
> 5. Las órdenes de trabajo **con el nombre del equipo y el del cliente** (aquí necesitas `JOIN`).
> 6. El técnico que más órdenes ha cerrado.
> 7. Los equipos que **nunca** han tenido una orden de trabajo.
> 8. Las órdenes del último mes.
> 9. El cliente con más equipos.
> 10. Las órdenes cuya descripción menciona "mantención".
>
> La 7 es la difícil. Investiga `LEFT JOIN` — y si te cuesta, es la señal de que estás aprendiendo algo que vale.

### Ejercicio 4 · El accidente controlado
> En una copia de tu base de datos:
> 1. Ejecuta un `UPDATE` **sin** `WHERE` sobre la tabla de órdenes.
> 2. Mira lo que acaba de pasar.
> 3. Escribe en tu bitácora qué habría significado eso en un sistema en producción con 40.000 órdenes.
>
> Este susto de dos minutos, en una base de práctica, te va a hacer mirar dos veces antes de cada `UPDATE` por el resto de tu carrera.

### Ejercicio 5 · SQL desde Python
> Escribe `cargar_datos.py`: un script que crea la base, crea las tablas e inserta todos los datos de prueba. Que se pueda ejecutar cuantas veces quieras sin duplicar nada.
>
> Ese script se llama *seed* y los vas a ver en todos los proyectos serios, incluido Datamédica.

---

## Entregable de la semana

- [ ] Diagrama del modelo de datos, hecho por él, con las tres preguntas respondidas.
- [ ] Base SQLite creada y poblada con datos verosímiles.
- [ ] `consultas.sql` con las 10 consultas funcionando.
- [ ] `cargar_datos.py` reejecutable.
- [ ] Bitácora con la reflexión del `UPDATE` sin `WHERE`.

## Presentación P6 — lunes 2 de noviembre

**"Cómo se guardan los datos de Datamédica"**

- Diapositiva 2: **su** modelo de datos en diagrama. Esta es la mejor diapositiva 2 de toda la práctica: un diagrama entidad-relación explica en 30 segundos lo que en texto no se entiende.
- Diapositiva 3: la consulta 7, la difícil, y cómo llegó a ella.
- Pídele que termine explicando por qué el nombre del cliente no se guarda dentro de la orden. Si lo explica bien, entendió el modelo relacional.

## Tarea de mitad de semana *(1 hora)*

1. Armar P6 y pasar el diagrama a limpio (35 min).
2. Tres consultas más, inventadas por él, sobre preguntas que se le ocurran (25 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Repite datos en varias tablas | Aparece el concepto de normalización solo. Explícaselo en ese momento, no antes |
| No entiende el `JOIN` | Dibuja las dos tablas en papel y une las filas con una línea a mano. Funciona siempre |
| Usa `SELECT *` en todo | Está bien para aprender. Menciona por qué en producción se piden solo las columnas necesarias |
| Se le olvida el `WHERE` | Ya le pasó en el Ejercicio 4. Por eso está ese ejercicio |
| Quiere instalar PostgreSQL | Frénalo. SQLite hasta el final de la práctica; Postgres lo ve en el repo real en la semana 10 |
