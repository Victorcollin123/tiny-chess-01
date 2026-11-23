import json,os,sys,urllib.request,urllib.error
V=(0,100,320,330,500,900,0)
PH=(0,0,1,1,2,4,0)
MT=100000
IN=1000000
BG=min(int(os.environ.get("MAKEFUN_NODE_BUDGET","75000")),40000)
ND=0
QN=0
T={}
KL=[[-1,-1] for _ in range(128)]
HS=[[[0]*128 for _ in range(128)] for _ in range(2)]
PM=(0,0,0,0,0,0,0,0,5,10,10,-15,-15,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0)
PE=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,10,10,0,0,10,10,5,10,10,20,30,30,20,10,10,20,20,30,40,40,30,20,20,40,40,50,60,60,50,40,40,90,90,90,90,90,90,90,90,0,0,0,0,0,0,0,0)
NM=(-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50)
BM=(-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20)
RM=(0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0)
QM=(-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20)
KM=(20,30,10,0,0,10,30,20,20,20,0,0,0,0,20,20,-10,-20,-20,-20,-20,-20,-20,-10,-20,-30,-30,-40,-40,-30,-30,-20,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30)
KE=(-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50)
TM=(None,PM,NM,BM,RM,QM,KM)
TE=(None,PE,NM,BM,RM,QM,KE)
NJ=(-33,-31,-18,-14,14,18,31,33)
KS=(-17,-16,-15,-1,1,15,16,17)
DD=(-17,-15,15,17)
OD=(-16,-1,1,16)
L="abcdefgh"
FL={"p":1,"n":2,"b":3,"r":4,"q":5,"k":6}
PT={"n":2,"b":3,"r":4,"q":5}
class Z(Exception):pass
class P:
 __slots__=("b","s","c","e","h","k")
 def __init__(self,b,s,c,e,h,k):
  self.b=b;self.s=s;self.c=c;self.e=e;self.h=h;self.k=k
def Sq(n):return (int(n[1])-1)*16+(ord(n[0])-97)
def Fp(f):
 p=f.split();b=[0]*128;k=[0,0]
 for r,row in enumerate(p[0].split("/")):
  rk=7-r;f2=0
  for ch in row:
   if ch.isdigit():f2+=int(ch)
   else:
    cd=FL[ch.lower()]|(8 if ch.islower() else 0);sq=rk*16+f2;b[sq]=cd
    if cd&7==6:k[1 if cd&8 else 0]=sq
    f2+=1
 s=0 if p[1]=="w" else 1;c=0;r=p[2]
 if "K" in r:c|=1
 if "Q" in r:c|=2
 if "k" in r:c|=4
 if "q" in r:c|=8
 e=-1
 if p[3]!="-":e=Sq(p[3])
 h=int(p[4]) if len(p)>4 else 0
 return P(b,s,c,e,h,k)
def At(p,sq,bw):
 b=p.b
 if bw:
  for t in (sq-15,sq-17):
   if t&0x88==0 and b[t]==1:return True
 else:
  for t in (sq+15,sq+17):
   if t&0x88==0 and b[t]==9:return True
 wn=2 if bw else 10
 for d in NJ:
  t=sq+d
  if t&0x88==0 and b[t]==wn:return True
 wk=6 if bw else 14
 for d in KS:
  t=sq+d
  if t&0x88==0 and b[t]==wk:return True
 for d in DD:
  t=sq+d
  while t&0x88==0:
   pc=b[t]
   if pc:
    if pc&8==(0 if bw else 8) and pc&7 in (3,5):return True
    break
   t+=d
 for d in OD:
  t=sq+d
  while t&0x88==0:
   pc=b[t]
   if pc:
    if pc&8==(0 if bw else 8) and pc&7 in (4,5):return True
    break
   t+=d
 return False
def Mk(p,mv):
 fr=mv&127;to=(mv>>7)&127;pr=(mv>>14)&7;fl=mv>>17;b=p.b;pc=b[fr];w=pc&8==0
 cs=to;cp=b[to]
 if fl&1:
  cs=to-16 if w else to+16;cp=b[cs];b[cs]=0
 rf=-1;rt=-1
 if fl&2:
  if to>fr:rf=fr+3;rt=fr+1
  else:rf=fr-4;rt=fr-1
  b[rt]=b[rf];b[rf]=0
 un=(cs,cp,p.c,p.e,p.h,rf,rt)
 b[to]=(pr|(0 if w else 8)) if pr else pc;b[fr]=0
 if pc&7==6:
  p.k[0 if w else 1]=to;p.c&=~(3 if w else 12)
 if fr==0 or to==0:p.c&=~2
 if fr==7 or to==7:p.c&=~1
 if fr==112 or to==112:p.c&=~8
 if fr==119 or to==119:p.c&=~4
 if fl&4:p.e=fr+16 if w else fr-16
 else:p.e=-1
 p.h=0 if pc&7==1 or cp else p.h+1
 p.s^=1
 return un
