# 00 — Visión General del Programa

## Objetivo

Formar a un practicante desde cero absoluto hasta que pueda:

1. **Dar soporte supervisado a Datamédica en producción**: diagnosticar bugs, escribir fixes acotados, agregar tests, leer logs y seguir el runbook de incidentes.
2. **Entender el ciclo completo de desarrollo**: desde el requerimiento hasta el deploy, pasando por código, revisión, testing y documentación.
3. **Trabajar con IA como herramienta profesional**: desarrollar asistido por IA con criterio, y evaluar con sentido estratégico dónde la IA generativa aporta valor en un proyecto y dónde no.
4. **Iniciar su carrera como informático** con hábitos profesionales: comunicación técnica, autonomía para investigar, y capacidad de presentar y defender sus análisis.

## Contexto: qué es Datamédica

El proyecto que usaremos como base formativa es **datamedica-platform**: un sistema de gestión de **órdenes de trabajo (OT) de postventa para equipos de imagenología médica**. Datamédica (el cliente) da mantenimiento correctivo y preventivo a equipos médicos instalados en hospitales y clínicas de Chile; la plataforma gestiona sus cuentas (clientes), sucursales, inventario de equipos, órdenes de trabajo con evidencias fotográficas y firma del cliente en terreno, checklists, reportes PDF/Excel y alertas de vencimiento de contratos.

**Importante para explicárselo al practicante**: no es una plataforma clínica (no maneja pacientes ni exámenes); es una plataforma de servicio técnico para el rubro de salud.

### Stack tecnológico (lo que el practicante debe dominar al final)

| Capa | Tecnología |
|---|---|
| Monorepo | Turborepo + npm workspaces, Node 22, TypeScript 5.9 |
| API | NestJS 11 (REST), Prisma 6 + PostgreSQL 16, class-validator, Swagger |
| Web | Next.js 16 (App Router), React 19, Tailwind CSS 4, shadcn/Radix, TanStack React Query 5, react-hook-form |
| Mobile | Expo / React Native, expo-router, PowerSync (offline-first) — *nivel lectura, no dominio* |
| Compartido | `packages/shared-core` (cliente API, hooks, tipos, constantes) |
| Seguridad | JWT + refresh rotativo, MFA (TOTP/passkeys), CSRF, cifrado de payloads — *nivel comprensión conceptual* |
| Infra | Docker, Azure Container Apps, GitHub Actions, Azure Blob, Application Insights |
| Testing | Jest (API), Playwright (e2e web) |

## Duración y estructura

**22 semanas (~5,5 meses)**, ajustable al ritmo real del practicante. Si la práctica es más corta, el documento 09 indica qué recortar; la regla es recortar amplitud (mobile, infra avanzada), nunca fundamentos.

| Fase | Semanas | Tema | Resultado |
|---|---|---|---|
| 0 | 1–2 | Fundamentos: computador, terminal, Git, cómo funciona la web | Entorno funcionando; primer repo propio |
| 1 | 3–6 | Programación: JavaScript → TypeScript, HTML/CSS | Piensa en lógica; pequeños programas propios |
| 2 | 7–10 | Frontend: React, Next.js, Tailwind, React Query | Mini-app web funcional |
| 3 | 11–14 | Backend: NestJS, PostgreSQL, Prisma, REST, auth, Docker | API propia con BD, probada con tests |
| 4 | 15–18 | Datamédica: arquitectura, dominio, convenciones, código real | Navega el repo con soltura; primer PR |
| 5 | 19–22 | Soporte: testing, debugging, observabilidad, incidentes, deploy | Resuelve tickets reales supervisado |
| IA | transversal | Desarrollar con IA + consultoría de IA generativa | Usa IA con criterio; evalúa factibilidad |

### Proyecto integrador de las fases 1–3: "mini-OT"

A lo largo de las fases 1 a 3 el practicante construye **una versión en miniatura de Datamédica** — una app de órdenes de trabajo simplificada (clientes, equipos, OTs con estados). Cada fase le agrega una capa: lógica pura (fase 1), interfaz web (fase 2), API y base de datos (fase 3). Así, al llegar al proyecto real en fase 4, ya construyó una analogía completa con sus propias manos y todo le resulta reconocible.

## Ritmo semanal sugerido

- **Lunes**: planificación de la semana con el mentor (30 min). Qué va a estudiar, qué va a construir, qué duda quedó pendiente.
- **Martes a jueves**: estudio + práctica. Regla 40/60: máximo 40% consumiendo material, mínimo 60% escribiendo código o documentos.
- **Viernes**: demo o presentación corta (15–20 min) de lo construido/investigado + retro con el mentor.
- **Diario**: bitácora de aprendizaje (un archivo `.md` por semana en su repo personal): qué hizo, qué aprendió, qué lo trabó. Esto entrena escritura técnica y le da al mentor visibilidad real.

## Roles del equipo

- **Mentor principal**: guía diaria, revisa código, hace los checkpoints. Dedica ~1 hora/día las primeras 6 semanas, luego baja.
- **Equipo**: audiencia de las presentaciones de los viernes; rotar quién da feedback para que el practicante conozca distintos estilos.
- **Responsable de IA/consultoría**: lidera el eje transversal del documento 07 (puede ser el mismo mentor).

## Reglas de oro que se le comunican el día 1

1. **Preguntar después de intentar**: regla de los 30 minutos — intenta resolverlo solo (documentación, búsqueda, IA) durante 30 minutos; si sigue trabado, pregunta mostrando qué intentó.
2. **No hay preguntas tontas, hay preguntas sin contexto**: toda pregunta llega con "qué quiero lograr, qué intenté, qué pasó".
3. **La IA es calculadora, no cerebro**: puede usar IA desde el día 1, pero debe poder explicar cada línea que entrega. En los checkpoints se le pedirá explicar su código sin la IA delante.
4. **Todo queda escrito**: bitácora semanal, commits descriptivos, documentos de investigación. Escribir es parte del trabajo.
5. **Producción se respeta**: hasta la fase 5 no toca nada conectado a producción, y en fase 5 solo con revisión previa del mentor.
