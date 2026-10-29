import streamlit as st

st.set_page_config(page_title="LOVE YOU ❤️", page_icon="❤️", layout="centered")

st.markdown("""
<style>
.stApp { background-color: black !important; }
header, footer { visibility: hidden; }
</style>

<canvas id="canvas" style="width:100%; height:85vh; background:black; display:block;"></canvas>
<div id="love" style="position:fixed; top:52%; left:50%; transform:translate(-50%,-50%); color:white; font-family: 'Times New Roman', serif; font-size: 28px; letter-spacing: 2px; opacity:0; transition: opacity 2s;">LOVE YOU.</div>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight * 0.85;

let points = [];
for(let t=0; t<Math.PI*2; t+=0.01){
  let x = 16 * Math.pow(Math.sin(t), 3);
  let y = -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t));
  points.push({x,y});
}

let idx = 0;
let scale = Math.min(canvas.width, canvas.height) / 35;

function draw(){
  if(idx >= points.length){
    document.getElementById('love').style.opacity = '1';
    return;
  }
  ctx.fillStyle = 'black';
  if(idx==0) ctx.fillRect(0,0,canvas.width,canvas.height);
  
  let p = points[idx];
  let cx = canvas.width/2 + p.x * scale;
  let cy = canvas.height/2 + p.y * scale - 40;
  
  ctx.beginPath();
  ctx.arc(cx, cy, 3.5, 0, Math.PI*2);
  ctx.fillStyle = '#ff0015';
  ctx.shadowColor = '#ff0015';
  ctx.shadowBlur = 15;
  ctx.fill();
  
  // glow trail
  ctx.beginPath();
  ctx.arc(cx, cy, 1.5, 0, Math.PI*2);
  ctx.fillStyle = '#ff8a9a';
  ctx.fill();

  idx += 2;
  requestAnimationFrame(draw);
}
draw();

window.onresize = () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight * 0.85;
  scale = Math.min(canvas.width, canvas.height) / 35;
}
</script>
""", unsafe_allow_html=True)