def Um(p,mv,un):
 fr=mv&127;to=(mv>>7)&127;pr=(mv>>14)&7;fl=mv>>17;b=p.b;p.s^=1;w=p.s==0
 cs,cp,c,e,h,rf,rt=un;pc=b[to]
 if pr:pc=1|(0 if w else 8)
 b[fr]=pc;b[to]=0
 if cp:b[cs]=cp
 if fl&2:b[rf]=b[rt];b[rt]=0
 if pc&7==6:p.k[0 if w else 1]=fr
 p.c=c;p.e=e;p.h=h
def Gn(p,co):
 b=p.b;w=p.s==0;mn=0 if w else 8;ms=[]
 for fr in range(128):
  if fr&0x88:continue
  pc=b[fr]
  if not pc or pc&8!=mn:continue
  kd=pc&7
  if kd==1:
   st=16 if w else -16;hm=1 if w else 6;ls=7 if w else 0;one=fr+st
   if b[one]==0:
    if one>>4==ls:
     for pr in (5,4,3,2):ms.append(fr|(one<<7)|(pr<<14))
    elif not co:
     ms.append(fr|(one<<7))
     if (fr>>4)==hm:
      tw=fr+st*2
      if b[tw]==0:ms.append(fr|(tw<<7)|(4<<17))
   for d in (st-1,st+1):
    to=fr+d
    if to&0x88:continue
    tg=b[to]
    if tg and tg&8!=mn:
     if to>>4==ls:
      for pr in (5,4,3,2):ms.append(fr|(to<<7)|(pr<<14))
     else:ms.append(fr|(to<<7))
    elif to==p.e:ms.append(fr|(to<<7)|(1<<17))
  elif kd==2:
   for d in NJ:
    to=fr+d
    if to&0x88:continue
    tg=b[to]
    if tg==0:
     if not co:ms.append(fr|(to<<7))
    elif tg&8!=mn:ms.append(fr|(to<<7))
  elif kd==6:
   for d in KS:
    to=fr+d
    if to&0x88:continue
    tg=b[to]
    if tg==0:
     if not co:ms.append(fr|(to<<7))
    elif tg&8!=mn:ms.append(fr|(to<<7))
   if not co:
    rt=p.c&(3 if w else 12)
    if rt:
     bs=fr
     if rt&(1 if w else 4):
      if b[bs+1]==0 and b[bs+2]==0 and not At(p,bs,not w) and not At(p,bs+1,not w) and not At(p,bs+2,not w):ms.append(fr|((bs+2)<<7)|(2<<17))
     if rt&(2 if w else 8):
      if b[bs-1]==0 and b[bs-2]==0 and b[bs-3]==0 and not At(p,bs,not w) and not At(p,bs-1,not w) and not At(p,bs-2,not w):ms.append(fr|((bs-2)<<7)|(2<<17))
  else:
   ds=DD if kd==3 else OD if kd==4 else DD+OD
   for d in ds:
    to=fr+d
    while to&0x88==0:
     tg=b[to]
     if tg==0:
      if not co:ms.append(fr|(to<<7))
     else:
      if tg&8!=mn:ms.append(fr|(to<<7))
      break
     to+=d
 return ms
def Ev(p):
 b=p.b;mg=0;eg=0;ph=0;wb=0;bb=0;pf=0;wm=0;bm=0
 for sq in range(128):
  if sq&0x88:continue
  pc=b[sq]
  if not pc:continue
  kd=pc&7;r=sq>>4;f=sq&7
  if kd==1:pf|=1<<f
  if kd==4:
   if pc&8:bm|=1<<f
   else:wm|=1<<f
  if kd==3:
   if pc&8:bb+=1
   else:wb+=1
  if pc&8:
   ix=(7-r)*8+f;mg-=V[kd]+TM[kd][ix];eg-=V[kd]+TE[kd][ix]
  else:
   ix=r*8+f;mg+=V[kd]+TM[kd][ix];eg+=V[kd]+TE[kd][ix]
  ph+=PH[kd]
 if wb==2:mg+=30;eg+=30
 if bb==2:mg-=30;eg-=30
 for f in range(8):
  if not (pf>>f)&1:
   if (wm>>f)&1:mg+=15;eg+=15
   if (bm>>f)&1:mg-=15;eg-=15
 sc=(mg*ph+eg*(24-ph))//24
 v=sc if p.s==0 else -sc
 return v+10

def Tk(p):return (bytes(p.b),p.s,p.c,p.e)
def Or(p,ms,tm,pl):
 b=p.b;s=p.s
 def rk(mv):
  if mv==tm:return 1<<20
  to=(mv>>7)&127;tg=b[to]
  if tg or (mv>>17)&1:
   vc=1 if (mv>>17)&1 else tg&7
   return 10000+V[vc]*10-V[b[mv&127]&7]
  if pl<128 and (mv==KL[pl][0] or mv==KL[pl][1]):return 9000
  return HS[s][mv&127][to]
 return sorted(ms,key=rk,reverse=True)
