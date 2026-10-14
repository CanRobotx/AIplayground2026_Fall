# 이벤터스 본문 HTML + preview.html 생성
B="https://raw.githubusercontent.com/CanRobotx/AIplayground2026_Fall/main/images"
N="#1d3850"; O="#c8501e"; MUT="#4a5d70"; LINE="#dfe5ea"; CREAM="#f7f2e8"
h2=lambda t:f'<h2 style="font-size:25px;margin:0 0 16px;color:{N};line-height:1.4;font-weight:800;">{t}</h2>'
hr='<hr style="border:0;border-top:1px solid #dfe5ea;margin:44px 20px;" />'
sec=lambda inner:f'<div style="padding:0 20px 8px;">\n{inner}\n</div>'
acc=lambda t:f'<span style="color:{O};">{t}</span>'
st=lambda t:f'<strong style="color:{O};">{t}</strong>'
def info(label,val,extra=''):
    return f'<td style="padding:18px 20px;width:50%;vertical-align:top;{extra}"><div style="font-size:13px;color:{MUT};margin-bottom:4px;font-weight:700;">{label}</div><div style="font-weight:700;font-size:16px;color:{N};line-height:1.5;">{val}</div></td>'
def card(color,t,d):
    return f'<tr><td style="background:#fff;border:1px solid {LINE};border-left:5px solid {color};padding:16px 18px;"><div style="font-weight:800;color:{N};margin-bottom:4px;font-size:17px;">{t}</div><div style="color:#2f4356;font-size:15px;">{d}</div></td></tr>'
cards=lambda *c:'<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;">'+"".join(c)+'</table>'
import os
from data import WELCOME,S,BREAKS,TAIL,INDUSTRIES
def photo(slug,i):
    for ext in ("jpg","png"):
        if os.path.exists(f"images/speakers/{slug}.{ext}"): return f"{B}/speakers/{slug}.{ext}"
    return f"{B}/speakers/speaker{(i%8)+1:02d}.png"
td=f'padding:16px 14px;border-bottom:1px solid {LINE};vertical-align:top;'
tcell=lambda t0,t1:f'<td style="{td}width:64px;white-space:nowrap;"><div style="font-weight:800;font-size:16px;color:{O};line-height:1.3;">{t0}</div><div style="font-size:13px;color:{MUT};">~ {t1}</div></td>'
who=lambda co,name,role:f'<strong style="color:{N};">{co}</strong> · {name}'+(f' · {role}' if role else '')
def row(t0,t1,n,c,ind,t,desc,co,name,role,slug):
    return (f'<tr>{tcell(t0,t1)}<td style="{td}">'
      f'<div style="font-size:13px;font-weight:700;color:{MUT};margin-bottom:2px;"><span style="display:inline-block;width:9px;height:9px;background:{c};margin-right:6px;"></span>발표 {n} · {ind}</div>'
      f'<div style="font-size:17px;font-weight:700;color:{N};line-height:1.5;">{t}</div>'
      f'<div style="font-size:15px;color:#2f4356;margin-top:4px;">{who(co,name,role)}</div>'
      f'<div style="font-size:14px;color:{MUT};margin-top:6px;line-height:1.7;">{desc}</div></td></tr>')
def plain(t0,t1,ind,t,sp):
    return (f'<tr>{tcell(t0,t1)}<td style="{td}"><div style="font-size:13px;font-weight:700;color:{MUT};margin-bottom:2px;">{ind}</div>'
      f'<div style="font-size:17px;font-weight:700;color:{N};line-height:1.5;">{t}</div><div style="font-size:15px;color:#2f4356;margin-top:4px;">{sp}</div></td></tr>')
brk=lambda t0,t1:f'<tr><td colspan="2" style="padding:10px 14px;background:{CREAM};color:#7a5a2c;font-weight:700;font-size:14px;text-align:center;border-bottom:1px solid {LINE};">{t0} ~ {t1} · 쉬는 시간</td></tr>'
w=WELCOME
rows=[plain(w[0],w[1],"시작","환영 인사 — "+w[2],who(w[3],w[4],w[5]))]
rows+=[plain(*x[:5]) for x in TAIL if x[5]=="pre"]
for i,s_ in enumerate(S):
    rows.append(row(*s_))
    if i in BREAKS: rows.append(brk(*BREAKS[i]))
