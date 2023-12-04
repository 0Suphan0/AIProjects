import numpy as np

boyut = int(input("Lütfen matris boyutunu giriniz: "))
birim_matris = np.eye(boyut)
matris = np.random.randint(low=-100, high=100, size=(boyut, boyut))

transpose_matris = np.transpose(matris)

simetrik_mi = np.array_equal(matris, matris.T)
antisimetrik_mi = np.array_equal(matris, -matris.T)

trace = np.trace(matris)

print("Birim Matris:")
print(birim_matris)
print("Rastgele Oluşturulan Matris:")
print(matris)
print("Transpoze Matris:")
print(transpose_matris)
print(f"Simetrik matris: ", simetrik_mi)
print(f"Antisimetrik matris: ",  antisimetrik_mi)
print(f"Matrisin Trace: ", trace)
