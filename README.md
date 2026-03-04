# Kit Bootstrap

Sistema base de documentacion operativa para proyectos donde colaboran
personas y LLM en decisiones, ejecucion y trazabilidad.

Este repositorio te ayuda a construir un `docs/` robusto desde cero,
con Source of Truth por tema, fases con gates y contexto reutilizable
para trabajo humano + agentes.

## Que problema resuelve

En equipos mixtos (humanos + LLM), suele pasar lo mismo:

- decisiones importantes sin rastro claro,
- documentos duplicados o contradictorios,
- prompts sin contexto suficiente o demasiado ruido,
- roadmap y backlog desconectados del estado real.

`kit_bootstrap` propone una forma simple y disciplinada de operar
sin burocracia innecesaria.

## Enfoque

- `1 tema = 1 Source of Truth (SoT)`.
- Si ya existe SoT, se resume y se enlaza; no se duplica.
- Trabajo por fases con gates `PASS/FAIL`.
- Dudas severidad `A0` bloquean avance de fase.
- Priorizacion continua: `P0` bloqueante, `P1` critico, `P2` incremental.
- Cambios estructurales quedan trazados en decision log y release notes.

## Que incluye

- Prompt maestro de arranque: `INIT.md`.
- Kit de plantillas en `kit_bootstrap/` para generar `docs/`.
- Gobierno documental: indice, reglas de referencia, QA editorial,
  decision log, release notes.
- Producto y sistemas: PRD, GDD-lite, core loops, balance,
  diccionario de datos.
- Experiencia y contenido: UI/UX, localizacion, content bible,
  narrativa.
- Tecnico y delivery: ADD, specs, roadmap por fases, gates,
  backlog y estado de proyecto.
- Operativa LLM: info capsules y context packs por rol.
- Roles ultralight y RACI con playbooks accionables.

## Estructura del repositorio

```text
.
|- INIT.md
|- LICENSE
|- README.md
`- kit_bootstrap/
   |- 00_governance/
   |- 10_product/
   |- 20_systems/
   |- 30_experience/
   |- 40_technical/
   |- 50_delivery/
   |- 60_open-questions/
   |- 90_archive/
   |- QUICKSTART.md
   `- README.md
```

## Quickstart

1. Completa inputs del proyecto en `INIT.md`.
2. Copia plantillas de `kit_bootstrap/` a `docs/` en tu proyecto.
3. Sustituye placeholders `{{...}}` por datos reales.
4. Genera documentos en orden recomendado:
   - `docs/00_governance/*`
   - `docs/10_product/*`
   - `docs/20_systems/*`
   - `docs/30_experience/*`
   - `docs/40_technical/*`
   - `docs/50_delivery/*`
   - `docs/60_open-questions/*`
5. Ejecuta validacion final de coherencia y enlaces.

Para una version resumida del flujo, revisa `kit_bootstrap/QUICKSTART.md`.

## Flujo recomendado para colaboracion Humano + LLM

Para cada tarea, prepara un packet minimo con:

- objetivo,
- alcance in/out,
- SoT implicados,
- cambios esperados por archivo,
- criterios de aceptacion,
- verificacion,
- riesgo y rollback.

Esto reduce prompts ambiguos y mejora la calidad de salida del agente.

## Dominios documentales

- `00_governance`: normas de operacion, calidad y trazabilidad.
- `10_product`: vision, alcance y loops de valor.
- `20_systems`: entidades, balance y modelo de datos.
- `30_experience`: UX, contenido, narrativa y localizacion.
- `40_technical`: decisiones arquitectonicas y specs tecnicas.
- `50_delivery`: roadmap, gates, backlog y estado.
- `60_open-questions`: dudas abiertas y su resolucion.
- `90_archive`: historico no vigente.

## Resultado esperado

Al finalizar bootstrap deberias tener:

- documentacion activa sin duplicidades criticas,
- trazabilidad clara entre decision, cambio e impacto,
- fases y gates operativos para ejecucion,
- contexto compacto reutilizable para tareas con LLM,
- mejor continuidad entre sesiones y entre personas/agentes.

## Cuando usar este kit

- Equipos pequenos o medianos que quieren orden rapido.
- Proyectos 0->1 o reinicios con deuda documental.
- Entornos donde colaboran humanos y LLM en documentacion/decision.

## Licencia

Apache 2.0. Ver `LICENSE`.
