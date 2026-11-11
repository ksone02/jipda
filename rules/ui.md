# UI rules

## Tier 1 (a violation means not done; fix directly)
- **UI-1** No accent cards with a colored left border (border-left + faint background).
- **UI-2** No sparkle icons, emoji icons, or decorative gradients.
- **UI-3** Do not expose internal names on screen (model names, data source abbreviations, implementation terms like "engine").
- **UI-4** No invented figures, testimonials, or logo walls. Leave missing material empty.
- **UI-5** Every button, link, and input shows keyboard focus immediately.
- **UI-6** No horizontal scroll at 1440, 1366, or 390 widths.
- **UI-7** Colors and fonts come only from `:root` tokens. No raw color values in UI code.
- **UI-8** No body text under 11px; body contrast at least 4.5:1.

## Tier 2 (asked together)
- **UI-R1** Contrast: large text at least 3:1; secondary text on colored backgrounds is drawn from that color, not gray.
- **UI-R2** Shadows have offset and blur. Colored glow with no offset is decoration.
- **UI-R3** Spacing: tight within groups, wide between. More space above a heading than below.
- **UI-R4** Type: 65-75 characters per body line, clear size and weight steps.
- **UI-R5** States: hover, disabled, loading, error, and empty all exist.
- **UI-R6** Browser defaults: selection, scrollbars, focus ring, and tabular numbers match the theme.
- **UI-R7** Copy: buttons say what happens; errors give cause and next step.
- **UI-R8** Requirements: each spec requirement can be found on screen within seconds.

## Do not only subtract
Fill the space left by removed decoration with substance: large type, broad color fields, real content, real data. Removing decoration alone makes a screen look thin.

## Screen types
- Dashboards and tools (default): scanning, consistency, and real usage come before expression.
- Landing and intro: `design --landing` follows [landing.md](../skills/design/references/landing.md).
