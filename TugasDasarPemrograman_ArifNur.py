import pandas as pd

list_nim = []
list_nama = []
list_absen = []
list_tugas = []
list_uts = []
list_uas = []
list_total = []
list_grade = []
list_lulus = []
ulang = 2

for i in range(ulang):
    print("Data Ke : " + str(i+1))
    list_nim.append(input("Nim : "))
    list_nama.append(input("Nama : "))
    list_absen.append(float(input("Nilai Absen : ")))
    list_tugas.append(float(input("Nilai Tugas : ")))
    list_uts.append(float(input("Nilai UTS : ")))
    list_uas.append(float(input("Nilai UAS : ")))
    
for i in range(ulang):
    list_total.append((list_absen[i]*0.1) + (list_tugas[i]*0.2) + (list_uts[i]*0.3) + (list_uas[i]*0.4))

    if list_total[i] >= 80:
        grade = "A"
        lulus = "Anda Lulus"
    elif list_total[i] >= 70:
        grade = "B"
        lulus = "Anda Lulus"
    elif list_total[i] >= 60:
        grade = "C"
        lulus = "Anda Lulus"
    elif list_total[i] >= 50:
        grade = "D"
        lulus = "Anda Tidak Lulus"
    else:
        grade = "E"
        lulus = "Anda Tidak Lulus"
        
    list_grade.append(grade)
    list_lulus.append(lulus)
    
mhs = {
    "NIM": list_nim,
    "Nama Lengkap": list_nama,
    "Nilai Absen": list_absen,
    "Nilai Tugas": list_tugas,
    "Nilai UTS": list_uts,
    "Nilai UAS": list_uas,
    "Rata - rata Nilai": list_total,
    "Grade": list_grade,
    "Lulus/Tidak Lulus": list_lulus
    }

data_mhs = pd.DataFrame(mhs)       
print("==================================================Daftar Nilai Mahasiswa==================================================")
print(data_mhs)
print("==========================================================================================================================")