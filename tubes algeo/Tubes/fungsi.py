def buatMatrik(jml):
    matrik = []
    while True:
        barisMatrik = []
        while True: 
            bar = int(input(f"input barisMatrik ke {len(matrik) + 1} kolom ke {len(barisMatrik)+1} :"))
            barisMatrik.append(bar)
            if len(barisMatrik) == jml:
                break
        matrik.append(barisMatrik)
        if(len(matrik) == jml):
            break
    return matrik
def buatDiagonal(n, matrik, operasi):
    diagonal = []
    for index, data in enumerate(matrik):
        if operasi == '+':
            diagonal.append(data[index + n])
        else :
            diagonal.append(data[-1 + (-index) + n])
    return diagonal

# fungi operasi array
def kalikanArray(arr):
    hasil = 1
    for angka in arr:
        hasil *= angka
    return hasil

# fungsi mencetak diagonal
def cetakDiagonal(diag):
    id = 0
    while id < len(diag):
        print(f"{diag[id]}", end = ' ')
        id += 1
    print() #mengembalikan enter

# fungsi mencetak matrik
def cetakMatrik(arr):
    for matr in arr:
        cetakDiagonal(matr)
