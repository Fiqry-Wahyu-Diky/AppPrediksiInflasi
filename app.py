import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import base64
import numpy as np
import joblib


showWarningOnDirectExecution = False

with st.sidebar:
    selected = option_menu(
        menu_title="MENU",
        options=["HOME", "BI", "DATASET", "MODELING", "PREDIKSI"],
        icons=["house", "bar-chart", "table", "robot", "graph-up"],  # add the icons
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )
# ====================== Home ====================
if selected == "HOME":
    st.markdown('<h1 style = "text-align: center;"> INFLASI </h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image("data/img/inflation.png", width=250)
    with col3:
        st.write(' ')

    st.write(' ')
    st.markdown(
        '<p style = "text-align: justify;"> <b> Inflasi </b> adalah kenaikan harga barang dan jasa secara umum dalam perekonomian selama periode waktu tertentu, yang mengakibatkan penurunan daya beli uang. Inflasi dapat disebabkan oleh beberapa faktor seperti permintaan yang melebihi penawaran (demand-pull inflation), kenaikan biaya produksi (cost-push inflation), atau peningkatan jumlah uang beredar (monetary inflation). Dampaknya meliputi pengurangan daya beli masyarakat, ketidakpastian ekonomi, dan redistribusi pendapatan yang tidak merata, meskipun dalam beberapa kasus, inflasi moderat dapat mendorong investasi dan penyesuaian harga dalam ekonomi. Pengukuran inflasi biasanya dilakukan melalui Indeks Harga Konsumen (IHK) yang memantau perubahan harga barang dan jasa yang umum dikonsumsi oleh rumah tangga.</p>',
        unsafe_allow_html=True)

    st.markdown(
        '<p style = "text-align: justify;"> <b> Penyebab Inflasi </b> <br> Penyebab inflasi dapat disebabkan oleh hal-hal berikut. </p>',
        unsafe_allow_html=True)

    st.write('- Tekanan dari sisi penawaran (Cost Push Inflation) <br> <p style = "text-align: justify;"><b>Tekanan dari sisi penawaran (Cost Push Inflation) </b> merupakan Terjadi ketika inflasi disebabkan oleh tekanan dari sisi penawaran atau peningkatan biaya produksi.</p>',unsafe_allow_html=True)

    st.write(
        '- Tekanan dari sisi permintaan (Demand Pull Inflation) <br> <p style = "text-align: justify;"> <b>Tekanan dari sisi permintaan (Demand Pull Inflation)</b> Terjadi ketika inflasi disebabkan oleh tekanan dari sisi permintaan atau meningkatnya permintaan barang dan jasa relatif terhadap ketersediaannya. Dalam konteks makroekonomi, kondisi ini digambarkan oleh output riil yang melebihi output potensialnya atau permintaan total (agregate demand) lebih besar dari pada kapasitas perekonomian hal tersebut dapat mendorong kenaikan harga.</p>',
        unsafe_allow_html=True)
    st.write(
        '- Ekspektasi Inflasi <br> <p style = "text-align: justify;"> <b>Ekspektasi Inflasi</b> adalah faktor yang dipengaruhi oleh persepsi dan harapan masyarakat serta pelaku ekonomi terhadap tingkat inflasi di masa depan. Faktor ini dapat mempengaruhi keputusan konsumen, investor, dan pelaku ekonomi lainnya.</p>',
        unsafe_allow_html=True)


 # ====================== Bank Indonesia ====================
if selected == "BI":
    st.markdown('<h1 style="text-align: center;">BANK INDONESIA</h1>', unsafe_allow_html=True)
    st.image("data/img/bank indonesia.png", width=500, use_column_width=True)

    st.write(' ')
    st.markdown(
        '<p style = "text-align: justify;"> <b> Tentang BI </b><br> Dalam kapasitasnya sebagai bank sentral, Bank Indonesia mempunyai tujuan untuk mencapai stabilitas nilai rupiah, memelihara stabilitas Sistem Pembayaran, dan turut menjaga Stabilitas Sistem Keuangan dalam rangka mendukung pertumbuhan ekonomi yang berkelanjutan.​ Untuk mencapai tujuan tersebut Bank Indonesia bertugas mengelola tiga bidang yaitu Moneter, Sistem Pembayaran, dan Stabilitas Sistem Keuangan. Ketiga bidang tugas tersebut perlu diintegrasi agar tujuan tunggal dapat dicapai secara efektif dan efisien.</p>',
        unsafe_allow_html=True)

    col1, col2= st.columns(2)

    with col1:
        image_path_cardinflasi = "data/img/card inflasi.png"
        with open(image_path_cardinflasi, "rb") as f:
            image_bytes = f.read()
        image_cardinflasi = base64.b64encode(image_bytes).decode()

        card_inflasi = f"""
        <div>
            <a href="https://www.bi.go.id/id/statistik/indikator/data-inflasi.aspx" style="text-decoration: none; color: inherit;">
                <img src="data:image/png;base64,{image_cardinflasi}" style="max-width: 100%; margin: 0 auto;">
            </a>
        </div>
        """
        st.markdown(card_inflasi, unsafe_allow_html=True)

    with col2:
        image_path_cardinflasi = "data/img/berita terkini.png"
        with open(image_path_cardinflasi, "rb") as f:
            image_bytes = f.read()
        image_cardinflasi = base64.b64encode(image_bytes).decode()

        card_inflasi = f"""
        <div>
            <a href="https://www.bi.go.id/id/publikasi/ruang-media/news-release/Default.aspx" style="text-decoration: none; color: inherit;">
                <img src="data:image/png;base64,{image_cardinflasi}" style="max-width: 100%; margin: 0 auto;">
            </a>
        </div>
        """
        st.markdown(card_inflasi, unsafe_allow_html=True)

# # ====================== Dataset ====================
if selected == 'DATASET':
    st.write("# DATASET")
    dataset, visual, acf, pacf = st.tabs(["Data", "Visualisasi", "ACF", "PACF"])

    with dataset:
        dataset = pd.read_excel("data/dataset inflasi indonesia.xlsx")
        st.dataframe(dataset)
        st.info(f"Banyak Dataset : {len(dataset)}")
        st.warning(f'Informasi Dataset')
        st.write(dataset.describe())
    with visual:
        st.success("### Ploting Dataset")
        st.image('data/img/plot dataset.png')

    with acf:
        st.success("### Ploting Autokorelasi (ACF)")
        st.image('data/img/acf.png')

    with pacf:
        st.success("### Ploting Parsial Autokorelasi (PACF)")
        st.image('data/img/pacf.png')

# ======= model ==============
if selected == 'MODELING':
    st.write("## Model Ensemble SVR (Support Vector Regression)")
    skenario1, skenario2, skenario3 = st.tabs(['Skenario 1','Skenario 2','Skenario 3'])
    dataset = pd.read_excel("data/dataset inflasi indonesia.xlsx")
    dfdataset = pd.DataFrame(dataset)

    with skenario1:
        prediksiS1 = pd.read_excel("data/prediksi S1.xlsx")
        dfprediksiS1 = pd.DataFrame(prediksiS1)

        historiS1 = pd.read_excel("data/historiS1.xlsx")
        dfhistoriS1 = pd.DataFrame(historiS1)

        histori,visual = st.tabs(['Histori','Visual'])
        with histori:
            st.write('Pada skenario 1 digunakan pembagian dataset dengan rasio 80:20.')
            st.write(f"Banyak data train : {len(dfdataset) - len(dfprediksiS1)} data")
            st.write(f"Banyak data test : {len(dfprediksiS1)} data")

            st.info("#### Histori dari skenario 1")
            st.write(dfhistoriS1)

            st.info("##### Parameter terbaik yaitu:")
            idmax = dfhistoriS1['MAPE-denorm(%)'].idxmin()
            st.write(dfhistoriS1.iloc[idmax,1:7])

            st.info("##### Hasil Nilai Error Terendah:")
            st.write(f"Nilai MAPE : {round(dfhistoriS1['MAPE-denorm(%)'].min(),2)} %")
            st.write(f"Nilai RMSE : {round(dfhistoriS1['RMSE-denorm'].min(), 2)} %")

        with visual:
            st.info("##### Visualisasi grafik")
            st.image("data/img/grafikS1.png")

            st.info("##### Tabel Aktual dan Prediksi")

            col1,col2,col3 = st.columns(3)
            with col2:
                st.write(dfprediksiS1)


    with skenario2:
        prediksiS2 = pd.read_excel("data/prediksi S2.xlsx")
        dfprediksiS2 = pd.DataFrame(prediksiS2)

        historiS2 = pd.read_excel("data/historiS2.xlsx")
        dfhistoriS2 = pd.DataFrame(historiS2)

        histori,visual = st.tabs(['Histori','Visual'])
        with histori:
            st.write('Pada skenario 2 digunakan pembagian dataset dengan rasio 70:30.')
            st.write(f"Banyak data train : {len(dfdataset) - len(dfprediksiS2)} data")
            st.write(f"Banyak data test : {len(dfprediksiS2)} data")

            st.info("#### Histori dari skenario 2")
            st.write(dfhistoriS2)

            st.info("##### Parameter terbaik yaitu:")
            idmax = dfhistoriS2['MAPE-denorm(%)'].idxmin()
            st.write(dfhistoriS2.iloc[idmax,1:7])

            st.info("##### Hasil Nilai Error Terendah:")
            st.write(f"Nilai MAPE : {round(dfhistoriS2['MAPE-denorm(%)'].min(),2)} %")
            st.write(f"Nilai RMSE : {round(dfhistoriS2['RMSE-denorm'].min(), 2)} %")

        with visual:
            st.info("##### Visualisasi grafik")
            st.image("data/img/grafikS2.png")

            st.info("##### Tabel Aktual dan Prediksi")

            col1,col2,col3 = st.columns(3)
            with col2:
                st.write(dfprediksiS2)

    with skenario3:
        prediksiS3 = pd.read_excel("data/prediksi S3.xlsx")
        dfprediksiS3 = pd.DataFrame(prediksiS3)

        historiS3 = pd.read_excel("data/historiS3.xlsx")
        dfhistoriS3 = pd.DataFrame(historiS3)

        histori,visual = st.tabs(['Histori','Visual'])
        with histori:
            st.write('Pada skenario 3 digunakan pembagian dataset dengan rasio 60:40.')
            st.write(f"Banyak data train : {len(dfdataset) - len(dfprediksiS3)} data")
            st.write(f"Banyak data test : {len(dfprediksiS3)} data")

            st.info("#### Histori dari skenario 3")
            st.write(dfhistoriS3)

            st.info("##### Parameter terbaik yaitu:")
            idmax = dfhistoriS3['MAPE-denorm(%)'].idxmin()
            st.write(dfhistoriS3.iloc[idmax,1:7])

            st.info("##### Hasil Nilai Error Terendah:")
            st.write(f"Nilai MAPE : {round(dfhistoriS3['MAPE-denorm(%)'].min(),2)} %")
            st.write(f"Nilai RMSE : {round(dfhistoriS3['RMSE-denorm'].min(), 2)} %")

        with visual:
            st.info("##### Visualisasi grafik")
            st.image("data/img/grafikS3.png")

            st.info("##### Tabel Aktual dan Prediksi")

            col1,col2,col3 = st.columns(3)
            with col2:
                st.write(dfprediksiS3)

# ===== prediksi =======
if selected == 'PREDIKSI':
    modelnormalisasi = joblib.load("data/normalization_model.pkl")
    modelesvr = joblib.load('data/model_esvr.pkl')

    st.write("# Peramalan Inflasi")
    st.warning("###### Remainder")
    st.write("Pada halaman ini anda akan melakukan peramalan Inflasi dengan data masukan berupa Inflasi dari waktu sebelumnya. untuk informasi mengenai data Inflasi dapat melihat pada Menu BI dan memilih data histori Inflasi.")

    st.info("Masukkan Data Inflasi")

    col1,col2 = st.columns(2)
    with col1:
        t1 = st.number_input("Masukkan Inflasi 1 bulan sebelumnya")
    with col2:
        t2 = st.number_input("Masukkan Inflasi 2 bulan sebelumnya")

    col3,col4 = st.columns(2)
    with col3:
        t4 = st.number_input("Masukkan Inflasi 4 bulan sebelumnya")
    with col4:
        t8 = st.number_input("Masukkan Inflasi 8 bulan sebelumnya")
    t13 = st.number_input("Masukkan Inflasi 13 bulan sebelumnya")

    if st.button("Predict"):
        newdata = np.array([t1, t2, t4, t8, t13])
        normnewdata = modelnormalisasi.transform(newdata.reshape(-1, 1))
        prediksi = modelesvr.predict(normnewdata.reshape(1,-1))
        denormpredict = modelnormalisasi.inverse_transform(prediksi.reshape(-1,1))

        st.write(f"Hasil peramalan inflasi bulan depan sebesar: ")
        st.info(f"{round(denormpredict[0,0],2)}%")

        if st.button("Reset"):
            t1 = 0
            t2 = 0
            t4 = 0
            t8 = 0
            t13 = 0



# =========================
# numbbulan = st.number_input("", value=None, step=1, max_value=12, placeholder="Masukkan banyak bulan prediksi (max 12)")
    #
    # datainflasiolah = pd.read_excel("data/dataset inflasi indonesia.xlsx")
    # dfdatainflasiolah = pd.DataFrame(datainflasiolah)
    # list_inflasiolah = dfdatainflasiolah['Inflasi'].tolist()
    # dfdatainflasiolah_new = list_inflasiolah
    # # st.write(list_inflasiolah[-1])
    #
    # hasilpredict = []
    #
    # # #
    # if st.button("Predict"):
    #     for i in range(1, numbbulan + 1):
    #         newdata = np.array([t1, t2, t4, t8, t13])
    #         normnewdata = modelnormalisasi.transform(newdata.reshape(-1, 1))
    #         prediksi = modelesvr.predict(normnewdata.reshape(1,-1))
    #         denormpredict = modelnormalisasi.inverse_transform(prediksi.reshape(-1,1))
    #
    #         dfdatainflasiolah_new.append(denormpredict[0,0])
    #         hasilpredict.append((denormpredict[0, 0]))
    #
    #         # st.write(dfdatainflasiolah_new)
    #
    #
    #         t1 = dfdatainflasiolah_new[-1]
    #         # st.write(t1)
    #         t2 = dfdatainflasiolah_new[-2]
    #         t4 = dfdatainflasiolah_new[-4]
    #         t8 = dfdatainflasiolah_new[-8]
    #         t13 = dfdatainflasiolah_new[-13]
    #         # st.write(t13)
    #
    #
    #
    #     for j in range(len(hasilpredict)):
    #         st.info(f"Hasil Peramalan {j+1} Bulan kedepan: {round(hasilpredict[j],2)}")
    #     st.success("##### Data peramalan berhasil diproses")
    #     if st.button("Reset"):
    #         dfdatainflasiolah_new = list_inflasiolah
    #         t1 = 0
    #         t2 = 0
    #         t4 = 0
    #         t8 = 0
    #         t13 = 0
