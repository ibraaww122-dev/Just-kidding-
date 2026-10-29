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

  <div id="flowerText" style="display:none; position:absolute; top:10%; left:50%; transform:translateX(-50%); color:#ffb0d0; font-family:Georgia; font-style:italic; font-size:18px; text-align:center; z-index:10; text-shadow:0 0 15px #ff8ab0; width:90%;">This flower is for you,<br>beautiful girl 🌸</div>
  <div id="backBtn" style="display:none; position:absolute; bottom:20px; left:50%; transform:translateX(-50%); color:#888; cursor:pointer; font-size:12px; z-index:10;">← Back</div>
  <div id="loveText" style="position:absolute; top:68%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:1s; z-index:5;">LOVE<br>YOU.</div>
</div>

<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;

function clearAll(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  document.getElementById('loveText').style.opacity=0;
  document.getElementById('flowerText').style.display='none';
}

function drawFlowerBloom(){
  clearAll();
  document.getElementById('flowerText').style.display='block';
  const cx=canvas.width/2;
  const cy=canvas.height/2 + 40;
  let petalIndex=0;
  const totalPetals=16;
  function drawPetal(angle, scale){
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(angle);
    ctx.beginPath();
    ctx.ellipse(0, -90*scale, 28*scale, 85*scale, 0, 0, Math.PI*2);
    let grad=ctx.createRadialGradient(0,-90*scale,10,0,-90*scale,80);
    grad.addColorStop(0,'#FFDAB9');
    grad.addColorStop(0.5,'#FFB088');
    grad.addColorStop(1,'#FF8A65');
    ctx.fillStyle=grad;
    ctx.shadowColor='#FF8A65';
    ctx.shadowBlur=15*scale;
    ctx.fill();
    ctx.shadowBlur=0;
    ctx.restore();
  }
  function bloom(){
    if(petalIndex>=totalPetals){
      ctx.beginPath();
      ctx.arc(cx, cy, 45, 0, Math.PI*2);
      let g=ctx.createRadialGradient(cx-10, cy-10, 5, cx, cy, 45);
      g.addColorStop(0,'#FFD700');
      g.addColorStop(0.3,'#FFA000');
      g.addColorStop(1,'#5D4037');
      ctx.fillStyle=g;
      ctx.shadowColor='#FFD700';
      ctx.shadowBlur=20;
      ctx.fill();
      ctx.shadowBlur=0;
      for(let i=0;i<80;i++){
        let a=Math.random()*Math.PI*2;
        let r=Math.random()*35;
        ctx.beginPath();
        ctx.arc(cx+Math.cos(a)*r, cy+Math.sin(a)*r, 1.5,0,Math.PI*2);
        ctx.fillStyle='#3E2723';
        ctx.fill();
      }
      return;
    }
    let angle=(petalIndex/totalPetals)*Math.PI*2;
    let scale=0.6 + (petalIndex/totalPetals)*0.5;
    drawPetal(angle, scale);
    petalIndex++;
    setTimeout(bloom, 90);
  }
  bloom();
  setTimeout(()=>{
    ctx.beginPath();
    ctx.moveTo(cx, cy+45);
    ctx.lineTo(cx, canvas.height-50);
    ctx.strokeStyle='#4A7C59';
    ctx.lineWidth=8;
    ctx.lineCap='round';
    ctx.stroke();
  }, totalPetals*90 + 100);
}

function drawLove(){
  clear
