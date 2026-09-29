# 06 — Fase 5: Soporte a Producción (Semanas 19–22)

**Objetivo final del programa**: que el practicante pueda tomar tickets de soporte de Datamédica y resolverlos con supervisión — diagnosticar, reproducir, corregir, testear y seguir el proceso de deploy. Aquí se convierte en un miembro útil del equipo.

**Regla permanente**: en esta fase toca código que llega a producción. Todo pasa por PR revisado. Acceso a infra de producción: solo lectura (logs, métricas) y siempre acompañado al inicio.

---

## Semana 19 — El oficio del debugging

- **Metodología de diagnóstico** (enseñarla como proceso, no como intuición):
  1. Reproducir el problema (si no se reproduce, no se entiende).
  2. Aislar: ¿es frontend, API, base de datos, infra, o el usuario?
  3. Hipótesis → verificación → descarte. Una a la vez.
  4. Documentar el hallazgo aunque no haya fix todavía.
- Herramientas por capa:
  - Web: DevTools a fondo — Network (¿el request salió? ¿con qué status volvió?), Console, React DevTools.
  - API: logs de Winston, debugger de VS Code sobre NestJS, Swagger/Postman para reproducir requests aislados.
  - BD: conectarse y consultar; `EXPLAIN` básico para queries lentas.
- **Simulacros de bugs** (el mentor rompe cosas a propósito en el entorno dev y el practicante diagnostica): un guard que rechaza un rol válido, una migración no aplicada, un `staleTime` que muestra datos viejos, una variable de entorno faltante, un CORS mal configurado. Uno por día. Se evalúa el *proceso*, no la velocidad.

## Semana 20 — Testing en serio + calidad

- **Ampliar cobertura real**: continuar los tests unitarios de módulos CRUD sin specs (arrancado en fase 4). Meta concreta y medible: dejar 2 módulos con cobertura decente.
- **Playwright (e2e web)**: leer los specs existentes en `apps/e2e` (Page Objects, fixtures), correr la suite local, y escribir 1 spec nuevo para un flujo no cubierto.
- Qué es una regresión y por qué los tests son la red de seguridad del soporte: *"el fix que rompe otra cosa"*.
- **Revisión de código como disciplina**: el practicante revisa un PR real del equipo (aunque su aprobación no sea vinculante). Aprende a leer diffs y a comentar con respeto y precisión.
- Conversación abierta con el equipo: la deuda técnica del proyecto (CI sin lint/typecheck/tests, `ignoreBuildErrors`, archivos gigantes) — por qué existe, qué costó, qué haríamos distinto. *Formación de criterio: la deuda se gestiona, no se niega.*

## Semana 21 — Observabilidad, infra y proceso de incidentes

- **La infra real, guiada por `INFRA_RUNBOOK.md`**: Azure Container Apps (backend, frontend, PowerSync), PostgreSQL Flexible Server, Blob Storage, Container Registry. Tour guiado por el portal de Azure (solo lectura).
- **Logs y métricas**: Application Insights / Log Analytics — buscar un request por `request-id`, ver errores recientes, leer una traza.
- **CI/CD**: GitHub Actions (`deploy-api.yml`, `deploy-web.yml`) — qué pasa cuando se hace push a `develop`, cómo ver un deploy corriendo, cómo se vería un rollback.
- **Flujo de un ticket de soporte en la empresa** (formalizarlo si no está escrito — buen ejercicio conjunto):
  1. Llega el reporte → registrar con: quién, qué esperaba, qué pasó, cuándo, evidencia (pantallazo/OT afectada).
  2. Clasificar severidad: ¿producción caída? ¿funcionalidad bloqueada? ¿molestia cosmética?
  3. Reproducir en dev → diagnosticar → proponer fix → PR → revisión → deploy → **verificar en producción → avisar al usuario que reportó**.
- Casos típicos de Datamédica para practicar el guion de diagnóstico: "no puedo iniciar sesión" (¿bloqueo por intentos? ¿MFA? ¿sesión inactiva?), "no me llegó el correo de la OT", "la app móvil no sincroniza" (PowerSync/offline), "el PDF sale sin la firma".

## Semana 22 — Soporte real + cierre del programa

- **Tickets reales supervisados**: el practicante toma 2–3 tickets/tareas reales del backlog con el flujo completo. El mentor está disponible pero interviene solo si se lo pide o si hay riesgo.
- **Guardia acompañada**: si ocurre un incidente real durante la semana, lo vive junto al mentor de principio a fin.
- **Presentación final** (P-08, documento 08): ante todo el equipo — qué aprendió, qué construyó, sus contribuciones reales al proyecto, y una propuesta de mejora argumentada para Datamédica o para este mismo programa de formación.
- **Evaluación final y feedback bidireccional** (documento 09).

---

## Entregables de la fase

- [ ] Mínimo 5 simulacros de bug diagnosticados con su proceso documentado.
- [ ] 2 módulos del backend con tests unitarios nuevos + 1 spec de Playwright, mergeados.
- [ ] 2–3 tickets reales resueltos de punta a punta (diagnóstico → PR → verificación).
- [ ] Documento propio: **"Guía de diagnóstico de soporte Datamédica"** — su runbook personal con los casos típicos y cómo atacarlos. *Si queda bueno, se incorpora a la documentación oficial del proyecto: legado real de su práctica.*
- [ ] Presentación final.

## Señales de alerta para el mentor

- Adivina en vez de diagnosticar ("debe ser X, lo cambio y vemos") → volver al proceso de hipótesis-verificación; prohibido cambiar código sin haber reproducido.
- Miedo paralizante a romper producción → recordar las redes: PR revisado, tests, rollback posible. El miedo sano es bueno; el pánico, no.
- Resuelve pero no comunica → practicar el cierre del ticket: qué digo al usuario, qué dejo escrito.

## Perfil de salida logrado

Si completa esta fase, el practicante puede: tomar un ticket de soporte y llevarlo de reporte a fix verificado; escribir tests que protegen el sistema; leer logs y métricas en Azure; explicar la arquitectura completa de Datamédica; y trabajar con los estándares del equipo. Está listo para una oferta de continuidad o para iniciar su carrera con una base sólida real.
