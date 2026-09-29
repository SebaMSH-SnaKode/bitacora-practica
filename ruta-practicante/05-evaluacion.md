# 05 — Evaluación y seguimiento

## Los cuatro checkpoints

Son **bloqueantes**: si no los cumple, se repite, no se avanza. Es mejor cerrar noviembre con 14 sesiones sólidas que con 20 de barniz.

Cada uno se hace en 30 minutos, al inicio de la sesión, con él explicando **su propio código sin la IA delante**.

---

### Checkpoint 1 — S5 (lun 5 oct) · ¿Puede programar?

- [ ] Escribe una función con un condicional y un bucle **sin ayuda**.
- [ ] Explica qué hace cada línea de un programa suyo de la semana pasada.
- [ ] Sabe qué es una variable, una lista y una función, en sus palabras.
- [ ] Su repositorio tiene commits con el formato de la empresa.

**Si no lo cumple:** repetir la semana 2 con ejercicios más chicos. Es el checkpoint más recuperable y el más importante de no saltarse. Sin esto, todo lo demás es memorizar.

---

### Checkpoint 2 — S10 (lun 26 oct) · ¿Se desatora solo?

- [ ] Ante un error nuevo, lo lee antes de preguntar.
- [ ] Aplicó la regla de los 30 minutos al menos una vez de forma visible.
- [ ] Sus preguntas traen contexto: qué quería, qué intentó, qué pasó.
- [ ] Dibuja el viaje de un request sin ayuda.
- [ ] Su mini-OT responde a los clics.

**Si no lo cumple:** dedicar la sesión 11 completa a depuración con bugs plantados, y correr todo una sesión. Vale la pena: sin autonomía, el mentor se convierte en un cuello de botella hasta noviembre.

---

### Checkpoint 3 — S15 (mar 10 nov) · ¿Entiende el sistema completo?

- [ ] Agrega un campo nuevo que viaje **desde el formulario hasta la base de datos y vuelva a la pantalla**.
- [ ] Explica qué hace cada capa y por qué está separada.
- [ ] Sabe por qué la validación del servidor no es opcional.
- [ ] mini-OT pasa la prueba de aceptación de la semana 8.

**El primer punto es la prueba de fuego de toda la práctica.** Si puede recorrer las cuatro capas para agregar un campo, entendió cómo funciona un sistema. Si no, le falta una capa específica: identifica cuál y refuérzala antes del deploy.

---

### Checkpoint 4 — S20 (lun 30 nov) · ¿Puede trabajar en equipo?

- [ ] Toma un ticket acotado y **hace preguntas antes de empezar**.
- [ ] Trabaja en una rama y abre un PR con descripción útil.
- [ ] Atiende los comentarios de una revisión sin tomárselo a pecho.
- [ ] Traza una acción de punta a punta en el código real.
- [ ] Su presentación final tiene promedio 3 o más en la rúbrica de comunicación.

---

## Rúbrica técnica

Se evalúa al final de cada fase, de 1 a 4. Se conversa con él, no se le entrega una nota.

| Criterio | 1 · Inicial | 2 · En desarrollo | 3 · Esperado | 4 · Destacado |
|---|---|---|---|---|
| **Lógica** | Necesita ayuda para empezar | Resuelve con guía | Resuelve solo problemas conocidos | Descompone problemas nuevos |
| **Autonomía** | Pregunta de inmediato | Intenta un poco | Aplica la regla de los 30 | Investiga y propone alternativas |
| **Depuración** | Cambia cosas al azar | Lee el error | Aísla el problema con método | Diagnostica antes de tocar el código |
| **Calidad** | Todo junto, sin nombres | Funciones sueltas | Código legible y separado | Piensa en quien lo lea después |
| **Git** | Commits gigantes | Commits frecuentes | Formato de la empresa, historial claro | PRs bien descritos |
| **Casos borde** | Solo el caso feliz | A veces valida | Valida y maneja errores | Piensa qué puede fallar antes de escribir |
| **Comunicación** | Cuesta entenderle | Se entiende con esfuerzo | Explica con claridad | Lo entendería alguien no técnico |

**Meta al cierre:** promedio 3, con al menos dos criterios en 4. Empezar la práctica en 1 en casi todo es exactamente lo esperado — díselo.

---

## Seguimiento semanal

**Diez minutos cada martes a las 16:45**, y queda escrito en `SEGUIMIENTO.md`:

- Qué se completó de lo planificado.
- Qué quedó pendiente y por qué.
- Cómo está anímicamente. *(No es un detalle blando: la deserción en prácticas es casi siempre emocional, no técnica.)*
- Ajuste para la semana siguiente.

---

## Si el tiempo no alcanza

Va a pasar. Orden de recorte, de lo primero que se sacrifica a lo último:

1. **Ampliaciones** — todos los ejercicios marcados *(ampliación)*.
2. **Pruebas automatizadas** (S16) — pasa a demostración del mentor, sin ejercicio.
3. **Script de reportes en Python** (S17) — se recorta a media sesión.
4. **Deploy** (S16) — lo hace el mentor con él mirando y narrando. No es lo mismo, pero el concepto queda.
5. **Ticket real** (S19) — se reemplaza por un ticket simulado sobre mini-OT.

**Nunca se recorta:**
- La semana 1 y 2 (lógica). Sin base, lo demás es imitación.
- La sesión 5 (depurar). Es la que da autonomía; recortarla cuesta más caro que cualquier otra.
- El checkpoint 3 (S15). Es la prueba de que entendió el sistema.
- Las presentaciones. Son la mitad del valor del programa y lo que más lo va a diferenciar.

---

## Guía rápida del mentor

- **Prepara poco, corrige mucho.** No hacen falta clases magistrales; hace falta estar disponible y hacer buenas preguntas: *¿qué esperabas que pasara?*, *¿cómo lo verificarías?*
- **Déjalo equivocarse barato.** Interviene antes solo si el error va a costar días o moral.
- **Narra tu proceso en voz alta.** Cómo lees un error, cómo buscas, cómo decides. Es la clase más valiosa que va a recibir.
- **Los dos valles están marcados:** semana 3 y semana 10. Anúncialos antes de que lleguen.
- **La frustración se ve como aburrimiento.** Se calla, se pone lento, dice que sí a todo. Achica la tarea; no bajes la exigencia.
- **Celebra los hitos de verdad.** La app completa (S15) y el deploy (S16) merecen que el equipo se entere. Cuestan diez minutos y sostienen semanas.
- **Feedback en los dos sentidos.** Al final de cada fase, pregúntale qué mejorarías del programa, y actualiza estos documentos. Esto también está en desarrollo.
