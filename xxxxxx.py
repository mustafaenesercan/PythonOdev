# Değer döndürmeyen

def sayHello(name):
    print("Hoşgeldin:", name)


# Değer döndüren metodlar

def toplama(a, b):
    return a + b


def carpma(a, b):
    return a * b


def bolme(a, b):
    return a / b


def cikarma(a, b):
    return a - b


# Recursive Fonksiyon

def asalSayi():
    sayi = int(input("Lütfen Bir Sayı Giriniz:"))
    asalMi = True

    if sayi == 1:
        print("Asal Sayı Değildir!")
        return

    for deger in range(2, sayi):

        if (sayi % deger == 0):
            asalMi = False

    if asalMi:
        print("ASAL SAYI!")
    else:
        print("ASAL SAYI DEĞİLDİR!")


# Lambda örneği

def üs(n):
    return lambda a: a ** n


# List örneği

def bolenBulma():
    sayi = int(input("Lütfen Bir Sayı Giriniz:"))
    bolen = []

    for i in range(1, sayi + 1):
        if sayi % i == 0:
            bolen.append(i)
    print("Girdiğiniz Sayının Pozitif Bölenleri:{}".format(bolen))


print("Programda ulaşılabilecek işlemler:\n1)Ekrana Girilen İsime Göre Merhaba Yazdırma"
      "\n2)Dört İşlem"
      "\n3)Asal Sayı Bulma"
      "\n4)Üs Bulma"
      "\n5)Bolen Bulma")

while True:
    user = int(input("Lütfen Yapmak İstediğiniz işlemi Seçiniz:"))
    if (user > 5 or user < 1):
        print("Lütfen Geçerli Bir işlem Giriniz!")

    else:
        if (user == 1):
            isim = input("Lütfen İsminizi Giriniz:")
            sayHello(isim)
            break
        elif (user == 2):

            print(
                "Dört İşlem Bölümüne Hoşgeldiniz:\nAşağıda ki işlemlerden bir tanesini yanında verilen numaraya göre seçiniz:"
                "\n1)Toplama"
                "\n2)Çıkarma"
                "\n3)Çarpma"
                "\n4)Bölme")

            while True:
                choose = int(input("Hangi İşlemi Seçmek İstersiniz:"))
                if (choose > 4 or choose < 1):
                    print("Geçersiz İşlem!!")
                else:
                    if (choose == 1):
                        print("Toplama İşlemine Hoşgeldiniz!!")
                        a = int(input("Sayı1:"))
                        b = int(input("Sayı2:"))
                        print("Sonuç:", toplama(a, b))
                        break
                    elif (choose == 2):
                        print("Çıkarma İşlemine Hoşgeldiniz!!")
                        a = int(input("Sayı1:"))
                        b = int(input("Sayı2:"))
                        print("Sonuç:", cikarma(a, b))
                        break
                    elif (choose == 3):
                        print("Çarpma İşlemine Hoşgeldiniz!!")
                        a = int(input("Sayı1:"))
                        b = int(input("Sayı2:"))
                        print("Sonuç:", carpma(a, b))
                        break
                    elif (choose == 4):
                        print("Bölme İşlemine Hoşgeldiniz!!")
                        a = int(input("Sayı1:"))
                        b = int(input("Sayı2:"))
                        print("Sonuç:", bolme(a, b))
                        break
        elif (user == 3):
            asalSayi()
        elif (user == 4):
            user = int(input("Kaçıncı Dereceden üs almak istersiniz:"))
            x = üs(user)
            userSayi = int(input("Hangi Sayınının üssünü almak istersiniz:"))
            print("{}**{}={}".format(userSayi, user, x(userSayi)))
        elif (user == 5):
            bolenBulma()
