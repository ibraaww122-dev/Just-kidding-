import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LOVE YOU ❤️", page_icon="❤️", layout="centered")
st.markdown("<style>.stApp{background:black;} header,footer{visibility:hidden;}</style>", unsafe_allow_html=True)

components.html("""
<div style="background:black; width:100%; height:750px; position:relative;">
  <canvas id="c" style="width:100%; height:100%;"></canvas>
  <div style="position:absolute; top:60%; left:50%; transform:translate(-50%,-50%); color:#fff8dc; font-family:Georgia, serif; font-weight:bold; font-size:28px; text-align:center; line-height:1.1;">LOVE<br>YOU.</div>
</div>
<script>
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
canvas.width=600;
canvas.height=750;

let pts=[];
for(let t=0; t<Math.PI*2; t+=0.07){
  let x=16*Math.pow(Math.sin(t),3);
  let y=-(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t));
  pts.push({x,y});
}

let i=0;
let scale=15;

function draw(){
  if(i>=pts.length) return;
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
</script>
""", height=770)
