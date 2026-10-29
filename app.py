import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gift from IBRA", page_icon="🎁", layout="centered")
st.markdown('<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>', unsafe_allow_html=True)

html_code = '''
<div style="background:black; width:100%; height:800px; position:relative; overflow:hidden;">
  <canvas id="c" style="width:100%; height:100%; position:absolute; top:0; left:0;"></canvas>
  <audio id="bgMusic" loop>
    <source src="https://cdn.pixabay.com/audio/2022/06/07/audio_b9bd4170e8.mp3" type="audio/mpeg">
  </audio>

  <div id="layer1" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10;">
    <div style="color:#FFD700; font-family:Georgia; font-size:42px; font-weight:bold; text-shadow:0 0 20px #FFD700;">SURPRISE</div>
    <div style="color:#ff8ab0; font-size:18px;">from IBRA</div>
    <button id="openBtn" style="margin-top:25px; background:white; color:black; border:none; padding:12px 35px; border-radius:30px; font-weight:bold; cursor:pointer;">OPEN</button>
  </div>

  <div id="layer2" style="display:none; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10;">
    <div style="color:white; font-family:Georgia; font-size:22px; margin-bottom:30px;">Choose a mystery gift</div>
    <div style="display:flex; gap:25px; justify-content:center;">
      <div id="gift1" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; font-size:12px;">GIFT 1</div></div>
      <div id="gift2" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; font-size:12px;">GIFT 2</div></div>
    </div>
  </div>

  <div id="flowerText" style="display:none; position:absolute; top:8%; left:50%; transform:translateX(-50%); color:#ffb0d0; font-family:Georgia; font-style:italic; font-size:20px; text-align:center; z-index:10; text-shadow:0 0 15px #ff8ab0; width:90%;">This flower is for you,<br>beautiful girl 🌸</div>
  <div id="backBtn" style="display:none; position:absolute; bottom:20px; left:50%; transform:translateX(-50%); color:#888; cursor:pointer; font-size:12px; z-index:10;">Back</div>
  <div id="loveText" style="position:absolute; top:68%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:1s; z-index:5;">LOVE<br>YOU.</div>
</div>

<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;
const music=document.getElementById('bgMusic');

function clearAll(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  document.getElementById('loveText').style.opacity=0;
  document.getElementById('flowerText').style.display='none';
  music.pause();
}

function drawCosmosFront(){
  clearAll();
  document.getElementById('flowerText').style.display='block';
  music.volume=0.4;
  music.play().catch(()=>{});
  const cx=300; const cy=400;
  let petals=12;
  let idx=0;

  function petal(){
    if(idx>=petals){
      // tengah kuning cosmos menghadap depan
      ctx.beginPath();
      ctx.arc(cx, cy, 35, 0, 6.283);
      let g=ctx.createRadialGradient(cx-8, cy-8, 3, cx, cy, 35);
      g.addColorStop(0,'#FFEB3B');
      g.addColorStop(0.4,'#FFC107');
      g.addColorStop(1,'#FF6F00');
      ctx.fillStyle=g;
      ctx.shadowColor='#FFD700';
      ctx.shadowBlur=25;
      ctx.fill();
      ctx.shadowBlur=0;
      // bintik tengah
      for(let k=0;k<30;k++){
        let a=Math.random()*6.283;
        let r=Math.random()*20;
        ctx.beginPath();
        ctx.arc(cx+Math.cos(a)*r, cy+Math.sin(a)*r, 1.2, 0, 6.283);
        ctx.fillStyle='#5D4037';
        ctx.globalAlpha=0.6;
        ctx.fill();
        ctx.globalAlpha=1;
      }
      return;
    }
    let ang=(idx/petals)*6.283;
    // animasi mekar dari kecil ke gede
    let progress=0;
    function grow(){
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(ang);
      ctx.scale(progress, progress);
      ctx.beginPath();
      ctx.ellipse(0, -85, 32, 75, 0, 0, 6.283);
      let grad=ctx.createRadialGradient(0, -85, 10, 0, -85, 75);
      grad.addColorStop(0,'#FFD6F0');
      grad.addColorStop(0.3,'#FF85C8');
      grad.addColorStop(0.7,'#FF4FB7');
      grad.addColorStop(1,'#E91E8C');
      ctx.fillStyle=grad;
      ctx.shadowColor='#FF69B4';
      ctx.shadowBlur=15;
      ctx.fill();
      ctx.shadowBlur=0;
      ctx.restore();
      progress+=0.15;
      if(progress<1){
        requestAnimationFrame(grow);
      } else {
        idx++;
        setTimeout(petal, 80);
      }
    }
    grow();
  }
  petal();
}

function drawLove(){
  clearAll();
  let pts=[]; for(let t=0;t<6.283;t+=0.06){ let x=16*Math.pow(Math.sin(t),3); let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t)); pts.push({x:x,y:y}); }
  let i=0;
  function d(){ if(i>=pts.length){ document.getElementById('loveText').style.opacity=1; return; } let p=pts[i]; ctx.fillStyle="#ff2a5e"; ctx.font="bold 9px Courier New"; ctx.textAlign="center"; ctx.fillText("I LOVE YOU", 300+p.x*16, 300+p.y*16); i++; setTimeout(d,50); } d();
}

document.getElementById('openBtn').onclick=()=>{ document.getElementById('layer1').style.display='none'; document.getElementById('layer2').style.display='block'; };
document.getElementById('gift1').onclick=()=>{ document.getElementById('layer2').style.display='none'; drawCosmosFront(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('gift2').onclick=()=>{ document.getElementById('layer2').style.display='none'; drawLove(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('backBtn').onclick=()=>{ clearAll(); document.getElementById('backBtn').style.display='none'; document.getElementById('layer2').style.display='block'; };
</script>
'''

components.html(html_code, height=820)
