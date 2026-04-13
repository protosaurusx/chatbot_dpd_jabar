import streamlit as st
from openai import OpenAI
import json
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Asisten Virtual DPD RI Jabar", page_icon="🏛️", layout="centered")

# --- 2. STYLE CSS CUSTOM (Watermark & Layout) ---

st.markdown("""
    <style>
    /* Style untuk watermark - Diangkat ke 20px agar tidak terlalu mentok */
    .footer {
        position: fixed;
        left: 0;
        bottom: 20px; 
        width: 100%;
        background-color: transparent;
        color: #a0a0a0;
        text-align: center;
        font-size: 11px;
        z-index: 999;
        letter-spacing: 0.5px;
    }
    
    /* Jarak agar chat tidak tertutup watermark/input */
    .main .block-container {
        padding-bottom: 7rem;
    }
    
    .stChatInput {
        margin-bottom: 10px;
    }
    </style>
    <div class="footer">
        🚀 DPD RI Jabar Digital Assistant | <b>Made with ❤️ by Protosaurus</b>
    </div>
    """, unsafe_allow_html=True)

# --- 3. KONEKSI KE OPENROUTER ---
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"],
    )
except KeyError:
    st.error("⚠️ API Key OpenRouter belum disetting di file secrets.toml.")
    st.stop()

