# AI놀이터 2026 가을 밋업 — DEMO DAY

이벤터스(event-us.kr) 등록 페이지용 자료 저장소입니다.

**행사 성격** — 업무 현장에서 Microsoft 365 Copilot, Copilot Studio 등으로 추진하고 있는 AI·AX 활동의 추진 경험과 실제 적용 사례를 공유하는 자리. (초안 v0.2 · 2026-10-03)

| 항목 | 내용 |
|---|---|
| 행사명 | AI놀이터 2026 가을 밋업 — DEMO DAY |
| 일시 | 2026-10-25 (일) 13:00 시작 — **종료 시각 미확정** |
| 장소 | **미확정** |
| 등록 | 2026-10-07 (수) 오픈 / 2026-10-20 (화) 마감 |
| 목표 | 180명 등록 / 150명 참석 |
| 발표자 모집 마감 | 2026-10-12 (월) |

## 파일

- `이벤터스_에디터용_HTML.html` — 이벤터스 블록 에디터의 [HTML]에 붙여넣는 본문 (기본 태그만 사용, 모바일 대응)
- `이벤터스_에디터용_텍스트.md` — HTML 붙여넣기가 안 될 때 에디터에 직접 붙여넣는 텍스트
- `이벤터스_본문_HTML.html` — 인라인 스타일을 쓴 디자인 버전 (구 에디터용, 참고)
- `preview.html` — 로컬 미리보기용 (같은 본문, 이미지 상대경로)
- `images/banner_1920x1080.png` — 대표 이미지 (16:9)
- `images/banner_square_1080.png` — SNS/썸네일용 (1:1)
- `images/session_lineup_1560.png` — 세션 라인업 이미지
- `build.py` — 이벤터스 본문 HTML과 preview.html 생성 스크립트 (문구 수정은 여기서)
- `images/src/` — 이미지 원본 HTML/CSS. 수정 후 `python3 render.py` 로 다시 렌더링 (Playwright 필요)
- `images/speakers/speaker01~08.png` — 발표자 사진 자리(현재 임시 실루엣). 같은 파일명·정사각형으로 교체하면 본문에 바로 반영
- `images/sponsors/sponsor01.jpg`, `sponsor02.png` — 후원사 로고 (02는 빈 자리)
- `assets/logo/` — 업로드된 AI놀이터 로고
- `assets/reference/` — 타임테이블·등록 계획 시트 캡처 (기획 참고)

## 확정 필요 (TODO)

- [ ] 장소, 종료 시각
- [ ] 세션별 시간 — 시트의 시작/종료 시각이 서로 겹쳐 본문에는 순서만 표기
- [ ] 일시 재확인 — 시트 기준 10/25 는 일요일
- [ ] KBank 세션 제목, 2kTech 발표자, Education(2miles) 확정 여부, AI Trend 세션 Confirm
- [ ] IT Service 세션 제목 전체 (시트에서 "…Ai Workflow EZCu" 로 잘림)
- [ ] 스피커 초청 메일 내용 반영
