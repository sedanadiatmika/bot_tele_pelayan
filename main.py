from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import mysql.connector
from itertools import chain
from datetime import datetime

import re
from collections import Counter

# koneksi db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_bot_restoran"
)

# deklarasi respon
#region
mycursor_get_pembuka_awal = mydb.cursor(buffered=True)
mycursor_get_pembuka = mydb.cursor(buffered=True)
mycursor_get_menu = mydb.cursor(buffered=True)
mycursor_get_pesan = mydb.cursor(buffered=True)
mycursor_get_total = mydb.cursor(buffered=True)
mycursor_get_ulang = mydb.cursor(buffered=True)
mycursor_get_selesai = mydb.cursor(buffered=True)
mycursor_get_menu_makanan = mydb.cursor(buffered=True)
mycursor_get_menu_minuman = mydb.cursor(buffered=True)

mycursor_get_pembuka_awal.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'awal'")
mycursor_get_pembuka.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'pembuka'")
mycursor_get_menu.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'menu'")
mycursor_get_pesan.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'pesan'")
mycursor_get_total.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'total'")
mycursor_get_ulang.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'ulang'")
mycursor_get_selesai.execute("SELECT isi FROM tb_pencocokan WHERE jenis = 'selesai'")
mycursor_get_menu_makanan.execute("SELECT nama, harga FROM tb_menu WHERE jenis = 'makanan'")
mycursor_get_menu_minuman.execute("SELECT nama, harga FROM tb_menu WHERE jenis = 'minuman'")

mycursor_get_pembuka_hai = mydb.cursor(buffered=True)
mycursor_get_pembuka_halo = mydb.cursor(buffered=True)
mycursor_get_pembuka_pagi = mydb.cursor(buffered=True)
mycursor_get_pembuka_siang = mydb.cursor(buffered=True)
mycursor_get_pembuka_sore = mydb.cursor(buffered=True)
mycursor_get_pembuka_malam = mydb.cursor(buffered=True)

mycursor_get_pembuka_hai.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'hai'")
mycursor_get_pembuka_halo.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'halo'")
mycursor_get_pembuka_pagi.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'pagi'")
mycursor_get_pembuka_siang.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'siang'")
mycursor_get_pembuka_sore.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'sore'")
mycursor_get_pembuka_malam.execute("SELECT respon FROM tb_respon WHERE jenis = 'pembuka' AND jenis_tbh = 'malam'")

mycursor_get_respon_menu = mydb.cursor(buffered=True)
mycursor_get_respon_pesan = mydb.cursor(buffered=True)
mycursor_get_respon_total = mydb.cursor(buffered=True)
mycursor_get_respon_ulang = mydb.cursor(buffered=True)
mycursor_get_respon_selesai = mydb.cursor(buffered=True)
mycursor_get_respon_bingung = mydb.cursor(buffered=True)

mycursor_get_respon_menu.execute("SELECT respon FROM tb_respon WHERE jenis = 'menu'")
mycursor_get_respon_pesan.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan'")
mycursor_get_respon_total.execute("SELECT respon FROM tb_respon WHERE jenis = 'total'")
mycursor_get_respon_ulang.execute("SELECT respon FROM tb_respon WHERE jenis = 'ulang'")
mycursor_get_respon_selesai.execute("SELECT respon FROM tb_respon WHERE jenis = 'selesai'")
mycursor_get_respon_bingung.execute("SELECT respon FROM tb_respon WHERE jenis = 'bingung'")

mycursor_get_semua_menu = mydb.cursor(buffered=True)
mycursor_get_semua_menu.execute("SELECT nama FROM tb_menu")

mycursor_get_semua_menu_id = mydb.cursor(buffered=True)
mycursor_get_semua_menu_id.execute("SELECT id FROM tb_menu")

mycursor_get_semua_menu_harga = mydb.cursor(buffered=True)
mycursor_get_semua_menu_harga.execute("SELECT harga FROM tb_menu")
#endregion

# deklarasi variabel
#region
tokenKalimat = ''
salamPembuka = mycursor_get_pembuka_awal.fetchall()
arrayPembuka = [item[0] for item in mycursor_get_pembuka.fetchall()]
arrayMenu = [item[0] for item in mycursor_get_menu.fetchall()]
arrayPesan = [item[0] for item in mycursor_get_pesan.fetchall()]
arrayTotal = [item[0] for item in mycursor_get_total.fetchall()]
arrayUlang = [item[0] for item in mycursor_get_ulang.fetchall()]
arraySelesai = [item[0] for item in mycursor_get_selesai.fetchall()]

