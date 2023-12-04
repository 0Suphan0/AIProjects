import numpy as np

def toplama():
    if satir_bir == satir_iki and sutun_bir == sutun_iki:
        toplam_matris = matris1 + matris2
        print("Toplama Sonucu:")
        print(toplam_matris)
    else:
        print("Toplama işlemi yapılamaz.")
def cikarma():
    if satir_bir == satir_iki and sutun_bir == sutun_iki:
        fark_matris = matris1 - matris2
        print("Çıkarma Sonucu:")
        print(fark_matris)
    else:
        print("Çıkarma işlemi yapılamaz.")
def carpma():
    if sutun_bir == satir_iki:
        carpim_matris = np.dot(matris1, matris2)
        print("Çarpma Sonucu:")
        print(carpim_matris)
    else:
        print("Çarpma işlemi yapılamaz.")
def devrik():
    if satir_bir == sutun_bir:
        ters_matris1 = np.linalg.inv(matris1)
        print("1. Matrisin Tersi:")
        print(ters_matris1)
    else:
        print("1. Matrisin tersi hesaplanamaz.")

    if satir_iki == sutun_iki:
        ters_matris2 = np.linalg.inv(matris2)
        print("2. Matrisin Tersi:")
        print(ters_matris2)
    else:
        print("2. Matrisin tersi hesaplanamaz.")

while(True):
    satir_bir = int(input("1. Matrisin satır sayısını girin: "))
    sutun_bir = int(input("1. Matrisin sütun sayısını girin: "))
    satir_iki = int(input("2. Matrisin satır sayısını girin: "))
    sutun_iki = int(input("2. Matrisin sütun sayısını girin: "))

    matris1 = np.random.randint(low=-10, high=10, size=(satir_bir, sutun_bir))
    matris2 = np.random.randint(low=-10, high=10, size=(satir_iki, sutun_iki))
    print("[MATRISLER]")
    print("1. Matris:")
    print(matris1)
    print("2. Matris:")
    print(matris2)
    toplama()
    cikarma()
    carpma()
    devrik()