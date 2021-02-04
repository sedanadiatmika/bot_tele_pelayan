import json 
import requests
import urllib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import mysql.connector
from itertools import chain
from datetime import datetime
from datetime import timezone
import time

import re
from collections import Counter

TOKEN = "1451883999:AAEZVdmFI4k-_GIttODT4ru8SWD-rg7S44c"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

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
mycursor_get_respon_pesan.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan' and jenis_tbh = 'anda'")
mycursor_get_respon_total.execute("SELECT respon FROM tb_respon WHERE jenis = 'total'")
mycursor_get_respon_ulang.execute("SELECT respon FROM tb_respon WHERE jenis = 'ulang' and jenis_tbh = 'pesan'")
mycursor_get_respon_selesai.execute("SELECT respon FROM tb_respon WHERE jenis = 'selesai' and jenis_tbh = 'pesan'")
mycursor_get_respon_bingung.execute("SELECT respon FROM tb_respon WHERE jenis = 'bingung'")

mycursor_get_semua_menu = mydb.cursor(buffered=True)
mycursor_get_semua_menu.execute("SELECT nama FROM tb_menu")

mycursor_get_semua_menu_id = mydb.cursor(buffered=True)
mycursor_get_semua_menu_id.execute("SELECT id FROM tb_menu")

mycursor_get_semua_menu_harga = mydb.cursor(buffered=True)
mycursor_get_semua_menu_harga.execute("SELECT harga FROM tb_menu")

mycursor_get_respon_pesan_telah = mydb.cursor(buffered=True)
mycursor_get_respon_pesan_telah.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan' and jenis_tbh = 'telah'")
responPesanTelah = mycursor_get_respon_pesan_telah.fetchone()

mycursor_get_respon_pesan_salah = mydb.cursor(buffered=True)
mycursor_get_respon_pesan_salah.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan' and jenis_tbh = 'salah'")
responPesanSalah = mycursor_get_respon_pesan_salah.fetchone()

mycursor_get_respon_pesan_langsung = mydb.cursor(buffered=True)
mycursor_get_respon_pesan_langsung.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan' and jenis_tbh = 'langsung'")
responPesanLangsung = mycursor_get_respon_pesan_langsung.fetchone()

mycursor_get_respon_pesan_terima = mydb.cursor(buffered=True)
mycursor_get_respon_pesan_terima.execute("SELECT respon FROM tb_respon WHERE jenis = 'pesan' and jenis_tbh = 'terima'")
responPesanTerima = mycursor_get_respon_pesan_terima.fetchone()

mycursor_get_respon_ulang_berhasil = mydb.cursor(buffered=True)
mycursor_get_respon_ulang_berhasil.execute("SELECT respon FROM tb_respon WHERE jenis = 'ulang' and jenis_tbh = 'berhasil'")
responUlangBerhasil = mycursor_get_respon_ulang_berhasil.fetchone()

mycursor_get_respon_ulang_tidak = mydb.cursor(buffered=True)
mycursor_get_respon_ulang_tidak.execute("SELECT respon FROM tb_respon WHERE jenis = 'ulang' and jenis_tbh = 'tidak'")
responUlangTidak = mycursor_get_respon_ulang_tidak.fetchone()

mycursor_get_respon_ulang_apa = mydb.cursor(buffered=True)
mycursor_get_respon_ulang_apa.execute("SELECT respon FROM tb_respon WHERE jenis = 'ulang' and jenis_tbh = 'apa'")
responUlangApa = mycursor_get_respon_ulang_apa.fetchone()

mycursor_get_respon_belum = mydb.cursor(buffered=True)
mycursor_get_respon_belum.execute("SELECT respon FROM tb_respon WHERE jenis = 'belum'")
responBelum = mycursor_get_respon_belum.fetchone()

mycursor_get_respon_selesai_tidak = mydb.cursor(buffered=True)
mycursor_get_respon_selesai_tidak.execute("SELECT respon FROM tb_respon WHERE jenis = 'selesai' and jenis_tbh = 'tidak'")
responSelesaiTidak = mycursor_get_respon_selesai_tidak.fetchone()

mycursor_get_respon_selesai_apa = mydb.cursor(buffered=True)
mycursor_get_respon_selesai_apa.execute("SELECT respon FROM tb_respon WHERE jenis = 'selesai' and jenis_tbh = 'apa'")
responSelesaiApa = mycursor_get_respon_selesai_apa.fetchone()

