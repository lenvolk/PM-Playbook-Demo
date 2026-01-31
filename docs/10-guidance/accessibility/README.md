# Accessibility (PM checklist)

Use this page to ensure your requirements include accessibility (a11y) expectations from the start.

## What PMs should capture
- **Supported input methods:** keyboard, touch, mouse, voice (as applicable)
- **Screen reader expectations:** labels, roles, names, announced state changes
- **Focus management:** focus order, focus visibility, focus trapping avoidance
- **Color & contrast:** don’t rely on color alone; meet contrast requirements
- **Error handling:** clear error text, associated fields, recovery guidance
- **Dynamic content:** announce updates (toasts, validation, async loading)
- **Media:** captions/transcripts when audio/video is present

## Triggers: when to involve accessibility specialists
- Building a new UI surface or navigation model
- Introducing complex widgets (grids, editors, drag/drop)
- Changing critical flows (auth, checkout, onboarding)
- Shipping PDF/doc exports or embedded media

## Evidence / artifacts to link
- Annotated designs (states: empty/loading/error)
- Keyboard interaction model
- Accessibility acceptance criteria in ADO

## ADO copy/paste block
Use: [Accessibility acceptance criteria snippet](../../20-templates/ado-snippets/accessibility-acceptance-criteria.md)
