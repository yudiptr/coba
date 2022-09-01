# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

# lengkapi fungsi berikut
def load_stop_words(filename):
    """
    Parameters
    ----------
    filename : string
        nama file yang menyimpan daftar stopwords.
        Di soal, nama default-nya adalah stopwords.txt

    Returns
    -------
    stop_words : set
        himpunan stopwords (unik)

    Fungsi menerima nama file yang berisi daftar stopwords,
    kemudian memuat semua stopwords ke dalam struktur data
    set. Perhatikan bahwa semua stopwords yang ada di dalam
    file sudah dalam bentuk huruf kecil semua.
    """
    # membuka file stopwords perline dan menghapus \n agar tidak double space
    stop_words = set()
    stopword = open(filename, encoding = 'utf-8')
    log_word = stopword.readlines() # Membaca file yang dibuka per line
    for a in log_word:
        for b in a.split():
            if b[-2:] == '\n':
                stop_words.add(b[:-2])
            else :
                stop_words.add(b)
    stopword.close()
    return stop_words

# lengkapi fungsi berikut
def count_words(filepath, stop_words):
    """
    Parameters
    ----------
    filepath : string
        path atau lokasi dari file yang berisi sekumpulan
        kalimat-kalimat yang memiliki polaritas sentiment,
        yaitu rt-polarity.neg atau rt-polarity.pos

    stop_words : set
        himpunan stopwords

    Returns
    -------
    word_freq : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut.

    Fungsi ini akan scan semua baris (semua kalimat) yang
    ada di file dan kemudian mengakumulasikan frekuensi dari
    setiap kata yang muncul pada file tersebut.

    Contoh
    ------
    Jika isi dari file adalah:

        I just watched a good movie
        wow! a good movie
        a good one

    Fungsi akan mengembalikan dictionary:
        {'i':1, 'just':1, 'watched':1, 'a':3, 'good':3,
         'movie':2, 'wow!':1, 'one':1}

    Notes
    -----
    1. stopwords diabaikan
    2. karakter tanda baca seperti , . / dan sebagainya juga
       diabaikan (gunakan string.punctuation di library string)
    """
    word_freq = {}
    with open(filepath, encoding = 'utf-8') as op_file:
        for a in op_file: # membuka file perbaris
            b = a.split() # Memisahkan tiap kata dalam baris
            for c in b:
                if len(c.strip(string.punctuation)) > 0:
                    if (c.strip(string.punctuation) not in stop_words): # Validasi tiap kata jika kata tidak ada di stopwords, kalau ada valuenya + 1
                        if (c.strip(string.punctuation) not in word_freq):
                            word_freq[c.strip(string.punctuation)] = 1
                        else:
                            word_freq[c.strip(string.punctuation)] = word_freq[c.strip(string.punctuation)] + 1
    return word_freq

# lengkapi fungsi berikut
def compute_ndsi(word_freq_pos, word_freq_neg):
    """
    Parameters
    ----------
    word_freq_pos : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.pos
    word_freq_neg : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah frekuensi (int) dari kemunculan
        kata tersebut. Frekuensi dari kata dihitung dari
        file rt-polarity.neg

    Returns
    -------
    word_ndsi : dictionary
        sebuah dictionary, dimana key merupakan kata (string)
        dan value adalah NDSI score (float)

    Notes
    -----
    NDSI dari sebuah kata dihitung dengan:

              word_freq_pos[word] - word_freq_neg[word]
              -----------------------------------------
              word_freq_pos[word] + word_freq_neg[word]

    Jika kata tidak ditemukan pada salah satu dictionary,
    frekuensi kata tersebut adalah 0.

    Contoh
    ------
    Jika word_freq_neg = {'bad':10, 'worst':5, 'good':1} dan
         word_freq_pos = {'good':20, 'nice':5, 'bad':2},

    maka word_ndsi = {'bad':-0.67, 'worst':-1, 'good':0.90, 'nice':1}

    """
    word_ndsi = {}
    for positive in word_freq_pos: # Iterasi tiap key di positive dan cek apakah ada di negatif juga atau tidak
        if positive in word_freq_neg:
            word_ndsi[positive] = (word_freq_pos[positive] - word_freq_neg[positive]) / (word_freq_pos[positive] + word_freq_neg[positive])
        else :
            word_ndsi[positive] = 1 
    for negative in word_freq_neg: # Iterasi tiap key di negative dan cek apakah ada di positif juga atau tidak
        if negative in word_freq_pos:
            word_ndsi[negative] = (word_freq_pos[negative] - word_freq_neg[negative]) / (word_freq_pos[negative] + word_freq_neg[negative])
        else :
            word_ndsi[negative] = -1
    return word_ndsi

# Fungsi berikut sudah selesai. Anda tidak perlu implementasikan
def show_ndsi_histogram(word_ndsi):
    """
    Parameters
    ----------
    word_ndsi : dictionary
        sebuah dictionary, dimana key adalah kata (string)
        dan value adalah NDSI score (float) dari kata tersebut.

    Returns
    -------
    None.

    Plot histogram dari semua NDSI scores yang dihasilkan

    """
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")




if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi
    # word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # LENGKAPI BAGIAN INI
    # urutkan pasangan kata dan skor ndsi yang ada
    # di word_freq_ndsi berdasarkan nilai ndsi saja, dari terkecil
    # ke yang terbesar

    # ... your code

    # LENGKAPI BAGIAN INI
    # simpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # file ndsi.txt
    # ... your code
    sort_value = dict(sorted(word_freq_ndsi.items(), key=lambda item: (item[1]), reverse=False)) 
    ndsi_filename = "ndsi.txt"
    with open(ndsi_filename, 'w', encoding = 'utf-8') as output:
        for a,b in sort_value.items():
            print(a,b, file = output)

