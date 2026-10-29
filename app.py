import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LOVE YOU ❤️", page_icon="❤️", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:680px; position:relative;">
  <canvas id="c" style="width:100%; height:100%;"></canvas>
  <div style="position:absolute; top:58%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia, serif; font-weight:bold; font-size:24px; letter-spacing:1px;">LOVE YOU.</div>
</div>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
canvas.width = 800;
canvas.height = 680;

let points=[];
for(let t=0; t<Math.PI*2; t+=0.03){
  let x = 16*Math.pow(Math.sin(t),3);
  let y = -(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t));
  points.push({x,y});
}

let idx=0;
let scale=18;

function draw(){
  if(idx >= points.length) return;
  
  // gambar 2 lapis biar tebal kayak di video
  for(let k=0;k<2;k++){
    let p = points[idx];
    let offset = k*0.5;
    let cx = canvas.width/2 + (p.x+offset)*scale;
    let cy = canvas.height/2 + (p.y+offset)*scale - 20;
    
    ctx.fillStyle = k==0 ? "#ff0a4a" : "#ff5a8a";
    ctx.font = "bold 9px Arial";
    ctx.fillText("LOVE", cx, cy);
  }
  
  idx++;
  setTimeout(()=>requestAnimationFrame(draw), 20);
}
draw();
</script>
""", height=700)
