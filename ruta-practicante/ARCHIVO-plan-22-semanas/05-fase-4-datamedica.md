# 05 — Fase 4: Inmersión en Datamédica (Semanas 15–18)

**Objetivo**: que el practicante pase de "sé programar" a "conozco NUESTRO sistema". Al final navega el monorepo con soltura, entiende el dominio de negocio, respeta las convenciones y hace su **primer Pull Request real**.

**Preparación del mentor**: darle acceso al repo, credenciales de entorno de desarrollo (nunca producción), y agendar una sesión de kickoff de 1 hora contando la historia del proyecto: quién es el cliente, qué problema le resolvimos, cómo fue el desarrollo (¡incluida la parte de que se construyó asistido con IA — conecta con documento 07!).

---

## Semana 15 — El dominio y el mapa del monorepo

### El negocio primero (día 1–2)
Nadie soporta bien un sistema cuyo negocio no entiende.

- Qué hace Datamédica (la empresa): postventa de equipos de imagenología médica en hospitales y clínicas de Chile.
- El flujo de negocio completo: cliente reporta falla → se crea la **orden de trabajo** → se asigna a un **ingeniero** → va a terreno → ejecuta con **checklist** → sube **evidencias fotográficas** → el cliente **firma** en el teléfono → se cierra con GPS y calificación → se genera **informe PDF** → se notifica por correo.
- Los 5 roles y qué puede hacer cada uno: `administrador`, `supervisor`, `ingeniero` (terreno), `tecnico`, `aplicacionista`.
- Entidades núcleo y sus relaciones: Account → Branch → Equipment → WorkOrder; catálogo Brand/EquipmentType/Model; ServiceModality con vigencias (→ alertas de vencimiento).
- **Ejercicio**: dibujar el modelo de dominio en papel ANTES de ver `schema.prisma` (24 modelos), luego comparar con el real y analizar las diferencias.

### El mapa del código (día 3–5)
Lectura guiada, con el mentor las primeras sesiones:

- `README.md`, `ONBOARDING.md`, `CLAUDE.md` del proyecto.
- Estructura del monorepo: `apps/{api,web,mobile,e2e}` + `packages/{shared-core,ui-web,...}`. Qué es Turborepo y npm workspaces.
- Levantar el entorno local completo siguiendo el ONBOARDING (docker + `npm run dev`). **Documentar cada tropiezo**: su primer aporte real será mejorar el ONBOARDING con lo que encontró desactualizado.
- `apps/api/ARQUITECTURA.md` (leerlo por capítulos, no de una vez).

## Semana 16 — Trazar el sistema de punta a punta

La técnica estrella de esta fase: **trazas end-to-end**. Elegir una funcionalidad y seguirla por todas las capas con el debugger y `console.log`.

**Traza guiada con el mentor** (1 sesión): "Listar órdenes de trabajo"
1. Web: página `(dashboard)/work-orders` → hook `use-ordenes-trabajo.ts` → factory en `packages/shared-core` → `RequestAdapter` en `src/lib/api.ts` (cookies, refresh, CSRF).
2. API: `work-orders.controller.ts` (guards JWT + roles, DTO de query) → `work-orders.service.ts` → repositorio → `work-orders.prisma.repository.ts` → SQL real (activar log de Prisma).
3. Vuelta: respuesta paginada → caché de React Query → render de la tabla.

**Trazas en solitario** (presenta cada una en 10 min al mentor):
- [ ] Crear una OT (formulario → validaciones DTO → INSERT → email de notificación).
- [ ] Login completo (contraseña → MFA → cookies httpOnly → refresh) — apoyo: investigación I-08.
- [ ] Subir una evidencia fotográfica (upload → Azure Blob → URL SAS).
- [ ] Generar el PDF de una OT (`/reports/work-order/:id/pdf` con pdfkit).

## Semana 17 — Convenciones, seguridad y mobile (panorama)

- **Convenciones obligatorias del proyecto** (sesión dedicada + chuleta escrita por el practicante):
  - Commits en español `tipo: descripción`; ramas desde `develop`.
  - Código/tipos en inglés; mensajes de validación, comentarios y docs en español.
  - Fechas siempre `es-CL`, `America/Santiago`, 24h.
  - Soft delete en todo; paginación `Promise.all([findMany, count])`; `@Roles()` explícito en cada endpoint.
  - Reglas espejadas web/mobile con fuente única en `shared-core` (roles asignables, validaciones).
- **Seguridad del proyecto — nivel comprensión** (no implementación): mapa de las capas — JWT + refresh rotativo, MFA obligatorio (TOTP/passkeys), step-up para operaciones sensibles, CSRF, cifrado de payloads, rate limiting, bloqueo de cuenta. La meta: que al soportar un "no puedo entrar" sepa distinguir bloqueo por intentos, sesión expirada por inactividad, o MFA pendiente.
- **Mobile — nivel panorama**: qué es Expo, cómo se estructura `apps/mobile`, y el concepto clave de **PowerSync/offline-first** (el ingeniero trabaja en sótanos de hospitales sin señal). Apoyo: investigación I-09. No se le pide desarrollar en mobile.
- **Auditoría y ciclo de vida de usuarios**: `AuditLog`, invitaciones, desbloqueo — el pan de cada día del soporte.

## Semana 18 — Primeras contribuciones reales (supervisadas)

Tareas reales, acotadas y de bajo riesgo, elegidas de la deuda técnica conocida del proyecto. Flujo completo: rama → código → PR → revisión del mentor → merge a `develop`.

**Banco de primeras tareas sugeridas** (elegir 2–3 según estado actual del repo):
1. **Actualizar documentación desactualizada**: el `README.md` dice 18 modelos y el schema tiene 24; el `DEPLOYMENT_GUIDE.md` describe una infra (VPS/PM2) que ya no existe (hoy es Azure Container Apps). Auditar y corregir. *Tarea ideal: obliga a verificar contra el código real.*
2. **Mejorar `ONBOARDING.md`** con los tropiezos que documentó en la semana 15.
3. **Tests unitarios para un módulo CRUD sin cobertura**: `accounts`, `branches`, `contacts`, `equipment` o `service-modalities` no tienen specs. Empezar por el más simple, usando `work-orders.service.spec.ts` como plantilla de estilo. *Esta es LA tarea puente hacia la fase 5.*
4. **Un fix de bug menor real** del backlog, si hay uno etiquetable como "good first issue".

---

## Entregables de la fase

- [ ] Entorno local completo funcionando de forma autónoma.
- [ ] Diagrama propio del modelo de dominio + diagrama de arquitectura (los defiende en presentación P-04, documento 08).
- [ ] 4 trazas end-to-end documentadas en su bitácora.
- [ ] Chuleta personal de convenciones del proyecto.
- [ ] 2–3 PRs reales mergeados a `develop`.

## Señales de alerta para el mentor

- Se pierde en el tamaño del repo → volver a las trazas: siempre una funcionalidad concreta, nunca "leer código" en abstracto.
- Toca código sin entender el radio de impacto → introducir la pregunta ritual pre-PR: "¿qué más usa esto?" (buscar referencias antes de editar).
- PRs gigantes → enseñar a partir en PRs chicos; regla: si la descripción necesita "y también...", son dos PRs.

## Checkpoint de salida (ver documento 09)

Explica el flujo de negocio completo y el modelo de dominio; traza una funcionalidad nueva por todas las capas sin ayuda; sus PRs pasan revisión con máximo 2 rondas de comentarios; respeta convenciones sin que se las recuerden.
