# Session Operating Standard

Proyecto: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Estado: Vigente

## 1. Objetivo

Definir como operar sesiones de desarrollo/documentacion con continuidad inter-sesion.

## 2. Estructura oficial

- Raiz: `README.md`, `app/`, `docs/`.
- Documentacion activa solo en `docs/`.
- Historico en `docs/90_archive/`.

## 3. Flujo por fases

- Fases con gates PASS/FAIL.
- No avanzar con A0 abiertas.

## 3.b Roles y capsulas

- Usar roles ultralight para tareas/gates/decisiones clave.
- Mantener capsulas de informacion para reducir contexto en prompts.
- No declarar rol en cada mensaje cotidiano.

## 4. Priorizacion

- P0 bloqueante
- P1 critico
- P2 incremental

## 5. Intake de archivos nuevos

1. clasificar activo vs archivo,
2. mover a dominio correcto,
3. actualizar enlaces,
4. actualizar indice/release notes,
5. registrar dudas.

## 6. Cierre de sesion

- [ ] enlaces validados
- [ ] decision log actualizado
- [ ] release notes actualizado
- [ ] riesgos/dudas actualizados