responPembukaHai = mycursor_get_pembuka_hai.fetchall()
responPembukaHalo = mycursor_get_pembuka_halo.fetchall()
responPembukaPagi = mycursor_get_pembuka_pagi.fetchall()
responPembukaSiang = mycursor_get_pembuka_siang.fetchall()
responPembukaSore = mycursor_get_pembuka_sore.fetchall()
responPembukaMalam = mycursor_get_pembuka_malam.fetchall()

responMenu = mycursor_get_respon_menu.fetchall()
responPesan = mycursor_get_respon_pesan.fetchall()
responTotal = mycursor_get_respon_total.fetchall()
responUlang = mycursor_get_respon_ulang.fetchall()
responSelesai = mycursor_get_respon_selesai.fetchall()
responBingung = mycursor_get_respon_bingung.fetchall()

daftarMenuMakanan = mycursor_get_menu_makanan.fetchall()
daftarMenuMinuman = mycursor_get_menu_minuman.fetchall()

daftarSemuaMenu = [i[0] for i in mycursor_get_semua_menu.fetchall()]
daftarSemuaMenuId = [i[0] for i in mycursor_get_semua_menu_id.fetchall()]
daftarSemuaMenuHarga = [i[0] for i in mycursor_get_semua_menu_harga.fetchall()]

daftarSemuaMenuSimpel = [i.split()[0] for i in daftarSemuaMenu]

daftarSemuaMenuSimpel = [x.lower() for x in daftarSemuaMenuSimpel]

listKuantitas = []
listNamaMenu = []
listNamaMenuSimpel = []
listHargaMenu = []
listTotalMenu = []
listIdMenu = []
#endregion

# koreksi kata
#region
def words(text): return re.findall(r'\w+', text.lower())
WORDS = Counter(words(open('Sastrawi/Stemmer/data/kata-dasar.txt').read()))
def P(word, N=sum(WORDS.values())):
    # "Probability of `word`."
    return WORDS[word] / N
def correction(word):
    # "Most probable spelling correction for word."
    return max(candidates(word), key=P)
def candidates(word):
    # "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
def known(words):
    # "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)
def edits1(word):
    # "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
    deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
    inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
    return set(deletes + transposes + replaces + inserts)
def edits2(word):
    # "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
#endregion

#define Jaccard Similarity function
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

# create stopword
factoryStop = StopWordRemoverFactory()
stopword = factoryStop.create_stop_word_remover()

# create stemmer
factoryStem = StemmerFactory()
stemmer = factoryStem.create_stemmer()

# list aksi
def textProcessing(inputKalimat):
    stemKalimat   = stemmer.stem(inputKalimat)
    stopKalimat   = stopword.remove(stemKalimat)
    tokenKalimat = stopKalimat.split()

    return tokenKalimat

# salam pembuka
for row in salamPembuka:
  print(row[0])

