import streamlit as st
import pandas as pd

# Inisialisasi session state untuk mengontrol tampilan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Halaman Home
def home_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Kebutuhan Gula Manusia Dalam Buah
        </h1>
        <h3 style='text-align: center; color: #5D6D7E;'>
            Solusi dalam kebutuhan gula buah yang harus dikonsumsi berdasarkan berat badan
        </h3>
        """,
        unsafe_allow_html=True
    )

    image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.liputan6.com%2Fcitizen6%2Fread%2F2848741%2Fwaspadai-7-buah-yang-memiliki-kandungan-gula-sangat-tinggi&psig=AOvVaw326pcQfBNYc1m54bZpWddr&ust=1737427123518000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLCh4ceig4sDFQAAAAAdAAAAABAE.jpg"
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{image_url}" style="width: 100%; max-width: 600px; border-radius: 15px; transition: transform 0.3s ease;" 
                 onmouseover="this.style.transform='scale(1.05)'" 
                 onmouseout="this.style.transform='scale(1)'">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <h2 style='text-align: center;'>
             Kelompok 4
        </h2>
        <p style='text-align: Left;'>
            Anggota: <br>
            - Arie Prasetyo Nugroho     (2350075) <br>
            - Hana Mahdiyyah            (2350096) <br>
            - Muhammad Ihya Ulumudin    (2350110) <br>
            - Shafa Noer Hafizhah       (2350134) <br>
            - Vinny Valvita BR Ketaren  (2350138) <br>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Penjelasan tentang berat badan dan gula buah"):
            st.session_state.page = "penjelasan"
    with col2:
        if st.button("Kalkulator kebutuhan gula dalam buah "):
            st.session_state.page = "kalkulator"
            
# Halaman Penjelasan Berat Badan dan Gula Buah
def penjelasan_bmi():
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Penjelasan tentang Berat Badan dan Gula Buah
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Garis Pemisah
    st.markdown("---")

    st.markdown(
        """
        ### Pengertian Gula
        Gula adalah salah satu sumber energi utama yang dibutuhkan tubuh untuk menjalankan berbagai fungsi vital, termasuk aktivitas otak, otot, dan organ lainnya. 
        Dalam bentuk glukosa, gula berperan penting dalam menjaga stamina dan metabolisme tubuh. WHO merekomendasikan konsumsi gula tambahan tidak lebih dari 10 persen dari total kebutuhan energi harian, atau sekitar 25 sampai 50 gram gula per hari untuk orang dewasa. 
        Namun, seringkali kita tidak menyadari bahwa asupan gula harian tidak hanya berasal dari gula pasir atau pemanis tambahan, tetapi juga dari sumber alami seperti buah-buahan. 
        Buah mengandung gula alami dalam bentuk fruktosa, yang biasanya disertai serat, vitamin, dan mineral penting. 
        Gula alami dari buah ini lebih sehat dibandingkan gula tambahan, karena serat dalam buah memperlambat penyerapan gula, sehingga tidak menyebabkan lonjakan kadar gula darah secara drastis. 
        Meskipun demikian, konsumsi buah secara berlebihan juga dapat menyumbang kelebihan asupan gula total harian. Ditambah dengan gula tersembunyi dari makanan olahan, banyak orang secara tidak sadar melampaui batas yang dianjurkan. 
        Oleh karena itu, penting untuk memahami perbedaan antara gula alami dan gula tambahan, serta mengelola asupan gula total agar tetap seimbang untuk menjaga kesehatan tubuh. Aplikasi web ini akan membantu anda.

        """
    )

    # Garis pemisah
    st.markdown("---")

    if st.button("Kembali ke Home "):
        go_home() 


# Data gula per 100 gram buah (untuk contoh, Anda bisa menambahkan lebih banyak buah)
buah_data = {
    'Nama Buah': ['Apel', 'Arbei', 'Apricot', 'Anggur', 'Alpukat', 'Bit' , 'Belimbing','Bengkuang','Blueberi','Blewah','Ceri','Ciplukan','Carica','Cermai','Cranberry','Cempedak','Delima','Durian','Duku','Jeruk','Jambu Biji','Jambu Air','Kurma', 'Kedondong','Kelapa','Kecapi','Kelengkeng','Kiwi','Kesemek','Leci','Labu','Lemon','Mangga','Murbei','Matoa','Mengkudu', 'Manggis','Melon','Markisa','Naga','Nangka','Nanas','Pepaya','Pir','Persik','Plum','Pisang','Rambutan','Sirsak','Sukun','Salak','Stroberi','Semangka','Sawo','Tin','Tomat','Tebu','Timun','Zaitun'],
    'Gula (gram)': [10,8,9,16,0.7,8,5,1.8,14,8,8,3,3,3,4,13.5,16,19,20,9,9,4.5,66,6,3,14,65,9,20,21.5,3.5,2.5,13.7,8,21,8,15.6,8,11,13,19.3,10,7.8,10,10,10,12,15,13.5,24.5,21,7.4,6,18,16,2.6,16,5,0],  # Gula per 100 gram
}
#untuk input gambar background
def add_gradient_overlay_background(image_url, overlay_opacity=1):
    """
    Menambahkan background gambar dengan overlay warna hitam dan opacity yang dapat diatur.
    
    Parameters:
    - image_url: URL gambar untuk background.
    - overlay_opacity: Opacity overlay hitam (0.0 - 1.0).
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: 
                linear-gradient(
                    rgba(0, 0, 0, {overlay_opacity}), /* Overlay warna hitam dengan opacity */
                    rgba(0, 0, 0, {overlay_opacity})
                ),
                url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL gambar Anda (ganti dengan URL gambar yang Anda gunakan)
