import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gift from IBRA 🎁", page_icon="🎁", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:800px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center; flex-direction:column;">
  <canvas id="c" style="width:100%; height:100%; position:absolute; top:0; left:0;"></canvas>
  
  <div id="layer1" style="text-align:center; z-index:10;">
    <div style="color:#FFD700; font-family:Georgia, serif; font-size:42px; font-weight:bold; text-shadow:0 0 20px #FFD700;">SURPRISE</div>
    <div style="color:#ff8ab0; font-size:18px; margin-top:5px; letter-spacing:2px;">from IBRA</div>
    <button id="openBtn" style="margin-top:25px; background:white; color:black; border:none; padding:12px 35px; border-radius:30px; font-weight:bold; cursor:pointer;">OPEN 🎁</button>
  </div>

  <div id="layer2" style="display:none; text-align:center; z-index:10; width:90%;">
    <div style="color:white; font-family:Georgia; font-size:22px; margin-bottom:30px;">Choose your gift ✨</div>
    <div style="display:flex; gap:20px; justify-content:center;">
      <div id="gift1" style="background:#1a1a1a; border:1px solid #ff8ab0; border-radius:15px; padding:20px; width:130px; cursor:pointer;">
        <div style="font-size:50px;">🌸</div><div style="color:#ff8ab0; margin-top:10px; font-size:14px; font-weight:bold;">GIFT 1<br>Flower</div>
      </div>
      <div id="gift2" style="background:#1a1a1a; border:1px solid #ff2a5e; border-radius:15px; padding:20px; width:130px; cursor:pointer;">
        <div style="font-size:50px;">💝</div><div style="color:#ff2a5e; margin-top:10px; font-size:14px; font-weight:bold;">GIFT 2<br>LOVE</div>
      </div>
    </div>
    <div id="backBtn" style="display:none; margin-top:20px; color:#888; cursor:pointer; font-size:13px;">← Back to gifts</div>
  </div>

  <div id="flowerText" style="position:absolute; top:75%; left:50%; transform:translate(-50%,-50%); color:#ffb0d0; font-family:Georgia, serif; font-style:italic; font-size:18px; text-align:center; opacity:0; transition:2s; z-index:5; width:80%;">This flower is for you,<br>beautiful girl 🌸</div>
  <div id="loveText" style="position:absolute; top:65%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:2s; z-index:5;">LOVE<br>YOU.</div>
</div>

<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;

function playSound(freqs){
  const ac = new (window.AudioContext||window.webkitAudioContext)();
  let t=ac.currentTime;
  freqs.forEach(f=>{
    const o=ac.createOscillator(); const g=ac.createGain();
    o.frequency.value=f; o.connect(g); g.connect(ac.destination);
    o.start(t); g.gain.setValueAtTime(0.3,t); g.gain.exponentialRampToValueAtTime(0.01,t+0.5); o.stop(t+0.5);
    t+=0.15;
  });
}
function clearAll(){ ctx.setTransform(1,0,0,1,0,0); ctx.clearRect(0,0,canvas.width,canvas.height); document.getElementById('flowerText').style.opacity=0; document.getElementById('loveText').style.opacity=0; }

function drawFlower(){
  clearAll();
  ctx.save(); ctx.translate(canvas.width/2, canvas.height);
  function branch(x,y,len,angle,depth){
    if(depth==0 || len<4) return;
    let x2 = x + Math.cos(angle)*len;
    let y2 = y + Math.sin(angle)*len;
    ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(x2,y2);
    ctx.strokeStyle = depth>2 ? "#5a3a2a" : "#ff7aa0";
    ctx.lineWidth = depth; ctx.stroke();
    if(depth<=2){
      ctx.beginPath(); ctx.arc(x2,y2,5,0,Math.PI*2);
      ctx.fillStyle = ["#ff2a5e","#ff8ab0","#FFD700","#ff5ae0"][Math.floor(Math.random()*4)];
      ctx.fill();
    }
    let newLen=len*0.74;
    setTimeout(()=>{ branch(x2,y2,newLen,angle-0.55,depth-1); branch(x2,y2,newLen,angle+0.55,depth-1); }, 120);
  }
  branch(0,0,90,-Math.PI/2,7);
  ctx.restore();
  setTimeout(()=>{ document.getElementById('flowerText').style.opacity=1; }, 3500);
}

function drawLove(){
  clearAll();
  let pts=[];
  for(let t=0; t<Math.PI*2; t+=0.07){
    let x=16*Math.pow(Math.sin(t),3);
    let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t));
    pts.push({x,y});
  }
  let i=0; let scale=15;
  function draw(){
    if(i>=pts.length){ document.getElementById('loveText').style.opacity=1; return; }
    let p=pts[i];
    let cx=canvas.width/2 + p.x*scale;
    let cy=canvas.height/2 + p.y*scale - 100;
    ctx.fillStyle="#ff2a5e"; ctx.font="bold 9px Courier New"; ctx.textAlign="center";
    ctx.fillText("I LOVE YOU", cx, cy);
    i++; setTimeout(draw, 90);
  }
  draw();
}

document.getElementById('openBtn').onclick=()=>{
  playSound([440,660,880]);
  document.getElementById('layer1').style.display='none';
  document.getElementById('layer2').style.display='block';
};
document.getElementById('gift1').onclick=()=>{ playSound([523,659,784]); drawFlower(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('gift2').onclick=()=>{ playSound([440,550,660]); drawLove(); document.getElementById('backBtn').style.display='block'; };
document.getElementById('backBtn').onclick=()=>{ clearAll(); document.getElementById('backBtn').style.display='none'; };
</script>
""", height=820)
