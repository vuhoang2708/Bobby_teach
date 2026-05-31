# Gemini Browser UAT Prompt - Scratch YouTube Examples

Use this prompt with Gemini Browser / Browser Subagent.

```text
You are verifying the Bobby Teaching LandingPage after the Scratch example update.

Open this plan first:
C:\Users\vu.hoang\.gemini\antigravity\scratch\Bobby-Teaching\LandingPage\Implementation Plan\implementation_plan_20260531_VerifyScratchYoutubeExamples.md

Live target:
https://passionate-developer-2026.vercel.app/

Scope:
- Read-only browser UAT. Do not edit files.
- Verify only the LandingPage Scratch example section, YouTube links, schedule copy, and mobile layout.
- Do not touch registration backend, quiz, Google Sheet, Apps Script, email flow, pricing, commits, or deploy settings.

Critical user intent:
The YouTube links are only broad examples of Scratch products that are equivalent to what learners may build. They do not need to match each course week exactly.

Must verify:
1. The live page contains the Scratch examples section.
2. The section has four YouTube video cards:
   - Video: Platformer Game
   - Video: Fruit Catcher
   - Video: Fireworks Clone
   - Video: Zombie Shooter
3. Each video link opens to an available YouTube video:
   - https://www.youtube.com/watch?v=D16hTnDGweo
   - https://www.youtube.com/watch?v=En-wDfJZKpI
   - https://www.youtube.com/watch?v=3audNZs7uV8
   - https://www.youtube.com/watch?v=nyGE64VWsws
4. The LandingPage itself must not contain a YouTube iframe or `youtube.com/embed`.
5. The LandingPage must not show "Video khong co san", "Video unavailable", or any broken video box.
6. Schedule remains:
   - Trial class: 14h30 Thu Ba 02/06/2026
   - Main sessions: 14h30 - 16h30 Thu Ba & Thu Nam
   - Practice/fix session: 2 gio/tuan, lich xac nhan rieng
   - Main course starts Thu Ba 09/06/2026
   - Graduation Thu Nam 16/07/2026
7. Duration remains 36 hours / 6h per week. It must not say 24 hours.

Required viewports:
- Desktop 1366x768
- Mobile 390x844
- Mobile 414x896

Evidence required:
- Screenshot of the Scratch examples section on desktop.
- Screenshot of the Scratch examples section on mobile.
- Screenshot or clear observation for each YouTube link opening successfully.
- A final evidence table using this format:

| ID | Time | Target | Viewport | Action | Expected | Observed | Evidence | Status |
|---|---|---|---|---|---|---|---|---|

Do not write "looks good". Write concrete observations such as:
- "All four YouTube cards visible."
- "Link opened to playable YouTube page with title ..."
- "No youtube.com/embed found in page source/DOM."
- "Schedule shows 14h30 - 16h30 and duration remains 36 hours."

Mark final result:
- PASS only if every required check passes.
- FAIL if any link is unavailable, any iframe error appears, the schedule is wrong, or the page says 24 hours.
- BLOCKED only if the browser cannot access the live site or YouTube, and include exact error evidence.
```


