# Semana 2 — Lógica que resuelve, y control de versiones

**S3** Lun 28 sep · **S4** Mar 29 sep
**Objetivo:** que escriba programas que manejan muchos datos y los organice en funciones, y que todo su trabajo quede versionado en GitHub desde ahora.

---

## S3 — Lunes 28 de septiembre · Bucles, listas y funciones

### 10:00 – 10:30 · **Presentación P1**

### 10:30 – 11:45 · Concepto

Los tres, en este orden, cada uno resolviendo un dolor que él ya sintió la semana pasada:

1. **Listas** — *"¿y si quiero registrar diez equipos, hago diez variables?"*. `equipos = []`, `.append()`, acceso por índice, `len()`.
2. **Bucles** — `for` recorriendo una lista, `while` con condición. El `for` de Python se lee en español: `for equipo in equipos:`. Aprovéchalo, es la ventaja de haber empezado acá.
3. **Funciones** — `def`, parámetros, `return`. Vender la idea correcta: *no es para ahorrar líneas, es para ponerle nombre a una idea.*

**Concepto que hay que nombrar hoy:** *descomponer*. Un problema grande es varios problemas chicos con nombre.

### 11:45 – 13:00 · Juntos
Refactorizar juntos el Ejercicio 3 de la semana pasada: pasar de un equipo suelto a una lista de equipos con funciones `agregar_equipo()` y `listar_equipos()`. Que vea su propio código mejorar.

### 14:00 – 17:00 · Ejercicios 1 y 2, revisión, bitácora

---

## S4 — Martes 29 de septiembre · Diccionarios, archivos y Git

### 10:15 – 11:00 · Diccionarios y archivos

- **Diccionarios** — `{"marca": "Siemens", "modelo": "P500"}`. Aquí se le enciende algo: *un equipo no son cuatro variables sueltas, es una cosa con propiedades*. Es la antesala de los objetos y de las filas de una tabla.
- **Archivos** — leer y escribir texto, y **JSON** con `json.dump()` / `json.load()`.
- El momento que importa: **cierra el programa, lo vuelve a abrir, y los datos siguen ahí.** Es la primera vez que algo suyo sobrevive.

### 11:00 – 13:00 · Git

Cuéntalo primero como historia, no como comandos: el `informe_final_v2_AHORA_SI_ESTA_BUENO.doc`. Todos lo vivieron; Git es la respuesta profesional a eso.

- **Por qué existe:** historial, volver atrás, trabajar entre varios sin pisarse.
- **Git vs. GitHub:** Git es el programa que corre en su computador y guarda el historial. GitHub es la página web donde ese historial vive una copia, para respaldo y para que otros lo vean. Uno funciona sin el otro; se usan juntos por conveniencia.
- **Convención de Snakode desde el commit número uno:** mensajes en español con formato `tipo: descripción`.
  `feat: agregar registro de equipos` · `fix: corregir cálculo de visitas` · `docs: actualizar bitácora` · `refactor:` · `chore:`

#### Instalar Git — nunca lo ha usado, no te saltes esto

No asumas nada: para él hoy Git es una palabra nueva. Instálenlo juntos, igual que hicieron con Python en la semana 1, y que anote cada paso en la bitácora.

