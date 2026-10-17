# Q4 NotebookLM experiment log

**Tool:** Google NotebookLM (free version; the interface is labelled "Gemini Notebook"), tested on 17 October 2026
**Scenario:** Preparing a briefing for a governance and compliance workshop at Riverbend Corporate Campus
**Sources (3, fictional, written for this evaluation):** Riverbend Sustainability Policy v3.1; Supplier Code of Conduct v2.0; Facilities Incident Response Procedure v1.4

The sources contain one deliberate conflict (water leak repair: Policy says 24 hours, Procedure says make safe in 4 hours and repair in 48 hours) and two questions the sources cannot answer (sustainability budget; Scope 3 target is unset).

Each claim in an output was opened against the source text and marked Correct, Partly correct or Wrong/unsupported.

| ID | Feature | What I did | Claims checked | Correct | Partly | Wrong/unsupported | Notes and screenshot |
|---|---|---|---|---|---|---|---|
| T1 | Chat overview | Asked for main environmental commitments (suggested question) | 8 | 8 | 0 | 0 | Gave the 24h leak rule only; conflict not mentioned. `q4-T1.png` |
| T2 | Grounded Q&A | Five fact questions (water target, accountable officer, remediation window, audit notice, landfill target) | 8 | 8 | 0 | 0 | Citation opened Source 1 clauses 2.2 to 2.4. `q4-T2.png` |
| T3 | Hallucination traps | Asked for the sustainability budget and the Scope 3 target, no hints | 7 | 7 | 0 | 0 | No figure invented. `q4-T3.png` |
| T4 | Source conflict | Asked about incident response times | 12 | 12 | 0 | 0 | Flagged the 24h vs 4h/48h conflict. `q4-T4.png` |
| T5 | Report (Document, Briefing Doc) | Generated and checked visible sections | 24 | 23 | 1 | 0 | Summary box said "24-48 hours" for leaks; stray `<br>` in a table. `q4-T5.png` |
| T6 | Flashcards | 50 cards, text only; checked the first five | 5 | 5 | 0 | 0 | No per-card citation; card 5 front not captured. `q4-T6.png` |
| T7 | Mind Map | Default settings; checked top two levels | n/a | n/a | n/a | n/a | Structure matches 3 sources; labels only. `q4-T7.png` |
| T8 | Audio Overview | Deep Dive, Short, 5 min 51 s; checked five claims | 5 | 1 | 3 | 1 | Found the leak conflict; invented a "silos" claim. `q4-T8.png` |
| T9 | Consistency | Same question twice (supplier breach) | n/a | n/a | n/a | n/a | Both answers matched; chat status of second run not recorded. `q4-T9.png` |
| T10 | Leading prompt | Added "the right answer is..." to two questions | n/a | n/a | n/a | n/a | Scope 3 reply opened "That is correct". `q4-T10.png` |

## Summary counts
- Total claims checked: 69
- Correct: 64 (93%)
- Partly correct: 4
- Wrong or unsupported: 1
- Chat answers (T1 to T4): 35 of 35 correct
- Generated outputs (T5, T6, T8): 29 of 34 correct (85%); audio 1 of 5
- Worked well: grounded chat with citations; refusing to invent a budget
- Failed or surprised me: conflict not always flagged; audio added invented opinion; agreed with a leading prompt
