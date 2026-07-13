"""Genera le icone Corsa (scarpa) senza dipendenze esterne."""
from PIL import Image, ImageDraw
BG=(14,21,18); ACCENT=(251,146,60); SOLE=(74,222,128)
def base(S):
    img=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(img)
    d.rounded_rectangle([0,0,S,S],radius=int(S*0.22),fill=BG); return img,d
def shoe(size,path):
    S=size*4; img,d=base(S); P=lambda x,y:(int(x*S),int(y*S))
    upper=[P(0.19,0.58),P(0.19,0.40),P(0.26,0.36),P(0.34,0.38),P(0.38,0.48),
           P(0.52,0.50),P(0.66,0.52),P(0.80,0.57),P(0.85,0.58)]
    d.polygon(upper,fill=ACCENT)
    solepts=[P(0.16,0.58),P(0.85,0.58),P(0.90,0.60),P(0.89,0.655),P(0.20,0.655),P(0.16,0.63)]
    d.polygon(solepts,fill=SOLE)
    d.line([P(0.19,0.40),P(0.24,0.40)],fill=ACCENT,width=int(S*0.03))
    d.line([P(0.30,0.55),P(0.60,0.50)],fill=BG,width=int(S*0.02))
    d.line([P(0.30,0.55),P(0.40,0.53)],fill=BG,width=int(S*0.02))
    for i in range(3):
        x=0.30+i*0.05; d.line([P(x,0.42),P(x+0.04,0.47)],fill=BG,width=int(S*0.012))
    img.resize((size,size),Image.LANCZOS).save(path); print("scritto",path)
for s,p in [(512,"icon-512.png"),(192,"icon-192.png"),(180,"apple-touch-icon.png"),(64,"favicon.png")]:
    shoe(s,"docs/icons/"+p)
