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
    # Membuka file stopwords dan menambahkannya kedalam set
    stop = open(filename, 'rt', encoding = 'utf-8') 
    stop_words = set()
    for a in stop: # Membuka file per line
        b = a.replace('\n','') # Menghapus \n untuk menghindari double space
        stop_words.add(b)
    stop.close()

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
    log = open(filepath,'r' , encoding = 'utf-8')
    for a in log : # Membuka file txt per line
        for c in a.split():
            d = c.strip(string.punctuation).lower() # Menghpaus trailing dan leading untuk punctuation dan membuatnya huruf kecil
            if d not in stop_words: # Validasi kata jika kata tidak ada di stopwords
                if len(d):
                    if d not in word_freq.keys(): # Jika data sudah ada di list, value + 1, jika tidak, set value = 1
                        word_freq[d] = 1
                    else :
                        word_freq[d] = word_freq[d] + 1
    log.close()
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
    for a in word_freq_pos.keys(): # Iterasi semua keys yang ada di positive
        if not (a in word_freq_neg.keys()): # Jika keys tidak ada di negative, hanya kalkulasi positive / +1
            b = word_freq_pos[a]/word_freq_pos[a] ## Hasilnya 1
            word_ndsi[a] = b
        else : # Jika keys ada di negative, digunakan rumus kalkulasi gabungan
            c = (word_freq_pos[a] - word_freq_neg[a]) / (word_freq_pos[a] + word_freq_neg[a])
            word_ndsi[a] = c
    for b in word_freq_neg.keys(): # Iterasi tiap keys negative
        # Tiap kata neg yang ada di pos sudah terhitung di loop positive tadi
        if not (b in word_ndsi): # Tiap kata neg yang tidak ada di positive hanya gunakan rumus kalkulasi negatif / -1
            c = -(word_freq_neg[b]/word_freq_neg[b]) ## Hasilnya -1
            word_ndsi[b] = c

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
    sorted_value = dict(sorted(word_freq_ndsi.items(), key=lambda item: (item[1]), reverse=False))  # Sort value berdasarkan terkecil ke terbesar
    # LENGKAPI BAGIAN INI
    # simpan daftar kata-kata dan nilai ndsi yang sudah diurutkan tadi ke
    # file ndsi.txt
    ndsi_filename = "ndsi.txt"
    # ... your code
    opened = open(ndsi_filename, 'w', encoding = 'utf-8')
    for a in sorted_value: # Print tiap pasangan kata - value untuk tiap linenya
        print(f"{a} {sorted_value[a]}", file = opened)
    opened.close()
