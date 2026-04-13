# 🏛️ Asisten Virtual DPD RI Jawa Barat

Chatbot pintar berbasis AI yang dirancang untuk membantu warga Jawa Barat mendapatkan informasi seputar tugas, wewenang, dan profil anggota DPD RI perwakilan Jawa Barat periode 2024-2029 secara interaktif.

## ✨ Fitur Utama
- **🤖 AI-Powered Chat**: Menggunakan model bahasa mutakhir via OpenRouter (Llama 3/DeepSeek) untuk menjawab pertanyaan warga secara alami.
- **📍 Cek Isu Wilayah**: Fitur khusus untuk melihat isu utama di 27 Kota/Kabupaten di Jawa Barat.
- **📚 Knowledge Base JSON**: Seluruh data informasi DPD tersentralisasi dalam file `data_faq.json` yang mudah diperbarui.
- **📱 Responsive UI**: Tampilan bersih dan modern menggunakan Streamlit, lengkap dengan pintasan pertanyaan populer.
- **🔗 Social Connect**: Akses cepat ke media sosial resmi DPD RI Jawa Barat melalui ikon SVG yang estetik.

## 🛠️ Tech Stack
- **Bahasa Pemrograman**: Python
- **Framework UI**: [Streamlit](https://streamlit.io/)
- **AI Engine**: [OpenRouter API](https://openrouter.ai/) (Format OpenAI)
- **Data Store**: JSON

## 🚀 Cara Menjalankan Secara Lokal

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username-kamu/chatbot-dpd-jabar.git](https://github.com/username-kamu/chatbot-dpd-jabar.git)
   cd chatbot-dpd-jabar

2. **Instalasi Library**
   Pastikan kamu sudah menginstal Python, lalu jalankan:
   ```pip install -r requirements.txt```
   
3. **Setting API Key**
   Buat folder ```.streamlit``` dan file ```secrets.toml``` di dalamnya:
   ```OPENROUTER_API_KEY = "your_api_key_here"```

4. **Jalankan Aplikasi**
   ```streamlit run app.py```
   ```pyhton -m streamlit run app.py```

## 🌐 Deployment
   Aplikasi ini dioptimalkan untuk di-deploy melalui Streamlit Cloud. Jangan lupa untuk memasukkan ```OPENROUTER_API_KEY``` pada bagian Advanced Settings > Secrets di dashboard Streamlit Cloud.

## 📁 Struktur File
- ``app.py``: Logika utama aplikasi dan antarmuka chat.
- ``data_faq.json``: Basis data pengetahuan seputar DPD Jabar.
- ``requirements.txt``: Daftar library Python yang dibutuhkan.

🚀 Developed with ❤️ by **Protosaurus**
