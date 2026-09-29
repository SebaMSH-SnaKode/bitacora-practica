# 04 — Fase 3: Backend con el stack de Datamédica (Semanas 11–14)

**Objetivo**: construir la API real del mini-OT con **NestJS + PostgreSQL + Prisma**, entendiendo REST, validación, autenticación y Docker — el corazón de `apps/api` de Datamédica.

---

## Semana 11 — Bases de datos y SQL

Antes del framework, los datos. Un desarrollador de soporte pasa la mitad de su vida mirando la base.

- Qué es una BD relacional: tablas, filas, columnas, tipos.
- Claves primarias y foráneas; relaciones 1-N y N-N (ejemplos del dominio real: una Cuenta tiene muchas Sucursales; una Sucursal tiene muchos Equipos; una OT pertenece a un Equipo y a un usuario asignado).
- SQL: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `GROUP BY` + agregaciones.
- Índices: qué son y por qué existen (a nivel conceptual).
- **Levantar PostgreSQL 16 con Docker Compose** — primer uso real de Docker, mismo `postgres:16-alpine` del proyecto. Conectarse con pgAdmin o TablePlus.
- **Soft delete**: patrón `deleted_at` — por qué Datamédica nunca borra de verdad (auditoría, recuperación) y qué implica en cada query (`WHERE deleted_at IS NULL`).

**Práctica**: diseñar en papel y crear en SQL el esquema del mini-OT: `accounts`, `branches`, `equipment`, `work_orders`, `users`. Poblarlo a mano y escribir 15 queries de dificultad creciente (la última: "OTs completadas por ingeniero en el último mes, con nombre del cliente").

## Semana 12 — NestJS: primera API

- Qué es un framework backend y qué resuelve NestJS: estructura, inyección de dependencias, módulos.
- Anatomía Nest: `Module`, `Controller`, `Service`. Decoradores (`@Get`, `@Post`, `@Param`, `@Body`, `@Query`).
- DTOs con `class-validator` + `class-transformer`: validación declarativa, **mensajes de error en español** (convención del proyecto).
- Manejo de errores: excepciones HTTP de Nest (`NotFoundException`, etc.).
- Swagger: documentar la API y probarla desde `/api/docs` — igual que Datamédica.

**Práctica**: API mini-OT v1 con datos en memoria: CRUD de cuentas y OTs, validaciones, Swagger. Probarla desde Postman Y desde su frontend de fase 2 (¡conectar sus dos mundos!).

## Semana 13 — Prisma + el patrón de arquitectura de Datamédica

- Prisma: `schema.prisma`, migraciones (`migrate dev`), Prisma Client tipado, seed.
- Reescribir la persistencia del mini-OT con Prisma sobre su PostgreSQL.
- **El patrón del proyecto real** (enseñarlo explícitamente, es el molde de todo el backend):
  ```
  src/<modulo>/
    <modulo>.controller.ts      ← recibe HTTP, valida con DTOs
    <modulo>.service.ts         ← lógica de negocio
    <modulo>.module.ts
    dto/*.dto.ts
    domain/repositories/        ← interfaz (puerto): "qué necesito"
    infra/prisma/               ← implementación (adaptador): "cómo lo hago con Prisma"
  ```
  Explicar el porqué: el servicio no sabe que existe Prisma → se puede testear con un repositorio falso y cambiar de ORM sin tocar la lógica.
- Paginación estilo Datamédica: `Promise.all([findMany, count])`, respuesta `{ data, total, page }`.
- Soft delete implementado en el repositorio.

**Práctica**: refactorizar el mini-OT al patrón completo Controller → Service → Repository → PrismaRepository, con paginación y soft delete.

## Semana 14 — Autenticación, testing y Docker

### Autenticación (conceptual + implementación simple)
- Hash de contraseñas con bcrypt (nunca texto plano — contar alguna historia de filtración real).
- JWT: qué contiene, firma, expiración. Access token corto + refresh token: por qué dos tokens.
- Guards de Nest: proteger rutas; decorador `@Roles()` + `RolesGuard` — patrón real del proyecto.
- **Solo lectura conceptual** (no implementar): MFA/TOTP, passkeys, CSRF, cookies httpOnly — se estudia sobre el proyecto real en fase 4 con la investigación I-08.

### Testing backend (crítico: será su primera tarea real en fase 5)
- Jest: `describe`, `it`, `expect`. Qué es un test unitario.
- Testear un Service con repositorio falso (mock) — aquí brilla el patrón de repositorios.
- Leer un spec real de Datamédica como referencia de estilo (`work-orders.service.spec.ts`).

### Docker
- Qué es una imagen y un contenedor; leer (no escribir de cero) el `Dockerfile` multi-stage del proyecto.
- `docker-compose` con API + Postgres.

**Práctica**: login con JWT en el mini-OT, rutas protegidas por rol, mínimo 10 tests unitarios del servicio de OTs, y todo corriendo con `docker compose up`.

---

## Entregables de la fase

- [ ] Repo `mini-ot-api`: NestJS + Prisma + PostgreSQL, patrón de repositorios, auth JWT con roles, paginación, soft delete, tests, Swagger, Docker Compose.
- [ ] Frontend de fase 2 conectado a esta API real (reemplaza la API de práctica).
- [ ] Investigaciones I-06 e I-07 presentadas (documento 08).
- [ ] Demo integrada: flujo completo crear cuenta → crear equipo → crear OT → avanzar estados → completar, desde la web hasta la BD.

## Recursos recomendados

- SQL: [sqlbolt.com](https://sqlbolt.com) (interactivo) + pgexercises.com.
- NestJS: documentación oficial, secciones "First steps" hasta "Guards"; curso oficial si se prefiere video.
- Prisma: docs oficiales, "Getting started" + "Prisma Migrate".
- JWT: jwt.io (debugger) + artículo introductorio.

## Señales de alerta para el mentor

- Confunde dónde va la lógica (todo en el controller o todo en el repositorio) → revisar juntos un módulo real de Datamédica como espejo.
- Los tests le parecen burocracia → mostrarle un bug real que un test habría atrapado.
- Se pierde con Prisma vs SQL → hacerle traducir 5 queries Prisma a SQL mental y verificar con `?query` logging.

## Checkpoint de salida (ver documento 09)

Explica el patrón Controller → Service → Repository y su porqué; escribe un endpoint nuevo completo en vivo; explica qué hay dentro de un JWT; sus tests corren y sabe qué cubren.
