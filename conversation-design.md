# Conversation design

## Purpose

One focused ESG use case: **incident reporting** for the fictional Riverbend Corporate Campus (about 2,400 staff, contractors and visitors across Building A administration, Building B laboratories and workshops, Building C offices and plant room). Reports currently arrive by phone or a shared inbox, so repeat problems are hard to track and urgent hazards can sit unread.

## ESG functions supported

| Function | Incident type value | Why it matters |
|---|---|---|
| Report a water leak | `water leak` | Unnoticed leaks waste water against the campus water-reduction goal |
| Report contaminated recycling | `recycling contamination` | Contamination can send a load to landfill, working against the landfill-diversion goal |
| Report energy waste in unoccupied spaces | `energy waste` | Equipment left running in empty rooms wastes energy |
| Report unsafe chemical or waste disposal | `hazardous disposal` | A safety and environmental risk; handled by the emergency branch |
| Report a blocked accessible path | `blocked accessible path` | Blocked routes exclude people with disability |
| Anything else | `other` | Catch-all so the user is never stuck |

## Pages and routes

| Page | Purpose | Leaves to |
|---|---|---|
| **Start Page** | Welcome message; matches the user's first request | Incident Type (report-incident intent), Human Hand-off (`speak.human`), Emergency Referral (urgent hazard intent) |
| **Incident Type** | Form page with two required parameters: `incident_type`, `building` | Emergency Referral when `incident_type = hazardous disposal`; otherwise Confirm |
| **Confirm** | Reads back the summary | Reference Given (confirm-yes intent); back to Incident Type (`confirm.change`) |
| **Reference Given** | Closing message | End Session |
| **Emergency Referral** | Safety message, no ticket | End Session |
| **Human Hand-off** | Passes the user to a person (simulated) | End Session |

**Branch condition on Incident Type** (order matters, the first match wins):

1. `$page.params.status = "FINAL" AND $session.params.incident_type = "hazardous disposal"` goes to **Emergency Referral**
2. `$page.params.status = "FINAL"` goes to **Confirm**

## Messages

| Where | Message |
|---|---|
| Welcome | "Hi there, I'm your Riverbend Green assistant. I can help you report a water leak, a recycling mix-up, energy left on in an empty room, unsafe disposal, or a blocked accessible path. What would you like to report?" |
| Incident type prompt | "What type of incident is it? For example, water leak, recycling, energy waste, unsafe disposal, or a blocked path" |
| Building prompt | "Which building is it in? A, B or C?" |
| Confirm | "Here's what I have: a $session.params.incident_type report in $session.params.building. Is that right, or would you like to change something?" |
| Emergency Referral | "This sounds urgent. If anyone is in danger, call 000 now or contact the on-site emergency number. I won't file this as a normal report." |
| Human Hand-off | "I'm having trouble with this one, so I'll pass it to the Facilities help desk. A person will follow up on your report." |

## Design reasoning

- **Flow-based, not generative.** A flow gives the same route for the same input, so every path, including the urgent one, can be tested and shown. A generative playbook would be harder to prove safe.
- **Two questions only.** Type and building are enough to route a report. Asking for less data keeps the conversation short and avoids collecting personal information.
- **The urgent route is plain.** The emergency message has no friendly wording on purpose.
- **Confirm before ending.** The summary read-back lets the user correct a wrong type or building.
- **A human can be requested.** The `speak.human` route sits on the Start Page. It was tested at the first turn (T4). Using it from the middle of a conversation was not tested.
