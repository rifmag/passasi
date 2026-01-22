import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Fungsi untuk membaca data dari file Excel
def read_excel_data(file_path):
    data = pd.read_excel(file_path)
    return data

# Fungsi untuk mencari data berdasarkan NIP dan OTP
def cari_data_berdasarkan_nip_otp(data, nip, otp):
    return data[(data["nip"] == nip) & (data["otp"] == otp)]

def main():
    st.title("")

    # Logo in the top-right corner
    logo = '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi9L7E2_2WuGtZqM03fu_AcQzq1cdlGrcp_27Vu3W0E1XyfU730QqtbiXNheHLZ4SuMw&usqp=CAU" style="float:left;">'
    st.markdown(logo, unsafe_allow_html=True)

    # Baca data dari file Excel
    data = read_excel_data("datasertif.xlsx")  # Ganti dengan path file Excel Anda

    # Isian NIP dan OTP
    nip_input = st.text_input("Masukkan NIP:", "").strip()
    otp_input = st.text_input("Masukkan OTP:", "").strip()
    st.markdown("<small>masukkan OTP dengan tanggal lahir Anda dengan format : <b>dd/mm/yyyy</b> contoh : <b>06091988</b></small>" , unsafe_allow_html=True)
    if st.button("Tampilkan"):
        if nip_input and otp_input:
            student_data = cari_data_berdasarkan_nip_otp(data, int(nip_input), int(otp_input))
            if not student_data.empty:
                student_name = student_data["Nama"].iloc[0]
                student_link = student_data["Link"].iloc[0]
                student_ttl = student_data["ttl"].iloc[0]
                student_jabatan = student_data["jabatan"].iloc[0]
                student_unit = student_data["unit"].iloc[0]
                

                # Tampilkan nama dalam kotak bergaris
                fields = {
                    "Nama": student_name,
                    "TTL": student_ttl,
                    "Jabatan": student_jabatan,
                    "Unit": student_unit
                    }

                with st.container(border=True):
                    col_l, col_r = st.columns([1, 3])

                    for label, value in fields.items():
                        with col_l:
                            st.markdown(f"**{label}**")
                        with col_r:
                            st.markdown(value)

                    st.divider()
                    st.link_button("🔗 Buka Sertifikat", student_link)



                # Tambahkan tulisan jika data ditemukan
                st.success(" Sertifikat ditemukan. Silahkan klik tautan diatas")
            else:
                st.warning("Data tidak ditemukan untuk NIP dan OTP tersebut.")

if __name__ == "__main__":
    main()

