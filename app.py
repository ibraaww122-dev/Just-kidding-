import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gift from IBRA 🎁", page_icon="🎁", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:800px; position:relative; overflow:hidden;">
  <canvas id="c" style="width:100%; height:100%; position:absolute; top:0; left:0;"></canvas>
  
  <div id="layer1" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10;">
    <div style="color:#FFD700; font-family:Georgia; font-size:42px; font-weight:bold; text-shadow:0 0 20px #FFD700;">SURPRISE</div>
    <div style="color:#ff8ab0; font-size:18px;">from IBRA</div>
    <button id="openBtn" style="margin-top:25px; background:white; color:black; border:none; padding:12px 35px; border-radius:30px; font-weight:bold; cursor:pointer;">OPEN 🎁</button>
  </div>

  <div id="layer2" style="display:none; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10;">
    <div style="color:white; font-family:Georgia; font-size:22px; margin-bottom:30px;">Choose a mystery gift ✨</div>
    <div style="display:flex; gap:25px; justify-content:center;">
      <div id="gift1" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; font-size:12px;">GIFT 1</div></div>
      <div id="gift2" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; font-size:12px;">GIFT 2</div></div>
    </div>
  </div>

  <div id="flowerText" style="display:none; position:absolute; top:8%; left:50%; transform:translateX(-50%); color:#ffb0d0; font-family:Georgia; font-style:italic; font-size:18px; text-align:center; z-index:10; text-shadow:0 0 10px #ff8ab0; width:90%;">This flower is for you,<br>beautiful girl 🌸</div>
  <div id="bouquetWrap" style="display:none; position:absolute; top:18%; left:50%; transform:translateX(-50%); width:90%; max-width:340px; z-index:5; text-align:center;"></div>
  
  <div id="loveText" style="position:absolute; top:68%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:1s; z-index:5;">LOVE<br>YOU.</div>
  <div id="backBtn" style="display:none; position:absolute; bottom:20px; left:50%; transform:translateX(-50%); color:#888; cursor:pointer; font-size:12px; z-index:10;">← Back to gifts</div>
</div>

<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;

function clearAll(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  document.getElementById('loveText').style.opacity=0;
  document.getElementById('flowerText').style.display='none';
  document.getElementById('bouquetWrap').style.display='none';
  document.getElementById('bouquetWrap').innerHTML='';
}

// BUNGA MUNCUL SATU-SATU CEPET - BUKET SUNFLOWER + PEACH ROSE
function drawBouquet(){
  clearAll();
  document.getElementById('flowerText').style.display='block';
  const wrap=document.getElementById('bouquetWrap');
  wrap.style.display='block';
  
  // 8 bunga yang muncul satu-satu membentuk buket
  const flowers = [
    {e:'🌻', x:0, y:0, s:70},
    {e:'🌹', x:-60, y:20, s:55},
    {e:'🌻', x:60, y:25, s:65},
    {e:'🌹', x:0, y:50, s:60},
    {e:'🌻', x:-40, y:70, s:50},
    {e:'🌹', x:50, y:75, s:55},
    {e:'🌼', x:-20, y:30, s:30},
    {e:'🌼', x:30, y:50, s:25}
  ];
  
  let i=0;
  function pop(){
    if(i>=flowers.length){
      // muncul bucket/wrapping di akhir
      const bucket=document.createElement('div');
      bucket.innerHTML='<div style="margin-top:140px; background:linear-gradient(#111,#000); border:1px solid #333; border-radius:10px 10px 80px 80px; padding:15px 10px 25px; color:#555; font-size:11px; letter-spacing:2px;">● FROM IBRA ●</div>';
      bucket.style.animation='pop 0.5s';
      wrap.appendChild(bucket);
      return;
    }
    const f=flowers[i];
    const d=document.createElement('div');
    d.textContent=f.e;
    d.style.position='absolute';
    d.style.left='50%';
    d.style.top='50%';
    d.style.fontSize=f.s+'px';
    d.style.transform=`translate(calc(-50% + ${f.x}px), calc(-50% + ${f.y}px)) scale(0)`;
    d.style.transition='0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
    d.style.filter='drop-shadow(0 0 10px rgba(255,200,0,0.5))';
    wrap.appendChild(d);
    setTimeout(()=>{ d.style.transform=`translate(calc(-50% + ${f.x}px), calc(-50% + ${f.y}px)) scale(1)`; }, 10);
    i++;
    setTimeout(pop, 250); // CEPET, 0.25 detik per bunga!
  }
  pop();
}

function drawLove(){
  clearAll();
  let pts=[]; for(let t=0;t<Math.PI*2;t+=0.07){ let x=16*Math.pow(Math.sin(t),3); let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t)); pts.push({x,y}); }
  let i=0; let scale=16;
  function d(){ if(i>=pts.length){ document.getElementById('loveText').style.opacity=1; return; } let p=pts[i]; ctx.fillStyle="#ff2a5e"; ctx.font="bold 9px Courier New"; ctx.textAlign="center"; ctx.fillText("I LOVE YOU", canvas.width/2+p.x*scale, canvas.height/2+p.y*scale-80); i++; setTimeout(d,60); } d();
}

document.getElementById('openBtn').onclick=()=>{ document.getElementById('layer1').style.display='none'; document.getElementById('layer2').style.display='block'; };
document.getElementById('gift1').onclick=()=>{ document.getElementById('layer2').style.display='none'; drawBouquet(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('gift2').onclick=()=>{ document.getElementById('layer2').style.display='none'; drawLove(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('backBtn').onclick=()=>{ clearAll(); document.getElementById('backBtn').style.display='none'; document.getElementById('layer2').style.display='block'; };
</script>
""", height=820)
