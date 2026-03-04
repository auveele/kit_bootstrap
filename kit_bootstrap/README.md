# Kit Bootstrap

Plantillas para arrancar un sistema documental completo de proyecto.

Objetivo:
- definir Source of Truth por dominio,
- evitar duplicidades,
- operar por fases con gates,
- dejar trazabilidad para trabajo humano + LLM.

Uso recomendado:
1. Completa `INIT.md` con el prompt maestro.
2. Genera docs finales en `docs/` usando estas plantillas.
3. Revisa enlaces, SoT y estado documental.

Estructura:
- `00_governance/`: reglas, indice, decisiones, QA, releases.
- `00_governance/roles-and-rituals-v1.template.md`: roles ultralight y rituales minimos.
- `00_governance/role-raci-matrix-v1.template.md`: responsabilidades por flujo.
- `00_governance/info-capsules-v1.template.md`: capsulas de contexto reutilizable.
- `00_governance/llm-context-packs-v1.template.md`: paquetes de contexto por rol.
- `00_governance/role-playbooks/`: playbook corto por rol.
- `10_product/`: vision y loops.
- `20_systems/`: balance y datos.
- `30_experience/`: UX, contenido, localizacion.
- `40_technical/`: arquitectura y specs.
- `50_delivery/`: roadmap, estado, gates, backlog.
- `50_delivery/meeting-templates-v1.template.md`: plantillas operativas de reuniones.
- `60_open-questions/`: ambiguedades y decisiones pendientes.
- `90_archive/`: historico, no SoT activo.

Nota:
- Los roles son para claridad operativa, no para burocracia.
- No hace falta declarar rol en cada mensaje, solo en tareas/gates/decisiones clave.