mycursor_get_respon_selesai_berikut = mydb.cursor(buffered=True)
mycursor_get_respon_selesai_berikut.execute("SELECT respon FROM tb_respon WHERE jenis = 'selesai' and jenis_tbh = 'berikut'")
responSelesaiBerikut = mycursor_get_respon_selesai_berikut.fetchone()

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

inputKalimat = ''
winner = ''

reply = ''
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


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def send_message(text, chat_id):
    # text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def echo_all(updates):
    for update in updates["result"]:
        try:
            # text = update["message"]["text"]
            # chat = update["message"]["chat"]["id"]
            insertInbox(update)
            replyInbox(update)
        except Exception as e:
            print(e)
    
    
def insertInbox(update):

    message_id = update["message"]["message_id"]
    username = update["message"]["from"]["username"]
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]
    statusChat = 0

    sql_get_id_max = mydb.cursor(buffered=True)
    sql_get_id_max.execute("SELECT MAX(message_id) FROM tb_inbox WHERE username = '{0}' AND chat_id = {1}".format(username, chat_id))

    idMax = sql_get_id_max.fetchone()
    idMax = idMax[0]

    # print('idMAx : ' + str(idMax))

    if idMax != None:
        sql_get_status_chat = mydb.cursor(buffered=True)
        sql_get_status_chat.execute("SELECT status_chat FROM tb_inbox WHERE username = '{0}' AND chat_id = {1} AND message_id = {2}".format(username, chat_id, idMax))
        statusChat = sql_get_status_chat.fetchone()
        statusChat = statusChat[0]

    if statusChat == 'None':
        statusChat = 0

    # print('status chat terakhir : ' + str(statusChat))

    text = text.lower()

    winner = ''
    # text preprocessing dengan Sastrawi
    inputKalimat = textProcessing(text)


    # koreksi kalimat
    for x in range(len(inputKalimat)):
        if inputKalimat[x].isnumeric():
            break
        else:
            kataAsli = inputKalimat[x]
            kataKoreksi = correction(inputKalimat[x])
            inputKalimat[x] = kataKoreksi

        
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


    if text == '/start':
        winner = 'mulai'
    elif statusChat == 6:
        winner = 'ulang'
    elif statusChat == 7:
        winner = 'selesai'
    elif winner == loser:
        winner = 'bingung'

    print('___________________')
    print('message_id : ' + str(message_id))
    print('username : ' + username)
    print('chat_id : ' + str(chat_id))
    print('text : ' + text)
    print('konteks : ' + winner)
    print('status chat terakhir : ' + str(statusChat))

    sql = "INSERT INTO tb_inbox(message_id, username, chat_id, TEXT, status_chat, konteks) VALUES ({0}, '{1}', {2}, '{3}', {4}, '{5}')".format(message_id, 
    username, chat_id, text, statusChat, winner)

    mycursor_insert_inbox = mydb.cursor(buffered=True)

    mycursor_insert_inbox.execute(sql)
    mydb.commit()


