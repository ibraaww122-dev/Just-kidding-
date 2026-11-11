<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>I LOVE YOU SAYANG</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#000;overflow:hidden;font-family:Arial,sans-serif}
  canvas{position:fixed;inset:0;display:block}
  #click{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;z-index:10;cursor:pointer;background:#000;text-align:center;font-size:22px;letter-spacing:2px}
  #click span{border:1px solid #ff5da2;padding:16px 28px;border-radius:50px;box-shadow:0 0 30px #ff5da255}
</style>
</head>
<body>
<div id="click"><span>💖 KLIK UNTUK MULAI 💖</span></div>
<canvas id="c"></canvas>
<script>
const canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
let W,H;
function resize(){W=canvas.width=innerWidth;H=canvas.height=innerHeight}
resize(); addEventListener('resize',resize);

// ===== MATRIX RAIN BACKGROUND =====
const cols=Math.floor(innerWidth/16);
let drops=[];
for(let i=0;i<cols;i++) drops[i]=Math.random()*-50;
const chars="ILOVEYOU".split("");
function drawMatrix(){
  ctx.fillStyle="rgba(0,0,0,0.12)";
  ctx.fillRect(0,0,W,H);
  ctx.font="14px monospace";
  for(let i=0;i<drops.length;i++){
    const ch=chars[Math.floor(Math.random()*chars.length)];
    ctx.fillStyle="rgba(255,255,255,0.35)";
    ctx.fillText(ch,i*16,drops[i]*16);
    if(drops[i]*16>H && Math.random()>0.975) drops[i]=0;
    drops[i]++;
  }
}

// ===== PARTICLE TEXT =====
let particles=[], state="IDLE", finalHeart=false, textOpacity=0;
class Particle{
  constructor(tx,ty){
    this.x=Math.random()*W; this.y=Math.random()*H;
    this.tx=tx; this.ty=ty;
    this.vx=(Math.random()-0.5)*12; this.vy=(Math.random()-0.5)*12;
    this.size=Math.random()*2+1;
    this.active=true;
  }
  update(){
    if(state==="EXPLODE"){ this.x+=this.vx; this.y+=this.vy; this.vx*=0.98; this.vy*=0.98; return; }
    const dx=this.tx-this.x, dy=this.ty-this.y;
    this.x+=dx*0.08; this.y+=dy*0.08;
  }
  draw(){
    ctx.fillStyle="rgba(255,255,255,0.95)";
    ctx.beginPath(); ctx.arc(this.x,this.y,this.size,0,Math.PI*2); ctx.fill();
  }
}

function getPoints(text, fontSize){
  const off=document.createElement('canvas');
  off.width=W; off.height=H;
  const octx=off.getContext('2d');
  octx.fillStyle="#fff"; octx.font=`900 ${fontSize}px Arial`;
  octx.textAlign="center"; octx.textBaseline="middle";
  octx.fillText(text, W/2, H/2);
  const data=octx.getImageData(0,0,W,H).data;
  const pts=[];
  for(let y=0;y<H;y+=6) for(let x=0;x<W;x+=6){
    if(data[(y*W+x)*4+3]>128) pts.push([x,y]);
  }
  return pts;
}
function setText(text){
  const fs=Math.min(W/3.5, 220);
  const pts=getPoints(text, fs);
  particles=[];
  pts.forEach(p=>particles.push(new Particle(p[0],p[1])));
  state="FORM";
}
function getHeartPoints(){
  const pts=[];
  for(let t=0;t<Math.PI*2;t+=0.02){
    const x=16*Math.pow(Math.sin(t),3);
    const y=13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t);
    const sx=W/2 + x*(Math.min(W,H)/32);
    const sy=H/2 - y*(Math.min(W,H)/32);
    pts.push([sx,sy]);
  }
  // isi biar padat
  for(let i=0;i<800;i++){
    const t=Math.random()*Math.PI*2, r=Math.random();
    const x=16*Math.pow(Math.sin(t),3)*r;
    const y=(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))*r;
    pts.push([W/2 + x*(Math.min(W,H)/32), H/2 - y*(Math.min(W,H)/32)]);
  }
  return pts;
}
function setHeart(){
  const pts=getHeartPoints();
  particles=[];
  pts.forEach(p=>particles.push(new Particle(p[0],p[1])));
  state="FORM"; finalHeart=true;
}
function explode(){ state="EXPLODE"; setTimeout(()=>{state="IDLE";},900); }
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));

async function startSequence(){
  document.getElementById('click').style.display='none';
  for(const txt of ["3","2","1"]){
    setText(txt); await sleep(1300); explode(); await sleep(700);
  }
  for(const word of ["You","Are","My","Love"]){
    setText(word); await sleep(1800); explode(); await sleep(600);
  }
  setHeart();
  // tunggu hati terbentuk lalu muncul teks
  setTimeout(()=>{ state="FINAL_HEART"; }, 1500);
}

function drawFinalText(){
  if(textOpacity<1) textOpacity+=0.01;
  ctx.font=`bold ${Math.min(W/22,28)}px Arial`;
  ctx.textAlign="center"; ctx.textBaseline="middle";
  ctx.fillStyle=`rgba(255,255,255,${textOpacity})`;
  ctx.fillText("I LOVE YOU SAYANG ♥", W/2, H/2);
}

function draw(){
  drawMatrix();
  if(state==="FORM" || state==="EXPLODE" || state==="FINAL_HEART"){
    particles.forEach(p=>{p.update(); p.draw();});
  }
  if(state==="FINAL_HEART") drawFinalText();
  requestAnimationFrame(draw);
}
draw();
document.getElementById('click').addEventListener('click', startSequence);
</script>
</body>
</html>
