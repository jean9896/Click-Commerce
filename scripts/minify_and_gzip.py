import re, gzip, os

def minify_css(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s*([{}:;,])\s*', r'\1', s)
    return s.strip()

files = ['assets/css/index-CWxZw2E6.css','assets/css/fontawesome.css']
for f in files:
    if not os.path.exists(f):
        print('missing',f)
        continue
    with open(f,'r',encoding='utf-8', errors='ignore') as fh:
        s = fh.read()
    m = minify_css(s)
    out = f.replace('.css','.min.css')
    with open(out,'w',encoding='utf-8') as oh:
        oh.write(m)
    with gzip.open(out+'.gz','wb') as gz:
        gz.write(m.encode('utf-8'))
    print('wrote',out,'and',out+'.gz')

# gzip the large JS bundle (leave JS unchanged)
js = 'assets/js/index-uNm_3oIC.js.baixados'
if os.path.exists(js):
    with open(js,'rb') as jh, gzip.open(js+'.gz','wb') as gj:
        gj.writelines(jh)
    print('wrote', js+'.gz')
else:
    print('missing', js)
