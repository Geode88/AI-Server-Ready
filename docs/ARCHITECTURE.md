# ELARA ZERO-OPS / DFN-0 — Architecture

## Purpose
This document defines the first executable technical nucleus of the ELARA ZERO-OPS / DFN-0 program.

## Core components
- GitHub: source of truth for code, docs, structure, and versioning
- Notion: workspace master, registries, ledgers, execution queue
- Replit: rapid prototype layer
- Vercel: deployment and hosting layer
- Hugging Face: R&D, models, datasets, documentation, low-cost mitigation support

## Boundaries
- GitHub is not deployment
- Replit is not the primary memory layer
- Vercel is not the system of record
- Hugging Face is not a substitute for runtime or CI/CD

## Initial repository zones
- docs/
- apps/web/
- services/api/
- registry/
- ops/
- artifacts/

## First implementation path
1. keep architecture and stack docs current
2. choose first lightweight software prototype
3. prepare deploy alignment for Vercel
4. use Hugging Face only where it improves model/dataset/research decisions
5. avoid premature expansion into heavy infrastructure
