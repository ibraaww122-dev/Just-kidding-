import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SURPRISE ❤️", page_icon="🎁", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:780px; position:relative; overflow:hidden; display:flex; justify-content:center; align-items:center;">
  <canvas id="c" style="width:100%; height:100%; position:absolute; top:0; left:0;"></canvas>
  
  <div id="surpriseBox" style="text-align:center; z-index:10;">
    <div style="color:#FFD700; font-family:Georgia, serif; font-size:42px; font-weight:bold; text-shadow:0 0 20px #FFD700; letter-spacing:4px;">SURPRISE</div>
    <div style="color:#ff8ab0; font-family:Georgia, serif; font-size:18px; margin-top:8px; letter-spacing:2px;">from IBRA</div>
    <button id="startBtn" style="margin-top:25px; background:white; color:black; border:none; padding:12px 35px; border-radius:30px; font-size:14px; font-weight:bold; cursor:pointer; letter-spacing:2px;">OPEN 🎁</button>
  </div>

  <div id="finalText" style="position:absolute; top:62%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia, serif; font-weight:bold; font-size:28px; text-align:center; line-height:1.1; opacity:0; transition:2s; z-index:5;">LOVE<br>YOU.</div>
</div>

<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
const surpriseBox=document.getElementById('surpriseBox');
const finalText=document.getElementById('finalText');
canvas.width=600; canvas.height=780;

function playSurpriseSound(){
  const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  const now = audioCtx.currentTime;
  // suara surprise TING! naik
  [440, 660, 880].forEach((freq, idx)=>{
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.frequency.value=freq; o.type='sine';
    o.connect(g); g.connect(audioCtx.destination);
    o.start(now + idx*0.12);
    g.gain.setValueAtTime(0, now + idx*0.12);
    g.gain.linearRampToValueAtTime(0.4, now + idx*0.12 + 0.05);
    g.gain.exponentialRampToValueAtTime(0.01, now + idx*0.12 + 0.6);
    o.stop(now + idx*0.12 + 0.6);
  });
}

let pts=[];
for(let t=0; t<Math.PI*2; t+=0.07){
  let x=16*Math.pow(Math.sin(t),3);
  let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t));
  pts.push({x,y});
}

function startHeart(){
  let i=0; let scale=15;
  function draw(){
    if(i>=pts.length){ finalText.style.opacity=1; return; }
    let p=pts[i];
    let cx=canvas.width/2 + p.x*scale;
    let cy=canvas.height/2 + p.y*scale;
    ctx.fillStyle="#ff2a5e";
    ctx.font="bold 9px Courier New";
    ctx.textAlign="center";
    ctx.fillText("I LOVE YOU", cx, cy);
    i++;
    setTimeout(draw, 90);
  }
  draw();
}

document.getElementById('startBtn').onclick = ()=>{
  playSurpriseSound();
  surpriseBox.style.transition="0.8s";
  surpriseBox.style.opacity=0;
  surpriseBox.style.transform="scale(1.5)";
  setTimeout(()=>{ surpriseBox.style.display="none"; startHeart(); }, 800);
};
</script>
""", height=800)
