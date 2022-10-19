
######################################################################
# FUNGSI UNTUK MEMBACA FILE DAN MENAMPILKAN DATA CSV

# LANGKAH PROGRAM NO 2
def baca_file(file):
    f = open(file).readlines()
    data = []
    for line in f:
        data = data+[csvtoarray(line)]
    return data


def csvtoarray(Arr):
    arr_baru = []
    idx = 0
    temp = 0

    for i in range(1, len(Arr)):
        if(i == len(Arr)-1):
            arr_baru += [Arr[temp:i]]

            if(Arr[-1:] != "\n"):
                arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

        else:
            if(Arr[i] == ';'):
                idx += 1
                string = Arr[temp:i]

                arr_baru = arr_baru+[string]
                temp = i+1
    return arr_baru


# lANGKAH PROGRAM NO 1 [1]
def show_data(data):
    # MENAMPILKAN DATA CSV
    final_arr = []
    for i in range(7):
        temp_arr = []
        for j in range(len(data)):
            temp_arr += [data[j][i]]
        final_arr += [temp_arr]
        # print(temp_arr)
    arr_len_max = []
    for i in range(len(final_arr)):
        len_max = len(str(final_arr[i][0]))
        for j in range(len(data)):
            if len_max < len(str(final_arr[i][j])):
                len_max = len(str(final_arr[i][j]))
        arr_len_max += [len_max]
    # print nya
    for i in range(len(data)):
        print(f'{data[i][0]}'+(arr_len_max[0] - len(str(data[i][0])))*' '+' | '+f'{data[i][1]}'+(arr_len_max[1] - len(str(data[i][1])))*' '+' | '+f'{data[i][2]}'+(
            arr_len_max[2] - len(str(data[i][2])))*' '+' | '+f'{data[i][3]}'+(arr_len_max[3] - len(str(data[i][3])))*' '+' | '+f'{data[i][4]}'+(arr_len_max[4] - len(str(data[i][4])))*' '+' | '+f'{data[i][5]}'+(arr_len_max[5] - len(str(data[i][5])))*' '+' | '+f'{data[i][6]}')
######################################################################


######################################################################
# LANGKAH PROGRAM NO 3
# Pengurutan data dengan model fungsi rekursif dengan metode insertion sort
def insertion_sort(arr, n):
    # base case
    if n <= 1:
        return

    insertion_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last
######################################################################


######################################################################
# LANGKAH PROGRAM NO 4 dan 1 [2]
# menampilkan data terurut berdasarkan kondisi stok
def show_data_based_on_stock_condition(data):
    arr = []
    for i in range(1, len(data)):
        arr += [int(data[i][6])]
    n = len(arr)
    insertion_sort(arr, n)

    final_arr = []
    for i in range(7):
        temp_arr = []
        for j in range(len(data)):
            temp_arr += [data[j][i]]
        final_arr += [temp_arr]

    arr_len_max = []
    for i in range(len(final_arr)):
        len_max = len(str(final_arr[i][0]))
        for j in range(len(data)):
            if len_max < len(str(final_arr[i][j])):
                len_max = len(str(final_arr[i][j]))
        arr_len_max += [len_max]

    print(f'{data[0][0]}'+(arr_len_max[0] - len(str(data[0][0])))*' '+' | '+f'{data[0][1]}'+(arr_len_max[1] - len(str(data[0][1])))*' '+' | '+f'{data[0][2]}'+(arr_len_max[2] - len(str(data[0][2])))*' '+' | ' +
          f'{data[0][3]}'+(arr_len_max[3] - len(str(data[0][3])))*' '+' | '+f'{data[0][4]}'+(arr_len_max[4] - len(str(data[0][4])))*' '+' | '+f'{data[0][5]}'+(arr_len_max[5] - len(str(data[0][5])))*' '+' | '+f'{data[0][6]}')
    for i in range(n):
        for j in range(len(data)):
            if str(data[j][6]) == str(arr[i]):
                print(f'{data[j][0]}'+(arr_len_max[0] - len(str(data[j][0])))*' '+' | '+f'{data[j][1]}'+(arr_len_max[1] - len(str(data[j][1])))*' '+' | '+f'{data[j][2]}'+(arr_len_max[2] - len(str(data[j][2])))*' '+' | ' +
                      f'{data[j][3]}'+(arr_len_max[3] - len(str(data[j][3])))*' '+' | '+f'{data[j][4]}'+(arr_len_max[4] - len(str(data[j][4])))*' '+' | '+f'{data[j][5]}'+(arr_len_max[5] - len(str(data[j][5])))*' '+' | '+f'{data[j][6]}')

######################################################################


######################################################################

# LANGKAH PROGRAM NO 5 dan 6
def stock_order(data):
    # cek kondisi stok barang
    SO = []
    for i in range(1, len(data)):
        stock_akhir = int(data[i][6])
        stock_awal = int(data[i][4])
        stock_awal = float(data[i][4])
        if stock_akhir <= (0.1 * stock_awal):
            SO += [stock_akhir]

    # menampilkan data berlabel SO (stock order)
    final_arr = []
    for i in range(7):
        temp_arr = []
        for j in range(len(data)):
            temp_arr += [data[j][i]]
        final_arr += [temp_arr]
    arr_len_max = []

    for i in range(len(final_arr)):
        len_max = len(str(final_arr[i][0]))
        for j in range(len(data)):
            if len_max < len(str(final_arr[i][j])):
                len_max = len(str(final_arr[i][j]))
        arr_len_max += [len_max]

    print(f'{data[0][0]}'+(arr_len_max[0] - len(str(data[0][0])))*' '+' | '+f'{data[0][1]}'+(arr_len_max[1] - len(str(data[0][1])))*' '+' | '+f'{data[0][2]}'+(arr_len_max[2] - len(str(data[0][2])))*' '+' | ' +
          f'{data[0][3]}'+(arr_len_max[3] - len(str(data[0][3])))*' '+' | '+f'{data[0][4]}'+(arr_len_max[4] - len(str(data[0][4])))*' '+' | '+f'{data[0][5]}'+(arr_len_max[5] - len(str(data[0][5])))*' '+' | '+f'{data[0][6]}')
    for i in range(len(SO)):
        for j in range(len(data)):
            if str(data[j][6]) == str(SO[i]):
                print(f'{data[j][0]}'+(arr_len_max[0] - len(str(data[j][0])))*' '+' | '+f'{data[j][1]}'+(arr_len_max[1] - len(str(data[j][1])))*' '+' | '+f'{data[j][2]}'+(arr_len_max[2] - len(str(data[j][2])))*' '+' | ' +
                      f'{data[j][3]}'+(arr_len_max[3] - len(str(data[j][3])))*' '+' | '+f'{data[j][4]}'+(arr_len_max[4] - len(str(data[j][4])))*' '+' | '+f'{data[j][5]}'+(arr_len_max[5] - len(str(data[j][5])))*' '+' | '+f'{data[j][6]}')


# Main program
# LANGKAH PROGRAM NO 1
data = baca_file('data_sembako.csv')

while True:
    print('''
    [1]. Tampilkan data
    [2]. Tampilkan data berdasarkan kondisi stok
    [3]. Stock Order
    [4]. Exit
    ''')
    menu_input = input('Pilih nomor menu: ')
    if menu_input == '1':
        show_data(data)
    elif menu_input == '2':
        show_data_based_on_stock_condition(data)
    elif menu_input == '3':
        stock_order(data)
    elif menu_input == '4':
        break
    else:
        print('Masukkan angka 1, 2, 3, atau 4')
