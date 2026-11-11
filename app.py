import streamlit as st

st.set_page_config(page_title="Top 5 Cutest Girls", layout="centered")

slides = [
    "Top 5\ncutest girls:",
    "1. always\nyou",
    "2. you",
    "3. literally\nyou",
    "4. still\nyou",
    "5. you ❤️",
]

if "i" not in st.session_state:
    st.session_state.i = 0

# Background pink + text gede
st.markdown("""
<style>
.stApp { background-color: #ff9ec4; }
.block-container { padding-top: 0 !important; }
h1 {
  text-align: center;
  font-size: 58px;
  color: black;
  margin-top: 120px;
  line-height: 1.1;
  white-space: pre-line;
}
div[data-testid="stButton"] > button {
  font-size: 30px;
  border-radius: 50px;
  width: 100%;
  background: white;
  border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<h1>{slides[st.session_state.i]}</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    if st.button("⬅️"):
        if st.session_state.i > 0:
            st.session_state.i -= 1
            st.rerun()
with c3:
    if st.button("➡️"):
        if st.session_state.i < len(slides)-1:
            st.session_state.i += 1
            st.rerun()

st.progress((st.session_state.i + 1) / len(slides))
st.markdown(f"<p style='text-align:center'>{st.session_state.i+1} / {len(slides)} - Klik ➡️ buat geser</p>", unsafe_allow_html=True)

if st.session_state.i == 5:
    st.balloons()
