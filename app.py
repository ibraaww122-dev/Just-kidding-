import streamlit as st

st.set_page_config(page_title="LOVE YOU ❤️", page_icon="❤️", layout="centered")

st.markdown("""
<style>
body { background-color: black; }
.heart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  flex-direction: column;
}
.heart {
  width: 250px;
  height: 250px;
  position: relative;
  animation: heartbeat 1s infinite;
}
.heart::before, .heart::after {
  content: "";
  width: 130px;
  height: 200px;
  position: absolute;
  border: 3px solid #ff4b6e;
  border-radius: 130px 130px 0 0;
  background: transparent;
}
.heart::before {
  left: 120px;
  transform: rotate(-45deg);
  transform-origin: 0 100%;
}
.heart::after {
  left: 0px;
  transform: rotate(45deg);
  transform-origin: 100% 100%;
}
.text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -20%);
  color: white;
  font-size: 28px;
  font-weight: bold;
  z-index: 10;
  letter-spacing: 2px;
}
@keyframes heartbeat {
  0% { transform: scale(1); }
  15% { transform: scale(1.15); }
  30% { transform: scale(1); }
  45% { transform: scale(1.15); }
  60% { transform: scale(1); }
}
</style>

<div class="heart-container">
  <div class="heart">
    <div class="text">LOVE YOU.</div>
  </div>
  <p style="color: gray; margin-top: 40px;">Sentuh hatinya ✨</p>
</div>
""", unsafe_allow_html=True)