# --- 4. LOAD DATA JSON ---
@st.cache_data
def load_data():
    if os.path.exists('data_faq.json'):
        with open('data_faq.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

faq_data = load_data()

# Mengambil daftar wilayah untuk selectbox
wilayah_list = ["-- Pilih Wilayah Anda --"]
for item in faq_data.get("faq_dpd_jabar", []):
    if item.get("kategori") == "wilayah_jabar":
        wilayah_list.extend([w["nama"] for w in item["daftar_wilayah"]])

# --- 5. INSTRUKSI SISTEM (Sesuai Permintaanmu) ---
SYSTEM_PROMPT = f"""
Kamu adalah 'Asisten Virtual Resmi DPD RI Perwakilan Jawa Barat'.
Tugas tunggalmu adalah memberikan informasi seputar DPD RI, anggota dari Jawa Barat, dan layanan aspirasi.

1. Gunakan data ini: {json.dumps(faq_data)} untuk menjawab pertanyaan pengguna.
2. Jawablah dengan ramah, informatif, dan gunakan sedikit sentuhan bahasa Sunda yang sopan (misal: Wilujeng sumping, Hatur nuhun, Muhun).
3. JIKA pengguna bertanya hal di luar konteks DPD atau Jawa Barat (misalnya: resep makanan, game, coding, gosip), TOLAK DENGAN HALUS dan arahkan kembali ke topik DPD Jabar.
4. Nasihati User jika ada indikasi Rasis atau menghina suatu ras suku agama atau budaya. Bahasa yang digunakan tidak boleh kasar atau yang mengarah pada perpecahan.
5. Jika User bertanya tentang kabar mereka, tanyakan kembali dengan empati karena khawatir mereka mengalami hal yang kurang mengenakkan.
6. JIKA User 'mengaku-ngaku' (halusinasi identitas), nasehati mereka supaya tidak halu secara halus.
"""

# --- 6. ASET SVG ---
ig_svg = """<a href="https://instagram.com/dpdrijabar" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#FFFF" viewBox="0 0 640 640"><path d="M320.3 205C256.8 204.8 205.2 256.2 205 319.7C204.8 383.2 256.2 434.8 319.7 435C383.2 435.2 434.8 383.8 435 320.3C435.2 256.8 383.8 205.2 320.3 205zM319.7 245.4C360.9 245.2 394.4 278.5 394.6 319.7C394.8 360.9 361.5 394.4 320.3 394.6C279.1 394.8 245.6 361.5 245.4 320.3C245.2 279.1 278.5 245.6 319.7 245.4zM413.1 200.3C413.1 185.5 425.1 173.5 439.9 173.5C454.7 173.5 466.7 185.5 466.7 200.3C466.7 215.1 454.7 227.1 439.9 227.1C425.1 227.1 413.1 215.1 413.1 200.3zM542.8 227.5C541.1 191.6 532.9 159.8 506.6 133.6C480.4 107.4 448.6 99.2 412.7 97.4C375.7 95.3 264.8 95.3 227.8 97.4C192 99.1 160.2 107.3 133.9 133.5C107.6 159.7 99.5 191.5 97.7 227.4C95.6 264.4 95.6 375.3 97.7 412.3C99.4 448.2 107.6 480 133.9 506.2C160.2 532.4 191.9 540.6 227.8 542.4C264.8 544.5 375.7 544.5 412.7 542.4C448.6 540.7 480.4 532.5 506.6 506.2C532.8 480 541 448.2 542.8 412.3C544.9 375.3 544.9 264.5 542.8 227.5zM495 452C487.2 471.6 472.1 486.7 452.4 494.6C422.9 506.3 352.9 503.6 320.3 503.6C287.7 503.6 217.6 506.2 188.2 494.6C168.6 486.8 153.5 471.7 145.6 452C133.9 422.5 136.6 352.5 136.6 319.9C136.6 287.3 134 217.2 145.6 187.8C153.4 168.2 168.5 153.1 188.2 145.2C217.7 133.5 287.7 136.2 320.3 136.2C352.9 136.2 423 133.6 452.4 145.2C472 153 487.1 168.1 495 187.8C506.7 217.3 504 287.3 504 319.9C504 352.5 506.7 422.6 495 452z"/></svg></a>"""
fb_svg = """<a href="https://facebook.com/dpdri" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#FFFF" viewBox="0 0 640 640"><path d="M576 320C576 178.6 461.4 64 320 64C178.6 64 64 178.6 64 320C64 440 146.7 540.8 258.2 568.5L258.2 398.2L205.4 398.2L205.4 320L258.2 320L258.2 286.3C258.2 199.2 297.6 158.8 383.2 158.8C399.4 158.8 427.4 162 438.9 165.2L438.9 236C432.9 235.4 422.4 235 409.3 235C367.3 235 351.1 250.9 351.1 292.2L351.1 320L434.7 320L420.3 398.2L351 398.2L351 574.1C477.8 558.8 576 450.9 576 320z"/></svg></a>""" 
x_svg = """<a href="https://x.com/dpdri" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#FFFF" viewBox="0 0 640 640"><path d="M453.2 112L523.8 112L369.6 288.2L551 528L409 528L297.7 382.6L170.5 528L99.8 528L264.7 339.5L90.8 112L236.4 112L336.9 244.9L453.2 112zM428.4 485.8L467.5 485.8L215.1 152L173.1 152L428.4 485.8z"/></svg></a>"""
yt_svg = """<a href="https://youtube.com/dpdrichannel" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#FFFF" viewBox="0 0 640 640"><path d="M581.7 188.1C575.5 164.4 556.9 145.8 533.4 139.5C490.9 128 320.1 128 320.1 128C320.1 128 149.3 128 106.7 139.5C83.2 145.8 64.7 164.4 58.4 188.1C47 231 47 320.4 47 320.4C47 320.4 47 409.8 58.4 452.7C64.7 476.3 83.2 494.2 106.7 500.5C149.3 512 320.1 512 320.1 512C320.1 512 490.9 512 533.5 500.5C557 494.2 575.5 476.3 581.8 452.7C593.2 409.8 593.2 320.4 593.2 320.4C593.2 320.4 593.2 231 581.8 188.1zM264.2 401.6L264.2 239.2L406.9 320.4L264.2 401.6z"/></svg></a>"""
web_svg = """<a href="https://jabar.dpd.go.id" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#FFFF" viewBox="0 0 640 640"><path d="M415.9 344L225 344C227.9 408.5 242.2 467.9 262.5 511.4C273.9 535.9 286.2 553.2 297.6 563.8C308.8 574.3 316.5 576 320.5 576C324.5 576 332.2 574.3 343.4 563.8C354.8 553.2 367.1 535.8 378.5 511.4C398.8 467.9 413.1 408.5 416 344zM224.9 296L415.8 296C413 231.5 398.7 172.1 378.4 128.6C367 104.2 354.7 86.8 343.3 76.2C332.1 65.7 324.4 64 320.4 64C316.4 64 308.7 65.7 297.5 76.2C286.1 86.8 273.8 104.2 262.4 128.6C242.1 172.1 227.8 231.5 224.9 296zM176.9 296C180.4 210.4 202.5 130.9 234.8 78.7C142.7 111.3 74.9 195.2 65.5 296L176.9 296zM65.5 344C74.9 444.8 142.7 528.7 234.8 561.3C202.5 509.1 180.4 429.6 176.9 344L65.5 344zM463.9 344C460.4 429.6 438.3 509.1 406 561.3C498.1 528.6 565.9 444.8 575.3 344L463.9 344zM575.3 296C565.9 195.2 498.1 111.3 406 78.7C438.3 130.9 460.4 210.4 463.9 296L575.3 296z"/></svg></a>"""

vertical_icons_html = f'''
<div style="display: flex; flex-direction: row; gap: 15px; align-items: center; justify-content: center; margin-bottom: 20px;">
    {web_svg}{ig_svg}{fb_svg}{x_svg}{yt_svg}
</div>
'''

# --- 7. TAMPILAN UTAMA ---
col_judul1, col_judul2 = st.columns([1, 5], vertical_alignment="center")
with col_judul1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("https://jabar.dpd.go.id/images/logo.png", width=100) 
with col_judul2:
    st.markdown("<h1 style='text-align: left; margin: 0;'>Asisten Virtual DPD RI Jabar</h1>", unsafe_allow_html=True)

st.markdown("Wilujeng sumping! Saya siap menjawab pertanyaan Anda seputar wakil daerah dan tugas DPD RI Jawa Barat.")

# --- 8. SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="display: flex; justify-content: center;"><img src="https://jabar.dpd.go.id/images/logo.png" width="150"></div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Menu Layanan</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<p style='text-align: center; font-weight: bold;'>Kontak & Media Sosial Resmi</p>", unsafe_allow_html=True)
    st.markdown(vertical_icons_html, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📍 Cek Isu Wilayah")
    pilihan_wilayah = st.selectbox("Pilih Kota/Kabupaten Anda di Jabar:", options=wilayah_list)

    info_wilayah = ""
    if pilihan_wilayah != "-- Pilih Wilayah Anda --":
        for item in faq_data.get("faq_dpd_jabar", []):
            if item.get("kategori") == "wilayah_jabar":
                for w in item["daftar_wilayah"]:
                    if w["nama"] == pilihan_wilayah:
                        info_wilayah = w["isu"]
        st.info(f"**Isu di {pilihan_wilayah}:**\n{info_wilayah}")
    
    if st.button("🗑️ Hapus Riwayat Percakapan", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- 9. MANAJEMEN RIWAYAT PESAN ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 10. TOMBOL PERTANYAAN CEPAT ---
st.markdown("<br>💡 **Coba tanyakan ini:**", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns(3)
pertanyaan_cepat = None

with col_btn1:
    if st.button("👥 Siapa Anggota Jabar?", use_container_width=True): pertanyaan_cepat = "Siapa saja anggota DPD RI dari Jawa Barat?"
with col_btn2:
    if st.button("🏛️ Apa Tugas DPD?", use_container_width=True): pertanyaan_cepat = "Apa tugas utama dari DPD RI?"
with col_btn3:
    if st.button("📢 Lapor Aspirasi", use_container_width=True): pertanyaan_cepat = "Bagaimana cara mengirimkan aspirasi ke DPD?"

# --- 11. LOGIKA CHAT & OPENROUTER ---
ketikan_user = st.chat_input("Tanyakan apa saja mengenai DPD...")
prompt = ketikan_user or pertanyaan_cepat

# Gabungkan instruksi dasar dengan konteks wilayah
konteks_wilayah = ""
if pilihan_wilayah != "-- Pilih Wilayah Anda --":
    konteks_wilayah = f"\nUser saat ini sedang memfokuskan pembicaraan pada wilayah: {pilihan_wilayah}. Isu daerah: {info_wilayah}"

SYSTEM_PROMPT_FINAL = SYSTEM_PROMPT + konteks_wilayah

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("⏳ Antosan sakedap, asisten sedang mengetik..."):
            try:
                # Menggunakan OpenRouter API
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "http://https://chatbotdpdjabar.streamlit.app", # Penting untuk OpenRouter
                        "X-Title": "Chatbot DPD Jabar",
                    },
                    model="google/gemma-4-26b-a4b-it:free", # Model stabil di OpenRouter
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT_FINAL},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                    ],
                    temperature=0.3,
                )
                
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Hapunten, terjadi kesalahan teknis (OpenRouter): {e}")
                st.stop()
