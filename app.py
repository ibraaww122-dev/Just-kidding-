import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LOVE YOU ❤️", page_icon="❤️", layout="centered")

# Sembunyiin menu streamlit biar full hitam
st.markdown("<style>header, footer, .stAppDeployButton {visibility:hidden;} .stApp {background:black;}</style>", unsafe_allow_html=True)

components.html(
"""
<div style="background:black; width:100%; height:600px; position:relative; overflow:hidden;">
  <canvas id="c" style="width:100%; height:100%;"></canvas>
  <div id="txt" style="position:absolute; top:55%; left:50%; transform:translate(-50%,-50%); color:white; font-size:30px; font-family:serif; opacity:0; transition:2s;">LOVE YOU.</div>
</div>
<script>
  const c = document.getElementById('c');
  const ctx = c.getContext('2d');
  const txt = document.getElementById('txt');
  
  function setup(){
    c.width = c.clientWidth * 2;
    c.height = c.clientHeight * 2;
  }
  setup();
  
  let pts=[];
  for(let t=0; t<6.28; t+=0.01){
    let x = 16*Math.pow(Math.sin(t),3);
    let y = 13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t);
    pts.push([x,-y]);
  }
  
  let i=0;
  function anim(){
    if(i>=pts.length){ txt.style.opacity=1; return; }
    
    let scale = Math.min(c.width, c.height) / 40;
    let x = c.width/2 + pts[i][0]*scale;
    let y = c.height/2 + pts[i][1]*scale - 50;
    
    ctx.fillStyle = "#ff0033";
    ctx.shadowBlur = 20;
    ctx.shadowColor = "#ff0033";
    ctx.beginPath();
    ctx.arc(x, y, 6, 0, Math.PI*2);
    ctx.fill();
    
    i++;
    requestAnimationFrame(anim);
  }
  anim();
</script>
""",
height=620
)
