import fungsi
import jawaban
import os
import numpy as su

os.system("cls")

while True:
    print('-'*35)
    pilihan=input('''
    menu:
    1.penjumlahan dan pengurangan matriks
    2.matriks transpos
    3.matriks balikan
    4.determinan
    5.sistem persamaan linier
    6.keluar
    Pilihan:''')
    if pilihan=='1':
        x=input('''
        1.penjumlahan matriks
        2.pengurangan matriks
        pilih:''')
        if x=='1':
            print('Matriks A:')
            a11,a12=map(float,input('matriks a11, a12:').split())
            a21,a22=map(float,input('Matriks a21, a22:').split())
            A=su.array([[a11,a12],
                        [a21,a22]])
            print(A)
            print('Matriks B:')
            b11,b12=map(float,input('matriks b11, b12:').split())
            b21,b22=map(float,input('matriks b21, b22:').split())
            B=su.array([[b11,b12],
                        [b21,b22]])
            print(B)
            AB=A+B
            print('outpot:')
            print(AB)
        elif x=='2':
            print('Matriks A:')
            b11,b12=map(float,input('matriks b11, b12:').split())
            b21,b22=map(float,input('matriks b21, b22:').split())
            A=su.array([[a11,a12],
                        [a21,a22]])
            print(A)
            print('Matriks B:')
            b11,b12=map(float,input('matriks b11, b12:').split())
            b21,b22=map(float,input('matriks b21, b22:').split())
            B=su.array([[b11,b12],
                        [b21,b22]])
            print(B)
            AB=A-B
            print('outpot:')
            print(AB)
    elif pilihan=='2':
        y=input('''
        1.matriks 2x2
        2.matriks 3x3
        pilih:''')
        if y=='1':
            print('matriks A:')
            a11,a12=map(float,input('masukan a11, a12:').split())
            a21,a22=map(float,input('Masukan a21, a22:').split())
            A=su.array([[a11, a12],
                        [a21, a22]])
            print(A)
            B=su.transpose(A)
            print('Transpos Matriks A :')
            print(B)

        elif y=='2':
            print('matriks A:')
            a11,a12,a13=map(float,input('masukan a11, a12, a13:').split())
            a21,a22,a23=map(float,input('Masukan a21, a22, a23:').split())
            a31,a32,a33=map(float,input('masukan a31, a32, a33:').split())
            A=su.array([[a11, a12, a13],
                        [a21, a22, a23],
                        [a31, a32, a33]])
            print(A)
            B=su.transpose(A)
            print('Matriks A`:')
            print(B)

    elif pilihan=='5':
        a11,a12,b1=map(float,input('masukan x1,x2,b1:').split())
        a21,a22,b2=map(float,input('Masukan x1,x2,b2').split())
        A=su.array([[a11,a12,b1],
                    [a21,a22,b2]])
        print('Matriks:')
        print(A)
        r11=a11/a11
        r12=a12/a11
        r13=b1/a11
        r21=a21-a21*r11
        r22=a22-a21*r12
        r23=b2-a21*r13
        print('eliminasi pertama')
        print([r11,r12,r13])
        print([r21,r22,r23])
        q1=r21/r22
        q2=r22/r22
        q3=r23/r22
        s1=r11-r12*q1
        s2=r12-r12*q2
        s3=r13-r12*q3
        print('eliminasi kedua')
        print([s1,s2,s3])
        print([q1,q2,q3])
        print('solusi')
        print('x1:',s3)
        print('x2:',q3)
    elif pilihan == '3':
        jawaban.soalNomor3(2)
    elif pilihan == '4':
        jenisMatrik = input('''
                1.matriks 2x2
                2.matriks 3x3
                pilih:''')
        if jenisMatrik == '1':
            jawaban.soalNomor4(2)
        if jenisMatrik == '2':
            jawaban.soalNomor4(3)
    # lanjut = input('lanjut soal berikutnya? : (y / n)')
    # if lanjut != 'y':
    #     os.system('cls')
    #     break
    elif pilihan == '6':
        break
print('terimakasih...')

    # def inputt():
        





























