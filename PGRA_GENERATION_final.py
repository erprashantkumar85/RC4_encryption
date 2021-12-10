# The initial state vector array
S = [i for i in range(0, 16)]
print("S : ", S)

key_list = [12, 3, 4]
print("Key list : ", key_list)
print(" ")

print("---------------------------------------------------------")


# Perform the KSA algorithm
def KSA():
    j = 0
    N = len(S)

    print(N)

    # Iterate over the range [0, N]
    for i in range(0, N):
        # Find the key
        j = (j + S[i] + key_list[i % len(key_list)]) % N

        # Update S[i] and S[j]
        S[i], S[j] = S[j], S[i]
        print(i, " ", end="")

        # Print S
        print(S)

    initial_permutation_array = S

    print(" ")
    print("The initial permutation array is : ",
          initial_permutation_array)


print("KSA iterations : ")
print(" ")
KSA()
print(" ")

print("---------------------------------------------------------")


# Perform PGRA algorithm
def PGRA():
    N = len(S)
    i = j = 0
    global key_stream
    key_stream = []

    # Iterate over [0, length of pt]
    for k in range(0, 5):
        i = (i + 1) % N
        j = (j + S[i]) % N

        # Update S[i] and S[j]
        S[i], S[j] = S[j], S[i]
        print(k, " ", end="")
        print(S)
        t = (S[i] + S[j]) % N
        key_stream.append(S[t])

    # Print the key stream
    print("Key stream : ", key_stream)
    print(" ")


print("PGRA iterations : ")
print(" ")
PGRA()


print("---------------------------------------------------------")
