import random
random_number = random.choices(range(1, 11), k = 20)
print (random_number)

angka = int(input("Masukkan angka : "))
if angka % 2 == 0:
    indexListRandomNumber = [index for index, value in enumerate(random_number) if value == angka]
    
    if indexListRandomNumber:
        print(f"Y1 : angka yang dimasukkan berada pada index {indexListRandomNumber}")
    else :
        print("angka tidak ada dalam list atau tidak genap")
else:
    print("Angka yang dimasukkan adalah angka ganjil ")