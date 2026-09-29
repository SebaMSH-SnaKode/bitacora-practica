# 01 — Fase 0: Fundamentos (Semanas 1–2)

**Objetivo**: que el practicante entienda cómo funciona un computador, la web y las herramientas básicas del oficio, y deje su entorno de trabajo operativo. Sin esta base, todo lo demás se vuelve magia incomprensible.

**Punto de partida asumido**: sabe usar un computador a nivel usuario. Nada más.

---

## Semana 1 — El computador, la terminal y Git

### Conceptos a enseñar (sesiones cortas con el mentor + práctica inmediata)

1. **Cómo funciona un computador para un programador**
   - CPU, memoria RAM, disco: qué es "ejecutar un programa".
   - Archivos y carpetas como árbol; rutas absolutas y relativas.
   - Qué es un sistema operativo; diferencias prácticas macOS/Linux/Windows.
   - Qué es un "proceso" y un "puerto" (lo verá a diario: "el puerto 3000 está ocupado").

2. **La terminal** (su herramienta de todos los días)
   - Navegación: `pwd`, `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `open`.
   - Conceptos: stdin/stdout, flags, `--help`, historial, autocompletado con Tab.
   - Editores: abrir VS Code desde terminal (`code .`).
   - Ejercicio: crear una estructura de carpetas de un proyecto ficticio solo con comandos.

3. **Git y GitHub** (versionar es respirar)
   - Por qué existe el control de versiones (contar la historia del "final_v2_AHORA_SI.doc").
   - `git init`, `add`, `commit`, `status`, `log`, `diff`.
   - Ramas: `branch`, `checkout`/`switch`, `merge`; qué es un conflicto y cómo resolverlo.
   - GitHub: repos remotos, `push`/`pull`, qué es un Pull Request y por qué revisamos código.
   - **Convención de la empresa desde el día 1**: commits en español, formato `tipo: descripción` (`feat`, `fix`, `refactor`, `docs`, `chore`) — igual que en Datamédica.

### Entregables semana 1

- [ ] Repo personal `bitacora-practica` en GitHub con su primera bitácora semanal en Markdown.
- [ ] Ejercicio de Git: repo con al menos 10 commits, 2 ramas mergeadas y 1 conflicto resuelto a propósito.
- [ ] **Aprende Markdown** en el camino (títulos, listas, tablas, código) — lo usará toda la práctica.

## Semana 2 — Cómo funciona la web + entorno de trabajo

### Conceptos a enseñar

1. **El viaje de un request** (dibujarlo en pizarra, es EL modelo mental del programa)
   - Cliente y servidor. Navegador → DNS → HTTP → servidor → base de datos → respuesta.
   - Qué es una URL (protocolo, dominio, ruta, query params).
   - HTTP: verbos (GET, POST, PUT/PATCH, DELETE), códigos de estado (200, 201, 400, 401, 403, 404, 500), headers, body.
   - JSON: el idioma en que hablan las APIs.
   - Frontend vs backend vs base de datos — mapear directo a Datamédica: "la web que ve el cliente (Next.js), el cerebro (NestJS), la memoria (PostgreSQL)".

2. **Herramientas del navegador**
   - DevTools: pestañas Elements, Console y Network. Inspeccionar una página real y ver los requests que hace.
   - Ejercicio: abrir cualquier sitio, encontrar en Network un request, identificar verbo, status, headers y respuesta JSON.

3. **Instalación del entorno** (guiada, documentando cada paso)
   - VS Code + extensiones: ESLint, Prettier, Prisma, GitLens.
   - `nvm` + **Node.js 22** (la versión de Datamédica). Qué es Node, qué es npm, qué es `package.json`.
   - Docker Desktop: solo instalar y entender el concepto ("una caja con todo lo necesario para correr un programa"); se usa en serio en fase 3.
   - Cliente HTTP: Postman o similar (Datamédica tiene una colección Postman que usará en fase 4).

### Entregables semana 2

- [ ] Documento propio: **"El viaje de un request"** — explicación con diagrama hecho por él/ella de qué pasa desde que escribes una URL hasta que ves la página. (Investigación I-01 del documento 08.)
- [ ] Entorno completo funcionando: `node -v` = 22.x, git configurado, VS Code operativo.
- [ ] Primer script Node: `hola.js` que imprime algo, ejecutado con `node hola.js` — puente hacia la fase 1.

---

## Recursos recomendados

- Terminal y shell: cualquier curso introductorio de línea de comandos Unix (~2 horas).
- Git: [learngitbranching.js.org](https://learngitbranching.js.org) (interactivo, gratis, en español).
- Web: MDN Web Docs — "Cómo funciona Internet" y "Generalidades del protocolo HTTP" (en español).
- Markdown: guía de GitHub "Basic writing and formatting syntax".

## Señales de alerta para el mentor

- Copia comandos sin poder decir qué hacen → frenar y volver a conceptos.
- Miedo a la terminal ("¿y si borro algo?") → normal; darle un sandbox y permiso explícito para romper cosas.
- No escribe la bitácora → conversarlo la primera semana; es hábito fundacional, no burocracia.

## Checkpoint de salida (ver documento 09)

Explica el viaje de un request sin ayuda; usa terminal y Git con soltura básica; entorno operativo; bitácoras escritas.
