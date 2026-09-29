# Semana 4 — La primera pantalla

**S7** Mar 13 oct · *(Lun 12 oct: feriado — Encuentro de Dos Mundos)*
**Objetivo:** que mini-OT deje de vivir en la consola y tenga una cara.

> ⚠️ **Semana de una sola sesión.** No intentes meter dos temas en el martes. HTML y CSS son ideales para esto: autocontenidos, muy visuales y no dejan nada a medias.

---

## S7 — Martes 13 de octubre · HTML y CSS

### 10:00 – 10:30 · **Presentación P3** *(corrida desde el lunes)*

### 10:30 – 11:45 · HTML: la estructura

- Qué es una etiqueta. Apertura, cierre, atributos.
- El esqueleto: `html`, `head`, `body`.
- Las que va a usar: `h1`–`h3`, `p`, `div`, `span`, `ul`/`li`, `table`, `a`, `img`, `form`, `input`, `button`, `label`, `select`.
- **HTML semántico**, y por qué importa: `header`, `nav`, `main`, `section`, `footer`. Vender el argumento correcto: *le importa a los lectores de pantalla, a Google y al próximo que lea tu código*. Un `div` para todo funciona y es de mal profesional.
- **Formularios** — `form`, `input` con sus tipos, `label` asociado, `select`. Los va a necesitar la próxima semana.

### 11:45 – 13:00 · CSS: la apariencia

Solo lo que necesita. CSS es adictivo y se le puede ir media práctica centrando un `div` bonito.

- Cómo se conecta: archivo `.css` y `<link>`.
- **Selectores:** por etiqueta, por clase (`.`), por id (`#`). Con las clases basta.
- **Modelo de caja:** contenido, `padding`, `border`, `margin`. Dibújalo en la pizarra. Es *el* concepto de CSS.
- **Flexbox:** `display: flex`, `justify-content`, `align-items`, `gap`. Con esto arma cualquier layout que necesite.
- **Responsive:** una `@media` y por qué existe. Los técnicos de Datamédica trabajan en terreno con el teléfono: no es un lujo teórico.
- **Variables CSS** para los colores. Le enseña a no repetir.

### 14:00 – 16:45 · Maquetar mini-OT

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · La pantalla de órdenes de trabajo ⭐
> Maqueta la pantalla principal de mini-OT. **Solo HTML y CSS, todavía sin nada interactivo.**
>
> Debe tener:
> 1. Un encabezado con el nombre del sistema.
> 2. Una barra con tres botones de filtro: *Todas · Abiertas · Cerradas* (no funcionan aún, pero se ven).
> 3. Una lista de al menos 5 órdenes de trabajo inventadas. Cada una muestra: equipo, cliente, fecha, técnico y estado.
> 4. El estado tiene que **notarse a simple vista** sin leerlo: color distinto para abierta, en proceso y cerrada.
> 5. Un botón *"Nueva orden"*.
> 6. Un pie de página con tu nombre y el año.
>
> **Requisitos:**
> - Usa etiquetas semánticas: `header`, `main`, `footer`.
> - El CSS va en un archivo aparte.
> - Los colores, definidos como variables CSS arriba del archivo.
> - Las fechas en formato chileno: `13-10-2026`.
>
> **Criterio de terminado:** que alguien que nunca vio el sistema entienda de un vistazo cuáles órdenes están pendientes.

### Ejercicio 2 · Que funcione en el teléfono
> Haz que la pantalla se vea bien en un celular.
> - En pantalla ancha, las órdenes se ven en dos columnas.
> - En pantalla angosta, en una sola.
> - Nada se sale de la pantalla ni obliga a hacer scroll horizontal.
>
> Pruébalo con las herramientas de dispositivo de DevTools, no achicando la ventana a ojo.

### Ejercicio 3 · El formulario de orden nueva
> Una segunda página, `nueva-orden.html`, con el formulario para crear una orden:
> - Equipo: un `select` con al menos 4 equipos.
> - Descripción del trabajo: un campo de texto largo.
> - Técnico: campo de texto.
> - Fecha: `input` de tipo fecha.
> - Botones *Guardar* y *Cancelar*.
>
> **Requisito:** cada campo con su `label` correctamente asociado. Averigua por qué eso importa para alguien que usa un lector de pantalla — y ponlo en tu bitácora.

### Ejercicio 4 · *(ampliación)* Lee código ajeno
> Abre DevTools en un sitio que te guste, busca un componente que te llame la atención y responde:
> 1. ¿Qué etiquetas usaron?
> 2. ¿Usaron flexbox o grid?
> 3. Replica algo parecido en tu propia página.
>
> Leer código ajeno es la mitad del trabajo de un desarrollador. Empieza hoy.

---

## Entregable de la semana

- [ ] `index.html` + `estilos.css` con la pantalla de órdenes, semántica y responsive.
- [ ] `nueva-orden.html` con el formulario completo.
- [ ] Todo commiteado con mensajes en el formato de la empresa.
- [ ] Bitácora de la sesión.

## Presentación P4 — lunes 19 de octubre

**"Cómo se construye una página web"**

- Diapositiva 1: captura de **su** pantalla de mini-OT. Es la primera vez que tiene algo bonito que mostrar: aprovéchalo.
- Diapositiva 2: el modelo de caja dibujado por él.
- Diapositiva 3: que cuente una pelea real con CSS. Todos tienen una.

## Tarea de mitad de semana *(1 hora + 3 días extra por el feriado)*

Esta semana tiene más aire: el feriado le regaló tiempo.

1. Armar P4 (30 min).
2. Terminar de pulir la pantalla: que quede algo que le dé orgullo mostrar (30 min).
3. Leer una guía visual de flexbox — un enlace, no una búsqueda (15 min).
4. **Opcional, y ofrécelo:** cambiar la paleta de colores a algo propio. Que el proyecto se sienta suyo.

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Un `div` para absolutamente todo | Corrígelo ahora. Cuesta poco y es un hábito que dura años |
| Estilos en línea con `style="..."` | Muéstrale por qué duele: pídele cambiar un color en 20 elementos |
| Se le va la tarde eligiendo colores | Ponle límite de tiempo. Es entretenido y es una trampa |
| No entiende por qué el margen no hace nada | Modelo de caja en la pizarra otra vez. Nadie lo entiende a la primera |
| Copia una plantilla entera de internet | Regla del día: *puede inspirarse en cualquier cosa, pero tiene que poder explicar cada regla CSS que quede en su archivo* |
