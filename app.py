import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gift from IBRA 🎁", page_icon="🎁", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:800px; position:relative; overflow:hidden;">
  <canvas id="c" style="width:100%; height:100%; position:absolute; top:0; left:0;"></canvas>
  
  <div id="layer1" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10;">
    <div style="color:#FFD700; font-family:Georgia; font-size:42px; font-weight:bold; text-shadow:0 0 20px #FFD700;">SURPRISE</div>
    <div style="color:#ff8ab0; font-size:18px; margin-top:5px;">from IBRA</div>
    <button id="openBtn" style="margin-top:25px; background:white; color:black; border:none; padding:12px 35px; border-radius:30px; font-weight:bold; cursor:pointer;">OPEN 🎁</button>
  </div>

  <div id="layer2" style="display:none; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; z-index:10; width:90%;">
    <div style="color:white; font-family:Georgia; font-size:22px; margin-bottom:30px;">Choose a mystery gift ✨</div>
    <div style="display:flex; gap:25px; justify-content:center;">
      <div id="gift1" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; margin-top:10px; font-size:12px;">GIFT 1</div></div>
      <div id="gift2" style="background:#1e1e1e; border:1px solid #444; border-radius:15px; padding:30px 20px; width:120px; cursor:pointer;"><div style="font-size:50px;">🎁</div><div style="color:white; margin-top:10px; font-size:12px;">GIFT 2</div></div>
    </div>
  </div>

  <div id="flowerText" style="position:absolute; top:78%; left:50%; transform:translate(-50%,-50%); color:#ffb0d0; font-family:Georgia; font-style:italic; font-size:17px; text-align:center; opacity:0; transition:1.5s; z-index:5; width:85%;">This flower is for you,<br>beautiful girl 🌸</div>
  <div id="loveText" style="position:absolute; top:68%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia; font-weight:bold; font-size:28px; text-align:center; opacity:0; transition:1.5s; z-index:5;">LOVE<br>YOU.</div>
  <div id="backBtn" style="display:none; position:absolute; bottom:20px; left:50%; transform:translateX(-50%); color:#666; cursor:pointer; font-size:12px; z-index:10;">← Back to gifts</div>
</div>

<script>
const canvas=document.getElementById('c'); const ctx=canvas.getContext('2d');
canvas.width=600; canvas.height=800;

function clearAll(){
  ctx.setTransform(1,0,0,1,0,0);
  ctx.clearRect(0,0,canvas.width,canvas.height);
  document.getElementById('flowerText').style.opacity=0;
  document.getElementById('loveText').style.opacity=0;
}

// BUNGA FIX CANTIK - TIDAK CACAT LAGI
function drawFlower(){
  clearAll();
  let steps=[];
  function addBranch(x,y,len,angle,depth){
    if(depth<=0 || len<5) return;
    let x2=x+Math.cos(angle)*len;
    let y2=y+Math.sin(angle)*len;
    steps.push({x,y,x2,y2,depth,len});
    let nlen=len*0.72;
    addBranch(x2,y2,nlen,angle-0.6,depth-1);
    addBranch(x2,y2,nlen,angle+0.6,depth-1);
    if(depth>4) addBranch(x2,y2,nlen*0.8,angle+(Math.random()-0.5)*0.3,depth-1);
  }
  addBranch(canvas.width/2, canvas.height, 85, -Math.PI/2, 8);
  
  let i=0;
  function anim(){
    if(i>=steps.length){
      document.getElementById('flowerText').style.opacity=1;
      return;
    }
    let s=steps[i];
    ctx.beginPath(); ctx.moveTo(s.x,s.y); ctx.lineTo(s.x2,s.y2);
    if(s.depth<=2){
      ctx.strokeStyle="#ff7aa0"; ctx.lineWidth=1.5; ctx.stroke();
      ctx.beginPath(); ctx.arc(s.x2,s.y2,7,0,Math.PI*2);
      ctx.fillStyle=["#ff2a5e","#ff8ab0","#FFD700","#ff9ac4"][Math.floor(Math.random()*4)];
      ctx.shadowColor=ctx.fillStyle; ctx.shadowBlur=10; ctx.fill(); ctx.shadowBlur=0;
    } else {
      ctx.strokeStyle=s.depth>5?"#4a2f1f":"#6b3a2a"; ctx.lineWidth=s.depth*0.9; ctx.stroke();
    }
    i++; setTimeout(anim, 25);
  }
  anim();
}

function drawLove(){
  clearAll();
  let pts=[]; for(let t=0;t<Math.PI*2;t+=0.07){ let x=16*Math.pow(Math.sin(t),3); let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t)); pts.push({x,y}); }
  let i=0; let scale=16;
  function d(){ if(i>=pts.length){ document.getElementById('loveText').style.opacity=1; return; } let p=pts[i]; ctx.fillStyle="#ff2a5e"; ctx.font="bold 9px Courier New"; ctx.textAlign="center"; ctx.fillText("I LOVE YOU", canvas.width/2+p.x*scale, canvas.height/2+p.y*scale-80); i++; setTimeout(d,80); } d();
}

document.getElementById('openBtn').onclick=()=>{
  document.getElementById('layer1').style.display='none';
  document.getElementById('layer2').style.display='block';
};
document.getElementById('gift1').onclick=()=>{
  document.getElementById('layer2').style.display='none'; // HILANGKAN PILIHAN!
  drawFlower(); document.getElementById('backBtn').style.display='block';
};
document.getElementById('gift2').onclick=()=>{
  document.getElementById('layer2').style.display='none'; // HILANGKAN PILIHAN!
  drawLove(); document.getElementById('backBtn').style.display='block';
};
document.getElementById('backBtn').onclick=()=>{
  clearAll(); document.getElementById('backBtn').style.display='none';
  document.getElementById('layer2').style.display='block';
};
</script>
""", height=820)
