#membuat bintang segitiga siku-siku


count = 1

for i in range(10):
    print("*"*count)
    count +=1


# membuat segitiga bintang segitiga


n = 10

for i in range(1, n + 1):
    print(" " * (n - i), "*"*(2* i -1))