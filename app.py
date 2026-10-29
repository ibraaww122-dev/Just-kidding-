import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# Pengaturan halaman agar pas di layar HP
st.set_page_config(page_title="LOVE YOU ❤️", layout="centered")

# Efek kejutan balon saat web dibuka di HP dia
st.balloons()

# Judul Website Romantis
st.markdown("<h2 style='text-align: center; color: #ff1744;'>Sebuah Kejutan Untukmu ❤️</h2>", unsafe_allow_html=True)
st.write("")

# Membuat data koordinat hati (Heart Curve) sesuai rumus kodemu
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Membuat grafik interaktif yang estetik di HP
fig = go.Figure()

# Menambahkan teks utama "LOVE YOU" di tengah-tengah hati
fig.add_annotation(
    x=0, y=0,
    text="LOVE YOU.",
    showarrow=False,
    font=dict(size=24, color="white", family="Georgia"),
)

# Menggambar garis hati berwarna pink neon
fig.add_trace(go.Scatter(
    x=x, y=y, 
    mode='lines', 
    line=dict(color='#ff477e', width=3.5),
    hoverinfo='skip'
))

# Mengatur tampilan background menjadi hitam pekat (sesuai tema awalmu)
fig.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    xaxis=dict(visible=False, range=[-20, 20]),
    yaxis=dict(visible=False, range=[-18, 18]),
    margin=dict(l=10, r=10, t=10, b=10),
    showlegend=False,
    height=450,
)

# Menampilkan grafik hati di layar HP nya
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# Pesan penutup di bawah gambar hati
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>Sentuh atau cubit (zoom) hatinya untuk melihat lebih dekat ✨</p>", unsafe_allow_html=True)
