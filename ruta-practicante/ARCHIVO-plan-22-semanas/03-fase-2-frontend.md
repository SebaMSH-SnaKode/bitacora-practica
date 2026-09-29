# 03 — Fase 2: Frontend con el stack de Datamédica (Semanas 7–10)

**Objetivo**: construir interfaces web con **React 19 + Next.js (App Router) + Tailwind CSS + TanStack React Query + react-hook-form** — exactamente el stack de `apps/web` de Datamédica. Al final construye la interfaz web del mini-OT.

**A partir de esta fase la IA entra como copiloto** con las reglas del documento 07 (etapa 2): puede generar código, pero el practicante lo revisa, lo entiende y lo defiende.

---

## Semana 7 — React: componentes y estado

- Qué problema resuelve React: UI = función del estado.
- Componentes, JSX, props, composición.
- Estado con `useState`; eventos; renderizado condicional; listas y `key`.
- Formularios controlados básicos.
- Efectos con `useEffect` — y cuándo NO usarlo (error clásico).
- Crear el proyecto con Vite primero (más simple que Next para aprender React puro).

**Práctica**: tarjetas de OT interactivas — lista de órdenes con filtro por estado, botón para avanzar estado, contador por estado. Reutiliza la lógica del mini-OT de fase 1.

## Semana 8 — Next.js App Router + Tailwind

- Por qué Next encima de React: routing por archivos, server/client components, layouts.
- App Router: `app/`, `page.tsx`, `layout.tsx`, rutas dinámicas `[id]`, grupos de rutas `(grupo)` — **mostrar que Datamédica usa `(auth)` y `(dashboard)`**.
- `"use client"` vs server components: modelo mental simple ("lo interactivo es cliente").
- Tailwind CSS: utilidades, responsive (`md:`, `lg:`), estados (`hover:`), composición con `clsx`/`tailwind-merge`.
- shadcn/ui: qué es (componentes que se copian al repo, no librería instalada), instalar Button, Card, Dialog, Table, Badge — los mismos que viven en `packages/ui-web` de Datamédica.

**Práctica**: migrar el proyecto a Next.js con dos zonas: login falso (grupo `(auth)`) y dashboard (grupo `(dashboard)`) con sidebar, tabla de OTs con shadcn y badges de estado con colores.

## Semana 9 — Datos remotos: React Query + formularios

- El problema del estado servidor: caché, recarga, sincronización, loading/error.
- TanStack React Query: `useQuery`, `useMutation`, `queryKey`, invalidación, `staleTime` — **contar que la convención de Datamédica es `staleTime: 30_000` en listados paginados**.
- Paginación y búsqueda con query params.
- `react-hook-form`: registro de campos, validación, mensajes de error (en español, como en el proyecto real).
- Consumir una API real: el mentor le levanta un JSON-server o una API simple con las entidades del mini-OT (en fase 3 la construirá él/ella misma).

**Práctica**: el dashboard ahora carga OTs desde la API con React Query (loading, error, refetch), formulario de creación de OT con react-hook-form y validaciones.

## Semana 10 — Patrones de Datamédica + pulido

- **Custom hooks**: extraer `useOrdenes()`, `useCrearOrden()` — explicar que Datamédica centraliza esto en `packages/shared-core` (factories de hooks) con wrappers en `apps/web/src/hooks/`.
- Contexto de React: un `AuthContext` falso con roles, y un componente `RoleGuard` que oculta acciones según rol — **patrón real del proyecto** (`role-guard.tsx`).
- Roles del mini-OT = roles reales: `administrador`, `supervisor`, `ingeniero`.
- Manejo de fechas con `date-fns`, formato chileno `es-CL`, zona `America/Santiago`, 24 horas — convención obligatoria del proyecto.
- Accesibilidad mínima: labels, foco, contraste.
- Demo final de fase ante el equipo.

---

## Entregables de la fase

- [ ] Repo `mini-ot-web`: Next.js + Tailwind + shadcn + React Query + react-hook-form, con login falso, dashboard, CRUD de OTs contra API de práctica, roles y RoleGuard.
- [ ] Investigaciones I-04 e I-05 presentadas (documento 08).
- [ ] Demo de 15 min ante el equipo mostrando la app y UNA decisión técnica que tomó y por qué.

## Recursos recomendados

- React: documentación oficial [react.dev](https://react.dev) (tutorial + "Learn React"), disponible en español.
- Next.js: tutorial oficial "Learn Next.js" (App Router).
- React Query: docs oficiales de TanStack Query, sección "Guides & Concepts".
- Tailwind: docs oficiales + jugar con el playground.

## Señales de alerta para el mentor

- `useEffect` para todo → sesión dedicada a "no necesitas ese efecto".
- Copia componentes de la IA sin entender el flujo de datos → pedirle que dibuje el árbol de componentes y por dónde viajan props/estado.
- Parálisis por CSS/diseño → recordar que el objetivo es funcionalidad; el diseño fino no se evalúa.

## Checkpoint de salida (ver documento 09)

Explica el flujo de datos de su app de punta a punta; distingue estado local vs estado servidor y justifica React Query; puede agregar un campo nuevo al formulario + tabla + API en vivo.
