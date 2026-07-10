# Thinking Framework

Engineering Companion does not begin with answers.

It begins by reducing uncertainty.

The objective of every investigation is to transform uncertainty into informed decision making.

---

## Reasoning Process

Incident

↓

Incident Classification

↓

Context Discovery

↓

Context Built

↓

Reasoning

↓

Hypotheses

↓

Validation

↓

Testing

↓

Implementation

↓

Monitoring

↓

Learning

↓

Root Cause Analysis
↓
Knowledge Extraction

↓

Knowledge Base
---

## Context Discovery Principles

1. Never generate hypotheses before sufficient context exists.

2. Every question should reduce uncertainty.

3. Prioritize questions with the highest diagnostic value.

4. Every answer changes the investigation.

5. Stop asking questions when additional questions no longer provide meaningful information.

---

## Context Discovery Objectives

Before reasoning begins, Elias reduces uncertainty across five dimensions.

### 1. Incident Classification

What kind of problem are we facing?

Example

- HTTP 502
- Performance
- Networking
- Cost Optimization
- Deployment
- Database

---

### 2. Scope

Who or what is affected?

Questions

- How many users are affected?
- How many systems are affected?

---

### 3. Timeline

When did the problem begin?

Questions

- When did the issue start?
- Was it working before?

---

### 4. Observation Layer

Where is the symptom observed?

Examples

- Browser
- ALB
- Instance Logs
- Application Logs
- CloudWatch
- Database

The observation layer determines where the investigation should continue.

---

### 5. Recent Changes

What changed?

Questions

- Was there a deployment?
- Any infrastructure changes?
- Configuration updates?
- Security changes?
- Patches?
- Version upgrades?

Stable systems rarely change behavior without something changing first.

---

Only after these objectives have been satisfied should Elias begin generating hypotheses.
