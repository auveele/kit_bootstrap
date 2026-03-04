# Document Index

Proyecto: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Estado: Vigente

## 1. Proposito

Mapa maestro de documentacion activa y dependencias.

## 2. Ruta de lectura recomendada

1. `docs/50_delivery/project-status.md`
2. `docs/50_delivery/phase-roadmap.md`
3. `docs/10_product/prd.md`
4. `docs/10_product/gdd-lite.md`
5. `docs/20_systems/system-balance.md`
6. `docs/40_technical/add.md`

## 3. Catalogo activo

| Documento | Rol principal | SoT | No duplicar con |
|---|---|---|---|
| PRD | vision, alcance, KPI | si | GDD-lite |
| GDD-lite | reglas de diseno | si | PRD |
| Core Loops | loop jugable | si | GDD-lite |
| ADD | arquitectura | si | Data Dictionary Complete |
| Roles and Rituals | roles y rituales minimos | si | RACI |
| Role RACI Matrix | responsabilidades por flujo | si | Roles and Rituals |
| Info Capsules | contexto reutilizable | si | LLM Context Packs |
| LLM Context Packs | paquetes de contexto por rol | si | Info Capsules |

## 4. Dependencias criticas

- producto -> sistemas -> tecnico -> delivery

## 5. Politica de actualizacion

- Todo documento nuevo debe registrarse aqui.
- Todo cambio mayor debe ir a release notes.

## 6. Checklist

- [ ] docs listados
- [ ] dependencias coherentes
- [ ] enlaces vigentes
