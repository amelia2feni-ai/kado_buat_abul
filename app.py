import streamlit as st
import datetime
# Kode untuk mengubah warna latar belakang
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
from PIL import Image

# Pengaturan halaman
st.set_page_config(page_title="Memori Kita", page_icon="❤️")

# --- JUDUL ---
st.title("❤️ PERJALANAN CINTA KURCACIII UNTUK ABULLL ❤️")
st.markdown("<h3 style='text-align: center; color: #D81B60;'>✨ ✨ ✨ ✨ ✨ ✨ ✨</h3>", unsafe_allow_html=True)

st.markdown("<marquee style='color: #D81B60; font-weight: bold;'>I Love You More Than Yesterday... and I Will Love You More Tomorrow...</marquee>", unsafe_allow_html=True)
st.write("Special for you.")

password = st.text_input("Masukkan tanggal jadian kita (DDMMYY) untuk masuk:", type="password")
tombol = st.button("Masuk")

if tombol:
    if password == "080625":
        st.success("Akses diterimaaaa! Halooo Gantengggg ❤️")
    
         # Mengatur selisih waktu (WIB adalah UTC+7)
        jam_utc = datetime.datetime.now().hour
        jam_wib = (jam_utc + 7) % 24

        if 4 <= jam_wib < 11:
            ucapan = "Selamat Pagi sayanggg, Semangat Hari Ininya! ☀️"
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
                st.write("Ini kita habis kejar-kejaran sampe capeee, bahagiaaa bangetttt waktu ituuu. Di sini aku sadar kalo cuma kamu yang bisa bikin aku bahagia dan bisa ketawa lepass.")

                    
        st.subheader("🎯 Game: Tangkap Sayangkuuuu")
        if "count" not in st.session_state:
                st.session_state.count = 0

        if st.button("Klik di sini kalau kamu sayang aku!"):
                st.session_state.count += 1
                st.balloons()
                st.write(f"Wah, kamu udah klik sebanyak {st.session_state.count} kali! Semangat banget sayangnya! 😂")
                        
        st.divider()

        # --- FOTO 2 ---
        col3, col4 = st.columns([1, 1])
        with col3:
                st.subheader("Momen Manis Lainnya")
                st.write("Kalo yang ini kita habis hujan-hujanan naik motor keliling kota solo. Tau ga sayang? itu first experience aku keliling kota solo dengan orang yang palingg spesialll. Makasiii yaa sayanggg udah mewarnaiii hidup akuuu.")

        with col4:
        try:
            # Pastikan kamu punya file bernama foto2.jpg di folder yang sama
            img2 = Image.open("foto2.jpg")
            st.image(img2, use_container_width=True)
        except:
            st.error("Foto 2 gak ketemu, pastikan ada file foto2.jpg di folder")


        st.divider()
        st.subheader("💡 Kenapa aku sayang Abulll?")

        tab1, tab2, tab3 = st.tabs(["Sifatmu", "Sikapmu", "Random"])

        with tab1:
                st.write("✨ **Sabar:** Makasiii yaaa udah sabar banget ngadepin mood aku yang naik turun.")
        with tab2:
                st.write("🍰 **Gentleman:** Aku sukaa liat kamu berusaha berubah sayanggg, semangattt yaa berubah jadi lebih baiknyaaa.")
                with tab3:
                st.write("💘 **Nyaman:** Cuma sama kamu aku bisa jadi diriku sendiri yang paling aneh tanpa takut dinilai.")

        st.divider()
        # --- VIDEO ---
        st.subheader("🎬 Video Kita")
        try:
            video_file = open("video_kita.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)
            st.write("Video random kitaa, aku sering liat video ini saat aku kangennnn, lucuu bangett kannn video kitaa? pastii lucuu dong hehe.")
        except:
            st.error("Video gak ketemu, pastikan namanya video_kita.mp4")

        st.divider()

        # --- TOMBOL KEJUTAN ---
        if st.button("Klik kalau kamu sayang akuuu"):
            st.balloons()
            st.snow()
            st.success("I LOVE YOUU ABULLLL! KAPAN NIKAHIN AKU NIH?? ❤️✨")

        st.divider()

        st.subheader("📊 Love Meter")
        love_score = st.slider("Seberapa sayang kamu sama aku hari ini?", 0, 100, 80)

        if love_score > 90:
            st.success(f"Wah, {love_score}%! Aku jauh lebih sayang kamu! ❤️")
        elif love_score > 50:
            st.info(f"Cuma {love_score}%? Tambahin lagi dong! 😋")
        else:
            st.warning("Kok dikit banget? Sini aku manjain dulu biar naik! 🥺") 

        # 2. Kotak Catatan Harapan (Expander)
        with st.expander("✨ Harapan Aku Buat Kita"):
            st.write("""
                - Semoga kita makin sabar satu sama lain.
                - Semoga makin banyak tempat yang kita kunjungi bareng.
                - Dan semoga 'kapan nikah'-nya segera terwujud! Amin. 🤲
                """)

        from datetime import date

        tgl_penting = date(2026, 6, 8) # Ganti ke tanggal anniversary atau ultahnya
        hari_ini = date.today()
        sisa_hari = (tgl_penting - hari_ini).days

        st.metric(label="Menuju Hari Spesial Kita", value=f"{sisa_hari} Hari Lagi")
                    
        #3. Footer Cantik di bawah
        st.markdown(
                            """
                            <br><br>
                            <div style="text-align: center; color: #D81B60; font-size: 12px;">
                                Made with ❤️ by Kurcaciii | 2026
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        else:
        st.warning("Eits, masa lupa? Coba diingat lagi yaa.")
