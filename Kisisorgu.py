import psycopg2
from getpass import getpass
from os import system, name


def sonuc():
    query_results = cur.fetchall()
    print("Sorgu Sonucu: ")
    for query_result in query_results:
        print( f"{query_result[1]} {query_result[2]} {query_result[3]} {query_result[4]} {query_result[5]} {query_result[6]} {query_result[7]} {query_result[8]} {query_result[9]} {query_result[10]} {query_result[12]} {query_result[13]} {query_result[14]} {query_result[15]}")
    return


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')



con = psycopg2.connect(database="kisisorgu", user="darkish4@tsorgu", password="TSorgu4128",host="tsorgu.postgres.database.azure.com", port="5432")

print("Mernise Başarıyla Bağlandı!")

cur = con.cursor()


while True:
    print("""    ***********************************************
    *    TSORGU V1.0 HOŞGELDİNİZ!                 *
    *    SEENEOU - ZEENEOU                        *
    *    Sunucu : ABD                             *
    *    1 - TC NO İLE SORGU                      *
    *    2 - ISIM SOYİSİM İLE SORGU (5K+ SONUÇ)   *
    *    3 - ADRES'DEN SORGU                      *
    *    98 - NASIL KULLANILIR ?                  *
    *    99 - ÇIKIŞ                               *
    ***********************************************""")
    islem = input("İslem Seç: ")

    if islem == "99":
        print("ÇIKIŞ YAPILIYOR !!!")
        break
    elif islem == "1":
        tcno = input("TC No Giriniz: ")
        clear()
        cur.execute("""select * from citizen where national_identifier='{}'""".format(tcno))
        query_results = cur.fetchall()
        print("Sorgu Sonucu: ")
        # print(query_results)
        for query_result in query_results:
            print(
                f"{query_result[1]} {query_result[2]} {query_result[3]} {query_result[4]} {query_result[5]} {query_result[6]} {query_result[7]} {query_result[8]} {query_result[9]} {query_result[10]} {query_result[12]} {query_result[13]} {query_result[14]} {query_result[15]}")
            sehir = query_result[11]
            adres1 = query_result[12]
            adres2 = query_result[13]
            adres3 = query_result[14]
            adres4 = query_result[15]
        tcno1 = input("Adres Bilgilerinden Sorgu Yapmak İçin 'E', Geri Dönmek İçin 'G' : ")
        if tcno1 == "g":
            clear()
            continue
        elif tcno1 == "e":
            cur.execute(
                """select * from citizen where address_city='{}' and address_district='{}' and address_neighborhood='{}' and street_address='{}' and door_or_entrance_number='{}'""".format(
                    sehir, adres1, adres2, adres3, adres4))
            query_results = cur.fetchall()
            print("Sorgu Sonucu: ")
            for query_result in query_results:
                print(
                    f"{query_result[1]} {query_result[2]} {query_result[3]} {query_result[4]} {query_result[5]} {query_result[6]} {query_result[7]} {query_result[8]} {query_result[9]} {query_result[10]} {query_result[12]} {query_result[13]} {query_result[14]} {query_result[15]}")
            tcno1 = input("Geri Dönmek İçin 'G' : ")
            if tcno1 == "g":
                clear()
                continue





    elif islem == "2":
        soru = input("Yaşadığı Şehir'i biliyormusunuz?(e veya h) : ")
        if soru == "e":
            sehir = input("Yaşadığı Şehir: ")
            isim = input("İsim : ")
            soyisim = input("Soyisim : ")

            clear()
            cur.execute("""select * from citizen where first='{}' and last='{}' and address_city='{}'""".format(isim,soyisim,sehir))
            sonuc()
            tcno1 = input("Geri Dönmek için 'G' : ")
            if tcno1 == "g" and "G":
                clear()
                continue
        elif soru == "h":

            isim = input("İsim : ")
            soyisim = input("Soyisim : ")
            clear()
            cur.execute("""select * from citizen where first='{}' and last='{}'""".format(isim,soyisim))
            sonuc()
            tcno1 = input("Geri Dönmek için 'G' : ")
            if tcno1 == "g" and "G":
                clear()
                continue
    elif islem == "3":
        sehir = input("Şehir : ")
        adres1 = input("Semt : ")
        adres2 = input("Mahalle : ")
        adres3 = input("Sokak : ")
        adres4 = input("Bina No : ")
        clear()
        cur.execute("""select * from citizen where address_city='{}' and address_district='{}' and address_neighborhood='{}' and street_address='{}' and door_or_entrance_number='{}'""".format(sehir, adres1,adres2,adres3,adres4))
        sonuc()
        tcno1 = input("Geri Dönmek için 'G' : ")
        if tcno1 == "g" and "G":
            clear()
            continue
    elif islem == "98":
        clear()
        print("""
        İSİM SOY İSİM GİBİ SORGULARDA INGILIZCE HARF KULLANINIZ.
        İSİM SOY İSİM SORGUSUNDA ŞEHİR BİLGİSİ EKLENMEZ İSE 5K+'DAN
        FAZLA SONUÇ VEREBİLİR!
        """)