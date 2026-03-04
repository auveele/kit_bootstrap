# Agentic Workflow (IDE + LLM)

Proyecto: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Estado: Vigente

## 1. Objetivo

Optimizar ejecucion con LLM manteniendo calidad y trazabilidad.

## 2. Task Packet obligatorio

Cada tarea debe incluir:
1. objetivo
2. alcance in/out
3. SoT implicados
4. cambios esperados por archivo
5. criterios de aceptacion
6. verificacion
7. riesgo/rollback

## 3. Plantilla de prompt

```text
Objetivo:

Contexto minimo:

Source of Truth:
-

Instrucciones de cambio:
-

Criterios de aceptacion:
- [ ]

Verificacion:
-

No hacer:
-
```

## 4. DoD para tareas con agente

- [ ] cumple criterios
- [ ] sin romper SoT
- [ ] docs actualizadas
- [ ] evidencia de verificacion