- **Verificar primero si ya está instalado** (en Mac suele venir de fábrica): abrir la terminal y correr `git --version`. Si responde con un número de versión, ya está — pasan directo a configurar. Si dice "command not found" o similar, falta instalarlo.
- **Windows:** descargar e instalar [Git for Windows](https://git-scm.com/download/win) (deja instalado también "Git Bash", una terminal aparte). Durante la instalación, dejar las opciones por defecto — no hay que tocar nada raro.
- **Mac:** si el paso anterior no lo encontró, `git --version` en la terminal suele disparar la instalación de las "Herramientas de línea de comandos de Xcode" — aceptar y esperar a que termine. Alternativa si eso falla: instalar con `brew install git` (si ya tienen Homebrew) o desde [git-scm.com](https://git-scm.com/download/mac).
- **Confirmar que quedó instalado:** de nuevo `git --version` en la terminal — ahora sí debe mostrar un número.
- **Configurar su identidad (una sola vez, recién instalado):**
  ```
  git config --global user.name "Nombre Apellido"
  git config --global user.email "correo@ejemplo.com"
  ```
  Explícale qué es esto antes de que lo tipee: es la firma que Git va a pegar en cada commit que haga de aquí en adelante, no un login ni una contraseña.

> **Advertencia de mentor:** igual que con el entorno de Python, si la instalación se tuerce más de 15-20 minutos, no pierdas la sesión ahí. Sigue con la teoría de Git en el pizarrón/pantalla mientras se resuelve en paralelo, y retómalo antes del primer commit — sin Git instalado no hay ejercicio 3 ni 4 posibles hoy.

#### Los comandos del día, uno por uno

Explícale qué problema resuelve cada uno, no solo la sintaxis:

| Comando | Para qué sirve |
|---|---|
| `git config --global user.name "..."` y `user.email "..."` | Se hace **una sola vez** en el computador. Es la firma que va a quedar pegada a cada commit que haga. |
| `git init` | Convierte una carpeta normal en un repositorio. Se corre **una vez**, al empezar el proyecto. Crea una carpeta oculta `.git/` donde vive todo el historial. |
| `git status` | El comando que más va a usar. Le dice qué archivos cambió, cuáles están listos para guardar y cuáles no. Cuando dude qué hacer, que corra esto primero. |
| `git add archivo.py` (o `git add .` para todo) | Pasa cambios al **área de preparación** (*staging*). No guarda nada todavía — es elegir qué va a entrar en la próxima foto. |
| `git commit -m "tipo: descripción"` | Toma una **foto** (snapshot) de lo que está en el área de preparación y la guarda en el historial, para siempre. |
| `git log` | Muestra el historial de fotos: quién, cuándo y qué mensaje. `git log --oneline` para la versión corta. |
| `git remote add origin <url>` | Le dice a Git *"la copia de este repositorio en internet está en esta dirección"*. Se hace **una vez** por proyecto. |
| `git push` | Sube los commits guardados localmente hacia GitHub. |
| `git pull` | Trae cambios desde GitHub hacia el computador. Hoy casi no lo va a usar porque trabaja solo, pero que sepa que existe — es el opuesto de `push`. |
| `git clone <url>` | Descarga un repositorio completo (con todo su historial) desde GitHub a su computador. Útil cuando el repo ya existe y quiere trabajar sobre él. |

> **No enseñes ramas hoy.** Van en la semana 10, cuando tengan un motivo real. Hoy: guardar historia y subirla, nada más.

#### Cómo crear y subir un proyecto desde cero — paso a paso

Este es el flujo que va a repetir toda su carrera. Hazlo juntos una vez, en vivo, con su carpeta `mini-ot/`.

**1. Preparar GitHub (una vez, si no tiene cuenta)**
- Crear cuenta en [github.com](https://github.com).
- En GitHub, botón **New repository**: ponerle nombre (`bitacora-practica`), dejarlo público, **sin** marcar "Add a README" (para evitar un conflicto al hacer el primer push desde una carpeta que ya tiene archivos).

**2. Iniciar el repositorio local**
```
cd mini-ot
git init
git status
```
`git status` en este punto le va a mostrar todos sus archivos como "untracked" — Git los ve, pero todavía no los sigue.

**3. Crear el `.gitignore` antes del primer commit**
Archivos que **nunca** deben subirse: contraseñas, `equipos.json` si tiene datos de prueba sensibles, carpetas como `__pycache__/`, entornos virtuales. Un `.gitignore` básico para esta semana:
```
__pycache__/
*.pyc
.venv/
```
Este es el momento de la semana para instalar el hábito: el `.gitignore` se crea **antes** del primer `add`, no después de subir algo por error.

**4. Primer commit**
```
git add .
git status
```
Que mire con `git status` qué quedó en verde (listo para commitear) antes de confirmar — es el hábito de revisar antes de guardar.
```
git commit -m "feat: iniciar proyecto de inventario de equipos"
git log --oneline
```

**5. Conectar con GitHub y subir**
En la página del repo recién creado, GitHub le muestra la URL (`https://github.com/usuario/bitacora-practica.git`). Con eso:
```
git branch -M main
git remote add origin https://github.com/usuario/bitacora-practica.git
git push -u origin main
```
El `-u` (de *upstream*) solo se usa esa primera vez: le dice a Git que de ahora en adelante `origin main` es el destino por defecto. Después de eso, con `git push` a secas alcanza.

> **Autenticación:** GitHub ya no acepta la contraseña de la cuenta al hacer `push` desde la terminal. Va a pedir un *Personal Access Token* (se genera en GitHub → Settings → Developer settings → Personal access tokens) o, si prefieres, configurar SSH. No lo dejes para el final del día — resuélvanlo apenas hagan el primer `push`, porque si no se traba ahí y pierden tiempo.

**6. El ciclo de todos los días de aquí en adelante**
```
git status
git add .
git commit -m "feat: agregar función listar_equipos"
git push
```
Ese es el ciclo completo. Que lo interiorice como un solo gesto, no como cuatro comandos sueltos: *reviso → preparo → guardo → subo*.

### 14:00 – 16:45 · Ejercicios 3 y 4, primer push, cierre

---

## Ejercicios — entregar tal cual

### Ejercicio 1 · Inventario de equipos
> Amplía tu programa de equipos para que maneje **varios**.
> Menú en bucle con cuatro opciones:
> ```
> 1. Agregar equipo
> 2. Listar todos los equipos
> 3. Buscar equipo por marca
> 4. Salir
> ```
> Debe seguir funcionando hasta que elija salir.
>
> **Requisitos:** cada opción vive en su propia función; la lista de equipos se pasa como parámetro; si elige una opción que no existe, se lo dices y vuelve al menú.

### Ejercicio 2 · Estadísticas del inventario
> Agrega una opción 5 al menú que muestre:
> - Cuántos equipos hay en total.
> - Cuántos hay de cada marca.
> - Cuál es la marca más repetida.
>
> **Pista:** para la segunda, un diccionario donde la clave es la marca y el valor es el contador.

### Ejercicio 3 · Que no se pierdan los datos
> Haz que el inventario se guarde en un archivo `equipos.json`.
> - Al abrir el programa, carga lo que había.
> - Al agregar un equipo, guarda.
> - Si el archivo no existe todavía, el programa **no debe reventar**: parte con la lista vacía.
>
> Ese último punto es tu primer manejo de error de verdad. Averigua qué es `try/except`.

### Ejercicio 4 · Tu repositorio
> 1. Crea el repositorio `bitacora-practica` en GitHub.
> 2. Sube tu carpeta `mini-ot/` y tus bitácoras.
> 3. Deja **al menos 6 commits** con mensajes en el formato de la empresa. No un commit gigante al final: uno por cada cosa que terminaste.
> 4. Escribe un `README.md` que explique qué hace el programa y cómo se ejecuta.
>
> **Ese README es lo primero que va a mirar alguien que te contrate. Escríbelo pensando en eso.**

### Ejercicio 5 · *(ampliación, si va rápido)* Órdenes de trabajo
> Agrega un segundo menú para registrar **órdenes de trabajo**: cada una asociada a un equipo del inventario (por número de serie), con fecha, descripción, técnico y estado inicial `abierta`.
> No puede crearse una orden para un equipo que no existe.

---

## Entregable de la semana

- [ ] Repositorio `bitacora-practica` público en GitHub con 6+ commits bien escritos.
- [ ] Inventario funcionando con menú, funciones y persistencia en JSON.
- [ ] README explicando el proyecto.
- [ ] Dos entradas de bitácora.

## Presentación P2 — lunes 5 de octubre

**"Qué es Git y por qué existe"**

- Que abra con la historia del `informe_final_v2`: tiene que **enganchar**, no informar.
- Diapositiva 2: un diagrama de commits en el tiempo, dibujado por él.
- Diapositiva 3: mostrar su propio `git log` y explicar un commit suyo.

## Tarea de mitad de semana *(1 hora)*

1. Armar P2 (30 min).
2. Leer una guía visual corta de Git — mándale un enlace concreto (15 min).
3. Hacer tres commits en su repositorio arreglando algo pequeño, cada uno con mensaje correcto (15 min).

---

## Errores típicos de esta semana

| Lo que pasa | Qué hacer |
|---|---|
| Modifica una lista mientras la recorre | Error clásico y buenísimo. Que lo diagnostique él con `print()` antes de que le expliques |
| Funciones que hacen `print` en vez de `return` | Explícale la diferencia entre *calcular* y *mostrar*. Es un concepto grande, no se entiende de una |
| Un solo commit gigante al final del día | Corrígelo el primer día. Que commitee cada vez que algo funciona |
| Sube contraseñas o datos personales a GitHub | Enséñale `.gitignore` hoy mismo. Es el momento |
| Se pierde con índices de listas | Que dibuje la lista en papel con los números al lado. Funciona siempre |
