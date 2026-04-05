# ELARA ZERO-OPS / DFN-0 — Data Model v0

## Purpose
Define the minimum data model required to power Ops Console v0.

## Design rule
Keep the data model summary-level and low-complexity.

## Entities
### 1. ProjectSummary
Fields:
- name
- currentPhase
- maturityConceptual
- maturityArchitectural
- maturityOperational
- maturityPhysical
- currentPriorityFocus

### 2. GapItem
Fields:
- code
- name
- currentPercent
- severity
- status
- colmability
- nextStep

### 3. ModuleItem
Fields:
- code
- name
- status
- maturity
- dependencies
- firstDeliverable

### 4. QueueItem
Fields:
- task
- status
- priority
- area
- owner
- notes

### 5. StackItem
Fields:
- name
- category
- state
- role
- notes

## Minimal JSON direction
### ProjectSummary
```json
{
  "name": "ELARA ZERO-OPS / DFN-0",
  "currentPhase": "Pre-implementation",
  "maturityConceptual": 75,
  "maturityArchitectural": 55,
  "maturityOperational": 15,
  "maturityPhysical": 1,
  "currentPriorityFocus": "G4 -> G1 -> G3"
}
```

### GapItem
```json
{
  "code": "G4",
  "name": "Database / knowledge base esterna",
  "currentPercent": 50,
  "severity": "Critical",
  "status": "Reducing",
  "colmability": "High",
  "nextStep": "Popolare registri e dashboard"
}
```

### ModuleItem
```json
{
  "code": "C",
  "name": "Stack digitale minimo",
  "status": "Active",
  "maturity": 55,
  "dependencies": "GitHub, Replit, Vercel, Drive, Notion",
  "firstDeliverable": "repo/structure/deploy blueprint"
}
```

### QueueItem
```json
{
  "task": "Definire blueprint repo + deploy",
  "status": "Next",
  "priority": "P1",
  "area": "Infrastructure",
  "owner": "Elara",
  "notes": "Usare GitHub + Replit + Vercel come nucleo operativo"
}
```

### StackItem
```json
{
  "name": "GitHub",
  "category": "Technical Backbone",
  "state": "Active",
  "role": "Versioning and technical source of truth",
  "notes": "Repository and documentation backbone"
}
```

## Initial rule for v0
Ops Console v0 should consume summary data first, not full operational depth.

## Non-goals
- no complex relational model in v0
- no heavy analytics schema in v0
- no multi-tenant logic
- no secret-bearing data model
