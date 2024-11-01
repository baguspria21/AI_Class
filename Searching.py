import random
random_number = random.choices(range(1, 10), k = 20)
print (random_number)

ang = int(input("Masukkan angka : "))
if ang % 2 == 0:
    list = [index for index, value in enumerate(random_number) if value == ang]
    
    if list:
        print(f"Y1 : angka yang dimasukkan berada pada index {list}")
    else :
        print("angka tidak ada dalam list atau tidak genap")
else:
    print("Angka yang dimasukkan adalah angka ganjil ")