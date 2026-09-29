# 04 — El proyecto integrador: mini-OT

Un solo proyecto que crece cada semana. **No hay 20 temas sueltos: hay una aplicación.**

*mini-OT* es una versión en miniatura de Datamédica. Cuando llegue al repositorio real en la semana 10, va a reconocer todo, porque ya construyó la analogía con sus manos.

## Qué es, en una frase que él pueda repetir

> Una aplicación donde un técnico registra las **órdenes de trabajo** que hace sobre los **equipos médicos** de un **cliente**: qué equipo era, qué le hizo, y en qué estado quedó.

Igual que Datamédica pero sin fotos, sin firma en terreno, sin PDFs, sin contratos y sin app móvil. El esqueleto y nada más.

## El modelo de datos

Tres tablas. Es lo mínimo que tiene relaciones de verdad y lo máximo que se puede enseñar en dos sesiones.

```
CLIENTE                 EQUIPO                    ORDEN DE TRABAJO
-------                 ------                    ----------------
id                      id                        id
nombre                  cliente_id  ──────┐       equipo_id  ──────┐
rut                     tipo              │       fecha            │
direccion               marca             │       descripcion      │
                        modelo            │       tecnico          │
                        numero_serie      │       estado           │
                                          │                        │
   un cliente tiene ────┘                 │   un equipo tiene ─────┘
   muchos equipos                             muchas órdenes
```

**Estados de una OT:** `abierta` → `en_proceso` → `cerrada`. También puede quedar `anulada`.

Esa máquina de estados, aunque tenga cuatro casillas, es la misma idea que gobierna el sistema real. Dibújasela en la pizarra la primera vez que aparezca.

## Cómo crece, semana a semana

| Semana | Qué se le agrega | Con qué |
|---|---|---|
| 2 | Programa de consola: registrar equipos y listarlos, guardados en un archivo | Python |
| 3 | Se versiona en GitHub y se le agregan órdenes de trabajo con estados | Python + Git |
| 4 | La primera pantalla: la lista de órdenes, maquetada y responsive | HTML + CSS |
| 5 | La pantalla cobra vida: crear una OT desde un formulario, cambiar su estado | JavaScript + DOM |
| 6 | El modelo pasa a una base de datos real, con consultas | SQL |
| 7 | Una API propia expone las órdenes por HTTP | Node + Express |
| 8 | La API habla con la base de datos y el front habla con la API | Todo junto |
| 9 | Publicada en internet, con pruebas y un script de reportes | Deploy + Jest + Python |
| 10 | Se compara contra Datamédica: qué falta y por qué el real es así | TypeScript (lectura) |

## Requisitos funcionales — la versión que se le entrega a él

Entrégale esto en la semana 4, cuando ya tiene la base. Redactado como un ticket real, porque es lo que va a recibir el resto de su carrera.

> ### mini-OT v1
>
> **Como** técnico de terreno, **quiero** registrar las órdenes de trabajo que realizo, **para** dejar constancia de qué se le hizo a cada equipo.
>
> **Debe permitir:**
> 1. Ver la lista de órdenes de trabajo, ordenadas de la más reciente a la más antigua.
> 2. Filtrar esa lista por estado.
> 3. Crear una orden nueva eligiendo un equipo de la lista de equipos existentes.
> 4. Cambiar el estado de una orden.
> 5. Ver el detalle de una orden con los datos del equipo y del cliente.
>
> **Reglas de negocio:**
> - Una orden no puede existir sin equipo asociado.
> - Una orden `cerrada` no vuelve a `abierta`.
> - La descripción es obligatoria y tiene mínimo 10 caracteres.
> - Las fechas se muestran en formato chileno: `21-09-2026`.
>
> **No incluye (y es importante que no lo incluyas):** fotos, firma del cliente, exportar a PDF, usuarios múltiples, notificaciones.

Esa última línea es tan formativa como el resto. Aprender a **no** construir lo que no se pidió es una de las cosas que más tarda en aprenderse.

## Datos de prueba

Que los invente él, pero con criterio: equipos médicos reales del rubro de Datamédica —rayos X, ecógrafo, mamógrafo, resonador, tomógrafo— y clientes con nombres de clínicas ficticias. Inventar datos verosímiles lo obliga a entender el dominio, y entender el dominio es la mitad del trabajo de un consultor.

## Criterio de "terminado"

Una funcionalidad está lista cuando:

- [ ] Funciona en el caso normal.
- [ ] Funciona cuando el dato viene vacío o mal escrito.
- [ ] Está commiteada con un mensaje que se entiende en seis meses.
- [ ] Él puede explicar cómo funciona sin mirar el código.

Los cuatro. Los dos últimos son los que nadie enseña y los que separan a un junior de alguien que recién empieza.
