# Gemini Browser UAT Script: Google Sheet + Email Registration Flow
*Date: 2026-05-26*

---

## 1. Objective

Verify the live Passionate Developer 2026 landing page and quiz flows after the Google Sheet + email registration upgrade.

This UAT must confirm:

1. Parent email is required in both registration and quiz entry.
2. Registration submit writes to Google Sheet and sends emails.
3. Quiz result submit writes to Google Sheet and sends emails.
4. Zalo Group Success Modal still appears after submit, but does not require parents to paste data after Sheet/email success.
5. If Google Sheet/email fails, the UI does not claim false success and keeps copy/Zalo fallback.

---

## 2. Preconditions

Before browser UAT, confirm Apps Script was redeployed with:

```javascript
SHEET_ID: '1vgcxRwvdz974cFeDsIWW8I49ZPI0tDheztPQuPEIk7k'
```

Do not use:

```javascript
SHEET_ID: '1vgcxRwvdz974cFeDsIWW8I49ZPI0tDheztPQuPEIk7k/edit?gid=1055917030#gid=1055917030'
```

The currently expected Apps Script Web App URL is:

```text
https://script.google.com/macros/s/AKfycbygIDUeAadahE7EXMf6GN1UUblrauDvuKoQ4NIP7HfMut-9NtWk7gr-SPyQtrIteKjntg/exec
```

Open that URL first. Expected response:

```json
{"ok":true,"service":"Passionate Developer 2026 registration endpoint"}
```

---

## 3. Test Data

Use obviously fake UAT data so rows/emails are easy to find and remove.

Registration:

```text
Parent name: GEMINI_UAT Phu Huynh
Parent phone: 0900000101
Parent email: vuhoang2708@gmail.com
Student name: GEMINI_UAT Registration Student
Birth year: 2016
Package: Buổi Trải Nghiệm Học Thử (0đ)
Preferred time: Lịch cố định: 09:30 - 11:30 (Thứ 2 - 4 - 6)
```

Quiz:

```text
Student name: GEMINI_UAT Quiz Student
Parent phone: 0900000102
Parent email: vuhoang2708@gmail.com
```

---

## 4. Registration Flow Test

1. Open live landing page:

```text
https://passionate-developer-2026.vercel.app
```

2. Click a registration CTA, such as `Đăng Ký Khóa Học`.
3. Confirm the modal contains required fields:
   - Họ tên Phụ huynh
   - Số điện thoại Zalo
   - Email phụ huynh
   - Họ tên Học sinh
   - Năm sinh
   - Gói đăng ký
   - Ca học mong muốn
4. Try submitting with email blank.
5. Expected: browser blocks submit or asks for email.
6. Fill all test data.
7. Submit.
8. Expected success copy if backend works:

```text
Thông tin đăng ký đã được ghi nhận vào Google Sheet và email xác nhận đã được gửi.
```

9. Confirm modal still shows:
   - QR code image
   - Button `Vào Nhóm Zalo Lớp Học`
   - textarea with registration content as backup/reference only, not as a required paste step
10. Verify Google Sheet tab `Registrations` has a row containing `GEMINI_UAT Registration Student`.
11. Verify email received:
   - BTC email: `vuhoang2708@gmail.com`
   - Secondary email: `chanphong.bobby@gmail.com` if configured as CC
   - Parent confirmation email to `vuhoang2708@gmail.com`

---

## 5. Quiz Flow Test

1. Open:

```text
https://passionate-developer-2026.vercel.app/quiz.html
```

2. Confirm start screen requires:
   - Họ tên học viên
   - Số điện thoại Zalo của phụ huynh
   - Email của phụ huynh
3. Try starting quiz with email blank.
4. Expected: quiz does not start and asks for complete parent info.
5. Fill quiz test data.
6. Complete all 14 quiz questions. Any answers are acceptable for UAT.
7. On result screen, click `Gửi Báo Cáo Qua Zalo Đăng Ký`.
8. Expected success copy if backend works:

```text
Kết quả bài test đã được ghi nhận vào Google Sheet và email tóm tắt đã được gửi.
```

9. Confirm modal still shows:
   - QR code image
   - Button `Vào Nhóm Zalo Lớp Học`
   - textarea with quiz report as backup/reference only, not as a required paste step
10. Confirm quiz email explains:
   - level is calculated from the first 11 scored logic questions
   - maximum score is 110
   - thresholds are Mức A `<50`, Mức B `50-79`, Mức C `>=80`
   - CTA is to join the Zalo group for consultation, trial-class scheduling, and class updates
11. Verify Google Sheet tab `QuizResults` has a row containing `GEMINI_UAT Quiz Student`.
12. Verify email received:
   - BTC email: `vuhoang2708@gmail.com`
   - Secondary email: `chanphong.bobby@gmail.com` if configured as CC
   - Parent quiz summary email to `vuhoang2708@gmail.com`

---

## 6. Fallback Test

If backend is intentionally unavailable or Apps Script is misconfigured:

1. Submit registration or quiz.
2. Expected UI should not claim Google Sheet/email success.
3. Expected fallback copy:

```text
Chưa xác nhận được việc ghi vào Google Sheet/email...
```

4. Confirm textarea still contains the report and parent can copy/paste into Zalo.

---

## 7. Pass/Fail Criteria

PASS only if:

- Registration row appears in `Registrations`.
- Quiz row appears in `QuizResults`.
- Emails are received by expected inboxes.
- Success modal appears and Zalo link works.
- Success modal does not ask parents to paste content into Zalo after Sheet/email success.
- Email blank is blocked in both flows.
- No severe console errors during submit.

FAIL if:

- Apps Script returns `Document ... /edit?gid=... is missing`.
- UI says Sheet/email succeeded while Sheet row is missing.
- Email field can be skipped.
- Zalo modal no longer appears.