def Qs(p,al,be,pl):
 global QN
 QN+=1
 if ND+QN>=3*BG:raise Z
 st=Ev(p)
 if st>=be:return be
 if st>al:al=st
 ck=At(p,p.k[p.s],p.s==1)
 ms=Gn(p,False) if ck else Gn(p,True)
 ms=Or(p,ms,-1,pl)
 fd=False
 for mv in ms:
  if not ck:
   pr=(mv>>14)&7
   if not pr:
    to=(mv>>7)&127;tg=p.b[to]
    vc=1 if (mv>>17)&1 else (tg&7 if tg else 0)
    if st+V[vc]+200<al:continue
  un=Mk(p,mv)
  if At(p,p.k[p.s^1],p.s==0):
   Um(p,mv,un);continue
  fd=True
  s=-Qs(p,-be,-al,pl+1)
  Um(p,mv,un)
  if s>=be:return be
  if s>al:al=s
 if ck and not fd:return -MT+pl
 return al
def Sr(p,d,al,be,pl):
 global ND
 ND+=1
 if ND>=BG:raise Z
 if d<=0:return Qs(p,al,be,pl)
 ck=At(p,p.k[p.s],p.s==1)
 key=Tk(p);en=T.get(key);tm=-1
 if en is not None:
  tm=en[3]
  if en[0]>=d:
   if en[2]==0:return en[1]
   if en[2]==1 and en[1]>=be:return en[1]
   if en[2]==2 and en[1]<=al:return en[1]
 if not ck and d>=3 and be<MT:
  ev=Ev(p)
  if ev>=be:
   hs=False
   for sq in range(128):
    pc=p.b[sq]
    if pc and pc&7 not in (1,6) and (pc&8)==(0 if p.s==0 else 8):hs=True;break
   if hs:
    oe=p.e;p.e=-1;p.s^=1
    try:s=-Sr(p,d-3,-be,-be+1,pl+1)
    finally:p.s^=1;p.e=oe
    if s>=be:return be
 if not ck and d<=2:
  ev=Ev(p);mg=300 if d==1 else 500
  if ev+mg<=al:return ev
 a0=al
 ms=Or(p,Gn(p,False),tm,pl)
 bs=-IN;bm=-1;fd=False
 for i,mv in enumerate(ms):
  un=Mk(p,mv)
  if At(p,p.k[p.s^1],p.s==0):
   Um(p,mv,un);continue
  fd=True
  if i==0:s=-Sr(p,d-1,-be,-al,pl+1)
  else:
   s=-Sr(p,d-1,-al-1,-al,pl+1)
   if al<s<be:s=-Sr(p,d-1,-be,-al,pl+1)
  Um(p,mv,un)
  if s>bs:bs=s;bm=mv
  if s>al:al=s
  if al>=be:
   to=(mv>>7)&127
   if not p.b[to] and not (mv>>17)&1:
    if KL[pl][0]!=mv:
     KL[pl][1]=KL[pl][0];KL[pl][0]=mv
    HS[p.s][mv&127][to]+=d*d
   break
 if not fd:return -MT+pl if ck else 0
 if len(T)>300000:T.clear()
 if bs>=be:fg=1
 elif bs<=a0:fg=2
 else:fg=0
 T[key]=(d,bs,fg,bm)
 return bs
def Uc(p,u):
 fr=Sq(u[:2]);to=Sq(u[2:4]);pr=PT[u[4]] if len(u)==5 else 0;fl=0;pc=p.b[fr]
 if pc&7==1 and to==p.e and (to&7)!=(fr&7):fl|=1
 elif pc&7==6 and abs((to&7)-(fr&7))==2:fl|=2
 elif pc&7==1 and abs(to-fr)==32:fl|=4
 return fr|(to<<7)|(pr<<14)|(fl<<17)
def Rt(p,lu):
 global ND,QN,KL,HS
 ND=0;QN=0;KL=[[-1,-1] for _ in range(128)];HS=[[[0]*128 for _ in range(128)] for _ in range(2)]
 sc=[(Uc(p,u),u) for u in lu]
 if len(sc)==1:return sc[0][1]
 ch=sc[0][1]
 try:
  for d in range(1,64):
   bs=-IN;al=-IN;nx=[]
   for i,(mv,u) in enumerate(sc):
    un=Mk(p,mv)
    if i==0:s=-Sr(p,d-1,-IN,-al,1)
    else:
     s=-Sr(p,d-1,-al-1,-al,1)
     if al<s<IN:s=-Sr(p,d-1,-IN,-al,1)
    Um(p,mv,un)
    nx.append((s,mv,u))
    if s>bs:bs=s;ch=u
    if s>al:al=s
   nx.sort(key=lambda t:t[0],reverse=True)
   sc=[(mv,u) for _,mv,u in nx]
 except Z:pass
 return ch
EU=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("MAKEFUN_ENV_URL is not set")
def Po(pt,bd):
 rq=urllib.request.Request(EU+pt,data=json.dumps(bd).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(rq) as r:return json.load(r)
 except urllib.error.HTTPError as e:sys.exit(f"{pt}: HTTP {e.code} {e.read().decode(errors='replace')}")
def Rn():
 while True:
  g=Po("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   g=Po("/move",{"game":g["game"],"move":Rt(Fp(g["fen"]),g["legal_moves"])})
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
if __name__=="__main__":Rn()
