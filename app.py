import streamlit as st
import datetime
from PIL import Image

# Pengaturan Halaman
st.set_page_config(page_title="Memori Kita", page_icon="💖")

# Kode untuk mengubah warna latar belakang & desain pesan
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5;
    }
    .farewell-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #6B7280;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Simpan status login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. Jika BELUM login, tampilkan form login saja
if not st.session_state.logged_in:
    st.title("💖 PERJALANAN CINTA KURCACIII UNTUK ABULLL 💖")
    st.markdown("<h3 style='text-align: center; color: #D81B60;'>✨ ✨ ✨ ✨ ✨ ✨ ✨</h3>", unsafe_allow_html=True)
    st.markdown("<marquee style='color: #D81B60; font-weight: bold;'>I Love You More Than Yesterday... and I Will Love You More Tomorrow...</marquee>", unsafe_allow_html=True)
    st.write("Special for you.")

    password = st.text_input("Masukkan tanggal jadian kita (DDMMYY) untuk masuk:", type="password")
    
    if st.button("Masuk"):
        if password == "080625":
            st.session_state.logged_in = True
            st.rerun()  # Refresh halaman agar langsung masuk ke konten utama
        else:
            st.warning("Eits, masa lupa? coba diingat lagi yaa.")

# 3. Jika SUDAH login, tampilkan seluruh isi web & game kamu
else:
    st.success("Akses diterimaaaa! Halooo Gantengggg 💖")

    # Mengatur selisih waktu (WIB adalah UTC+7)
    jam_utc = datetime.datetime.now().hour
    jam_wib = (jam_utc + 7) % 24

    if 4 <= jam_wib < 11:
        ucapan = "Selamat Pagi sayanggg, Semangat Hari Ininya! 🌞"
    elif 11 <= jam_wib < 15:
        ucapan = "Selamat Sianggg sayanggg, Jangan Lupa Mammm Yaaaa! 🍱"
    elif 15 <= jam_wib < 18:
        ucapan = "Selamat Soreee sayanggg, Mandi gihhh biar seger! ☕"
    else:
        ucapan = "Selamat Malammm sayanggg, Bobooo Yang Nyenyak Yaaaa! ✨"

    st.write(f"### {ucapan}")
    st.divider()

    # --- FOTO 1 ---
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            img1 = Image.open("foto1.jpg")
            st.image(img1, use_container_width=True)
        except:
            st.error("Foto 1 gak ketemu, cek lagi namanya ya!")

    with col2:
        st.subheader("Momen Berharga")
        st.write("Ini kita habis kejar-kejaran sampe capeee, bahagiaaa bangettt waktu ituuu. Di sini aku sadar kalo cuma kamu yang bisa bikin bahagia!")

        # Game: Tangkap Sayang
        st.subheader("🎯 Game: Tangkap Sayangkuuuu")
        if "count" not in st.session_state:
            st.session_state.count = 0

        if st.button("Klik di sini kalau kamu sayang aku!"):
            st.session_state.count += 1
            st.balloons()
            st.write(f"Wah, kamu udah klik sebanyak **{st.session_state.count}** kali! Semangat banget sayangnya! 😄")

    st.divider()

    # --- FOTO 2 ---
    col3, col4 = st.columns([1, 1])
    with col3:
        st.subheader("Momen Manis Lainnya")
        st.write("Kalo yang ini kita habis hujan-hujanan naik motor keliling kota solo. Tau ga sayang? itu first experience aku keliling hujan-hujanan naik motor bareng cowokk hehe.")

    with col4:
        try:
            img2 = Image.open("foto2.jpg")
            st.image(img2, use_container_width=True)
        except:
            st.error("Foto 2 gak ketemu, pastikan ada file foto2.jpg di folder")

    st.divider()

    # --- TABS KENAPA AKU SAYANG ---
    st.subheader("💡 Kenapa aku sayang Abull1?")
    tab1, tab2, tab3 = st.tabs(["Sifatmu", "Sikapmu", "Random"])

    with tab1:
        st.write("✨ **Sabar:** Makasiii yaaa udah sabar banget ngadepin mood aku yang naik turun.")
    with tab2:
        st.write("🍰 **Gentleman:** Aku sukaa liat kamu berusaha berubah sayanggg, semangattt yaa berubah jadi lebih baiknyaaa.")
    with tab3:
        st.write("💖 **Nyaman:** Cuma sama kamu aku bisa jadi diriku sendiri yang paling aneh tanpa takut dinilai.")

    st.divider()

    # --- VIDEO ---
    st.subheader("🎬 Video Kita")
    
    # Video 1
    try:
        st.video("video_kita.mp4")
        st.write("Video ini spesial banget menurutku, karena disini aku cantikkk bangettt hehe, ahh jadi maluuu.")
    except:
        st.error("Video gak ketemu, pastikan namanya video_kita.mp4")

    # Video Tambahan (Video 3, 4, 5 jika ada)
    for v_name in ["video_kita3.mp4", "video_kita4.mp4", "video_kita5.mp4"]:
        try:
            st.video(v_name)
        except:
            pass

    st.divider()

    # --- TOMBOL KEJUTAN & LOVE METER ---
    if st.button("Klik kalau kamu sayang akuuu"):
        st.balloons()
        st.snow()
        st.success("I LOVE YOUU ABULLL! KAPAN NIKAHIN AKU NIH?? 💖✨")

    st.divider()

    st.subheader("📊 Love Meter")
    love_score = st.slider("Seberapa sayang kamu sama aku hari ini?", 0, 100, 80)

    if love_score > 90:
        st.success(f"Wah, {love_score}%! Aku jauh lebih sayang kamu! 💖")
    elif love_score > 50:
        st.info(f"Cuma {love_score}%? Tambahin lagi dong! 😏")
    else:
        st.warning("Kok dikit banget? Sini aku manjain dulu biar naik! 😜")

    st.divider()

    # --- KOTAK CATATAN HARAPAN ---
    with st.expander("✨ Harapan Aku Buat Kita"):
        st.write("""
        - Semoga kita makin sabar satu sama lain.
        - Semoga makin banyak tempat yang kita kunjungi bareng.
        - Dan semoga 'kapan nikah'-nya segera terwujud! Amin. 🤲
        """)

    # --- PESAN PERPISAHAN (BAGIAN PALING BAWAH) ---
    st.subheader("🕊️ Catatan Terakhir")
    
    st.markdown("""
    <div class='farewell-box'>
        <h3>Untuk Abull,</h3>
        <p>Terima kasih ya sudah menyempatkan waktu untuk melihat kembali semua kenangan dan momen manis yang pernah kita lewati di atas.</p>
        <p>Setiap perjalanan pasti ada babak akhirnya, dan cerita kita ternyata harus berhenti di sini. Aku menulis ini tanpa rasa benci, melainkan dengan rasa terima kasih yang tulus. Terima kasih sudah pernah hadir dan memberi banyak pelajaran berharga.</p>
        <p>Semoga di langkah selanjutnya, kamu selalu dikelilingi kebahagiaan dan bisa mencapai semua hal yang kamu impikan. Sukses dan bahagia selalu ya, Abull.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Klik untuk pesan penutup"):
        st.write("""
        Maaf ya kalau selama kita bersama ada kata atau perbuatanku yang pernah melukai hatimu. 
        Jaga diri baik-baik ya di sana.
        
        *Pamit,*  
        **Aku**
        """)

    st.caption("✨ *Setiap akhir adalah awal yang baru di tempat lain.*")

    # Sidebar Logout
    if st.sidebar.button("Keluar / Logout"):
        st.session_state.logged_in = False
        st.rerun()
