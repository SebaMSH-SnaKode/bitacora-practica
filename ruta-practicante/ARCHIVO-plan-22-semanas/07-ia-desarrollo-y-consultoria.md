# 07 — Eje Transversal: IA para Desarrollar y Criterio de Consultoría en IA

Este eje corre en paralelo a todas las fases y cubre las dos competencias de IA que definen a la empresa:

1. **Desarrollar CON IA**: usar asistentes de IA (Claude Code, etc.) como parte del flujo profesional de desarrollo — como se construyó Datamédica.
2. **Aplicar IA generativa con sentido estratégico**: evaluar como consultor dónde la IA aporta valor real en un proyecto y dónde es solo moda. Recomendamos IA cuando aporta valor, y sabemos decir que no cuando no lo aporta — eso es lo que nos diferencia.

**Nota importante**: Datamédica **no tiene** integraciones de IA en su código, y eso es una lección en sí misma — fue una decisión con sentido: es un sistema transaccional de gestión de OTs donde la IA generativa no resolvía ningún problema del cliente. Fue, en cambio, **desarrollado con asistencia de IA**. El proyecto enseña ambas caras: cómo la IA multiplica al equipo que desarrolla, y cómo un buen consultor no la mete en el producto porque sí.

---

## Parte 1 — Desarrollar CON IA (progresión por etapas)

La IA acelera brutalmente a quien entiende lo que está haciendo, y estanca a quien no. Por eso el permiso de uso crece con la competencia:

### Etapa 1 — Fases 0–1: la IA es TUTOR, no generador
- **Permitido**: pedir explicaciones ("explícame qué hace este error", "dame otro ejemplo de map"), pedir ejercicios extra, pedir que le revise código YA escrito por él/ella y le señale problemas.
- **Prohibido**: pedirle que resuelva los ejercicios o genere el código de sus proyectos.
- Por qué: en esta etapa se está formando el músculo de pensar en lógica. Si la IA lo hace por él/ella, el músculo no crece — y en los checkpoints se nota de inmediato.

### Etapa 2 — Fases 2–3: la IA es COPILOTO con revisión obligatoria
- Puede generar código, con tres reglas:
  1. **Entender antes de aceptar**: si no puede explicar una línea, no entra al repo.
  2. **Verificar siempre**: la IA se equivoca con confianza; probar y testear todo lo generado.
  3. **Pedir chico**: prompts para funciones o componentes acotados, no "hazme la app". Quien pide chico entiende lo que recibe.
- Se enseña formalmente: **cómo escribir buenos prompts de desarrollo** (contexto + objetivo + restricciones + formato esperado), cómo iterar sobre una respuesta, cómo darle a la IA el contexto del proyecto (convenciones, ejemplos de código propio).
- Ejercicio quincenal: **autopsia de una sesión de IA** — trae al mentor una conversación real donde la IA lo ayudó y una donde lo confundió o alucinó; analiza por qué.

### Etapa 3 — Fases 4–5: la IA es HERRAMIENTA PROFESIONAL sobre código real
- Usos que se le enseñan sobre Datamédica: entender código ajeno ("explícame este módulo"), buscar en un repo grande, generar tests unitarios (¡su tarea real de la fase 5! — con la disciplina de revisar que los tests prueben algo de verdad y no solo pasen), redactar documentación, preparar PRs, hacer trazas asistidas.
- **Caso de estudio interno**: sesión con el equipo sobre cómo se desarrolló Datamédica con IA — qué se le delegó a la IA, qué se revisó con lupa, dónde ahorró semanas, dónde metió errores que hubo que atrapar, y cómo cambia el rol del desarrollador (de escribir todo a diseñar, dirigir y verificar).
- Regla profesional permanente: **el responsable del código es quien lo commitea, nunca la IA**. "Lo hizo la IA" no existe como excusa en revisión de código.

### Contenido conceptual mínimo (para no usar magia sin entenderla)
Una sesión + investigación I-10: qué es un LLM a nivel intuitivo (predicción de texto entrenada a escala), qué es el contexto/ventana, por qué alucina, qué son los tokens, qué es RAG a nivel concepto, y qué implica mandar código o datos de un cliente a un servicio de IA (confidencialidad — regla de la empresa: qué se puede compartir con qué herramienta).

