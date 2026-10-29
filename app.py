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

  <div id="bouquetBox" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; text-align:center; z-index:5; overflow-y:auto;">
    <div style="color:#ffb0d0; font-family:Georgia; font-style:italic; font-size:18px; margin-top:15px; text-shadow:0 0 10px #ff8ab0;">This flower is for you,<br>beautiful girl 🌸</div>
    <img src="https://images.unsplash.com/photo-1563241527-3004b7be0ee9?w=500&q=80" style="width:85%; max-width:340px; margin-top:15px; border-radius:15px; box-shadow:0 0 30px rgba(255,200,0,0.3);">
    <div style="color:#ccc; font-size:13px; margin-top:10px; font-family:Georgia; font-style:italic;">Sunflower & Peach Roses - Sunnies Bouquet 🌻</div>
  </div>

  <div id="loveText" style="position:absolute; top:68%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:1.5s; z-index:5;">LOVE<br>YOU.</div>
  <div id="backBtn" style="display:none; position:absolute; bottom:20px; left:50%; transform:translateX(-50%); color:#888; cursor:pointer; font-size:12px; z-index:10;">← Back to gifts</div>
</div>

<script>
const canvas=document.getElementById('c'); const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;
function clearAll(){ ctx.clearRect(0,0,canvas.width,canvas.height); document.getElementById('loveText').style.opacity=0; document.getElementById('bouquetBox').style.display='none'; }
function drawLove(){
  clearAll(); let pts=[]; for(let t=0;t<Math.PI*2;t+=0.07){ let x=16*Math.pow(Math.sin(t),3); let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t)); pts.push({x,y}); }
  let i=0; let scale=16;
  function d(){ if(i>=pts.length){ document.getElementById('loveText').style.opacity=1; return; } let p=pts[i]; ctx.fillStyle="#ff2a5e"; ctx.font="bold 9px Courier New"; ctx.textAlign="center"; ctx.fillText("I LOVE YOU", canvas.width/2+p.x*scale, canvas.height/2+p.y*scale-80); i++; setTimeout(d,80); } d();
}
document.getElementById('openBtn').onclick=()=>{ document.getElementById('layer1').style.display='none'; document.getElementById('layer2').style.display='block'; };
document.getElementById('gift1').onclick=()=>{ document.getElementById('layer2').style.display='none'; clearAll(); document.getElementById('bouquetBox').style.display='block'; document.getElementById('backBtn').style.display='block'; };
document.getElementById('gift2').onclick=()=>{ document.getElementById('layer2').style.display='none'; drawLove(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('backBtn').onclick=()=>{ clearAll(); document.getElementById('backBtn').style.display='none'; document.getElementById('layer2').style.display='block'; };
</script>
""", height=820)
