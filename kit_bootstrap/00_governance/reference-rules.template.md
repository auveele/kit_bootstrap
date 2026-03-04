# Reference Rules

Proyecto: {{PROJECT_NAME}}
Version: {{DOC_VERSION}}
Estado: Vigente

## 1. Objetivo

Definir reglas globales para evitar duplicidades y mantener trazabilidad.

## 2. Reglas globales

- 1 tema = 1 Source of Truth.
- Si ya existe SoT, resumir + enlazar.
- No copiar bloques largos entre docs.
- Prioridad por version mas reciente.

## 3. Control de duplicidades (obligatorio)

Antes de publicar un doc:

- [ ] Existe SoT previo de este tema.
- [ ] Si existe, este doc enlaza y no duplica.
- [ ] No se repiten tablas/formulas de otro SoT.
- [ ] Se actualizo Document Index si aplica.

Regla de decision:
- Si hay SoT previo -> no crear SoT nuevo.
- Si no hay SoT -> crear y registrar en indice.

## 4. Reglas de referencias

- Usar enlaces a `.md` reales.
- Evitar referencias ambiguas.
- Verificar enlaces despues de mover archivos.

## 5. Trazabilidad

- Cambios estructurales -> decision log.
- Cambios de version -> release notes.