---

## Parte 2 — Criterio de consultoría: ¿dónde aplicar IA generativa?

Se activa desde la fase 3 en adelante (necesita que ya entienda cómo se construye software). Formato: sesiones mensuales con el responsable de consultoría + los casos de análisis del documento 08.

### El marco de evaluación de la empresa (enseñarlo explícito)

Ante cualquier "¿le ponemos IA a esto?", el practicante aprende a responder cinco preguntas en orden:

1. **¿Cuál es el problema de negocio?** (no la tecnología). Si la respuesta empieza por "queremos usar IA", no hay problema definido todavía.
2. **¿La IA es la mejor herramienta para ESE problema?** Muchos problemas se resuelven mejor con un CRUD, una regla de negocio, una query o un formulario mejor diseñado. *Ejemplo interno: las alertas de vencimiento de modalidades de Datamédica son una query con fechas — meterle IA sería absurdo.*
3. **¿El error es tolerable?** La IA generativa es probabilística. ¿Qué pasa si se equivoca el 5% de las veces? Redactar un borrador de correo: tolerable. Calcular un cobro o decidir algo médico/legal: no tolerable sin humano en el circuito.
4. **¿Los números cierran?** Costo de API/infra + desarrollo + mantención vs. valor generado (horas ahorradas, ingresos, calidad). Estimación gruesa pero honesta.
5. **¿Riesgos y datos?** Confidencialidad de datos del cliente, privacidad (¡en salud, crítico!), dependencia del proveedor, y qué pasa cuando el modelo cambia.

**Salida del análisis**: una recomendación en una página — aplicar / no aplicar / aplicar en versión mínima primero — con argumentos. Se le enseña que **"no recomiendo IA aquí" es un entregable de consultoría valioso**, no un fracaso.

### Dónde SÍ suele aportar la IA generativa (mapa de casos de uso)
Procesamiento de lenguaje/documentos no estructurados (resumir, extraer, clasificar), búsqueda semántica sobre bases de conocimiento (RAG), borradores para revisión humana (correos, informes, propuestas), asistentes internos sobre documentación, y aceleración del propio desarrollo. Siempre con la pregunta 3 (tolerancia al error) delante.

### Ejercicio recurrente: comité de factibilidad
Una vez al mes (fases 3–5), el practicante recibe un caso (documento 08, serie C) y presenta 15 minutos ante el equipo su análisis con el marco de 5 preguntas. El equipo desafía sus argumentos como lo haría un cliente. Los casos incluyen deliberadamente:
- Casos donde la IA **sí** aporta (para que aprenda a diseñar la solución y estimarla).
- Casos donde la IA **no** aporta (para que aprenda a decir que no con argumentos).
- Casos grises (para que aprenda a proponer pilotos mínimos y medir).

### Ejercicio capstone (fase 5): propuesta de IA para Datamédica
Análisis serio: ¿hay algún lugar de la plataforma Datamédica donde IA generativa aportaría valor real hoy? Candidatos a evaluar (sin respuesta predefinida — que argumente): resumen automático del historial de un equipo antes de ir a terreno, borrador de la descripción de cierre de la OT a partir del checklist, clasificación automática de la falla reportada, chatbot de consulta para clientes. Debe aplicar el marco completo, incluyendo costos y el factor crítico del rubro salud/datos del cliente, y defender su recomendación — sea cual sea — ante el equipo.

---

## Entregables del eje IA

- [ ] Autopsias de sesiones de IA (quincenales desde fase 2) comentadas con el mentor.
- [ ] Investigación I-10 (qué es un LLM) presentada.
- [ ] 3 análisis de factibilidad (serie C) presentados al comité.
- [ ] Capstone: propuesta de IA para Datamédica defendida ante el equipo.

## Señales de alerta

- Dependencia: sin IA no puede escribir un bucle → volver una semana a etapa 1.
- Fe ciega: acepta salidas sin verificar → mostrarle una alucinación suya que llegó a PR y su costo.
- El péndulo contrario: rechaza la IA "porque se equivoca" → recordar que el estándar es el mismo que con código humano: se revisa todo.
- En factibilidad, recomienda IA en todos los casos → está evaluando la moda, no el problema; revisar juntos la pregunta 2.