while 1:
    winner = ''
    kalimatAwal = ''
    inputKalimatAwal = ''
    kataAwal = []

    # masukan pengguna
    inputKalimat = inputKalimatAwal = input('\nBalas: ')

    # text preprocessing dengan Sastrawi
    inputKalimat = textProcessing(inputKalimat)

    # koreksi kalimat
    for x in range(len(inputKalimat)):
        if inputKalimat[x].isnumeric():
            break
        else:
            kataAsli = inputKalimat[x]
            kataKoreksi = correction(inputKalimat[x])
            
            if kataAsli != kataKoreksi:
                while 1:
                    verifKoreksi = ''
                    print("Apakah yang anda maksud adalah '", kataKoreksi, "'?")
                    verifKoreksi = input("Balas: ")
                    verifkoreksi = verifKoreksi.lower()

                    if verifKoreksi == "ya" or verifKoreksi == "y":
                        inputKalimat[x] = kataKoreksi
                        break
                    elif verifKoreksi == "tidak" or verifKoreksi == "t":
                        inputKalimat[x] = kataAsli
                        break
                    else:
                        print("Saya tidak mengerti maksud anda. Mohon ulangi kembali.")

        
    # menghitung nilai kecocokan dengan jaccard
    valuePembuka = jaccard(inputKalimat, arrayPembuka)
    valueMenu = jaccard(inputKalimat, arrayMenu)
    valuePesan = jaccard(inputKalimat, arrayPesan)
    valueTotal = jaccard(inputKalimat, arrayTotal)
    valueUlang = jaccard(inputKalimat, arrayUlang)
    valueSelesai = jaccard(inputKalimat, arraySelesai)

    # mengurutkan nilai kecocokan
    urutValue = {'pembuka': valuePembuka, 'menu': valueMenu, 'pesan':valuePesan, 'total':valueTotal, 'ulang':valueUlang, 'selesai':valueSelesai}

    # print('\nNilai kecocokan pembuka: ', valuePembuka)
    # print('Nilai kecocokan menu: ', valueMenu)
    # print('Nilai kecocokan pesan: ',valuePesan)
    # print('Nilai kecocokan total: ',valueTotal)
    # print('Nilai kecocokan ulang: ',valueUlang)
    # print('Nilai kecocokan selesai: ',valueSelesai)

    winner = max(urutValue, key=urutValue.get)
    loser = min(urutValue, key=urutValue.get)

    if winner == loser:
        winner = ''

    # print('\nNilai terbesar:', winner, '\n')

    # membalas masukan pengguna
    if winner == 'pembuka':
        if 'hai' in inputKalimat:
            for row in responPembukaHai:
                print(row[0])
        elif 'halo' in inputKalimat:
            for row in responPembukaHalo:
                print(row[0])
        elif 'pagi' in inputKalimat:
            for row in responPembukaPagi:
                print(row[0])
        elif 'siang' in inputKalimat:
            for row in responPembukaSiang:
                print(row[0])
        elif 'sore' in inputKalimat:
            for row in responPembukaSore:
                print(row[0])
        elif 'malam' in inputKalimat:
            for row in responPembukaMalam:
                print(row[0])
        else:
            for row in responPembukaHai:
                print(row[0])
    if winner == 'menu':
        print('Berikut daftar menunya.\n')
        if 'makan' in inputKalimat and 'minum' not in inputKalimat:
            print("Makanan\n")
            print("Nama\t\tHarga")
            for row in daftarMenuMakanan:
                print(row[0], "\t", row[1])
        elif 'minum' in inputKalimat and 'makan' not in inputKalimat:
            print("Minuman\n")
            print("Nama\t\tHarga")
            for row in daftarMenuMinuman:
                print(row[0], "\t\t", row[1])
        else:
            print("Makanan\n")
            print("Nama\t\tHarga")
            for row in daftarMenuMakanan:
                print(row[0], "\t", row[1])

            print("=====================")

            print("Minuman\n")
            print("Nama\t\tHarga")
            for row in daftarMenuMinuman:
                print(row[0], "\t\t", row[1])
    elif winner == 'pesan':
        indexKuantitas = 0
        indexNamaMenu = 0
        indexNamaMenuSimpel = 0
        indexHargaMenu = 0
        indexIdMenu = 0
        
        if listNamaMenu:
            print("Anda telah membuat pesanan. Harap mengulang pesanan apabila terdapat perubahan.")
            continue
        else:
            for x in range(len(inputKalimat)):
                cekKata = inputKalimat[x]

                if cekKata.isnumeric():
                    cekKata = int(cekKata)
                    listKuantitas.insert(indexKuantitas, cekKata)
                    indexKuantitas += 1
                    continue
                else:       
                    for y in range(len(daftarSemuaMenuSimpel)):
                    
                        cekMenu = daftarSemuaMenuSimpel[y]
                        if cekMenu == cekKata:
                            namaMenu = daftarSemuaMenu[y]
                            namaMenuSimpel = daftarSemuaMenuSimpel[y]
                            hargaMenu = daftarSemuaMenuHarga[y]
                            idMenu = daftarSemuaMenuId[y]

                            listNamaMenu.insert(indexNamaMenu, namaMenu)
                            listHargaMenu.insert(indexHargaMenu, hargaMenu)
                            listIdMenu.insert(indexIdMenu, idMenu)
                            listNamaMenuSimpel.insert(indexNamaMenuSimpel, namaMenuSimpel)
                            indexNamaMenu += 1
                            indexNamaMenuSimpel += 1
                            indexHargaMenu += 1
                            indexIdMenu += 1

                            break
        
        if len(listNamaMenu) != len(listKuantitas):
            print('Terdapat kesalahan dalam memasukan pesanan. Harap dicoba kembali.')
            listKuantitas = []
            listNamaMenu = []
            listNamaMenuSimpel = []
            listHargaMenu = []
            listTotalMenu = []
            listIdMenu = []
        elif len(listNamaMenu) == 0 and len(listKuantitas) == 0:
            print('Harap memasukkan pesanan secara langsung.')
            continue
        else:
            for x in range(len(listNamaMenu)):
                menuKuantitas = listKuantitas[x]
                menuHarga = listHargaMenu[x]
                menuTotal = menuKuantitas * menuHarga

                listTotalMenu.insert(x, menuTotal)

            totalSemua = sum(listTotalMenu)

            print('Pesanan diterima. Berikut pesanan anda. \n')
            for x in range(len(listNamaMenu)):
                print('\nNama       :', listNamaMenu[x])
                print('Kuantitas  :', listKuantitas[x])
                print('Total      : Rp.', listTotalMenu[x])
            
            print('\nTotal pesanan: Rp.', totalSemua)

    elif winner == 'total':
        if not listNamaMenu:
            print("Anda belum membuat pesanan. Harap membuat pesanan terlebih dahulu.")
        else:
            for row in responTotal:
                print(row[0])
            
            for x in range(len(listNamaMenu)):
                print('\nNama       :', listNamaMenu[x])
                print('Kuantitas  :', listKuantitas[x])
                print('Total      : Rp.', listTotalMenu[x])
            
            print('\nTotal pesanan: Rp.', totalSemua)
    
    elif winner == 'ulang' :
        print("Apakah anda yakin ingin mengulang pesanan?")
        verifUlang = input('\nBalas: ')
        verifUlang = verifUlang.lower()

        while 1:
            if verifUlang == 'y' or verifUlang == 'ya':
                listKuantitas = []
                listNamaMenu = []
                listNamaMenuSimpel = []
                listHargaMenu = []
                listTotalMenu = []
                listIdMenu = []
                print('Pesanan telah diulang.')
                break
            elif verifUlang == 't' or verifUlang == 'tidak':
                print('Pesanan tidak jadi diulang.')
                break
            else:
                print('Maaf saya tidak mengerti. Mohon ulangi kembali.')

        
    elif winner == 'selesai':
        for row in responSelesai:
            print(row[0])

        if not listNamaMenu:
            print('Anda belum membuat pesanan. Harap membuat pesanan terlebih dahulu.')
        elif listNamaMenu:
            print('Berikut adalah pesanan yang telah anda buat.')

            for x in range(len(listNamaMenu)):
                print('\nNama       :', listNamaMenu[x])
                print('Kuantitas  :', listKuantitas[x])
                print('Total      : Rp.', listTotalMenu[x])
            
            print('\nTotal pesanan: Rp.', totalSemua)

            while 1:
                print('Apakah anda yakin telah selesai membuat pesanan?')
                konfirmPesanan = input('Balas: ')

                konfirmPesanan = konfirmPesanan.lower()

                if konfirmPesanan == 'y' or konfirmPesanan == 'ya':
                    print('Pesanan dibuat atas nama siapa?')
                    namaPesanan = input('Balas: ')

                    tanggal_waktu_sekarang = datetime.now()
                    formatTanggal = tanggal_waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')

                    sql_insert_pesanan = mydb.cursor(buffered=True)
                    sql_get_id_pesanan = mydb.cursor(buffered=True)
                    sql_insert_detail_pesanan = mydb.cursor(buffered=True)

                    sql_insert_pesanan.execute("INSERT INTO tb_pesanan (tanggal_waktu, nama_pengguna, total_harga) VALUES ('{0}', '{1}', {2})".format(formatTanggal, namaPesanan, totalSemua))
                    mydb.commit()

                    sql_get_id_pesanan.execute("SELECT id FROM tb_pesanan WHERE tanggal_waktu = '{0}' AND nama_pengguna = '{1}'".format(formatTanggal, namaPesanan))
                    
                    idPesanan = [i[0] for i in sql_get_id_pesanan.fetchall()]

                    for x in range(len(listNamaMenu)):
                        sql_insert_detail_pesanan.execute("INSERT INTO tb_detail_pesanan (id_pesanan, id_menu, kuantitas, harga_satuan, total) VALUES ({0}, {1}, {2}, {3}, {4})".format(idPesanan[0], listIdMenu[x], listKuantitas[x], listHargaMenu[x], listTotalMenu[x]))
                        mydb.commit()

                    print('Pesanan telah dicatat ke sistem. Terimakasih!')

                    listKuantitas = []
                    listNamaMenu = []
                    listNamaMenuSimpel = []
                    listHargaMenu = []
                    listTotalMenu = []
                    listIdMenu = []

                    break

                elif konfirmPesanan == 't' or konfirmPesanan == 'tidak':
                    print('Pesanan tidak jadi dicatat ke sistem. Mohon cek kembali pesanan.')
                    break
                else:
                    print('Mohon maaf saya tidak mengerti. Mohon ulangi kembali.')
                    continue


       
    elif winner == '':
        # apabila tidak ada yang cocok
        for row in responBingung:
            print(row[0])


