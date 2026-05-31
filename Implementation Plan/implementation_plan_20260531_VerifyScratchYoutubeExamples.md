# Implementation Plan - Verify Scratch YouTube Example Links

Date: 2026-05-31
Project: Bobby Teaching LandingPage
Primary live target: `https://passionate-developer-2026.vercel.app/`
Primary source file: `C:\Users\vu.hoang\.gemini\antigravity\scratch\Bobby-Teaching\LandingPage\index.html`
Related commit: `dfae665 feat: add verified youtube scratch examples`

## Objective

Verify that the LandingPage now uses working YouTube links as additional Scratch product examples, without reintroducing broken embedded iframes.

The user intent is not to map each video mechanically to a specific week. The intent is to show parents examples of Scratch products that are broadly equivalent to what learners can build during or after the course.

## Non-Negotiables

- Do not replace timeline images with YouTube iframes.
- Do not use any video that displays "Video khong co san", "Video unavailable", private, deleted, blocked, or not embeddable.
- Do not change registration, quiz, Google Sheet, Apps Script, email flow, pricing, or backend code.
- Keep total course duration as 36 hours, 6h/week.
- Keep schedule:
  - Trial class: `14h30 Thu Ba 02/06/2026`
  - Main sessions: `14h30 - 16h30 Thu Ba & Thu Nam`
  - Practice/fix session: `2 gio/tuan, lich xac nhan rieng`
  - Main course starts: `Thu Ba 09/06/2026`
  - Graduation: `Thu Nam 16/07/2026`

## Expected Current YouTube Links

These links were checked with YouTube oEmbed before being added:

| Purpose | YouTube ID | URL | Expected title |
|---|---|---|---|
| Platformer/final project example | `D16hTnDGweo` | `https://www.youtube.com/watch?v=D16hTnDGweo` | `Code a Platformer Game | 1. The Basics` |
| Fruit catcher/basic game example | `En-wDfJZKpI` | `https://www.youtube.com/watch?v=En-wDfJZKpI` | `Fruit Catcher 2022...` |
| Clone/particle effect example | `3audNZs7uV8` | `https://www.youtube.com/watch?v=3audNZs7uV8` | `Make Epic Fireworks & Particle Explosions...` |
| Shooter/game-state example | `nyGE64VWsws` | `https://www.youtube.com/watch?v=nyGE64VWsws` | `How To Make A Zombie Shooter Game in Scratch...` |

## Implementation State To Verify

The live page should contain a section named:

```text
Vi Du San Pham Scratch Tuong Duong
```

The section should include:

- Existing Scratch project links.
- Four YouTube example cards with text links/buttons labeled `Xem video`.
- No `youtube.com/embed` iframe usage.

## Verification Checklist

1. Open the live target.
2. Navigate to `Chuong trinh hoc` / `#chuong-trinh`.
3. Confirm the Scratch example section is visible and readable.
4. Confirm the four YouTube cards exist:
   - `Video: Platformer Game`
   - `Video: Fruit Catcher`
   - `Video: Fireworks Clone`
   - `Video: Zombie Shooter`
5. Click or open each YouTube link in a new tab.
6. Confirm each YouTube page loads a playable/available video.
7. Confirm the live page source/DOM does not contain `youtube.com/embed`.
8. Confirm there is no "Video khong co san" or "Video unavailable" visible in the LandingPage.
9. Confirm schedule and duration remain correct:
   - `14h30 - 16h30`
   - `Thu Ba`
   - `Thu Nam`
   - `36 gio`
   - no `24 gio`
10. Capture evidence screenshots for desktop and mobile.

## Required Browser Viewports

- Desktop: `1366x768`
- Mobile: `390x844`
- Mobile: `414x896`

## Evidence Table Template

| ID | Time | Target | Viewport | Action | Expected | Observed | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| YT-01 | | Live | 1366x768 | Inspect Scratch examples section | Four YouTube cards visible; no iframe error | | screenshot path | |
| YT-02 | | YouTube | desktop | Open Platformer link | Video page loads and is playable/available | | screenshot path | |
| YT-03 | | YouTube | desktop | Open Fruit Catcher link | Video page loads and is playable/available | | screenshot path | |
| YT-04 | | YouTube | desktop | Open Fireworks link | Video page loads and is playable/available | | screenshot path | |
| YT-05 | | YouTube | desktop | Open Zombie Shooter link | Video page loads and is playable/available | | screenshot path | |
| YT-06 | | Live | 390x844 | Inspect mobile layout | Cards stack cleanly; no horizontal overflow | | screenshot path | |
| YT-07 | | Live | 414x896 | Check schedule/duration copy | Shows 14h30, Tue/Thu, 36h; no 24h | | screenshot path | |

Status must be `PASS`, `FAIL`, or `BLOCKED`.

## Pass Criteria

The task can be marked complete only if:

- All four YouTube links are available when opened.
- LandingPage has no broken YouTube iframe or unavailable-video box.
- Live page still shows the correct schedule and 36-hour duration.
- Desktop and mobile screenshots are attached as evidence.

## Fail Conditions

Mark `FAIL` if any of these happen:

- Any YouTube link opens to a missing/private/unavailable video.
- The page contains `youtube.com/embed`.
- The page shows `24 gio`, `24 giờ`, or otherwise implies the course was reduced to 24 hours.
- Any mobile viewport has horizontal overflow or overlapping example cards.

