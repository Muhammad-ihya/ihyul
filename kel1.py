import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Configure the page layout
st.set_page_config(page_title="Antioxidant Calc", page_icon="💀")

def random_color():
    return f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)"  # 0.5 untuk opacity
# Warna acak untuk background
background_color = random_color()

# CSS untuk lapisan background
st.markdown(
    f"""
    <style>
    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 128, 0, 0.7);
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

def set_background():
    st.markdown(
        """
        <style>
        .bordered-text {
            border: 10px solid #ffff;  /* Warna border (merah-oranye) */
            padding: 10px;              /* Jarak antara teks dan border */
            border-radius: 20px;         /* Sudut border yang melengkung */
            font-size: 20px;            /* Ukuran font */
            color: #ffff;                /* Warna teks */
        }
        
        .typing {
                font-family: 'Consolas', 'Courier New', monospace;
                white-space: normal;  /* Mengizinkan teks untuk membungkus ke baris berikutnya */
                word-wrap: break-word; /* Memastikan kata yang terlalu panjang terpotong dan dibungkus */
                overflow: hidden;

            }

        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: 'Consolas', 'Courier New', monospace;
            text-align: center;
            color: #ffff
        }

        /* Header */
        h1, h2, h3, h4, p {
            color: #FFFF;
            font-family: 'Consolas', 'Courier New', monospace;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 0, 0, 0.5) !important; /* Warna oranye dengan transparansi 80% */
    }

        /* Button */
        .stButton > button {
            background-color: #FF9933;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 24px;
        }

        /* Card Box */
        .info-box {
            background-color: #edf2f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }

        /* Image Style */
        .stImage > img {
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Terapkan Background ---
set_background()

# Membuat header dengan logo di kanan atas dan teks di kiri
with st.container():
    col1, col2 = st.columns([14, 1])  # Membagi halaman menjadi dua kolom (5:1)

    with col1:
        # Teks di kiri
        st.write("""
        <div style="font-family: 'Consolas', 'Courier New', monospace; margin-top: -50px; text-align: right;">
            <h1 style="font-weight: bold; margin: 0px; font-size: 24px; line-height: 1;">Politeknik AKA Bogor</h1>
            <p style="margin: 0px; font-size: 18px; line-height: 1; margin-top: -10px; color: #ffff; ">D-IV Nanoteknologi Pangan</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Logo di kanan atas tanpa ikon rantai
        st.write("""
        <div style="text-align: right; margin-top: -25px;">
            <img src="https://1.bp.blogspot.com/-I8f-TbrhPeQ/WFd0_c1VaJI/AAAAAAAAAgE/_aPhNqeAR0QV1yphTw69HC4rC4KxUKLFwCLcB/s1600/logo%2BAKA%2BBogor.jpg" 
                 alt="Logo Politeknik AKA Bogor" style="width: 90px;">
        </div>
        """, unsafe_allow_html=True)

image_url = "https://indonesiacollege.co.id/blog/wp-content/uploads/2022/10/jurusan-politeknik-aka-bogor.jpg"

# CSS untuk mengatur gambar sebagai background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{image_url}');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Initialize session state if not already done
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def set_page(page_name):
    st.session_state.current_page = page_name

# Sidebar Navigation
if st.sidebar.button("🏠 Home"):
    st.session_state.current_page = "Home"
elif st.sidebar.button("🧮 About Us"):
    st.session_state.current_page = "About Us"
elif st.sidebar.button("🔍 Contact"):
    st.session_state.current_page = "Contact"



def home():
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #28a745;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 class='typing'>💀 Antioxidant Calc 💀</h1>", unsafe_allow_html=True)

    if st.button("Start to Calculate", key="start_button", use_container_width=True):
        st.session_state.current_page = "Page 2"

    st.write("""
<div class="typing bordered-text">
        Antioksidan adalah suatu zat yang dapat melindungi senyawa kimia dalam tubuh dari oksidasi yang dapat merusak dengan cara bereaksi dengan radikal bebas dan spesi oksigen reaktif, sehingga dapat menghambat oksidasi. Antioksidan juga disebut sebagai scavenger (zat/peredam) radikal bebas dan dapat menetralkan radikal bebas. Antioksidan sebagai senyawa yang dapat menonaktifkan radikal bebas dengan 
        menggunakan dua mekanisme utama yaitu Hidrogen Atom Transfer (HAT) dan 
        Single Electron Transfer (SET). Kedua mekanisme tersebut menjadi dasar metode
        pengujian antioksidan.
        Metode HAT mengukur kemampuan antioksidan untuk meredam radikal bebas dengan 
        sumbangan hidrogen (donor proton), Metode SET mengukur kemampuan antioksidan 
        untuk mereduksi radikal bebas melalui transfer elektron tunggal. Sedangkan pada
        mekanisme SET, antioksidan mendonasikan satu elektron ke radikal bebas sehingga
        radikal bebas menjadi netral dan stabil. Proses ini mencegah radikal bebas 
        merusak molekul biologis seperti lipid, protein, dan DNA.
    </div>
    """, unsafe_allow_html=True)

def page_2():
    st.markdown("""<style>.title {color: pink; text-align: center; font-size: 40px;} .custom-button {background-color: #32CD32; color: white; border: 1px solid white; border-radius: 10px; padding: 10px 20px; cursor: pointer; display: inline-block;} .custom-button:hover {background-color: #28a745;} .center-content {text-align: center;}</style>""", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Select a Test Method</h1>", unsafe_allow_html=True)

    test_methods = ["ORAC", "TRAP", "LPIC", "FRAP", "TEAC", "DPPH", "CUPRAC", "ABTS"]
    cols = st.columns(4)
    for i, method in enumerate(test_methods):
        with cols[i % 4]:
            if st.button(method, key=method):
                st.session_state.current_page = f"ATOX.CALC-{method}"
    if st.button("Back to Menu"):
        set_page("Home")

def atox_calc_page(method):
    if method == "DPPH":
        st.markdown("<h1 style='color: #330066; text-align: center;'>DPPH</h1>", unsafe_allow_html=True)
        blank = st.number_input("Input blanko", format="%.6f")
        num_samples = st.number_input("Berapa banyak sampel ingin diuji", min_value=0, step=1)

        if num_samples > 0:
            st.write("Masukkan konsentrasi (ppm) dan absorbansi untuk setiap sampel")
            cols = st.columns(2)
            concentrations = []
            absorbances = []
            for i in range(num_samples):
                with cols[0]:
                    concentrations.append(st.number_input(f"Input konsentrasi (ppm) sampel {i+1}", format="%.6f"))
                with cols[1]:
                    absorbances.append(st.number_input(f"Input absorbansi sampel {i+1}", format="%.6f"))

            # Calculate % inhibition and other results
            if st.button("Calculate"):
                results = pd.DataFrame({
                    "Konsentrasi (ppm)": concentrations,
                    "% Inhibisi": [(1 - a/blank)*100 if blank != 0 else 0 for a in absorbances]
                })
                st.table(results)

                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Inhibisi"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"
                st.markdown(f"**Persamaan Regresi:** {regression_eq}")

                # Graph
                fig, ax = plt.subplots()
                ax.plot(concentrations, results["% Inhibisi"], 'o-', label="Data Points")
                ax.plot(concentrations, slope * np.array(concentrations) + intercept, '-', label="Regresi")
                ax.set_xlabel("Konsentrasi (ppm)")
                ax.set_ylabel("% Inhibisi")
                ax.legend()
                st.pyplot(fig)

                # Display IC50 value
                ic50 = (50 -intercept) / slope if slope != 0 else None
                if ic50:
                    st.markdown(f"**IC50 Value:** {ic50:.6f} ppm")
                else:
                    st.markdown("**IC50 Value:** Tidak dapat dihitung.")
        if st.button("Back to Menu"):
            set_page("Home")

    elif method == "FRAP":
        st.markdown("<h1 style='color: #FF3333; text-align: center;'>FRAP</h1>", unsafe_allow_html=True)
        blank = st.number_input("Input blanko", format="%.6f")
        num_samples = st.number_input("Berapa banyak sampel ingin diuji", min_value=0, step=1)

        if num_samples > 0:
            st.write("Masukkan konsentrasi (ppm) dan absorbansi untuk setiap sampel")
            cols = st.columns(2)
            concentrations = []
            absorbances = []
            for i in range(num_samples):
                with cols[0]:
                    concentrations.append(st.number_input(f"Input konsentrasi (ppm) sampel {i+1}", format="%.6f"))
                with cols[1]:
                    absorbances.append(st.number_input(f"Input absorbansi sampel {i+1}", format="%.6f"))

            # Calculate % reducing power and other results
            if st.button("Calculate"):
                results = pd.DataFrame({
                    "Konsentrasi (ppm)": concentrations,
                    "% Reducing Power": [(1 - (blank / a)) * 100 if blank != 0 else 0 for a in absorbances]
                })
                st.table(results)

                # Linear regression
                coefficients = np.polyfit(concentrations, results["% Reducing Power"], 1)
                slope, intercept = coefficients
                regression_eq = f"y = {slope:.6f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.6f}"
                st.markdown(f"**Persamaan Regresi:** {regression_eq}")

                # Graph
                fig, ax = plt.subplots()
                ax.plot(concentrations, results["% Reducing Power"], 'o-', label="Data Points")
                ax.plot(concentrations, slope * np.array(concentrations) + intercept, '-', label="Regresi")
                ax.set_xlabel("Konsentrasi (ppm)")
                ax.set_ylabel("% Reducing Power")
                ax.legend()
                st.pyplot(fig)

                # Display EC50 value
                ec50 = (50 - intercept) / slope if slope != 0 else None
                if ec50:
                    st.markdown(f"**EC50 Value:** {ec50:.6f} ppm")
                else:
                    st.markdown("**EC50 Value:** Tidak dapat dihitung.")
        if st.button("Back to Menu"):
            set_page("Home")
    else:
        st.markdown("""<div style="text-align: center;">
                        <p>Kalkulator sedang dalam pengembangan.</p>
                        <span style="font-size: 50px;">😓</span>
                      </div>""", unsafe_allow_html=True)
        if st.button("Back to Menu"):
            set_page("Home")


# Main App Logic

if st.session_state.get("current_page") == "Home":
    home()
elif st.session_state.get("current_page") == "About Us":
    st.title("About Us")
    st.markdown("""
    <style>
        .team-member {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .team-member img {
            width: 100px;
            height: 100px;
            border-radius: 20%;
            margin-right: 20px;
            object-fit: cover;
            border: 2px solid #ddd;
        }
        .team-member div {
            font-size: 18px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Daftar nama dan foto
    members = [
        {"name": "Muhammad Fakhri Al-Fathi - 2350108", "photo": "C:/Users/YourUsername/Downloads/ara.jpg"},
        {"name": "Nabila Azizi Rohmah - 2350116", "photo": "path_to_images/nabila.jpg"},
        {"name": "Pinkan Regina Ayu Maharani - 2350126", "photo": "path_to_images/pinkan.jpg"},
        {"name": "Syifa Ahista Maharani - 2350136", "photo": "path_to_images/syifa.jpg"},
        {"name": "Anargya Cinta Ismoyo - 2350073", "photo": "path_to_images/anargya.jpg"}
    ]

    # Menampilkan daftar nama dengan foto
    for member in members:
        st.markdown(f"""
        <div class="team-member">
            <img src="file://{member['photo']}" alt="Profile Photo">
            <div>{member['name']}</div>
        </div>
        """, unsafe_allow_html=True)
elif st.session_state.get("current_page") == "Contact":
    st.title("Contact")
    st.write("This is the Contact page.")
elif "ATOX.CALC-" in st.session_state.current_page:
    method = st.session_state.current_page.split("-")[1]
    atox_calc_page(method)
else:
    page_2()

# if st.session_state.current_page == "Home":
#     home()
# elif st.session_state.current_page == "About Us":
#     st.title("About Us")

# elif st.session_state.current_page == "Contact":
#     st.title("Contact")
#     st.write("This is the Contact page.")

# else:
#     page_2()


