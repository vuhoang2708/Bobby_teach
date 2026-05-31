# Handoff - Gemini Browser Test For Scratch YouTube Examples

Date: 2026-05-31
Owner: Codex prepared the handoff
Executor: Gemini Browser / Browser Subagent
Mode: Read-only UAT

## Start Here

Open these two files first:

```text
C:\Users\vu.hoang\.gemini\antigravity\scratch\Bobby-Teaching\LandingPage\Implementation Plan\implementation_plan_20260531_VerifyScratchYoutubeExamples.md
C:\Users\vu.hoang\.gemini\antigravity\scratch\Bobby-Teaching\LandingPage\Implementation Plan\gemini_browser_uat_20260531_scratch_youtube_examples.md
```

Live page:

```text
https://passionate-developer-2026.vercel.app/
```

## User Intent

The user asked for YouTube links that show Scratch products broadly equivalent to the course outcomes.

Important:

- The examples do not need to match each exact week.
- The goal is to help parents understand what a Scratch product can look like.
- The LandingPage should not embed broken YouTube iframes.

## What Changed

Current deployed commits:

```text
741981e fix: restore timeline media and update class schedule
dfae665 feat: add verified youtube scratch examples
```

Expected live behavior:

- Timeline images are restored.
- A Scratch examples section exists.
- Four YouTube links are present as buttons, not iframes.
- Course duration remains 36 hours.
- Main schedule is 14h30 - 16h30 on Tuesday and Thursday.

## Browser Test Script

1. Open `https://passionate-developer-2026.vercel.app/`.
2. Capture a desktop screenshot at `1366x768`.
3. Navigate to the `Chuong trinh hoc` section.
4. Verify the section title equivalent to `Vi Du San Pham Scratch Tuong Duong`.
5. Verify four YouTube cards:
   - `Video: Platformer Game`
   - `Video: Fruit Catcher`
   - `Video: Fireworks Clone`
   - `Video: Zombie Shooter`
6. Open each YouTube link in a new tab and verify it loads an available playable video:
   - `https://www.youtube.com/watch?v=D16hTnDGweo`
   - `https://www.youtube.com/watch?v=En-wDfJZKpI`
   - `https://www.youtube.com/watch?v=3audNZs7uV8`
   - `https://www.youtube.com/watch?v=nyGE64VWsws`
7. Return to the LandingPage.
8. Confirm the page does not contain a visible unavailable-video box.
9. If possible, inspect page source/DOM and confirm there is no `youtube.com/embed`.
10. Repeat section screenshot on mobile viewports:
    - `390x844`
    - `414x896`
11. Check copy:
    - Has `14h30 - 16h30`
    - Has Tuesday/Thursday schedule
    - Has 36-hour duration
    - Does not say 24 hours

## Evidence Required

Return a short report with:

| ID | Time | Target | Viewport | Action | Expected | Observed | Evidence | Status |
|---|---|---|---|---|---|---|---|---|

Minimum evidence:

- Desktop screenshot of the Scratch examples section.
- Mobile screenshot of the Scratch examples section.
- One screenshot or exact observed title for each YouTube link.
- DOM/source check result for `youtube.com/embed`.
- Copy check result for `36 hours` and no `24 hours`.

## Stop Conditions

Stop and report `FAIL` if:

- Any YouTube link is unavailable/private/deleted.
- Any iframe unavailable box is visible.
- The page contains `youtube.com/embed`.
- Schedule or duration regresses to 24 hours.
- Mobile layout has horizontal overflow or overlapping cards.

Stop and report `BLOCKED` if:

- The live page cannot load.
- YouTube cannot be accessed from the browser environment.
- Browser tool cannot capture evidence.

Do not edit files, commit, push, or deploy during this test.


