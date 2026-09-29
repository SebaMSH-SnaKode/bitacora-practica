# 09 — Evaluación, Seguimiento y Guía del Mentor

## Filosofía de evaluación

Evaluamos para **ajustar el ritmo**, no para castigar. Un checkpoint no cumplido significa "esta fase necesita más tiempo", nunca "el practicante falló". Lo único inaceptable es la deshonestidad (fingir entender, presentar trabajo de la IA como comprensión propia) — y se maneja conversando, porque casi siempre nace del miedo a decepcionar.

## Instrumentos de seguimiento

1. **Bitácora semanal** del practicante (repo personal): qué hizo, qué aprendió, qué lo trabó. El mentor la lee antes del 1:1.
2. **1:1 semanal** (lunes, 30 min): revisar semana anterior, planificar la siguiente, destrabar.
3. **Demo/presentación de los viernes** (15–20 min): ritmo de exposición constante.
4. **Checkpoint de fin de fase**: sesión de 1–1,5 h con los criterios de abajo. En vivo, sin IA, con pantalla compartida.
5. **Revisión de código**: desde fase 2, todo proyecto se revisa como un PR real — es donde más se enseña.

## Checkpoints de salida por fase

El practicante avanza cuando cumple **todos** los criterios de la fase. Formato: el mentor plantea las tareas en vivo; se evalúa proceso y comprensión, no velocidad.

### Fase 0 → 1
- [ ] Explica el viaje de un request (con su diagrama) respondiendo preguntas.
- [ ] En terminal: navega, crea estructura de carpetas, usa Git (add/commit/branch/merge) sin mirar apuntes.
- [ ] Entorno completo funcionando (node 22, git, VS Code).
- [ ] Bitácoras de las 2 semanas escritas.

### Fase 1 → 2
- [ ] Resuelve en vivo un ejercicio de lógica nuevo (nivel: filtrar y transformar un array de objetos) **sin IA**, pensando en voz alta.
- [ ] Explica cualquier fragmento de su mini-OT que el mentor elija al azar.
- [ ] Demuestra async/await consumiendo una API y explica qué pasaría sin `await`.
- [ ] Explica 3 errores de TypeScript reales y cómo los resolvió.

### Fase 2 → 3
- [ ] Dibuja el árbol de componentes de su app y el flujo de datos.
- [ ] Explica qué es estado servidor y por qué React Query (con el ejemplo de caché e invalidación de su propia app).
- [ ] En vivo: agrega un campo nuevo a formulario + tabla (con la API de práctica) en menos de una hora.
- [ ] Distingue server/client components con ejemplos de su código.

### Fase 3 → 4
- [ ] Explica el patrón Controller → Service → Repository y POR QUÉ existe (testabilidad, independencia del ORM).
- [ ] En vivo: escribe un endpoint nuevo completo (DTO + service + repo + Prisma) con ayuda de documentación.
- [ ] Explica qué hay dentro de un JWT y el porqué de access + refresh.
- [ ] Escribe 5 queries SQL sobre su esquema, incluyendo un JOIN y un GROUP BY.
- [ ] Sus tests corren y explica qué protege cada uno.

### Fase 4 → 5
- [ ] Cuenta el flujo de negocio completo de Datamédica (de la falla al informe PDF) y los 5 roles.
- [ ] Traza en vivo una funcionalidad que NO haya trazado antes (el mentor elige) por todas las capas.
- [ ] 2+ PRs mergeados a `develop` con máximo 2 rondas de revisión.
- [ ] Recita las convenciones clave sin apuntes (commits, idiomas, fechas es-CL, soft delete, @Roles).

### Fase 5 → egreso
- [ ] Ticket simulado completo en vivo: reporte → reproducción → diagnóstico → fix → test → PR (el mentor hace de usuario que reportó).
- [ ] Encuentra un error real en Application Insights / logs a partir de un request-id.
- [ ] Su "Guía de diagnóstico de soporte" está escrita y revisada.
- [ ] Capstone de IA defendido: aplicó el marco de 5 preguntas con rigor (la conclusión es libre).
- [ ] Presentación final realizada.

## Rúbrica transversal (aplicar en cada checkpoint, escala 1–4)

| Dimensión | 1 — Inicial | 2 — En desarrollo | 3 — Logrado | 4 — Destacado |
|---|---|---|---|---|
| Comprensión técnica | Recita sin entender | Entiende con ayuda | Explica con sus palabras y ejemplos | Conecta conceptos entre capas y anticipa consecuencias |
| Autonomía | Se bloquea y espera | Intenta antes de preguntar | Regla de 30 min internalizada; preguntas con contexto | Se destraba solo y documenta el camino para otros |
| Calidad de código | No funciona / caótico | Funciona pero desordenado | Funciona, legible, sigue convenciones | Además simple: elige la solución más sencilla que sirve |
| Uso de IA | Dependencia o fe ciega | Usa pero verifica a medias | Etapa correcta del doc 07: entiende y verifica todo | La usa estratégicamente y detecta sus errores rápido |
| Comunicación | No puede explicar su trabajo | Explica con dificultad | Presenta claro, admite lo que no sabe | Adapta el mensaje a la audiencia; sus docs sirven a otros |

**Umbral para avanzar de fase**: nada en 1, y comprensión técnica mínimo en 3.

## Si el tiempo no alcanza (prácticas más cortas)

Prioridad de recorte, de lo primero que se sacrifica a lo último:
1. Mobile/PowerSync (queda solo mención) y semana 21 de infra (se reduce a 2 días).
2. Serie C completa → dejar 1 caso + capstone reducido.
3. Fase 2 y 3 se comprimen fusionando semanas de práctica (proyectos más pequeños).
4. **Nunca recortar**: fase 1 (lógica), el patrón backend de la fase 3, las trazas de la fase 4, ni el flujo de ticket de la fase 5.

## Guía rápida del mentor

- **Prepara poco, corrige mucho**: no necesitas clases magistrales; necesitas estar disponible, revisar código a diario (10–15 min) y hacer buenas preguntas ("¿qué esperabas que pasara?", "¿cómo lo verificarías?").
- **Deja que se equivoque barato**: el error en dev es el mejor profesor; interviene antes solo si el error va a costar días o moral.
- **Modela el oficio en voz alta**: cuando resuelvas algo delante del practicante, narra tu proceso — cómo lees un error, cómo buscas, cómo decides. Es la clase más valiosa que puede recibir.
- **Cuida la moral**: aprender a programar desde cero tiene valles profundos (típico: semanas 4–5 y la llegada al repo real en la 15). Nómbralo antes de que pase: "esto le pasa a todos, es señal de que estás aprendiendo".
- **Feedback bidireccional**: al final de cada fase, pregunta qué mejorarías del programa — y usa las respuestas para actualizar estos documentos. Este programa también está en desarrollo.

## Registro

Mantener en este mismo directorio un `SEGUIMIENTO.md` (privado del mentor si se prefiere) con: fecha de inicio, resultado y notas de cada checkpoint, acuerdos de los 1:1, y ajustes hechos al plan. Sirve para el informe final de práctica y para mejorar el programa con el siguiente practicante.
