# 08 — Investigaciones, Análisis y Presentaciones

Catálogo de tareas para que el practicante **investigue, analice y presente**. Son tan formativas como el código: entrenan autonomía para aprender, pensamiento crítico y comunicación técnica — el corazón del rol de consultor.

## Formato estándar

- **Investigación (serie I)**: documento Markdown de 1–3 páginas en su repo de bitácora + presentación de 15 min al mentor o al equipo (viernes). Debe incluir: qué es, por qué importa para nosotros/Datamédica, cómo funciona (con un diagrama propio), y 3 preguntas que le quedaron abiertas.
- **Análisis de código (serie A)**: sobre el repo real de Datamédica. Documento + walkthrough en vivo compartiendo pantalla.
- **Casos de consultoría (serie C)**: análisis de factibilidad de IA con el marco de 5 preguntas del documento 07. Presentación de 15 min + ronda de preguntas del equipo actuando como cliente escéptico.
- **Presentaciones hito (serie P)**: demos de fin de fase ante el equipo.

**Regla de calidad**: toda afirmación importante con fuente (documentación oficial > blog random). Puede investigar CON IA, pero debe contrastar con fuentes: la presentación se defiende en vivo y las preguntas del equipo detectan rápido el conocimiento prestado.

---

## Serie I — Investigaciones (calendario por fase)

| # | Fase | Tema | Pregunta guía |
|---|---|---|---|
| I-01 | 0 | El viaje de un request | ¿Qué pasa desde que escribo una URL hasta que veo la página? (DNS, HTTP, servidor, BD) |
| I-02 | 1 | Historia y ecosistema de JavaScript | ¿Por qué el mismo lenguaje corre en el navegador y en el servidor? ¿Qué es Node.js realmente? |
| I-03 | 1 | Tipado: ¿por qué existe TypeScript? | ¿Qué clase de errores atrapa un compilador y cuánto cuesta un error en producción? |
| I-04 | 2 | Renderizado web: SPA vs SSR | ¿Qué hace Next.js que React solo no hace, y por qué Datamédica usa Next? |
| I-05 | 2 | Estado servidor y caché | ¿Qué problemas resuelve React Query? ¿Qué pasa si dos usuarios editan lo mismo? |
| I-06 | 3 | SQL vs NoSQL | ¿Por qué Datamédica usa PostgreSQL y no MongoDB? ¿Cuándo elegirías lo contrario? |
| I-07 | 3 | APIs REST bien diseñadas | Verbos, códigos de estado, paginación, versionado. Auditar 5 endpoints del mini-OT propio contra las buenas prácticas. |
| I-08 | 4 | Autenticación moderna | JWT, refresh rotativo, MFA/TOTP, passkeys, cookies httpOnly — explicado sobre el flujo REAL de login de Datamédica. |
| I-09 | 4 | Offline-first | ¿Por qué la app móvil de Datamédica funciona sin señal? ¿Qué es PowerSync y qué problema del negocio resuelve (ingenieros en sótanos de hospitales)? |
| I-10 | 3–4 | ¿Qué es un LLM? | Cómo funciona a nivel intuitivo, por qué alucina, qué son tokens y contexto, qué es RAG. Base del eje de consultoría. |
| I-11 | 5 | Observabilidad | Logs, métricas y trazas: ¿cómo sabemos que producción está sana? ¿Qué es Application Insights? |
| I-12 | 5 | Seguridad en aplicaciones de salud | ¿Qué datos maneja Datamédica, qué obligaciones existen (ley de protección de datos en Chile), y cómo el diseño del sistema las aborda? |

## Serie A — Análisis sobre el código real (fases 4–5)

