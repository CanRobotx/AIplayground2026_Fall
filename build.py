# 이벤터스 본문 HTML + preview.html 생성
B="https://raw.githubusercontent.com/CanRobotx/AIplayground2026_Fall/main/images"
N="#1d3850"; O="#c8501e"; MUT="#5b7185"; LINE="#dfe5ea"; CREAM="#f7f2e8"
h2=lambda t:f'<h2 style="font-size:24px;margin:0 0 14px;color:{N};line-height:1.35;">{t}</h2>'
hr='<hr style="border:0;border-top:1px dashed #cfd8df;margin:36px 20px;" />'
sec=lambda inner:f'<div style="padding:0 20px 8px;">\n{inner}\n</div>'
acc=lambda t:f'<span style="color:{O};">{t}</span>'
st=lambda t:f'<strong style="color:{O};">{t}</strong>'
def info(label,val,extra=''):
    return f'<td style="padding:18px 20px;width:50%;vertical-align:top;{extra}"><div style="font-size:12px;color:{MUT};margin-bottom:4px;font-weight:700;">{label}</div><div style="font-weight:700;font-size:15px;color:{N};">{val}</div></td>'
def card(color,t,d):
    return f'<td style="background:#fff;border:1px solid {LINE};padding:16px;width:33%;vertical-align:top;"><div style="font-weight:700;color:{N};margin-bottom:6px;font-size:16px;"><span style="display:inline-block;width:10px;height:10px;background:{color};margin-right:8px;"></span>{t}</div><div style="color:{MUT};font-size:13px;">{d}</div></td>'
S=[("01","#F25022","제조","LG전자 CHATDA 3.0","LG전자","우정훈 CVP · HS AX Lead"),
("02","#7FBA00","자동차","현대자동차 Microsoft 365 전사 도입과 확대","Microsoft","민경천 · Enterprise Hyundai, ATS"),
("03","#00A4EF","식품","Physical AI 시대 준비를 위한, Soft AI 도입기","풀무원","박경덕"),
("04","#FFB900","금융","KBank의 AI 활용 사례 (제목 확정 예정)","KBank","김형준 · IT서비스허브팀"),
("05","#F25022","뷰티","업무 자동화와 AI 적용 사례","2kTech","발표자 확정 예정"),
("06","#7FBA00","IT 서비스","GitHub Copilot을 활용한 AI Workflow","Extropy","박건우 · AX 전문가"),
("07","#00A4EF","교육","교육 시장의 AI (조율 중)","2miles","윤혜식 · Microsoft MVP"),
("08","#FFB900","AI 트렌드","글로벌 빅테크의 AX 전환 성공 조건, 팀십","Microsoft","이소영 · 아시아 총괄 매니저")]
td=f'padding:12px 10px;border-bottom:1px solid {LINE};vertical-align:top;font-size:14px;'
def row(n,c,ind,t,co,sp):
    return f'<tr><td style="{td}width:36px;font-weight:800;color:{O};">{n}</td><td style="{td}width:100px;color:{N};font-weight:700;font-size:13px;"><span style="display:inline-block;width:8px;height:8px;background:{c};margin-right:6px;"></span>{ind}</td><td style="{td}color:{N};font-weight:700;">{t}</td><td style="{td}width:190px;color:{MUT};font-size:13px;"><strong style="color:{N};">{co}</strong><br/>{sp}</td></tr>'
def plain(ind,t,sp):
    return f'<tr><td style="{td}"></td><td style="{td}color:{MUT};font-size:13px;">{ind}</td><td style="{td}color:{N};font-weight:700;">{t}</td><td style="{td}color:{MUT};font-size:13px;">{sp}</td></tr>'
brk=f'<tr><td colspan="4" style="padding:8px 10px;background:{CREAM};color:#8a6a3c;font-weight:700;font-size:13px;text-align:center;border-bottom:1px solid {LINE};">쉬는 시간</td></tr>'
rows=[plain("시작","환영 인사",f'<strong style="color:{N};">Microsoft</strong><br/>Juhyun Song · ASEAN Lead'),plain("인사 나누기","조별 인사 — “나 사용설명서”","참가자 전원")]
for i,s in enumerate(S):
    rows.append(row(*s))
    if i in (1,4): rows.append(brk)