image_url = "https://akcdn.detik.net.id/community/media/visual/2022/05/16/buah-buahan-1_169.jpeg?w=700&q=90"

# Tambahkan background dengan overlay hitam (opacity 0.5)
add_gradient_overlay_background(image_url, overlay_opacity=0.7)



# Membuat DataFrame untuk buah
df_buah = pd.DataFrame(buah_data)

# Fungsi untuk menghitung kebutuhan gula berdasarkan berat badan dan usia
def hitung_kebutuhan_gula(usia, berat_badan):
    # Asumsi kebutuhan gula (contoh: 10% dari kalori harian, dengan 1 gram gula = 4 kalori)
    kebutuhan_kalori = berat_badan * 24  # Asumsi 24 kalori per kg berat badan
    kebutuhan_gula = (kebutuhan_kalori * 0.1) / 4  # 10% kalori berasal dari gula
    return kebutuhan_gula

# Fungsi untuk menghitung gula dalam jumlah buah yang dikonsumsi
def hitung_gula_buah(fruit, jumlah_gram):
    gula_per_100gram = df_buah[df_buah['Nama Buah'] == fruit]['Gula (gram)'].values[0]
    gula_total = (gula_per_100gram / 100) * jumlah_gram
    return gula_total

# Tampilan Streamlit
st.title("Kalkulator Kebutuhan gula manusia dalam buah ")

# Input Usia dan Berat Badan
usia = st.number_input("Masukkan Usia (tahun)", min_value=1, max_value=100, value=30)
berat_badan = st.number_input("Masukkan Berat Badan (kg)", min_value=30, max_value=200, value=70)

# Hitung kebutuhan gula berdasarkan berat badan dan usia
kebutuhan_gula = hitung_kebutuhan_gula(usia, berat_badan)
st.write(f"Kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.")

# Input Buah dan jumlahnya
buah_terpilih = st.multiselect("Pilih Buah", df_buah['Nama Buah'].tolist())
jumlah_buah = st.number_input("Masukkan berat Buah (gram)", min_value=50, max_value=1000, value=100)

# Menampilkan informasi gula dari buah yang dipilih
if buah_terpilih:
    for buah in buah_terpilih:
        gula_buah = hitung_gula_buah(buah, jumlah_buah)
        st.write(f"Untuk {jumlah_buah} gram {buah}, Anda akan mengkonsumsi {gula_buah:.2f} gram gula.")

    total_gula = sum([hitung_gula_buah(buah, jumlah_buah) for buah in buah_terpilih])
    st.write(f"Total gula yang dikonsumsi dari buah-buah terpilih: {total_gula:.2f} gram.")
    
# Fungsi untuk memberikan kesimpulan korelasi
def kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula):
    if usia < 18:
        usia_kategori = "usia muda"
    elif 18 <= usia <= 60:
        usia_kategori = "usia dewasa"
    else:
        usia_kategori = "usia tua"

    if total_gula > kebutuhan_gula:
        rekomendasi = "Anda telah mengonsumsi gula melebihi kebutuhan harian. Kurangi konsumsi buah dengan kadar gula tinggi."
    elif total_gula < kebutuhan_gula * 0.5:
        rekomendasi = "Anda mengonsumsi gula jauh di bawah kebutuhan harian. Anda bisa menambah konsumsi buah."
    else:
        rekomendasi = "Anda mengonsumsi gula dalam kisaran yang sehat. Pertahankan pola konsumsi ini."

    kesimpulan_teks = (
        f"Dengan kategori {usia_kategori} dan berat badan {berat_badan} kg, kebutuhan gula harian Anda adalah sekitar {kebutuhan_gula:.2f} gram.\n"
        f" total gula sebesar {total_gula:.2f} gram dari buah-buahan yang dipilih.\n"
        f"{rekomendasi}"
    )
    return kesimpulan_teks

# Hitung dan tampilkan kesimpulan
if buah_terpilih:
    kesimpulan_teks = kesimpulan(usia, berat_badan, total_gula, kebutuhan_gula)
    st.subheader("Kesimpulan")
    st.write(kesimpulan_teks)