def replyInbox(update):

    message_id = update["message"]["message_id"]

    sql_get_id_pesan = mydb.cursor(buffered=True)

    sql_get_id_pesan.execute("SELECT * FROM tb_inbox WHERE message_id = {0}".format(message_id))

    hasilPesan = sql_get_id_pesan.fetchall()


    for row in hasilPesan:
        username = row[2]
        chat_id = row[3]
        text = row[4]
        statusChat = row[5]
        winner = row[6]
        
    inputKalimat = textProcessing(text)
    
    listKuantitas = []
    listNamaMenu = []
    listNamaMenuSimpel = []
    listHargaMenu = []
    listTotalMenu = []
    listIdMenu = []

    sql_cek_pesanan = mydb.cursor(buffered=True)
    sql_cek_pesanan_baris = mydb.cursor(buffered=True)

    sql_cek_pesanan_baris.execute("SELECT COUNT(*) FROM tmp_pesanan WHERE username = '{0}' AND chat_id = {1}".format(username, chat_id))

    cek_baris = sql_cek_pesanan_baris.fetchone()

    cek_baris = cek_baris[0]

    sql_cek_pesanan.execute("SELECT id_menu, nama_menu, nama_simpel, kuantitas, harga_menu, total_menu FROM tmp_pesanan WHERE username = '{0}' AND chat_id = {1}".format(username, chat_id))
    cek_pesanan = sql_cek_pesanan.fetchall()

    for x in range(cek_baris):
        listKuantitas.append(cek_pesanan[x][3])
        listNamaMenu.append(cek_pesanan[x][1])
        listNamaMenuSimpel.append(cek_pesanan[x][2])
        listHargaMenu.append(cek_pesanan[x][4])
        listTotalMenu.append(cek_pesanan[x][5])
        listIdMenu.append(cek_pesanan[x][0])
    
    totalSemua = sum(listTotalMenu)

    if winner == 'mulai':
        for row in salamPembuka:
            send_message(row[0], chat_id)
    if winner == 'pembuka':
        if 'hai' in inputKalimat:
            for row in responPembukaHai:
                send_message(row[0], chat_id)
        elif 'halo' in inputKalimat:
            for row in responPembukaHalo:
                send_message(row[0], chat_id)
        elif 'pagi' in inputKalimat:
            for row in responPembukaPagi:
                send_message(row[0], chat_id)
        elif 'siang' in inputKalimat:
            for row in responPembukaSiang:
                send_message(row[0], chat_id)
        elif 'sore' in inputKalimat:
            for row in responPembukaSore:
                send_message(row[0], chat_id)
        elif 'malam' in inputKalimat:
            for row in responPembukaMalam:
                send_message(row[0], chat_id)
        else:
            for row in responPembukaHai:
                send_message(row[0], chat_id)
    elif winner == 'menu':
        for row in responMenu:
            send_message(row[0], chat_id)
        if 'makan' in inputKalimat and 'minum' not in inputKalimat:
            message = 'Makanan\n'
            message = message + 'Nama Harga'
            for row in daftarMenuMakanan:
                message = message + '\n' + row[0] + ' ' +  str(row[1])
        elif 'minum' in inputKalimat and 'makan' not in inputKalimat:
            message = 'Minuman\n'
            message = message + 'Nama Harga'
            for row in daftarMenuMinuman:
                message = message + '\n' + row[0] + ' ' + str(row[1])
        else:
            message = 'Makanan\n'
            message = message + 'Nama Harga'
            for row in daftarMenuMakanan:
                message = message + '\n' + row[0] + ' ' +  str(row[1])

            message = message + '\n\nMinuman\n'
            message = message + 'Nama Harga'
            for row in daftarMenuMinuman:
                message = message + '\n' + row[0] + ' ' + str(row[1])
        send_message(message, chat_id)
    elif winner == 'pesan':
        indexKuantitas = 0
        indexNamaMenu = 0
        indexNamaMenuSimpel = 0
        indexHargaMenu = 0
        indexIdMenu = 0

        
        if listNamaMenu:
            send_message(responPesanTelah[0], chat_id)
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
                send_message(responPesanSalah[0], chat_id)
                listKuantitas = []
                listNamaMenu = []
                listNamaMenuSimpel = []
                listHargaMenu = []
                listTotalMenu = []
                listIdMenu = []
            elif not listNamaMenu:
                send_message(responPesanLangsung[0], chat_id)
            else:
                for x in range(len(listNamaMenu)):
                    menuKuantitas = listKuantitas[x]
                    menuHarga = listHargaMenu[x]
                    menuTotal = menuKuantitas * menuHarga

                    listTotalMenu.insert(x, menuTotal)

                totalSemua = sum(listTotalMenu)

                send_message(responPesanTerima[0], chat_id)

                message = ''

                for x in range(len(listNamaMenu)):
                    message = message + '\n\nNama       : ' + listNamaMenu[x]
                    message = message + '\nKuantitas  : ' + str(listKuantitas[x])
                    message = message + '\nTotal        : Rp.' + str(listTotalMenu[x])
                
                message = message + '\n\nTotal pesanan: Rp.' + str(totalSemua)
                
                send_message(message, chat_id)

                sql_insert_tmp_pesanan = mydb.cursor(buffered=True)
            
                for x in range(len(listNamaMenu)):
                    sql_insert_tmp_pesanan.execute("INSERT INTO tmp_pesanan (username, chat_id, id_menu, nama_menu, nama_simpel, kuantitas, harga_menu, total_menu) VALUES ('{0}', {1}, {2}, '{3}', '{4}', {5}, {6}, {7})".format(username, chat_id, listIdMenu[x], listNamaMenu[x], listNamaMenuSimpel[x],  listKuantitas[x], listHargaMenu[x], listTotalMenu[x]))
                    mydb.commit()
    elif winner == 'total':
        if not listNamaMenu:
            send_message(responBelum[0], chat_id)
        else:
            for row in responTotal:
                send_message(row[0], chat_id)
            
            message = ''

            for x in range(len(listNamaMenu)):
                message = message + '\n\nNama       : ' + listNamaMenu[x]
                message = message + '\nKuantitas  : ' + str(listKuantitas[x])
                message = message + '\nTotal        : Rp.' + str(listTotalMenu[x])
                
            message = message + '\n\nTotal pesanan: Rp.' + str(totalSemua)

            send_message(message, chat_id)
    elif winner == 'ulang' :
        if not listNamaMenu:
            send_message(responBelum[0], chat_id)
        else:
            if statusChat == 6:
                if text == 'ya' or text == 'y':
                    sql_delete_tmp_pesanan = mydb.cursor(buffered=True)
                    sql_delete_tmp_pesanan.execute("DELETE FROM tmp_pesanan WHERE username = '{0}' AND chat_id = {1}".format(username, chat_id))
                    mydb.commit()

                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 0 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))                   
                    mydb.commit()

                    send_message(responUlangBerhasil[0], chat_id)
                elif text == 'tidak' or text == 't':
                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 0 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))                    
                    mydb.commit()

                    send_message(responUlangTidak[0], chat_id)
                else:
                    for row in responBingung:
                        send_message(row[0], chat_id)
                    send_message(responUlangApa[0], chat_id)

                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 6 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))
                    mydb.commit()
            else:

                send_message(responUlangApa[0], chat_id)

                sql_update_status_chat = mydb.cursor(buffered=True)
                sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 6 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))
                mydb.commit()

    elif winner == 'selesai':

        if not listNamaMenu:
            send_message(responBelum[0], chat_id)
        elif listNamaMenu:
            if statusChat == 7:
                if text == 'ya' or text == 'y':
                    tanggal_waktu_sekarang = datetime.now()
                    formatTanggal = tanggal_waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')
                    
                    sql_insert_pesanan = mydb.cursor(buffered=True)
                    sql_get_id_pesanan = mydb.cursor(buffered=True)
                    sql_insert_detail_pesanan = mydb.cursor(buffered=True)
                    
                    unix = int(time.time())

                    id_order = str(unix) + username

                    sql_insert_pesanan.execute("INSERT INTO tb_pesanan (id_order, tanggal_waktu, username, chat_id, total_harga) VALUES ('{0}', '{1}', '{2}', {3}, {4})".format(id_order, formatTanggal, username, chat_id, totalSemua))
                    mydb.commit()

                    sql_get_id_pesanan.execute("SELECT id FROM tb_pesanan WHERE id_order = '{0}'".format(id_order))
                    
                    idPesanan = [i[0] for i in sql_get_id_pesanan.fetchall()]

                    for x in range(len(listNamaMenu)):
                        sql_insert_detail_pesanan.execute("INSERT INTO tb_detail_pesanan (id_pesanan, id_menu, kuantitas, harga_satuan, total) VALUES ({0}, {1}, {2}, {3}, {4})".format(idPesanan[0], listIdMenu[x], listKuantitas[x], listHargaMenu[x], listTotalMenu[x]))
                        mydb.commit()

                    sql_delete_tmp_pesanan = mydb.cursor(buffered=True)
                    sql_delete_tmp_pesanan.execute("DELETE FROM tmp_pesanan WHERE username = '{0}' AND chat_id = {1}".format(username, chat_id))
                    mydb.commit()

                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 0 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))                    
                    mydb.commit()

                    send_message('Pesanan telah dicatat ke sistem dengan ID order ' + id_order + '.' ' Terimakasih!', chat_id)
                elif text == 'tidak' or text == 't':

                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 0 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))                    
                    mydb.commit()

                    send_message(responSelesaiTidak[0], chat_id)
                else:
                    sql_update_status_chat = mydb.cursor(buffered=True)
                    sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 7 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))                    
                    mydb.commit()

                    for row in responBingung:
                        send_message(row[0], chat_id)
                    send_message(responSelesaiApa[0], chat_id)
            else:
                send_message('Berikut adalah pesanan yang telah anda buat.', chat_id)

                message = ''

                for x in range(len(listNamaMenu)):
                    message = message + '\n\nNama       : ' + listNamaMenu[x]
                    message = message + '\nKuantitas  : ' + str(listKuantitas[x])
                    message = message + '\nTotal        : Rp.' + str(listTotalMenu[x])
                    
                message = message + '\n\nTotal pesanan: Rp.' + str(totalSemua)

                send_message(message, chat_id)
                send_message(responSelesaiApa[0], chat_id)

                sql_update_status_chat = mydb.cursor(buffered=True)
                sql_update_status_chat.execute("UPDATE tb_inbox SET status_chat = 7 WHERE username = '{0}' AND message_id = {1} AND chat_id = {2}".format(username, message_id, chat_id))
                mydb.commit()
            
    elif winner == 'bingung':
        # apabila tidak ada yang cocok
        for row in responBingung:
            send_message(row[0], chat_id)

def main():
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)

        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
