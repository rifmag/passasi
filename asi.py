import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Fungsi untuk membaca data dari file Excel
def read_excel_data(file_path):
    data = pd.read_excel(file_path)
    return data

# Fungsi untuk mencari data berdasarkan NIP
def cari_data_berdasarkan_nip_otp(data, nip, otp):
    return data[(data["nip"] == nip) & (data["otp"] == otp)]

def main():
    st.title("Cek Password")
    
    # Baca data dari file Excel
    data = read_excel_data("dataasi.xlsx")  # Ganti dengan path file Excel Anda

    # Isian NIP dan OTP
    nip_input = st.text_input("Masukkan NIP:", "").strip()
    otp_input = st.text_input("Masukkan OTP:", "").strip()
    if st.button("Tampilkan"):
        if nip_input and otp_input:
            student_data = cari_data_berdasarkan_nip_otp(data, int(nip_input), int(otp_input))
            if not student_data.empty:
                student_name = student_data["Nama"].iloc[0]
                st.markdown(f"<p style='font-size: 36px; font-weight: bold;'>Nama: {student_name}</p>", unsafe_allow_html=True)
                student_password = student_data["password"].iloc[0]
                st.markdown(f"<p style='font-size: 36px; font-weight: bold;'>password: {student_password}</p>", unsafe_allow_html=True)
                st.success("Password ditemukan. Silahkan masuk melalui tautan [https://upkp2023.asi-asesmen.com/](https://upkp2023.asi-asesmen.com/)")
            else:
                st.warning("Data tidak ditemukan untuk NIP dan OTP tersebut.")

if __name__ == "__main__":
    main()