rows+=[plain(*x[:5]) for x in TAIL if x[5]=="post"]
table=f'<table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;background:#fff;border:1px solid {LINE};border-top:4px solid {N};">'+"\n".join(rows)+'</table>'
ul=lambda items:'<ul style="margin:0;padding-left:22px;color:#24384b;">'+"".join(f'<li style="margin-bottom:8px;">{i}</li>' for i in items)+'</ul>'
faq=lambda q,a:f'<div style="background:#fff;border:1px solid {LINE};padding:16px 18px;margin-bottom:10px;"><div style="font-weight:800;font-size:16px;color:{N};margin-bottom:6px;">{q}</div><div style="color:#2f4356;">{a}</div></div>'

SP=[("환영",w[4],w[3],w[5],"환영 인사",w[6])]+[(x[2],x[8],x[7],x[9],x[5],x[10]) for x in S]
def spcard(n,name,org,role,talk,slug,_i=[0]):
    src=photo(slug,_i[0]); _i[0]+=1
    r=f' · {role}' if role else ''
    return (f'<tr><td style="vertical-align:top;background:#fff;border:1px solid {LINE};padding:16px 18px;">'
      f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;"><tr>'
      f'<td style="width:104px;vertical-align:top;"><img src="{src}" alt="{name} 발표자 사진" width="88" height="88" style="width:88px;height:88px;border-radius:50%;display:block;border:0;object-fit:cover;" /></td>'
      f'<td style="vertical-align:top;"><div style="font-weight:800;font-size:18px;color:{N};line-height:1.4;">{name}</div>'
      f'<div style="font-size:15px;color:#2f4356;margin:2px 0 8px;"><strong style="color:{N};">{org}</strong>{r}</div>'
      f'<div style="font-size:15px;color:#2f4356;"><strong style="color:{O};">{"" if n=="환영" else "발표 "}{n}</strong> &nbsp;{talk}</div></td></tr></table></td></tr>')
speakers='<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;">'+"".join(spcard(*x) for x in SP)+'</table>'
LI="https://www.linkedin.com/feed/update/urn:li:activity:"
lk=lambda u,t:f'<a href="{u}" style="color:{N};font-weight:700;">{t}</a>'
def meet(season,links):
    return f'<tr><td style="padding:12px 14px;border-bottom:1px solid {LINE};font-weight:700;color:{N};width:150px;font-size:15px;">{season}</td><td style="padding:12px 14px;border-bottom:1px solid {LINE};font-size:15px;color:#2f4356;">{links}</td></tr>'
meets=(meet("2026년 여름 밋업",lk(LI+"7463619588719681536","초청 글 보기"))
 +meet("2026년 봄 밋업",lk(LI+"7436994779856556034","초청 글 보기")+" · "+lk(LI+"7454808718665379840","감사 글 보기"))
 +meet("2025년 겨울 밋업",lk(LI+"7409576242817114112","초청 글 보기")))
about=(h2(f"{acc('AI놀이터')}를 소개합니다")
 +f'<p style="color:#2f4356;margin:0 0 16px;">AI놀이터는 Microsoft AI 커뮤니티입니다. AI를 배우는 곳이라기보다 <strong>AI와 놀아 보는 곳</strong>으로, 편하게 질문하고, 직접 해 보고, 알게 된 것을 서로 나눕니다. AI를 처음 접하는 분부터 현업에서 새로운 가능성을 찾는 분까지 누구나 함께할 수 있습니다.</p>'
 +cards(card("#F25022","질문","무엇이든 편하게 물어볼 수 있는 곳에서 시작합니다."),card("#7FBA00","놀이","직접 해 본 시도가 진짜 경험이 됩니다."),card("#00A4EF","공유","알게 된 것을 나누면 누군가의 실마리가 됩니다."))
 +f'<p style="color:#2f4356;margin:20px 0 10px;">계절마다 밋업을 열고, 그 사이에는 소규모 모임 ‘작은 놀이터’를 이어 가고 있습니다.</p>'
 +f'<table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;background:#fff;border:1px solid {LINE};">{meets}</table>'
 +f'<p style="margin:16px 0 0;font-size:15px;color:#2f4356;">'+lk("https://www.linkedin.com/groups/14571141/","LinkedIn ‘AI 놀이터’ 그룹 참여하기")+' · '+lk("https://aiplayground-kr.github.io/home/","공식 사이트 바로가기")+'</p>')