rows.append(plain("마무리","네트워킹 및 마무리","참가자 전원"))
th=f'padding:10px;background:{N};color:#fff;font-size:12px;text-align:left;'
table=f'<table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;background:#fff;border:1px solid {LINE};"><tr><td style="{th}">순서</td><td style="{th}">분야</td><td style="{th}">발표 주제</td><td style="{th}">발표자</td></tr>'+"\n".join(rows)+'</table>'
ul=lambda items:'<ul style="margin:0;padding-left:20px;color:#2d4a63;">'+"".join(f"<li>{i}</li>" for i in items)+'</ul>'
faq=lambda q,a:f'<div style="background:#fff;border:1px solid {LINE};padding:14px 18px;margin-bottom:8px;"><div style="font-weight:700;color:{N};margin-bottom:6px;">{q}</div><div style="color:#3b556c;">{a}</div></div>'

SP=[("01","우정훈","LG전자","CVP · HS AX Lead","LG전자 CHATDA 3.0"),
("02","민경천","Microsoft","Enterprise Hyundai, ATS","현대자동차 Microsoft 365 전사 도입과 확대"),
("03","박경덕","풀무원","","Physical AI 시대 준비를 위한, Soft AI 도입기"),
("04","김형준","KBank","IT서비스허브팀","KBank의 AI 활용 사례 (제목 확정 예정)"),
("05","발표자 확정 예정","2kTech","","업무 자동화와 AI 적용 사례"),
("06","박건우","Extropy","AX 전문가 · 삼성전자 출신","GitHub Copilot을 활용한 AI Workflow"),
("07","윤혜식","2miles","Microsoft MVP","교육 시장의 AI (조율 중)"),
("08","이소영","Microsoft","아시아 총괄 매니저","글로벌 빅테크의 AX 전환 성공 조건, 팀십")]
def spcard(n,name,org,role,talk):
    r=f'<br/>{role}' if role else ''
    return (f'<td style="width:50%;vertical-align:top;background:#fff;border:1px solid {LINE};padding:14px;">'
      f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr>'
      f'<td style="width:84px;vertical-align:top;"><img src="{B}/speakers/speaker{n}.png" alt="{name} 발표자 사진" width="72" height="72" style="width:72px;height:72px;border-radius:50%;display:block;border:0;" /></td>'
      f'<td style="vertical-align:top;"><div style="font-weight:800;font-size:16px;color:{N};">{name}</div>'
      f'<div style="font-size:13px;color:{MUT};margin:2px 0 8px;"><strong style="color:{N};">{org}</strong>{r}</div>'
      f'<div style="font-size:13px;color:{O};font-weight:700;">발표 {n}</div><div style="font-size:13px;color:#3b556c;">{talk}</div></td></tr></table></td>')
sprows="".join("<tr>"+spcard(*SP[i])+spcard(*SP[i+1])+"</tr>" for i in range(0,8,2))
speakers=f'<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;">{sprows}</table>'
LI="https://www.linkedin.com/feed/update/urn:li:activity:"
lk=lambda u,t:f'<a href="{u}" style="color:{N};font-weight:700;">{t}</a>'
def meet(season,links):
    return f'<tr><td style="padding:12px 14px;border-bottom:1px solid {LINE};font-weight:700;color:{N};width:150px;font-size:14px;">{season}</td><td style="padding:12px 14px;border-bottom:1px solid {LINE};font-size:14px;color:#3b556c;">{links}</td></tr>'
meets=(meet("2026년 여름 밋업",lk(LI+"7463619588719681536","초청 글 보기"))
 +meet("2026년 봄 밋업",lk(LI+"7436994779856556034","초청 글 보기")+" · "+lk(LI+"7454808718665379840","감사 글 보기"))
 +meet("2025년 겨울 밋업",lk(LI+"7409576242817114112","초청 글 보기")))
