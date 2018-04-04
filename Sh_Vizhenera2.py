def h_line0(): return "---------------------------------------------------------------"


def h_line1(): return "---------------------Cryptography_by_#571----------------------"


def c_vishener():
    #     0      1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21
    arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    #       22   23   24   25
    print()

    def switch(n):
        while n < 26:
            for i in arr:
                if i == arr[0]:
                    print(end="|")
                print(i, end="|")
            arr.append(arr[0])
            arr.remove(arr[0])
            print()
            n += 1

    switch(0)
    print()
    print(h_line0() + "\n" + h_line1() + "\n" + h_line0())
    print("1) Create the Crypt and Key files")
    print("2) Create the Crypt and Key files (Disposable)")
    print("3) Read the Crypt-file with Key-file")
    print("4) Read the Crypt-text with Key\n")
    try:
        answer = int(input(">> Choose the Number: "))
        print()
        if answer == 1:
            with open("key.txt", "w") as file_key:
                m = input("Write the text: ").upper()
                k = input("Write the key: ").upper()
                k *= len(m) // len(k) + 1
                file_key.write(k)
            with open("crypt.txt", "w") as file_crypt:
                c = ""
                for i, j in enumerate(m):
                    gg = (ord(j) + ord(k[i]))
                    c += chr(gg % 26 + ord('A'))
                print()
                print("Encrypted message: " + str(c))
                file_crypt.write(c)
            v = ""
            for i, j in enumerate(c):
                gg = (ord(j) - ord(k[i]))
                v += chr(gg % 26 + ord('A'))
            print("Decrypted message: " + str(v) + "\n")
            print("Encrypted file: crypt.txt")
            print("Key-file: key.txt\n")
        elif answer == 2:
            with open("key.txt", "w") as file_key:
                m = input("Write the text: ").upper()
                length = len(m)
                import random
                k = ""
                for i in range(length):
                    rand = random.randint(0, 25)
                    k += arr[rand]
                print("Key: " + k)
                file_key.write(k)
            with open("crypt.txt", "w") as file_crypt:
                c = ""
                for i, j in enumerate(m):
                    gg = (ord(j) + ord(k[i]))
                    c += chr(gg % 26 + ord('A'))
                print()
                print("Encrypted message: " + str(c))
                file_crypt.write(c)
            v = ""
            for i, j in enumerate(c):
                gg = (ord(j) - ord(k[i]))
                v += chr(gg % 26 + ord('A'))
            print("Decrypted message: " + str(v) + "\n")
            print("Encrypted file: crypt.txt")
            print("Key-file: key.txt\n")
        elif answer == 3:
            with open("crypt.txt", "r") as file_crypt:
                c = file_crypt.read()
            with open("key.txt", "r") as file_key:
                k = file_key.read()
            v = ""
            for i, j in enumerate(c):
                gg = (ord(j) - ord(k[i]))
                v += chr(gg % 26 + ord('A'))
            print("Encrypted file: crypt.txt")
            print("Key-file: key.txt\n")
            print("Decrypted message: " + str(v) + "\n")
        elif answer == 4:
            c = input("Write the Crypt-text: ").upper()
            k = input("Write the Key: ").upper()
            v = ""
            for i, j in enumerate(c):
                gg = (ord(j) - ord(k[i]))
                v += chr(gg % 26 + ord('A'))
            print("\nDecrypted message: " + str(v) + "\n")
        else:
            print("Number is not Defined!")
    except ValueError:
        print("[x] Error!")
        print("Write only Integer Numbers!\n")
    except FileNotFoundError:
        print("[x] Error!")
        print("Crypt/Key Files is not Defined!\n")


c_vishener()
