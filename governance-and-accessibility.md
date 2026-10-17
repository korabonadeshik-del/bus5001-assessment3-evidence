# Governance, privacy and accessibility

## Privacy and data minimisation

- The bot asks only for the **incident type** and the **building**. It asks for no name, staff ID, phone number or health information.
- The agent is hosted in **`australia-southeast1` (Sydney)** (03-agent-settings-location.png)).
- Test conversations used made-up reports only.

## Human oversight

- **Urgent hazards are not handled by the bot.** The Emergency Referral page tells the user to call 000 or the on-site emergency number and ends without filing anything.
- **A person can be requested at any time** through the `speak.human` route.
- The bot gives no safety advice of its own and promises no response time.

## Accessibility

- One short question at a time, in plain language.
- Text-only conversation, so screen readers can read it and nothing depends on colour or images.
- Incident types are given as examples in the prompt, and synonyms (for example "tap", "ceiling" and "flood" for a water leak) let users describe a problem in their own words.
- A route to a person is always available.
- **Not tested:** use with a screen reader, and voice input.

## Known limitations

See the Limitations section in the [main README](README.md).
