# Praktikum 6
data_mahasiswa = {}

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    print("Data Mahasiswa berhasil ditambahkan!")

def lihat_data():
    print("\nDaftar Nilai Mahasiswa:")
    print("===============================================================================================")
    print("|   NO   |    NIM    |       NAMA      |    TUGAS    |     UTS     |     UAS     |    AKHIR   |")
    print("===============================================================================================")
    if not data_mahasiswa:
        print("|                                  TIDAK ADA DATA MAHASISWA                                   |")
    else:
        no = 1
        for nim, mhs in data_mahasiswa.items():
            print(f"| {no:^6} | {nim:^8} | {mhs['nama']:<15} | {mhs['tugas']:^11.1f} | {mhs['uts']:^11.1f} | {mhs['uas']:^11.1f} | {mhs['nilai_akhir']:^10.1f} |")
            no += 1
    print("===============================================================================================")

def ubah_data():
    nim = input("Masukkan NIM Mahasiswa yang akan diubah: ")
    if nim in data_mahasiswa:
        print("Data ditemukan. Silakan masukkan data baru.")
        nama = input("Masukkan Nama: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        }
        print("Data Mahasiswa berhasil diubah!")
    else:
        print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

def cari_data():
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data_mahasiswa:
        mhs = data_mahasiswa[nim]
        print("\nData Mahasiswa:")
        print(f"NIM         : {nim}")
        print(f"Nama        : {mhs['nama']}")
        print(f"Tugas       : {mhs['tugas']}")
        print(f"UTS         : {mhs['uts']}")
        print(f"UAS         : {mhs['uas']}")
        print(f"Nilai Akhir : {mhs['nilai_akhir']:.1f}")
    else:
        print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

def main():
    print("PROGRAM INPUT NILAI MAHASISWA")
    while True:
        opsi = input("\nSilahkan pilih opsi [L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar = ").lower()

        if opsi == 'k':
            print("Terima kasih telah menggunakan program ini.")
            break
        elif opsi == 't':
            tambah_data()
        elif opsi == 'l':
            lihat_data()
        elif opsi == 'u':
            ubah_data()
        elif opsi == 'h':
            hapus_data()
        elif opsi == 'c':
            cari_data()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
main()
