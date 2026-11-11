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
<div id="click"><span>KLIK UNTUK MULAI</span></div>
<canvas id="c"></canvas>
<script>
const canvas=document.getElementById('c'), ctx=canvas.getContext('2d');
let W,H;
function resize(){W=canvas.width=innerWidth;H=canvas.height=innerHeight}
resize(); addEventListener('resize',resize);

let drops=[];
for(let i=0;i<Math.floor(innerWidth/16);i++) drops[i]=Math.random()*-50;
const chars="ILOVEYOU".split("");
function drawMatrix(){
  ctx.fillStyle="rgba(0,0,0,0.12)";
  ctx.fillRect(0,0,W,H);
  ctx.font="14px monospace";
  for(let i=0;i<drops.length;i++){
    ctx.fillStyle="rgba(255,255,255,0.35)";
    ctx.fillText(chars[Math.floor(Math.random()*chars.length)],i*16,drops[i]*16);
    if(drops[i]*16>H && Math.random()>0.975) drops[i]=0;
    drops[i]++;
  }
}

let particles=[], state="IDLE", textOpacity=0;
class Particle{
  constructor(tx,ty){
    this.x=Math.random()*W; this.y=Math.random()*H;
    this.tx=tx; this.ty=ty;
    this.vx=(Math.random()-0.5)*12; this.vy=(Math.random()-0.5)*12;
    this.size=Math.random()*2+1;
  }
  update(){
    if(state==="EXPLODE"){ this.x+=this.vx; this.y+=this.vy; this.vx*=0.98; this.vy*=0.98; return; }
    this.x+=(this.tx-this.x)*0.08; this.y+=(this.ty-this.y)*0.08;
  }
  draw(){
    ctx.fillStyle="#fff";
    ctx.beginPath(); ctx.arc(this.x,this.y,this.size,0,Math.PI*2); ctx.fill();
  }
}
function getPoints(text, fs){
  const off=document.createElement('canvas'); off.width=W; off.height=H;
  const octx=off.getContext('2d');
  octx.fillStyle="#fff"; octx.font="900 "+fs+"px Arial";
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
  const pts=getPoints(text, Math.min(W/3.5, 220));
  particles=[]; pts.forEach(p=>particles.push(new Particle(p[0],p[1])));
  state="FORM";
}
function setHeart(){
  const pts=[];
  for(let t=0;t<Math.PI*2;t+=0.02){
    const x=16*Math.pow(Math.sin(t),3);
    const y=13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t);
    pts.push([W/2 + x*(Math.min(W,H)/32), H/2 - y*(Math.min(W,H)/32)]);
  }
  for(let i=0;i<800;i++){
    const t=Math.random()*Math.PI*2, r=Math.random();
    const x=16*Math.pow(Math.sin(t),3)*r;
    const y=(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))*r;
    pts.push([W/2 + x*(Math.min(W,H)/32), H/2 - y*(Math.min(W,H)/32)]);
  }
  particles=[]; pts.forEach(p=>particles.push(new Particle(p[0],p[1])));
  state="FORM";
}
function explode(){ state="EXPLODE"; setTimeout(()=>{state="IDLE"},900); }
const sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
async function start(){
  document.getElementById('click').style.display='none';
  for(const txt of ["3","2","1"]){ setText(txt); await sleep(1300); explode(); await sleep(700); }
  for(const word of ["You","Are","My","Love"]){ setText(word); await sleep(1800); explode(); await sleep(600); }
  setHeart();
  setTimeout(()=>{ state="FINAL_HEART"; },1500);
}
function draw(){
  drawMatrix();
  if(state==="FORM" || state==="EXPLODE" || state==="FINAL_HEART"){
    particles.forEach(p=>{p.update(); p.draw();});
  }
  if(state==="FINAL_HEART"){
    if(textOpacity<1) textOpacity+=0.01;
    ctx.font="bold "+Math.min(W/22,28)+"px Arial";
    ctx.textAlign="center"; ctx.textBaseline="middle";
    ctx.fillStyle="rgba(255,255,255,"+textOpacity+")";
    ctx.fillText("I LOVE YOU SAYANG", W/2, H/2);
  }
  requestAnimationFrame(draw);
}
draw();
document.getElementById('click').addEventListener('click', start);
</script>
</body>
</html>
