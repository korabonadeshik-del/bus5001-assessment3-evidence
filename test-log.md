# Test log

Tested in the Dialogflow CX **Preview** simulator (Draft environment, Default Start Flow). Only tests with a screenshot or log are listed as run. Anything else is listed under "Not tested".

## Tests run

| ID | Date / time on screenshot | Input | Expected | Result | Evidence |
|---|---|---|---|---|---|
| T0 | 16 Oct, 8:31 PM | First intent test; "hi" | Custom welcome | **Fail**: the default Dialogflow greeting appeared | [30](30-iter-intent-matching-first-test.png), [31](31-iter-default-greeting-bug.png) |
| T1 | 17 Oct | Welcome message | One custom welcome | **Pass** after fix | [10](10-welcome-route-and-test.png) |
| T2 | 17 Oct, 4:09 PM | Normal report (not hazardous) | Asks type, then building, then confirm summary | **Pass** | [20](20-test-T2-normal-report.png) |
| T3 | 17 Oct | Urgent report (building "lab", type "hazardous disposal") | Emergency Referral message, session ends | **Fail, then fixed**: the urgent message showed, then the page looped | [raw log](T3-execution-log-raw.txt), [11](11-emergency-referral-page.png) |
| T5 | 17 Oct | "lab", then "b" and "B" typed at the building question | The bot should re-ask when it does not understand | **Pass for re-asking**: default replies "Sorry, can you say that again?" and "I didn't get that. Can you say it again?" appeared. No hand-off after repeated misses is configured. | [34](34-iter-single-letter-building.png) |
| T4 | 17 Oct, 6:48 PM | User asks for a person | Human Hand-off message, session ends | **Pass** | [22](22-test-T4-human-handoff.png) |

## Faults found and fixed

| # | Fault | Cause | Fix | Evidence |
|---|---|---|---|---|
| 1 | Default greeting ("Hi! How are you doing?") appeared instead of the custom welcome | Default welcome variants still present | Deleted the extra variants and kept one custom welcome | [31](31-iter-default-greeting-bug.png) |
| 2 | Conversation stalled after the type and building were collected | Route transition set to *Flow* with an empty destination | Changed the transition to *Page*, then Emergency Referral or Confirm | [33](33-iter-route-transition-blank.png) |
| 3 | Emergency Referral showed the urgent message, then repeated until the step limit ("maximum allowed state machine execution steps") | The `true` route on the page pointed back at the same page | Set that route to **End Session**. The same fix was applied to Human Hand-off and Reference Given. | [raw log](T3-execution-log-raw.txt), [01](01-flow-map-final.png) |
| 4 | "Building B" was not recognised | The entity matched only its listed synonyms | Synonyms added (B block, lab, laboratory, workshop) | [32](32-iter-building-not-recognised.png), [06](06-entity-building-saved.png) |

## Open issue

| Issue | Evidence |
|---|---|
| Single-letter answers "b" and "B" were not recognised. "lab" worked and was resolved to Building B. | [34](34-iter-single-letter-building.png) |

## Not tested (no evidence)

- Confirm step: answering **yes** through to the closing message
- Confirm step: answering **change** and returning to the questions
- The global urgent-hazard route from the Start Page (for example a message describing a gas smell)
- Asking for a person from the middle of a conversation (T4 was at the first turn)
- No-match handlers leading to the human hand-off after repeated misses (not configured)
- Clean re-run of T3 after the loop fix
- Screen reader and voice input