| # | Tema | Consigna |
|---|---|---|
| A-01 | Modelo de dominio | Dibujar el diagrama entidad-relación de los 24 modelos de `schema.prisma` agrupados por área (identidad, comercial, catálogo, operación). Detectar y reportar que el README dice 18. |
| A-02 | Anatomía de un módulo | Diseccionar el módulo `equipment` completo (controller → service → repository → prisma) y explicar qué hace cada capa y por qué existe la separación. |
| A-03 | El archivo gigante | `apps/web/(dashboard)/work-orders/page.tsx` tiene ~2.700 líneas. Analizar qué responsabilidades mezcla y proponer un plan de refactor en componentes/hooks (solo propuesta escrita — ejecutarlo es decisión del equipo). |
| A-04 | Auditoría de deuda técnica | Con la lista de deuda conocida (CI sin tests, `ignoreBuildErrors`, módulos sin specs, docs desactualizadas): priorizarla por riesgo/esfuerzo en una matriz y defender el orden. *Ejercicio de criterio de consultor sobre código.* |
| A-05 | Propuesta de pipeline CI | Diseñar (en documento) el pipeline que falta: lint + typecheck + tests antes de deploy. Qué correría, en qué orden, qué bloquearía. Comparar con el `deploy-api.yml` actual. |

## Serie C — Casos de consultoría de IA (1/mes desde fase 3)

Aplicar siempre el marco de 5 preguntas (documento 07). El mentor puede ajustar los casos a clientes/contextos reales de la empresa.

| # | Caso | Trampa pedagógica |
|---|---|---|
| C-01 | Una clínica quiere un chatbot con IA para agendar horas médicas. | Gris: el agendamiento es transaccional (formulario/reglas lo hace mejor), pero la consulta ambigua en lenguaje natural puede aportar. Debe separar el problema en partes. |
| C-02 | Una empresa de mantención (como Datamédica) quiere "IA que prediga fallas de equipos". | La IA generativa NO es esto; sería ML predictivo clásico y requiere datos históricos que quizá no existen. Debe distinguir tipos de IA y evaluar los datos disponibles. |
| C-03 | Un estudio de abogados quiere resumir y buscar en miles de contratos. | Caso donde SÍ: lenguaje no estructurado, error tolerable con revisión humana, RAG clásico. Debe diseñar la solución y estimar costos, y abordar la confidencialidad. |
| C-04 | Un gerente pide "ponerle IA" al dashboard de su ERP "porque la competencia lo anunció". | No hay problema definido. Debe practicar la conversación de descubrimiento: qué preguntas haría antes de proponer nada, y cómo decir "no todavía" sin perder al cliente. |
| Capstone | ¿Dónde aportaría IA generativa dentro de Datamédica hoy? | Sin respuesta predefinida. Candidatos en documento 07. Se evalúa el rigor del análisis, no la conclusión. |

## Serie P — Presentaciones hito

| # | Momento | Contenido |
|---|---|---|
| P-01 | Fin fase 1 | Demo del mini-OT en consola + qué aprendió programando por primera vez. |
| P-02 | Fin fase 2 | Demo del mini-OT web + una decisión técnica defendida. |
| P-03 | Fin fase 3 | Demo full-stack (web + API + BD) + arquitectura dibujada por él/ella. |
| P-04 | Fin fase 4 | "Datamédica explicada por mí": dominio, arquitectura y una traza end-to-end en vivo ante el equipo. |
| P-08 | Fin del programa | Presentación final: trayectoria, contribuciones reales mergeadas, capstone de IA, y una propuesta de mejora (al producto o a este programa). |

---

## Guía para evaluar presentaciones (mentor y equipo)

Puntuar 1–4 en cada eje; retroalimentar siempre con algo bueno + algo a mejorar:

1. **Comprensión**: ¿explica con sus palabras o recita? Las preguntas de seguimiento lo revelan.
2. **Estructura**: ¿problema → concepto → cómo funciona → por qué nos importa?
3. **Honestidad técnica**: ¿distingue lo que sabe de lo que no? ¿Dice "no sé, lo voy a averiguar"? (Se premia, nunca se castiga.)
4. **Comunicación**: ¿se entiende? ¿Los diagramas ayudan? ¿Respeta el tiempo?
