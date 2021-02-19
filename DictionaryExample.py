ogrenciler = {} # Dictionary Tanimlamasi

ogrenciNumarasi = input("Ogrenci Numarasini Giriniz: ")
ogrenciAdi      = input("Ogrenci Adını Giriniz: ")
ogrenciSoyadi   = input("Ogrenci Soyadını Giriniz: ")
ogrenciTelefonu = input("Ogrenci Telefon Numarasını Giriniz: ")

#Girilen değerlerin objelere aktarilmasi 
ogrenciler[ogrenciNumarasi] = { 
    'Name':ogrenciAdi,
    'Surname':ogrenciSoyadi,
    'PhoneNumber' :ogrenciTelefonu
}
print(ogrenciler)

aramaParametresi = input("Arama yapılacak öğrenci numarasını giriniz")
ogrenci= ogrenciler[aramaParametresi]

print("Aradığınız öğrenci numarasına ait bilgiler {}",ogrenci)