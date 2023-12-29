import fungsi

# ----------------------------------------------------
# ===================== nomor 3 ======================
# ----------------------------------------------------
def soalNomor3(jml):
    soal = fungsi.buatMatrik(jml)
    print('-'*30)
    print("\n soal no 3 :")
    fungsi.cetakMatrik(soal)

    # cari diagonal utama dan diagonal min utama
    diagonalUtama = fungsi.buatDiagonal(0, soal, '+')
    diagonalMinUtama = fungsi.buatDiagonal(0, soal, '-')

    # mengurangi hasil perkalian diagonal utama dengan hasil perkalian diagonal minUtama
    hasilPengurangan = fungsi.kalikanArray(diagonalUtama) - fungsi.kalikanArray(diagonalMinUtama)
    determinan = 1/hasilPengurangan
    # print( determinan)
    # membalikan matrik baris 1 kolom 1 ke baris 2 kolom 2 (adjoin)
    a = []  
    b = []
    a.append(soal[1][1])
    a.append(-soal[0][1])
    b.append(-soal[1][0])
    b.append(soal[0][0])

    adjoind = [a, b]
    print('\n cetak adjoind')
    fungsi.cetakMatrik(adjoind)

    c = []
    d = []

    c.append(adjoind[0][0] * determinan)
    c.append(adjoind[0][1] * determinan)

    d.append(adjoind[1][0] * determinan)
    d.append(adjoind[1][1] * determinan)

    print('...........JAWABANNYA ............:')
    # mengalikan hasil pengurangan deng an masing-masing isi matrik
    jawaban = [c, d]
    
    fungsi.cetakMatrik(jawaban)


# ----------------------------------------------------------
# ======================== nomor 4==========================
# ----------------------------------------------------------
def soalNomor4(jml):
    soal3 = fungsi.buatMatrik(jml)

    print('-'*36)
    # cetak matrik soal
    print("menampilkan soal matrik:")

    fungsi.cetakMatrik(soal3)
    # buat salinan array untuk di olah
    determinan3kali3 = soal3.copy()

    # menambahkan dua matrik pertama di akhir setiap barik matrik
    if len(determinan3kali3[0]) < 3:
        diagonalUtama = fungsi.kalikanArray(fungsi.buatDiagonal(0, determinan3kali3, '+'))
        diagonalMinUtama = fungsi.kalikanArray(fungsi.buatDiagonal(0, determinan3kali3, '-'))
        jawaban = diagonalUtama - diagonalMinUtama
        print('\n-------------- jawaban----------------')
        print(f"{diagonalUtama} - {diagonalMinUtama} = {jawaban}")
    else:
        print('\nJAWABAN :\n1. Tambahkan dua kolom matrik diakhir setiap baris matrik:')
        for det in determinan3kali3:
            det.append(det[0])
            det.append(det[1])

        fungsi.cetakMatrik(determinan3kali3)
        # membuat diagonal
        diagonalUtama = fungsi.kalikanArray(fungsi.buatDiagonal(0, determinan3kali3, '+'))
        diagonalSatu = fungsi.kalikanArray(fungsi.buatDiagonal(1, determinan3kali3, '+'))
        diagonalDua = fungsi.kalikanArray(fungsi.buatDiagonal(2, determinan3kali3, '+'))
        diagonalMinUtama = fungsi.kalikanArray(fungsi.buatDiagonal(0, determinan3kali3, '-'))
        diagonalMinSatu = fungsi.kalikanArray(fungsi.buatDiagonal(-1, determinan3kali3, '-'))
        diagonalMinDua = fungsi.kalikanArray(fungsi.buatDiagonal(-2, determinan3kali3, '-'))
 
        s = ''
        jawabanDeterminan = diagonalUtama + diagonalSatu + diagonalDua - diagonalMinUtama - diagonalMinSatu - diagonalMinDua
        print('\n2. Kalikan setiap diagonal :')
        print(f"{s:<1} {diagonalUtama} + {diagonalSatu} + {diagonalDua} -{diagonalMinUtama} - {diagonalMinSatu} - {diagonalMinDua} ")
        print(f"\n----------------------hasil------------------- ")

        print(f"= {jawabanDeterminan}")