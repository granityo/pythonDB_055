import tkinter as tk
import sqlite3
from tkinter import messagebox

def hasilprediksi(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris: 
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak bisa diprediksi"


def simpan_data_ke_sqlite(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect("kelasB.db")
    cursor = conn.cursor()

# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nama_siswa INTEGER,
                biologi INTEGER, 
                fisika INTEGER,
                inggris INTEGER,
                prediksi_fakultas TEXT)''')

# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute('''INSERT INTO hasil_prediksi 
                (nama_siswa,
                biologi, 
                fisika, 
                inggris, 
                prediksi_fakultas) VALUES (?, ?, ?, ?, ?)''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()
 
# fungsi untuk menampilkan
def show():
    nama_siswa = entry_namaMhs.get()
    bio = int(entry_hasil1.get())
    fis = int(entry_hasil2.get())
    ing = int(entry_hasil3.get())

    predik = hasilprediksi(bio, fis, ing)

    namaMhs = f"Nama Siswa : {nama_siswa}"
    hasil1 = f"Nilai Biologi : {bio}"
    hasil2 = f"Nilai Fisika : {fis}"
    hasil3 = f"Nilai Inggris : {ing}"
    hasil4 = f"Prediksi Fakultas : {predik}"

    label_namaMhs.config(text=namaMhs)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)
    label_hasil4.config(text=hasil4)

    frame_hasil.pack()
    simpan_data_ke_sqlite(nama_siswa=nama_siswa, biologi=bio, fisika=fis, inggris=ing, prediksi_fakultas=predik)
    messagebox.showinfo("info", f"Data Tersimpan")

# Buat Jendela Halaman
root = tk.Tk()
root.title("Prediksi Fakultas")
root.geometry("500x500")
root.resizable(False, False)

# Buat Label Judul
label_judul = tk.Label(root, text="Prediksi Fakultas", font=("Times", 14, "bold"))
label_judul.pack(pady=20)

# Buat Frame Inputan
frame_input =tk.LabelFrame(root, labelanchor="n", pady=10, padx=10)
frame_input.pack()

# Label Nama Siswa
label_namaMhs = tk.Label(frame_input, text="Nama Siswa : ")
label_namaMhs.grid(row=0, column=0, pady=10)
entry_namaMhs = tk.Entry(frame_input)
entry_namaMhs.grid(row=0, column=1)

# Label Nilai biologi
label_hasil1 = tk.Label(frame_input, text="Nilai Biologi : ")
label_hasil1.grid(row=1, column=0, pady=10)
entry_hasil1 = tk.Entry(frame_input)
entry_hasil1.grid(row=1, column=1)

# Label Nilai fisika
label_hasil2 = tk.Label(frame_input, text="Nilai Fisika : ")
label_hasil2.grid(row=2, column=0, pady=10)
entry_hasil2 = tk.Entry(frame_input)
entry_hasil2.grid(row=2, column=1)

# Label Nilai inggris
label_hasil3 = tk.Label(frame_input, text="Nilai Bahasa : ")
label_hasil3.grid(row=3, column=0, pady=10)
entry_hasil3 = tk.Entry(frame_input)
entry_hasil3.grid(row=3, column=1)


# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root, labelanchor="n", padx=10, pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_nama_siswa = tk.Label(frame_hasil, text="")
label_nama_siswa.pack()

label_hasil1 = tk.Label(frame_hasil, text="")
label_hasil1.pack()

label_hasil2 = tk.Label(frame_hasil, text="")
label_hasil2.pack()

label_hasil3 = tk.Label(frame_hasil, text="")
label_hasil3.pack()

label_hasil4 = tk.Label(frame_hasil, text="")
label_hasil4.pack()

# Jalankan Aplikasi
root.mainloop()