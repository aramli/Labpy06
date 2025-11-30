# Praktikum5
Tugas Pemrograman Dasar Pertemuan Ke 11 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Tugas Praktikum
<ul>
  <li>Flowchart</li>
  <img src="https://github.com/aramli/labpy06/raw/main/img/20.png" width="750"/>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy06/raw/main/img/1.png" width="750"/>
  <img src="https://github.com/aramli/labpy06/raw/main/img/2.png" width="750"/>
  <img src="https://github.com/aramli/labpy06/raw/main/img/3.png" width="750"/>
  <li>Hasil Program</li>
    1. Lihat Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/12.png" width="750"/><br>
    2. Menambahkan Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/13.png" width="750"/><br>
    3. Mengubah Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/14.png" width="750"/><br>
    4. Menghapus Data Mahasiswa <br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/15.png" width="750"/><br>
    5. Mencari Data Mahasiswa<br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/16.png" width="750"/><br>
    6. Keluar Dari Program<br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/17.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy06/raw/main/img/4.png" width="750"/><br>
  1. Pertama-tama, Program membuat sebuah dictionary kosong bernama data_mahasiswa. Dictionary ini berfungsi sebagai wadah untuk menyimpan semua data mahasiswa. Nantinya, setiap mahasiswa akan disimpan dengan NIM sebagai key dan detail nilai sebagai value.
<br><br>
 <img src="https://github.com/aramli/labpy06/raw/main/img/5.png" width="750"/><br>
  2. Selanjutnya, Fungsi ini dipakai untuk menambahkan data mahasiswa baru. User diminta memasukkan NIM, nama, dan nilai tugas/UTS/UAS. Nilai akhir dihitung dengan bobot (30% tugas, 35% UTS, 35% UAS). Semua data disimpan ke dictionary data_mahasiswa.
<img src="https://github.com/aramli/labpy06/raw/main/img/6.png" width="750"/><br>
  3. Kemudian, Fungsi ini menampilkan daftar semua mahasiswa dalam bentuk tabel. Jika data_mahasiswa kosong, muncul pesan “TIDAK ADA DATA MAHASISWA”. Kalau ada data, setiap mahasiswa ditampilkan dengan nomor urut, NIM, nama, nilai tugas, UTS, UAS, dan nilai akhir.
<br><br>
<img src="https://github.com/aramli/labpy06/raw/main/img/.7png" width="750"/><br>
  4. Lalu, Fungsi ini digunakan untuk mengedit data mahasiswa. User memasukkan NIM, lalu jika NIM ada di dictionary, data lama diganti dengan data baru. Kalau NIM tidak ditemukan, muncul pesan error.
<br><br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/8.png" width="750"/><br>
  5. Selanjutnya Fungsi ini dipakai untuk menghapus data mahasiswa berdasarkan NIM. Jika NIM ada, data dihapus dari dictionary. Kalau tidak ada, muncul pesan error.
<br><br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/9.png" width="750"/><br>
  6. Berikutnya, Fungsi ini digunakan untuk mencari data mahasiswa tertentu berdasarkan NIM. Jika ditemukan, detail mahasiswa ditampilkan lengkap (NIM, nama, nilai tugas, UTS, UAS, nilai akhir). Kalau tidak ditemukan, muncul pesan error.
<br><br>
  <img src="https://github.com/aramli/labpy06/raw/main/img/10.png" width="750"/><br>
  7. Kemudian, Fungsi ini adalah program utama. Di dalamnya ada loop while True yang membuat program terus berjalan sampai user memilih keluar (K). User dimintamemilih menu:
- T → tambah data
- L → lihat data
- U → ubah data
- H → hapus data
- C → cari data
- K → keluar program
Jika input tidak sesuai, muncul pesan “Pilihan tidak valid”.
<br><br>
<img src="https://github.com/aramli/labpy06/raw/main/img/11.png" width="750"/><br>
  8. Terakhir, memanggil fungsi main() sehingga program benar-benar berjalan.
<br><br>
</ul>
