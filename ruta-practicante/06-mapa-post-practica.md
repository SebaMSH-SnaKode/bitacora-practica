# 06 — Lo que queda fuera, y en qué orden seguir

Este documento se le entrega **el 30 de noviembre**, en la sesión de cierre. No antes: entregado al principio, abruma; entregado al final, orienta.

## Primero, lo honesto

En 120 horas cada tema que entra saca a otro. Lo que sigue **no se dejó fuera por poco importante**, sino porque sin las bases que ya tiene se habría convertido en palabras memorizadas.

La buena noticia: ahora tiene las bases. Todo esto le va a costar una fracción de lo que le habría costado en septiembre.

El plan completo original, con todo el detalle, está en [`ARCHIVO-plan-22-semanas/`](ARCHIVO-plan-22-semanas/). Es su hoja de ruta de los próximos meses.

---

## Orden recomendado para los próximos seis meses

### 1. React y Next.js — *empieza por aquí*
Es lo que más lo separa hoy de poder trabajar en Datamédica. Ya sabe DOM y eventos, que es la base real; un framework le va a parecer razonable en vez de mágico.
**Señal de que lo logró:** reescribir mini-OT completa en Next.js.

### 2. TypeScript
Lo vio a nivel lectura en la semana 10. Ahora toca escribirlo. Va segundo y no primero porque resuelve un dolor que recién ahora conoce: código que se rompe y no sabes por qué.
**Señal:** su mini-OT en Next.js, tipada de punta a punta.

### 3. Programación orientada a objetos
Clases, objetos, herencia, y **para qué sirve la inyección de dependencias** — que es lo que hace que NestJS parezca incomprensible hasta que se entiende. Sin esto, el backend real le va a seguir pareciendo magia.
**Señal:** explicar qué hace un decorador de NestJS y por qué está ahí.

### 4. NestJS y Prisma
Con lo anterior, esto deja de ser difícil. Ya construyó una API con Express: son las mismas ideas con más estructura.
**Señal:** migrar el backend de mini-OT de Express a NestJS.

### 5. Testing en serio
Cobertura, mocks, pruebas de integración, y Playwright para extremo a extremo.

### 6. Docker y despliegue
Ya lo usó como comando. Ahora entenderlo: imágenes, contenedores, `docker compose`, y qué hace un pipeline de CI/CD.

---

## Lo que puede esperar más

| Tema | Por qué puede esperar |
|---|---|
| **Complejidad algorítmica (Big-O)** | Importa para entrevistas, no para el primer año de trabajo real. Estudiarlo cuando busque cambiarse |
| **Patrones de diseño** | Sin haber sufrido un proyecto grande, son dogma. Primero el dolor, después el patrón |
| **Arquitectura (hexagonal, microservicios)** | No se puede diseñar lo que no se ha construido |
| **GraphQL** | Alternativa a REST. Solo si el trabajo lo pide |
| **React Native / Expo** | La app móvil de Datamédica. Útil, pero después del web |
| **CSS avanzado y animaciones** | Muy visible y muy adictivo. Se le puede ir un mes entero |
| **Kubernetes y nube avanzada** | Es otra carrera, no la continuación de esta |

---

## Los hábitos que ya tiene y no debe soltar

Esto vale más que la lista de tecnologías. Un desarrollador con estos hábitos y la mitad de los conocimientos rinde más que el caso contrario.

1. **Leer el error antes de tocar el código.**
2. **La regla de los 30 minutos** — intentar solo, y después preguntar con contexto.
3. **No dejar entrar código que no puede explicar**, venga de una IA o de internet.
4. **Commits chicos y descritos**, en vez de un bulto al final del día.
5. **Pensar en los tres estados** — cargando, éxito, error — y en el caso vacío.
6. **Escribir lo que hace.** Bitácora, README, documentación.
7. **Explicar en voz alta lo que construyó.** Diez presentaciones en diez semanas: eso no lo tiene casi ningún junior.

---

## Su portafolio, al 30 de noviembre

Que lo arme hoy mismo, antes de que se enfríe:

- **mini-OT**, con URL pública y repositorio ordenado.
- **`API.md`** — documentación que alguien más pudo usar sin ayuda.
- **`seguridad.md`** — dos vulnerabilidades reales que encontró y cerró. Esto llama la atención en una entrevista más que cualquier curso.
- **`DEPLOY.md`** — llevar algo a producción y documentar lo que se rompió.
- **Las 10 presentaciones.**
- **Su primer PR** sobre un repositorio de producción real.
- **Diez semanas de bitácora**, que es la historia completa de cómo aprendió.

Para el CV, la frase honesta y fuerte es esta: *construí y publiqué una aplicación completa —interfaz, API, base de datos y despliegue— y cerré mi primer ticket sobre un sistema en producción.*

No dice que es senior. Dice exactamente lo que hizo. Eso es lo que sirve.
