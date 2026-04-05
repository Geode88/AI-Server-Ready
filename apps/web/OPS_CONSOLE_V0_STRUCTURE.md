# Ops Console v0 — Frontend Structure

## Proposed route structure
- `/` -> Overview
- `/gaps` -> Gap Ledger summary
- `/modules` -> Module Registry summary
- `/queue` -> Execution Queue summary
- `/stack` -> Stack Status

## Component groups
### Layout
- AppShell
- TopBar
- SideNav
- StatusStrip

### Overview page
- ProjectSummaryCard
- MaturitySnapshotCard
- CurrentPriorityCard
- StackSummaryCard

### Gap page
- GapTable
- GapStatusBadge
- NextStepNote

### Module page
- ModuleTable
- MaturityBadge
- DependencySummary

### Queue page
- TaskTable
- PriorityBadge
- OwnerLabel

### Stack page
- ConnectedAppsList
- RepoStatusCard
- DeployStatusCard
- RuntimeReadinessNote

## Visual rule
Start with a single clean dashboard style and avoid design complexity.
