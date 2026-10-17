# Intents, entities and parameters

## Intents

| Intent | Purpose | Used by |
|---|---|---|
| Report-incident intent | The user wants to report a problem | Start Page route to Incident Type |
| `speak.human` | The user asks for a person | Start Page route to Human Hand-off |
| Confirm-yes intent | The user confirms the summary | Confirm route to Reference Given |
| Confirm-change intent | The user wants to change the summary | Confirm route to Incident Type |
| Urgent hazard intent (`report.urgent`) | The user describes an immediate danger | Start Page route to Emergency Referral |

Only the training phrases for `speak.human` are shown in a screenshot: [evidence/12](../evidence/12-intent-speak-human-phrases.png).

## Entity types

**`incident_type`** (six values, with synonyms): `water leak` (synonyms not captured in a screenshot), `recycling contamination` (bin, contaminated, recycle bin, recycling, wrong bin), `energy waste` (AC, air conditioning, heater left on, lights on, power), `hazardous disposal` (batteries, chemicals, hazardous, paint, unsafe disposal), `blocked accessible path` (blocked entrance, blocked path, ramp blocked, wheelchair access), `other` (other issue, something else).
Screenshots: [evidence/04](../evidence/04-entity-incident_type-saved.png), [evidence/05](../evidence/05-entity-incident_type-synonyms.png). The `water leak` row is below the visible area in these screenshots; it matched in test T2.

**`building`** (four values): `Building A` (A block, admin building, administration), `Building B` (B block, lab, laboratory, workshop), `Building C` (C block, main office, plant room), `other` (another building, somewhere else).
Screenshot: [evidence/06](../evidence/06-entity-building-saved.png).

## Parameters (Incident Type page)

| Parameter | Entity type | Required | Prompt |
|---|---|---|---|
| `incident_type` | `@incident_type` | Yes | "What type of incident is it? For example, water leak, recycling, energy waste, unsafe disposal, or a blocked path" |
| `building` | `@building` | Yes | "Which building is it in? A, B or C?" |

Screenshots: [evidence/07](../evidence/07-parameter-incident_type.png), [evidence/08](../evidence/08-parameter-incident_type-prompt.png), [evidence/09](../evidence/09-parameter-building-prompt.png).