about=(h2(f"{acc('AI놀이터')}를 소개합니다")
 +f'<p style="color:#3b556c;margin:0 0 16px;">AI놀이터는 Microsoft AI 커뮤니티입니다. AI를 배우는 곳이라기보다 <strong>AI와 놀아 보는 곳</strong>으로, 편하게 질문하고, 직접 해 보고, 알게 된 것을 서로 나눕니다. AI를 처음 접하는 분부터 현업에서 새로운 가능성을 찾는 분까지 누구나 함께할 수 있습니다.</p>'
 +f'<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;"><tr>'
 +card("#F25022","질문","무엇이든 편하게 물어볼 수 있는 곳에서 시작합니다.")+card("#7FBA00","놀이","직접 해 본 시도가 진짜 경험이 됩니다.")+card("#00A4EF","공유","알게 된 것을 나누면 누군가의 실마리가 됩니다.")+'</tr></table>'
 +f'<p style="color:#3b556c;margin:20px 0 10px;">계절마다 밋업을 열고, 그 사이에는 소규모 모임 ‘작은 놀이터’를 이어 가고 있습니다.</p>'
 +f'<table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;background:#fff;border:1px solid {LINE};">{meets}</table>'
 +f'<p style="margin:16px 0 0;font-size:14px;color:#3b556c;">'+lk("https://www.linkedin.com/groups/14571141/","LinkedIn ‘AI 놀이터’ 그룹 참여하기")+' · '+lk("https://aiplayground-kr.github.io/home/","공식 사이트 바로가기")+'</p>')
def spon(f,alt):
    return f'<td style="width:50%;padding:24px;vertical-align:middle;background:#fff;text-align:center;border:1px solid {LINE};"><img src="{B}/sponsors/{f}" alt="{alt}" style="max-width:180px;width:100%;height:auto;display:inline-block;border:0;" /></td>'
sponsors=(h2("후원사")+f'<p style="color:{MUT};margin:0 0 12px;">이번 밋업을 함께 만들어 주시는 곳입니다.</p>'
 +f'<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;"><tr>{spon("sponsor01.jpg","Microsoft")}{spon("sponsor02.png","후원사 로고")}</tr></table>')
