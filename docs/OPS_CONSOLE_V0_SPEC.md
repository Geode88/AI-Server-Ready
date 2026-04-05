# ELARA ZERO-OPS / DFN-0 — Ops Console v0 Specification

## Purpose
Ops Console v0 is the first lightweight web surface for the ELARA ZERO-OPS / DFN-0 program.

It should make the project visible, governable, and deployable without introducing premature complexity.

## Primary goal
Expose the minimum operational picture of the project through a simple web console.

## Core screens
### 1. Overview
Display:
- project name
- current phase
- maturity snapshot
- current priority focus
- connected stack summary

### 2. Gap Ledger
Display:
- G1–G7
- current percentage for each gap
- status label
- short next-step note

### 3. Module Registry
Display:
- modules A–H
- current status
- maturity
- dependency summary

### 4. Execution Queue
Display:
- next tasks
- priority labels
- status labels
- owner

### 5. Stack Status
Display:
- connected apps currently active
- repository status
- deploy status
- runtime readiness note

## UX rules
- keep the interface simple
- avoid dense controls
- prioritize readability over feature count
- do not add advanced workflow features in v0
- do not add authentication complexity in v0 unless required later

## Data model v0
The console only needs a minimal data shape:
- project summary
- gap summary list
- module summary list
- execution queue list
- stack summary list

## Backend rule
No dedicated backend is required at the start unless the frontend cannot remain simple.

## Deployment rule
The first target should remain compatible with lightweight deployment on Vercel.

## Non-goals for v0
- full orchestration engine
- secret management
- multi-user admin system
- physical-world control logic
- heavy analytics
- large-scale automation engine

## Success criteria
Ops Console v0 is successful if it:
- gives the project a real web runtime target
- improves visibility of gaps, modules, and tasks
- stays easy to prototype and deploy
- supports future extension without forcing it now