def spon(f,alt):
    return f'<td style="width:50%;padding:24px;vertical-align:middle;background:#fff;text-align:center;border:1px solid {LINE};"><img src="{B}/sponsors/{f}" alt="{alt}" style="max-width:180px;width:100%;height:auto;display:inline-block;border:0;" /></td>'
sponsors=(h2("후원사")+f'<p style="color:{MUT};margin:0 0 12px;">이번 밋업을 함께 만들어 주시는 곳입니다.</p>'
 +f'<table role="presentation" cellpadding="0" cellspacing="8" border="0" style="width:100%;border-collapse:separate;"><tr>{spon("sponsor01.jpg","Microsoft")}{spon("sponsor02.png","후원사 로고")}</tr></table>')
VENUE="한국마이크로소프트 13층<br/>서울 종로구 종로1길 50"
body=f'''<div style="max-width:780px;margin:0 auto;background:#fbf9f4;color:#24384b;font-family:'Pretendard','Apple SD Gothic Neo','맑은 고딕',sans-serif;font-size:16px;line-height:1.8;padding:0;">

  <!-- 1) 배너 -->
  <p style="margin:0;"><img src="{B}/banner_1920x1080.png" alt="AI놀이터 2026 가을 밋업 — DEMO DAY · 2026년 10월 25일(일)" style="width:100%;height:auto;display:block;border:0;" /></p>

  <!-- 2) 핵심 정보 -->
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;background:#fff;border:1px solid {LINE};border-collapse:separate;margin:0 0 28px;">
    <tr>{info("일시","2026년 10월 25일(일)<br/>오후 1시 ~ 6시 10분",f"border-right:1px solid {LINE};border-bottom:1px solid {LINE};")}{info("장소",VENUE,f"border-bottom:1px solid {LINE};")}</tr>
    <tr>{info("참가비","무료 (현장 참석만 가능)",f"border-right:1px solid {LINE};")}{info("신청 기간","10월 7일(수) ~ 10월 20일(화) · 선착순 180명")}</tr>
  </table>

  <!-- 3) 소개 -->
  {sec(h2(f"업무 현장의 {acc('AI·AX 추진 경험')}을 나누는 자리")+f"""
    <p style="color:#2f4356;margin:0 0 12px;">AI놀이터 2026 가을 밋업은 <strong>DEMO DAY</strong>로 진행합니다.</p><p style="color:#2f4356;margin:0 0 12px;">Microsoft 365 Copilot, Copilot Studio 등을 활용해 업무 현장에서 AI·AX(AI 전환)를 직접 추진해 온 분들이, 그 과정에서 얻은 경험과 실제 적용 사례를 들려드립니다.</p><p style="color:#2f4356;margin:0 0 18px;">{INDUSTRIES} — 서로 다른 현장의 이야기를 하루에 만나보세요.</p>
    <div style="padding:14px 18px;border-left:4px solid {O};background:#fdf1e2;font-weight:700;color:{N};">한 줄 요약 — 여러 산업 현장에서 AI·AX를 추진한 경험과 실제 적용 사례를 함께 나누는 커뮤니티 밋업입니다.</div>""")}

  {hr}

  <!-- 4) 특징 -->
  {sec(h2(f"이번 밋업에서 {acc('얻어 가실 것')}")+f'''
    {cards(card("#F25022","현장의 추진 경험","어떻게 시작했고, 어떤 어려움을 어떻게 풀었는지 담당자가 직접 이야기합니다."),card("#00A4EF","실제 적용 사례","Microsoft 365 Copilot, Copilot Studio 등을 실제 업무에 적용한 모습을 봅니다."),card("#FFB900","사람과의 연결","조별로 인사를 나누고, 비슷한 고민을 가진 분들과 편하게 이야기합니다."))}''')}

  {hr}

  <!-- 5) 발표 순서 -->
  {sec(h2(f"발표 {acc('순서')}")+f'<p style="color:{MUT};margin:0 0 16px;">2026년 10월 25일(일) 오후 1시 ~ 6시 10분 · 발표 9개 · 쉬는 시간 2회</p>'+table+f'<p style="color:{MUT};font-size:14px;margin:12px 0 0;">※ 세부 시간과 발표 내용은 주최 측 사정에 따라 일부 바뀔 수 있습니다.</p>')}

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
  {sec(h2("참가 전 꼭 확인해 주세요")+ul([f"{st('현장 참석만 가능')}하며, 온라인 중계는 없습니다.",f"조별 활동이 있으니 {st('오후 1시 전까지 도착')}해 주세요.",f"신청은 {st('10월 20일(화)')}까지이며, 정원 180명이 차면 일찍 마감될 수 있습니다.","행사 전에 신청하신 이메일로 입장 방법을 안내드립니다.","일정과 발표 내용은 주최 측 사정에 따라 일부 바뀔 수 있습니다."]))}

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
    {faq("Q6. 장소는 어디인가요?","한국마이크로소프트 13층입니다(서울 종로구 종로1길 50). 지하철 광화문역이나 종각역에서 걸어오실 수 있습니다.")}
    {faq("Q7. 참석이 어려워지면 어떻게 하나요?","이벤터스 마이페이지의 신청 내역에서 직접 취소해 주세요. 대기 중인 분께 자리가 돌아갑니다.")}
    {faq("Q8. 사진이나 영상 촬영이 있나요?","운영진이 행사 사진을 촬영하며, 일부는 후기 공유에 쓰일 수 있습니다. 직접 촬영하실 때는 다른 참가자의 초상권을 지켜 주시고, 발표자가 비공개를 요청한 내용은 촬영·공유하지 말아 주세요.")}
  </div>

  <div style="height:6px;background:#F25022;width:100%;"></div><div style="height:6px;background:#7FBA00;width:100%;"></div><div style="height:6px;background:#00A4EF;width:100%;"></div><div style="height:6px;background:#FFB900;width:100%;"></div>
  <p style="text-align:center;color:{MUT};font-size:13px;padding:14px;margin:0;">AI놀이터 · 놀다 보면 알게 되는 AI — <a href="https://aiplayground-kr.github.io/home/" style="color:{N};">aiplayground-kr.github.io/home</a></p>
</div>'''
head='''<!--
============================================================
  이벤터스 에디터 전용 HTML (인라인 스타일 + 테이블 레이아웃) — 초안 v0.6
  사용법: 이벤터스 본문 에디터의 [HTML] 탭에 아래 div 전체를 붙여넣기
  주의: 이벤터스는 style 태그 / class / 스크립트 / flex·grid 를 제거하므로
        본 파일은 인라인 style + table 로만 작성되어 있습니다.
  이미지: GitHub raw URL 사용 (저장소가 public 이어야 표시됨)
============================================================
-->
'''
import re
clean=re.sub(r'\n?\s*<!--.*?-->','',body,flags=re.S)  # 이벤터스 보안 필터 대응: 주석 없이 출력
open('이벤터스_본문_HTML.html','w',encoding='utf-8').write(clean.strip()+"\n")
open('preview.html','w').write('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>미리보기 — AI놀이터 2026 가을 밋업 DEMO DAY</title></head><body style="margin:0;background:#e9edf0;">'+body.replace(B,"images")+'</body></html>')