VENUE="확정 후 안내드립니다 (서울)"
body=f'''<div style="max-width:780px;margin:0 auto;background:#fbf9f4;color:#2d4a63;font-family:'Pretendard','Apple SD Gothic Neo','맑은 고딕',sans-serif;line-height:1.7;padding:0;">

  <!-- 1) 배너 -->
  <p style="margin:0;"><img src="{B}/banner_1920x1080.png" alt="AI놀이터 2026 가을 밋업 — DEMO DAY · 2026년 10월 25일(일)" style="width:100%;height:auto;display:block;border:0;" /></p>

  <!-- 2) 핵심 정보 -->
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;background:#fff;border:1px solid {LINE};border-collapse:separate;margin:0 0 28px;">
    <tr>{info("일시","2026년 10월 25일(일) 오후 1시 시작",f"border-right:1px solid {LINE};border-bottom:1px solid {LINE};")}{info("장소",VENUE,f"border-bottom:1px solid {LINE};")}</tr>
    <tr>{info("참가비","무료 (현장 참석만 가능)",f"border-right:1px solid {LINE};")}{info("신청 기간","10월 7일(수) ~ 10월 20일(화) · 선착순 180명")}</tr>
  </table>

  <!-- 3) 소개 -->
  {sec(h2(f"업무 현장의 {acc('AI·AX 추진 경험')}을 나누는 자리")+f"""
    <p style="color:#3b556c;margin:0 0 16px;">AI놀이터 2026 가을 밋업은 <strong>DEMO DAY</strong>로 진행합니다.<br/>Microsoft 365 Copilot, Copilot Studio 등을 활용해 업무 현장에서 AI·AX(AI 전환)를 직접 추진해 온 분들이, 그 과정에서 얻은 경험과 실제 적용 사례를 들려드립니다.<br/>제조, 자동차, 식품, 금융, 뷰티, IT 서비스, 교육까지 — 서로 다른 현장의 이야기를 하루에 만나보세요.</p>
    <div style="padding:14px 18px;border-left:4px solid {O};background:#fdf1e2;font-weight:500;color:{N};">한 줄 요약 — 여러 산업 현장에서 AI·AX를 추진한 경험과 실제 적용 사례를 함께 나누는 커뮤니티 밋업입니다.</div>""")}

  {hr}

  <!-- 4) 특징 -->
  {sec(h2(f"이번 밋업에서 {acc('얻어 가실 것')}")+f'''
    <table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;"><tr>
      {card("#F25022","현장의 추진 경험","어떻게 시작했고, 어떤 어려움을 어떻게 풀었는지 담당자가 직접 이야기합니다.")}
      {card("#00A4EF","실제 적용 사례","Microsoft 365 Copilot, Copilot Studio 등을 실제 업무에 적용한 모습을 봅니다.")}
      {card("#FFB900","사람과의 연결","조별로 인사를 나누고, 비슷한 고민을 가진 분들과 편하게 이야기합니다.")}
    </tr></table>''')}

  {hr}

  <!-- 5) 발표 순서 -->
  {sec(h2(f"발표 {acc('순서')}")+f'<p style="color:{MUT};margin:0 0 16px;">2026년 10월 25일(일) 오후 1시 시작 · 발표당 약 30분</p>'+table+f'<p style="color:{MUT};font-size:12px;margin:12px 0 0;">※ 발표별 시간과 일부 발표는 확정되는 대로 안내드립니다. 주최 측 사정에 따라 바뀔 수 있습니다.</p>')}

  {hr}

  <!-- 5-1) 발표자 소개 -->
  {sec(h2(f"발표자 {acc('소개')}")+f'<p style="color:{MUT};margin:0 0 12px;">각 산업 현장에서 AI·AX를 직접 추진해 온 분들입니다.</p>'+speakers)}

  {hr}

  <!-- 5-2) 후원사 -->
  {sec(sponsors)}

  {hr}

  <!-- 6) 추천 대상 -->
  {sec(h2("이런 분께 추천합니다")+ul(["다른 회사는 AI를 어떻게 도입하고 있는지 궁금하신 분","사내 AI·AX 추진을 맡고 있어, 전사 확산 경험과 시행착오를 듣고 싶으신 분","Microsoft 365 Copilot, Copilot Studio를 실제 업무에 어떻게 쓰는지 보고 싶으신 분","다른 산업의 실무자와 고민을 나누고 싶으신 분","개발자가 아니어도 괜찮습니다. AI에 관심 있는 분이라면 누구나 환영합니다."]))}

  {hr}

  <!-- 7) 유의사항 -->
  {sec(h2("참가 전 꼭 확인해 주세요")+ul([f"{st('현장 참석만 가능')}하며, 온라인 중계는 없습니다.",f"조별 활동이 있으니 {st('오후 1시 전까지 도착')}해 주세요.",f"신청은 {st('10월 20일(화)')}까지이며, 정원 180명이 차면 일찍 마감될 수 있습니다.","행사 전에 신청하신 이메일로 장소와 입장 방법을 안내드립니다.","일정과 발표 내용은 주최 측 사정에 따라 일부 바뀔 수 있습니다."]))}

  {hr}

  <!-- 8) 취소 안내 -->
  {sec(h2("취소 안내")+ul([f"무료 행사지만 좌석이 한정되어 있습니다. {st('참석이 어려워지면 꼭 직접 취소')}해 주세요.","취소하시면 대기 중인 분께 자리가 돌아갑니다.",f"취소는 {st('이벤터스 마이페이지')}에서 하실 수 있습니다."]))}

  <!-- 9) 신청 안내 -->
  <div style="margin:36px 20px 20px;border:2px solid {N};background:#fff;padding:28px 20px;text-align:center;">
    <h2 style="margin:0 0 10px;font-size:24px;color:{N};">10월 25일(일), DEMO DAY에서 만나요</h2>
    <p style="color:{MUT};margin:0 0 18px;">좌석이 한정되어 있어 <strong style="color:{N};">선착순으로 마감</strong>됩니다.</p>
    <div style="display:inline-block;padding:12px 24px;background:{N};color:#fff;font-weight:800;font-size:15px;">▶ 신청하기 버튼을 눌러 주세요</div>
  </div>

  {hr}

  <!-- 9-1) AI놀이터 소개 -->
  {sec(about)}

  {hr}

  <!-- 10) 자주 묻는 질문 -->
  <div style="padding:0 20px 28px;">
    {h2("자주 묻는 질문")}
    {faq("Q1. 누구나 참가할 수 있나요?","네. 개발자, 기획자, 현업 담당자, 학생 등 AI에 관심 있는 분이라면 누구나 참가하실 수 있습니다.")}
    {faq("Q2. 참가비가 있나요?","무료입니다. 다만 좌석이 한정되어 있어 선착순으로 마감됩니다.")}
    {faq("Q3. 개발자가 아니어도 이해할 수 있나요?","네. 기술 구현보다는 업무 현장에서 AI를 어떻게 도입하고 확산했는지를 중심으로 한 사례 발표입니다.")}
    {faq("Q4. 노트북이 필요한가요?","없어도 됩니다. 실습 없이 발표를 듣는 행사라 편하게 오시면 됩니다.")}
    {faq("Q5. 온라인 중계나 다시 보기가 있나요?",f"없습니다. {st('현장 참석만 가능')}합니다.")}
    {faq("Q6. 장소는 어디인가요?","확정되는 대로 이 페이지와 안내 메일로 알려드리겠습니다.")}
    {faq("Q7. 참석이 어려워지면 어떻게 하나요?","이벤터스 마이페이지의 신청 내역에서 직접 취소해 주세요. 대기 중인 분께 자리가 돌아갑니다.")}
    {faq("Q8. 사진이나 영상 촬영이 있나요?","운영진이 행사 사진을 촬영하며, 일부는 후기 공유에 쓰일 수 있습니다. 직접 촬영하실 때는 다른 참가자의 초상권을 지켜 주시고, 발표자가 비공개를 요청한 내용은 촬영·공유하지 말아 주세요.")}
  </div>

  <div style="height:6px;background:#F25022;width:100%;"></div><div style="height:6px;background:#7FBA00;width:100%;"></div><div style="height:6px;background:#00A4EF;width:100%;"></div><div style="height:6px;background:#FFB900;width:100%;"></div>
  <p style="text-align:center;color:{MUT};font-size:12px;padding:14px;margin:0;">AI놀이터 · 놀다 보면 알게 되는 AI — <a href="https://aiplayground-kr.github.io/home/" style="color:{N};">aiplayground-kr.github.io/home</a></p>
</div>'''
head='''<!--
============================================================
  이벤터스 에디터 전용 HTML (인라인 스타일 + 테이블 레이아웃) — 초안 v0.3
  사용법: 이벤터스 본문 에디터의 [HTML] 탭에 아래 div 전체를 붙여넣기
  주의: 이벤터스는 style 태그 / class / 스크립트 / flex·grid 를 제거하므로
        본 파일은 인라인 style + table 로만 작성되어 있습니다.
  이미지: GitHub raw URL 사용 (저장소가 public 이어야 표시됨)
  확정 필요: 장소, 종료 시각, 발표별 시간, 미확정 발표자
============================================================
-->
'''
open('이벤터스_본문_HTML.html','w').write(head+body+"\n")
open('preview.html','w').write('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>미리보기 — AI놀이터 2026 가을 밋업 DEMO DAY</title></head><body style="margin:0;background:#e9edf0;">'+body.replace(B,"images")+'</body></html>')
