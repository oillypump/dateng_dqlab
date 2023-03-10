# Modul Content : Manipulation with Pandas Part 1
[1. Introduction to Pandas](#introduction-to-pandas)
- [Pendahuluan](#pendahuluan)
- [Memanggil Library Pandas](#memanggil-library-pandas)
- [DataFrame & Series](#dataframe--series)
- [Atribut DataFrame & Series - Part 1](#atribut-dataframe--series---part-1)
- [Atribut DataFrame & Series - Part 2](#atribut-dataframe--series---part-2)
- [Atribut DataFrame & Series - Part 3](#atribut-dataframe--series---part-3)
- [Quiz](#quiz)
- [Creating Series & Dataframe from List](#creating-series--dataframe-from-list)
- [Creating Series & Dataframe from Dictionary](#creating-series--dataframe-from-dictionary)
- [Creating Series & Dataframe from Numpy Array](#creating-series--dataframe-from-numpy-array)
- [Quiz](#quiz-1)

[2. Dataset I/O](#dataset-io)
- [Pendahuluan](#pendahuluan-1)
- [Read Dataset - CSV dan TSV](#read-dataset---csv-dan-tsv)
- [Read Dataset - Excel](#read-dataset---excel)
- [Read Dataset - JSON](#read-dataset---json)
- [Read Dataset - SQL](#read-dataset---sql)
- [Read Dataset - Google BigQuery](#read-dataset---google-bigquery)
- [Write Dataset](#write-dataset)
- [Head & Tail](#head--tail)
- [Quiz](#quiz-2)

[3. Indexing, Slicing and Transforming](#indexing-slicing-dan-transforming)
- [Pendahuluan](#pendahuluan-2)
- [Indexing - Part 1](#indexing---part-1)
- [Indexing - Part 2](#indexing---part-2)
- [Indexing - Part 3](#indexing---part-3)
- [Indexing - Part 4](#indexing---part-4)
- [Indexing - Part 5](#indexing---part-5)
- [Quiz](#quiz-3)
- [Slicing - Part 1](#slicing---part-1)
- [Slicing - Part 2](#slicing---part-2)
- [Quiz](#quiz-4)
- [Transforming - Part 1](#transforming---part-1)
- [Transforming - Part 2](#transforming---part-2)
- [Transforming - Part 3](#transforming---part-3)
- [Transforming - Part 4](#transforming---part-4)
- [Penutup dari Andra](#penutup-dari-andra)

[4. Handling Missing Values](#handling-missing-values)
- [Pendahuluan](#pendahuluan-3)
- [Inspeksi Missing Value](#inspeksi-missing-value)
- [Treatment untuk Missing Value - Part 1](#treatment-untuk-missing-value---part-1)
- [Treatment untuk Missing Value - Part 2](#treatment-untuk-missing-value---part-2)
- [Treatment untuk Missing Value - Part 3](#treatment-untuk-missing-value---part-3)
- [Treatment untuk Missing Value - Part 4](#treatment-untuk-missing-value---part-4)
- [Treatment untuk Missing Value - Part 5](#treatment-untuk-missing-value---part-5)
- [Quiz](#quiz-5)

[5. Mini Project](#mini-project)
- [Pendahuluan](#pendahuluan-4)
- [Project dari Andra](#project-dari-andra)
- [Evaluasi Andra untuk Project yang Telah Disubmit](#evaluasi-andra-untuk-project-yang-telah-disubmit)
- [Hasil Belajarku](#hasil-belajarku)

# Introduction to Pandas #

## Pendahuluan
“Apa kegunaan mempelajari Pandas? Aku tahunya Pandas nama hewan,” kelakarku pada Andra. Benar kan! Lagi-lagi aku menemukan istilah umum tapi punya makna berbeda di dunia data.

“Itu Panda, Aksara. Kalau Pandas berguna untuk melakukan analisis dan pengolahan data dari menengah sampai besar. Coba dibaca saja dulu modulnya biar lebih jelas. Nanti akan ada praktik yang memperjelas,” tukas Andra.

Seperti yang bisa kutebak, aku harus memahami modul dan pembelajaran baru ini sendiri. Karena kulihat Andra sudah melengang pergi setelah memberi intruksi sederhana seperti itu. Tak apa, perlahan aku terbiasa juga belajar mandiri. Walau memang lebih nyaman kalau dibimbing, hehehe.

## Memanggil Library Pandas
Pandas adalah library python open source yang biasanya digunakan untuk kebutuhan data analisis. Pandas membuat Python supaya dapat bekerja dengan data yang berbentuk tabular seperti spreadsheet dengan cara pemuatan data yang cepat, manipulasi data, menggabungkan data, serta ada berbagai fungsi yang lain.

Pertama-tama, harus di import dulu Pandas library di Python script yang telah tersedia.

![pd](../../pict/pandas1.png)


biasanya ketika menggunakan library Pandas, library Numpy juga di-import, sehingga menjadi:

![pd](../../pict/pandas2.png)

**Tugas praktek:**

Pada code editor dapat terlihat kode-kode yang tidak lengkap. Tugasnya sekarang mengimpor library pandas dan juga library numpy dengan mengisi _ _ _ pada masing-masing baris.

## DataFrame & Series

Di Pandas terdapat 2 kelas data baru yang digunakan sebagai struktur dari spreadsheet:

Series: satu kolom bagian dari tabel dataframe yang merupakan 1 dimensional numpy array sebagai basis datanya, terdiri dari 1 tipe data (integer, string, float, dll).
DataFrame: gabungan dari Series, berbentuk rectangular data yang merupakan tabel spreadsheet itu sendiri (karena dibentuk dari banyak Series, tiap Series biasanya punya 1 tipe data, yang artinya 1 dataframe bisa memiliki banyak tipe data).

Contoh:

![df](../../pict/df1.png)

![df](../../pict/df2.png)

**Tugas praktek:**

Pada code editor terlihat kode-kode yang tidak lengkap. Tugasnya sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

## Atribut DataFrame & Series - Part 1
```
Info: Theory dan Predefined code telah diperbarui pada tanggal 12 Mei 2022, pastikan kode yang telah ditulis disesuaikan kembali.
```

Dataframe dan Series memiliki sangat banyak atribut yang digunakan untuk transformasi data, tetapi ada beberapa attribute yang sering dipakai. Di sini series number_list dan dataframe matrix_list pada subbab sebelumnya digunakan kembali.

![attr](../../pict/attr_df1.png)

Tampilan output di console untuk masing-masing penggunaan attribute berikut merupakan hasil setelah menuliskan seluruh kode di code editor dan kemudian mengklik tombol .

**1. Method .info()**

Method .info() digunakan untuk mengecek kolom apa yang membentuk dataframe itu, data types, berapa yang non null, dll. Method ini tidak dapat digunakan pada series, hanya pada dataframe saja.

![attr](../../pict/attr_df2.png)

Output di console untuk penggunaan method .info() ini adalah:

![attr](../../pict/attr_df3.png)

**2. Attribute .shape**

Attribute .shape digunakan untuk mengetahui berapa baris dan kolom, hasilnya dalam format tuple (baris, kolom).

![attr](../../pict/attr_df4.png)

Output di console untuk penggunaan attribute .shape ini adalah:

![attr](../../pict/attr_df5.png)

**3. Attribute .dtypes**

Attribute .dtypes digunakan untuk mengetahui tipe data di tiap kolom. Tipe data object: kombinasi untuk berbagai tipe data (number & text, etc).

![attr](../../pict/attr_df6.png)

Output di console untuk penggunaan attribute .dtypes ini adalah:

![attr](../../pict/attr_df7.png)

**4. Method .astype(nama_tipe_data)**

Method .astype(nama_tipe_data) untuk convert tipe data berdasarkan tipe data seperti: float, int, str, numpy.float, numpy.int ataupun numpy.datetime.

![attr](../../pict/attr_df8.png)

Output di console untuk penggunaan method .astype() ini adalah:

![attr](../../pict/attr_df9.png)

**Tugas praktek:**

Pada code editor dapat terlihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Atribut DataFrame & Series - Part 2
Dataframe dan Series memiliki sangat banyak atribut yang digunakan untuk transformasi data, tetapi ada beberapa attribute yang sering dipakai. Di sini series number_list dan data frame matrix_list digunakan kembali.

![attr](../../pict/attr_df10.png)

Tampilan output di console untuk masing-masing penggunaan attribute berikut merupakan hasil setelah menuliskan seluruh kode di code editor dan kemudian mengklik tombol .

**5. Attribute .copy()**

Attribute .copy() digunakan melakukan duplikat, untuk disimpan di variable yang berbeda mungkin supaya tidak loading data lagi.

![attr](../../pict/attr_df11.png)

Output di console untuk penggunaan attribute .copy() ini adalah:

![attr](../../pict/attr_df12.png)

**6. Attribute .to_list()**

Attribute .to_list() digunakan untuk mengubah series menjadi list dan tidak dapat digunakan untuk dataframe.

![attr](../../pict/attr_df13.png)

Output di console untuk penggunaan attribute .to_list() ini adalah:

![attr](../../pict/attr_df14.png)

**7. Attribute .unique()**

Attribute .unique() digunakan menghasilkan nilai unik dari suatu kolom, hasilnya dalam bentuk numpy array. Attribute ini hanya digunakan pada series saja.

![attr](../../pict/attr_df15.png)

Output di console untuk penggunaan attribute .unique() ini adalah:

![attr](../../pict/attr_df16.png)

**Tugas praktek:**

Pada code editor dapat terlihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Atribut DataFrame & Series - Part 3
Dataframe dan Series memiliki sangat banyak atribut yang digunakan untuk transformasi data, tetapi ada beberapa attribute yang sering dipakai. Di sini series number_list dan data frame matrix_list pada subbab sebelumnya digunakan kembali.

![attr](../../pict/attr_df10.png)

Tampilan output di console untuk masing-masing penggunaan attribute berikut merupakan hasil setelah menuliskan seluruh kode di code editor dan kemudian mengklik tombol .

**8. Attribute .index**

Attribute .index digunakan untuk mencari index/key dari Series atau Dataframe.

![attr](../../pict/attr_df17.png)

Output di console untuk penggunaan attribute .index ini adalah:

![attr](../../pict/attr_df18.png)

**9. Attribute .columns**

Attribute .columns digunakan untuk mengetahui apa saja kolom yang tersedia di dataframe tersebut (hanya digunakan untuk dataframe saja). 

![attr](../../pict/attr_df19.png)

Output di console untuk penggunaan attribute .columns ini adalah:

![attr](../../pict/attr_df20.png)

**10. Attribute .loc**

Attribute .loc digunakan slice dataframe atau series berdasarkan nama kolom dan/atau nama index.

![attr](../../pict/attr_df21.png)

Output di console untuk penggunaan attribute .loc[] ini adalah:

![attr](../../pict/attr_df22.png)

**11. Attribute .iloc**

Attribute .iloc digunakan untuk slice dataframe atau series berdasarkan index kolom dan/atau index.

![attr](../../pict/attr_df23.png)

Output di console untuk penggunaan attribute .iloc[] ini adalah:

![attr](../../pict/attr_df24.png)

### **Tugas praktek:**

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Quiz
Diberikan dataframe
```
matrix = [[1,2,3],
          ['a','b','c'],
          [3,4,5],
          ['d',4,6]]
matrix_list = pd.DataFrame(matrix)
```

Apakah yang akan dihasilkan untuk command berikut?
```
matrix_list.iloc[0:2,2].to_list()
```

## Creating Series & Dataframe from List
Untuk membuat Series atau Dataframe bisa dari berbagai macam tipe data container/mapping di python, seperti list dan dictionary, maupun dari numpy array.

Pada sub bagian ini, kamu akan membuat Series dan Dataframe yang bersumber dari list. Sekadar meninjau bahwa list merupakan sebuah kumpulan data berbagai macam tipe data yang mutable (dapat diganti).

**Series**
Contoh membuat series dari list:

![csdflist](../../pict/csdffromlist1.png)

Output di console:

![csdflist](../../pict/csdffromlist2.png)

**DataFrame**

Contoh membuat dataframe dari list of list:

![csdflist](../../pict/csdffromlist3.png)

Output di console: 

![csdflist](../../pict/csdffromlist4.png)

### Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Creating Series & Dataframe from Dictionary

Untuk membuat Series atau Dataframe bisa dari berbagai macam tipe data container/mapping di python, seperti list dan dictionary, maupun dari numpy array.

Pada sub bagian ini, akan membuat Series dan Dataframe yang bersumber dari dictionary. Sekadar meninjau bahwa, dictionary merupakan kumpulan data yang strukturnya terdiri dari key dan value.

Series

Contoh membuat series dari dictionary:

![cddf](../../pict/csdffromdict1.png)

Output di console:

![cddf](../../pict/csdffromdict2.png)

DataFrame

Contoh membuat dataframe dari dict dengan setiap pasangan key dan value-nya berisi list yang sama panjangnya:

![cddf](../../pict/csdffromdict3.png)

Output di console:

![cddf](../../pict/csdffromdict4.png)

Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Creating Series & Dataframe from Numpy Array

Untuk membuat Series atau Dataframe bisa dari berbagai macam tipe data container/mapping di python, seperti list dan dictionary, maupun dari numpy array.

 

Pada sub bagian ini, akan membuat Series dan Dataframe yang bersumber dari numpy array. Sekadar meninjau bahwa, numpy array kumpulan data yang terdiri atas berbagai macam tipe data, mutable, tapi dibungkus dalam array oleh library Numpy.

Series

Contoh membuat series dari numpy array 1D:

![numpy](../../pict/csdffromnumpy1.png)

Output:

![numpy](../../pict/csdffromnumpy2.png)

DataFrame

Contoh membuat dataframe dari numpy array 2D:

![numpy](../../pict/csdffromnumpy3.png)

Output:

![numpy](../../pict/csdffromnumpy4.png)

### Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas.

## Quiz
Diberikan dataframe

```
arr_df = np.array([[1,2,3,5],
                   [5,6,7,8],
                   ['a','b','9',10]])
df = pd.DataFrame(arr_df)
```
Bagaimana cara mengubah data yang berupa string menjadi angka misal 'a' menjadi 11 dan 'b' menjadi 12?

# Dataset I/O

## Pendahuluan

Aku berhenti sejenak dari bacaan modul dan latihan kuis. Timbul satu pertanyaan yang menggelitikku. Dan, pas sekali aku melihat Andra sedang mampir ke meja di seberangku. Waktu yang tepat untuk memanggilnya dan bertanya.

“Ndra, memangnya file apa saja sih yang bisa dibaca oleh Pandas? Aku penasaran.”

“Saya kirim saja yah lengkapnya ada di link. Coba kamu cek di email,” jawab Andra singkat, padat, jelas.

Sesaat setelah aku bertanya, aku melihat Andra mengutak-atik ponselnya. Semenit kemudian, aku sudah menemukan link di kotak masuk email-ku yang berisi file-file yang bisa diakses Pandas. Aku pun membukanya dan menyimaknya satu per satu:

Pandas menyediakan berbagai method untuk membaca file tersebut hanya dengan dipanggil method itu, code yang lebih simple dan loading yang lebih, tentu saja output nya dapat berupa Series atau Dataframe.

Terdapat sangat banyak file yang dapat dibaca/dapat disimpan oleh Pandas, tapi ada beberapa file yang paling umum dan sering digunakan oleh praktisi data seperti berikut ini:

1. CSV (Comma Separated Values), antar data dalam satu baris dipisahkan oleh comma, ",".
2. TSV (Tab Separated Values), antar data dalam satu baris dipisahkan oleh "Tab".
3. Excel
4. Google BigQuery
5. SQL Query
6. JSON (Java Script Object Notation)

## Read Dataset - CSV dan TSV

CSV dan TSV pada hakikatnya adalah tipe data text dengan perbedaan terletak pada pemisah antar data dalam satu baris. Pada file CSV, antar data dalam satu baris dipisahkan oleh comma, ",". Namun, pada file TSV antar data dalam satu baris dipisahkan oleh "Tab".

Fungsi .read_csv() digunakan untuk membaca file yang value-nya dipisahkan oleh comma (default), terkadang pemisah value-nya bisa di set ‘\t’ untuk file tsv (tab separated values).

**Notes :**
Dataset csv : https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

Dataset tsv : https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv

**Membaca file CSV**

![pdread](../../pict/pdread1.png)

Jika dijalankan akan menghasilkan output di console:

![pdread](../../pict/pdread2.png)

**Membaca file TSV**

![pdread](../../pict/pdread3.png)


Jika dijalankan akan menghasilkan output di console:

![pdread](../../pict/pdread4.png)

Tugas praktek:

Pada code editor dapat kamu lihat kode-kode yang tidak lengkap. Tugas kamu sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

Tampilkanlah tiga data teratas dari kedua jenis file yang telah dibaca!

## Read Dataset - Excel

File Excel dengan ekstensi *.xls atau *.xlsx cukup banyak digunakan dalam menyimpan data. Pandas juga memiliki fitur untuk membaca file excel.

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx

Fungsi .read_excel() digunakan untuk membaca file excel menjadi dataframe pandas.

![pdread](../../pict/pdreadexcel1.png)

Jika dijalankan code di atas akan menghasilkan output di console seperti berikut:

![pdread](../../pict/pdreadexcel2.png)

Tugas praktek:

Pada code editor dapat kamu lihat kode-kode yang tidak lengkap. Tugas kamu sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

Tampilkanlah empat data teratas dari file excel yang telah dibaca!

## Read Dataset - JSON
Method .read_json() digunakan untuk membaca URL API yang formatnya JSON dan mengubahnya menjadi dataframe pandas. Method ini dapat digunakan seperti yang dicontohkan berikut ini:

![pdread](../../pict/pdreadjson1.png)

Dataset JSON: https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json

Jika dengan benar dituliskan code-nya di code editor maka setelah tombol  diklik kemudian akan mendapatkan hasilnya di console seperti berikut:

![pdread](../../pict/pdreadjson2.png)

Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

Tampilkanlah sepuluh data teratas dari file JSON yang telah dibaca!

## Read Dataset - SQL
Fungsi .read_sql() atau .read_sql_query() digunakan untuk membaca query dari database dan translate menjadi pandas dataframe, contoh case ini database sqlite.

Contoh penggunaannya:

![pdread](../../pict/pdreadsql1.png)

Jika menggunakan .read_sql_query

![pdread](../../pict/pdreadsql2.png)

Output:

![pdread](../../pict/pdreadsql3.png)

Jika menggunakan .read_sql

![pdread](../../pict/pdreadsql4.png)

Output:

![pdread](../../pict/pdreadsql5.png)

Terlihat keduanya menghasilkan output yang sama.

## Read Dataset - Google BigQuery

Untuk data yang besar (big data), umumnya digunakan Google BigQuery. Layanan ini dapat digunakan jika telah memiliki Google BigQuery account.

Fungsi .read_gbq() digunakan untuk membaca Google BigQuery table menjadi dataframe pandas.

![pdread](../../pict/pdreadgooglebq1.png)

project_id="XXXXXXXX" adalah ID dari Google BigQuery account.

Output-nya:

![pdread](../../pict/pdreadgooglebq2.png)

## Write Dataset

Dalam bekerja sebagai data scientist/analis setelah dilakukan data cleaning dataset yang sudah rapi tentunya disimpan terlebih dahulu ke dalam media penyimpanan.  

Pandas menyediakan fitur demikian secara ringkas melalui penerapan method pada dataframe/series yang ditabelkan berikut ini:

Method      |    Code
----------  | ------------
.to_csv() → digunakan untuk export dataframe kembali ke csv atau tsv   | CSV ```df.to_csv("csv1.csv", index=False)```   TSV ```df.to_csv("tsv1.tsv", index=False, sep='\t')```
.to_clipboard() → export dataframe menjadi bahan copy jadi nanti bisa tinggal klik paste di excel atau google sheets    | ```df.to_clipboard()```
.to_excel() → export dataframe menjadi file excel   | ```df_excel.to_excel("xlsx1.xlsx", index=False)```
.to_gbq() → export dataframe menjadi table di Google BigQuery   | ```df.to_gbq("temp.test", project_id="XXXXXX", if_exists="fail")``` **temp**: nama dataset, **test**: nama table, if_exists: ketika tabel dengan dataset.table_name yang sama sudah ada, apa action yang ingin dilakukan (**"fail"**: tidak melakukan apa-apa, **"replace"**: membuang tabel yang sudah ada dan mengganti yang baru, **"append"**: menambah baris di tabel tersebut dengan data yang baru)

## Head & Tail

Seperti yang telah dipelajari sebelumnya bahwa ada method .head yang diterapkan pada suatu variabel bertipe pandas dataframe/series.

Method .head ditujukan untuk membatasi tampilan jumlah baris teratas dari dataset. Sementara itu, method .tail ditujukan untuk membatasi jumlah baris terbawah dari dataset.

Secara umum kedua method ini memiliki bentuk

```[nama_dataframe].head(n)``` 

dan 

```[nama_dataframe].tail(n)```

dengan n merupakan jumlah baris yang akan ditampilkan, jika tidak disebutkan n = 5 (sebagai nilai default dari n). 

Tugas Praktek:

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

Berdasarkan file sample_csv.csv cetaklah 3 data teratas dan 3 data terbawah. 

Jika berhasil maka tampilan berikut yang akan kamu peroleh di console.
![ds](../../pict/headtail.png)

## Quiz
Lakukan analisis dengan menggunakan BigQuery karena ada beberapa data BigQuery public datasets yang informasinya akurat dan sudah banyak data point-nya sehingga sudah bisa digunakan.

Tapi masalahnya, ada beberapa data adhoc yang bergantung tim lain yang belum terlalu melek data dan datanya masih disimpan dalam bentuk CSV.

Bagaimana langkah efektif yang dapat diambil untuk melakukan analisis gabungan data dari BigQuery dan CSV?

Hint: coba explore BigQuery public datasets dulu, kamu akan dapati data size yang besar (>1juta baris), akan susah kalau harus di export dan dilakukan analisis di excel.

# Indexing, Slicing, dan Transforming

## Pendahuluan
Aku masih fokus mengutak-atik dokumen yang bisa dibaca oleh Pandas ketika Andra menyahut dari belakangku. “Sudah dipelajari modulnya, Aksara? Apakah sudah cukup paham dasarnya penggunaan basic data of Pandas? Terutama cara bikin dataframe dan data source yang diolah dari Pandas?”

Seperti biasa, Andra ingin memastikan proses belajarku berjalan lancar. Tapi, mumpung ia berada di sini dan aku punya pertanyaan, lebih baik kusampaikan.

“Iya, Ndra. Tapi aku masih agak bingung soal manipulasi data, seperti membuat index, slicing, dan transform tipe data di series maupun dataframe,” ungkapku jujur. Apakah Andra akan membantuku? Aku menunggu responsnya sampai kemudian Andra menarik bangku ke sebelahku.

“Oke, coba sini saya bantu jelaskan.”

Mataku berbinar. Aku tak akan melewatkan kesempatan ini. Aku pun menggeser bangku agar lebih dekat dengan Andra yang siap menampilkan beberapa contoh manipulasi data, terutama membuat index, seperti yang dijelaskan selanjutnya.

## Indexing - Part 1
Index merupakan key identifier dari tiap row/column untuk Series atau Dataframe (sifatnya tidak mutable untuk masing-masing value tapi bisa diganti untuk semua value sekaligus).

Jika tidak disediakan, pandas akan membuat kolom index default secara otomatis sebagai bilangan bulat (integer) dari 0 sampai range jumlah baris data tersebut.

Kolom index dapat terdiri dari:

satu kolom (single index), atau
multiple kolom (disebut dengan hierarchical indexing).
Index dengan multiple kolom ini terjadi karena unique identifier tidak dapat dicapai hanya dengan set index di 1 kolom saja sehingga membutuhkan beberapa kolom yang menjadikan tiap row menjadi unique.

## Indexing - Part 2
Secara default setelah suatu dataframe dibaca dari file dengan format tertentu, index-nya merupakan single index.

Pada sub bab ini akan mencetak index dan kolom yang dimiliki oleh file "https://storage.googleapis.com/dqlab-dataset/sample_csv.csv". Untuk menentukan index dan kolom yang dimiliki oleh dataset yang telah dinyatakan sebagai sebuah dataframe pandas dapat dilakukan dengan menggunakan atribut .index dan .columns.

Untuk lebih jelasnya diberikan oleh kode yang ditampilkan berikut ini:

![idx](../../pict/indexing2_1.png)

Jika dijalankan dengan menekan tombol  maka akan menghasilkan output seperti berikut di console untuk masing-masing indeks dan kolom yang dimiliki oleh dataframe df.

![idx](../../pict/indexing2_2.png)

Tugas praktek:

Pada code editor kamu lihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

Tampilkanlah index dan kolom data teratas dari file TSV "https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv" yang telah dibaca!

Jika kode yang dituliskan telah benar dan kemudian tombol ditekan, maka hasil berikut yang akan kamu peroleh di console.

![idx](../../pict/indexing2_3.png)

## Indexing - Part 3
Di sub bab sebelumnya telah dibahas terkait single index, tentunya pada sub bab ini akan bahas multi index atau disebut juga dengan hierarchical indexing.

Untuk membuat multi index (hierarchical indexing) dengan pandas diperlukan kolom-kolom mana saja yang perlu disusun agar index dari dataframe menjadi sebuah hirarki yang kemudian dapat dikenali.

Pada sub bab sebelumnya telah diberikan nama-nama kolom dari dataframe yang telah dibaca, yaitu:

![idx](../../pict/indexing3_1.png)

dengan output

![idx](../../pict/indexing3_2.png)

Selanjutnya akan membuat multi index dengan menggunakan kolom 'order_id', 'customer_id', 'product_id', dan 'order_date' dengan menggunakan method .set_index(). Mari perhatikan contoh kode yang diberikan berikut ini:

![idx](../../pict/indexing3_3.png)

berikut hasil tampilan dataframe df_x-nya:

![idx](../../pict/indexing3_4.png)

Untuk melihat multi index yang telah diset dapat dilakukan dengan:

![idx](../../pict/indexing3_5.png)

yang memberikan output:

![idx](../../pict/indexing3_6.png)

Perlu diketahui bahwa kumpulan index dari multi index adalah list dari banyak tuples, tuples-nya merupakan kombinasi yang ada dari gabungan index-index tersebut. Dari multi index tersebut juga terdapat atribut levels yang menunjukkan urutan index, dalam case ini 'order_id' > 'customer_id' > 'product_id' > 'order_date'.

![idx](../../pict/indexing3_7.png)

yang menghasilkan output berupa:

![idx](../../pict/indexing3_8.png)

Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai seperti yang diberikan pada contoh di atas. 

Tampilkanlah multi index dari file TSV "sample_tsv.tsv" yang telah dibaca berupa nama dan level index-nya.

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv

Kolom yang menjadi index-nya yaitu 'order_date', 'city', dan 'customer_id'!

Jika di code editor telah dengan benar ditulis kodenya dan kemudian setelah menekan tombol , maka akan memperoleh hasil berikut di console:
![idx](../../pict/indexing3_8.png)

## Indexing - Part 4
Terdapat beberapa cara untuk membuat index, salah satunya adalah seperti yang telah dilakukan pada sub bab sebelumnya dengan menggunakan method .set_index().

Di sub bab ini akan menggunakan assignment untuk menset index dari suatu dataframe. Untuk itu file "sample_excel.xlsx" yang digunakan. Perhatikan code berikut!

![idx](../../pict/indexing4_1.png)

Jika dijalankan dengan mengklik tombol  hasilnya adalah sebagai berikut:

![idx](../../pict/indexing4_2.png)

Note:

Cara yang ditunjukkan oleh baris ketujuh (ke-7) pada code editor di atas hanya berlaku jika index yang di-assign tersebut memiliki panjang yang sama dengan jumlah baris dari dataframe.
Jika ingin kembalikan dataframe ke index default-nya yaitu dari 0 s/d jumlah baris data - 1, maka dapat menggunakan method .reset_index(drop=True), argument drop=True bertujuan untuk menghapus index lama. 
 
Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai. 

Baca kembali file TSV "sample_tsv.tsv" hanya untuk 10 baris pertama. Set index-nya dengan menggunakan nama "Pesanan ke-i" i adalah bilangan bulat dari 1 sampai dengan jumlah baris (10 baris data).

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv

Jika berhasil dijalankan kodenya maka akan tampil hasil berikut:
![idx](../../pict/indexing4_3.png)

## Indexing - Part 5
Jika file yang akan dibaca melalui penggunaan library pandas dapat di-preview terlebih dahulu struktur datanya maka melalui fungsi yang ditujukan untuk membaca file dapat diset mana kolom yang akan dijadikan index.

Fitur ini telah dimiliki oleh setiap fungsi yang digunakan dalam membaca data dengan pandas, yaitu penggunaan argumen index_col pada fungsi yang dimaksud. Untuk jelasnya dapat diperhatikan pada kode berikut ini.

![idx](../../pict/indexing5_1.png)

Dari dataset sample_csv.csv, sample_tsv.tsv, atau sample_excel.xlsx sudah tahu bahwa kolom dataset adalah 'order_id'; 'order_date'; 'customer_id'; 'city'; 'province'; 'product_id'; 'brand'; 'quantity'; and 'item_price'. Sehingga kode di atas digunakan langsung kolom 'order_date' pada saat membaca file-nya.

Jika dijalankan dengan mengklik tombol  maka akan menghasilkan output berikut di console.

![idx](../../pict/indexing5_2.png)

Terlihat bahwa kolom order_date sudah jadi index, dan tentunya jumlah kolom dataframe berkurang satu, yaitu menjadi delapan kolom.

Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai.  

Baca kembali file TSV "sample_tsv.tsv" dan set lah kolom "order_date" dan "order_id" sebagai index_col-nya dan cetaklah dataframe untuk delapan baris pertama. 

Notes : 

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv

Jika berhasil dijalankan kodenya maka akan tampil hasil berikut:
![idx](../../pict/indexing5_3.png)

## Quiz
Diberikan dataframe
```
df_week = pd.DataFrame({'day_number':[1,2,3,4,5,6,7],
                        'week_type':['weekday' for i in range(5)] + ['weekend' for i in range(2)]
                       })
df_week_ix = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
df_week.index = [df_week_ix, df_week['day_number'].to_list()]
df_week.index.names = ['name','num']
```

Ketika code print ```(df_week.index.names)``` ditulis kembali dan kemudian dieksekusi, apakah yang akan dihasilkan melaluiconsole?

## Slicing - Part 1
Slicing - Part 1
Seperti artinya slicing adalah cara untuk melakukan filter ke dataframe/series berdasarkan kriteria tertentu dari nilai kolomnya ataupun kriteria index-nya.

Terdapat 2 cara paling terkenal untuk slicing dataframe, yaitu dengan menggunakan method .loc dan .iloc pada variabel bertipe pandas DataFrame/Series. Method .iloc ditujukan untuk proses slicing berdasarkan index berupa nilai integer tertentu. Akan tetapi akan lebih sering menggunakan dengan method .loc karena lebih fleksibel. 

*Mari ikuti ilustrasi berikut ini.*

Dataset belum dilakukan indexing, jadi slicing berdasarkan nilai kolomnya. Untuk itu "sample_csv.csv" dibaca kembali dan dipraktikkan metode .loc[] dengan mengambil tanggal 1 Januari 2019 dari kolom order_date dan product_id nya adalah P2154 dan P2556.

![slicing](../../pict/slicing1_1.png)

Jika kode di atas dijalankan dengan menekan  diperoleh:

![slicing](../../pict/slicing1_2.png)

Tugas praktek:

Pada code editor dapat dilihat kode-kode yang tidak lengkap. Tugas sekarang adalah mengganti tanda _ _ _ di code editor dengan yang sesuai.  

Baca kembali file TSV "sample_csv.csv" dan slice/filter-lah dataset jika customer_id adalah 18055 dan product_id-nya yaitu P0029, P0040, P0041, P0116, dan P0117. 

Notes :

Dataset: https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

Jika berhasil dijalankan kodenya maka akan tampil hasil berikut:

![slicing](../../pict/slicing1_3.png)

## Slicing - Part 2
Dalam sub bab sebelumnya telah mempelajari bagaimana melakukan slicing/filtering dataset dengan menggunakan method .loc pada kolom dataset.

Sekarang, menerapkan berdasarkan index. Tentu syaratnya adalah dataset sudah dilakukan indexing terlebih dahulu melalui penerapan method .set_index 

Cara 1: Gunakan method .loc seperti yang dicontohkan berikut:

![slicing](../../pict/slicing2_1.png) 

Output cara 1:

![slicing](../../pict/slicing2_2.png) 

Cara 2: Gunakan pd.IndexSlice sebagai varaibel untuk melakukan slicing index

![slicing](../../pict/slicing2_3.png) 

Output cara 2:

![slicing](../../pict/slicing2_4.png) 

Tugas praktek:

Pada code editor dapat terlihat kode-kode yang tidak lengkap. Tugas kamu adalah mengganti tanda _ _ _ di code editor dengan yang sesuai.  

Baca kembali file TSV "sample_csv.csv" dan set terlebih dahulu indexnya yaitu order_date, order_id, dan product_id. Kemudian slice/filter-lah dataset jika order_date adalah 2019-01-01, order_id adalah 1612339 dan product_id-nya yaitu P2154 dan P2159. Gunakanlah cara pertama.

Notes :

Dataset :  https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

Jika berhasil dijalankan kodenya maka akan tampil hasil berikut:
![slicing](../../pict/slicing2_5.png) 

## Quiz
Diberikan variabel

```
sample_csv = pd.read_csv('sample_csv.csv')
sample_csv = sample_csv.set_index(['province','product_id'])
idx = pd.IndexSlice
```

Code mana yang akan menghasilkan semua kolom, dengan filter province = ‘Sulawesi Selatan’ dan product_id dari ‘P3082’ sampai ‘P3357’?


## Transforming - Part 1
Transform adalah ketika mengubah dataset yang ada menjadi entitas baru, dapat dilakukan dengan:

konversi dari satu data type ke data type yang lain,
transpose dataframe,
atau yang lainnya.
Hal yang biasa dilakukan pertama kali setelah data dibaca adalah mengecek tipe data di setiap kolomnya apakah sesuai dengan representasinya. Untuk itu dapat menggunakan atribut .dtypes pada dataframe yang telah kita baca tadi,

```
[nama_dataframe].dtypes 
```

Untuk konversi tipe data, secara default system akan mendeteksi data yang tidak bisa di render as date type or numeric type sebagai object yang basically string. Tidak bisa di render oleh system ini karena berbagai hal, mungkin karena formatnya asing dan tidak dikenali oleh python secara umum (misal: date type data → '2019Jan01').

Data contoh tersebut tidak bisa di render karena bulannya Jan tidak bisa di translate menjadi in form of number (00-12) dan tidak ada ‘-’ di antara tahun, bulan dan harinya. Jika seluruh data pada kolom di order_date sudah tertulis dalam bentuk 'YYYY-MM-DD' maka ketika dibaca, kolom order_date sudah langsung dinyatakan bertipe data datetime.

Untuk merubah kolom date_order yang sebelumnya bertipe object menjadi kolom bertipe datetime, cara pertama yang dapat dilakukan adalah menggunakan:
```
pd.to_datetime(argumen) 
```
dengan argumen adalah isi kolom dari dataframe yang akan dirubah tipe datanya, misal dalam format umum.
```
nama_dataframe["nama_kolom"]
```
Sehingga lengkapnya dapat ditulis sebagai:
```
nama_dataframe["nama_kolom"] = pd.to_datetime(nama_dataframe["nama_kolom"]) 
```

Tugas praktek:

Ubahlah tipe data di kolom order_date yang semula bertipe objek menjadi bertipe datetime.

Di code editor telah disediakan kode yang tidak lengkap, silakan diisi sesuai dengan instruksi yang diberikan. 

Jika dengan benar dituliskan dan berhasil dijalankan maka output berikut yang akan diperoleh pada console.

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

![trsfrm](../../pict/transform1_1.png)

## Transforming - Part 2
Pada sub bab ini akan mengubah tipe data pada kolom dataframe yang telah dibaca menjadi tipe data float (kolom quantity) dan tipe kategori (kolom city).

Secara umum, untuk mengubah ke numerik dapat menggunakan pd.to_numeric(), yaitu:
```
nama_dataframe["nama_kolom"] = pd.to_numeric(nama_dataframe["nama_kolom"], downcast="tipe_data_baru")
```

Sedangkan untuk menjadi suatu kolom yang dapat dinyatakan sebagai kategori dapat menggunakan method .astype() pada dataframe, yaitu
```
nama_dataframe["nama_kolom"] = nama_dataframe["nama_kolom"].astype("category")
```

### Tugas Praktek:

Ubahlah tipe data di kolom

* quantity yang semula bertipe int64 menjadi bertipe float32, dan
* city yang semula bertipe object menjadi bertipe category
Di code editor telah disediakan kode yang tidak lengkap, silakan diisi sesuai dengan instruksi yang diberikan. 

Jika dengan benar dituliskan dan berhasil dijalankan maka output berikut yang akan kamu peroleh di console.

Notes : 

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

![trsfrm](../../pict/transform2_1.png)


## Transforming - Part 3
Sekarang akan mempelajari teknik/cara berikutnya dalam proses transformasi suatu dataframe. Di sub bab ini akan memakai method .apply() dan .map() pada suatu dataframe.

Method .apply() digunakan untuk menerapkan suatu fungsi python (yang dibuat dengan def atau anonymous dengan lambda) pada dataframe/series atau hanya kolom tertentu dari dataframe. 

Berikut ini adalah contohnya yaitu akan merubah setiap baris pada kolom brand menjadi lowercase.  

![trsfrm](../../pict/transform3_1.png)

Jika dijalankan maka akan menghasilkan:

![trsfrm](../../pict/transform3_2.png)

Method .map() hanya dapat diterapkan pada series atau dataframe yang diakses satu kolom saja. Method ini digunakan untuk mensubstitusikan suatu nilai ke dalam tiap baris datanya.

Mari lihat contoh yang diberikan berikut ini yang mana akan ambil huruf terakhir dari brand.

![trsfrm](../../pict/transform3_3.png)

Jika dijalankan maka akan menghasilkan:

![trsfrm](../../pict/transform3_4.png)

Tugas praktek:

Kerjakanlah seperti yang diinstruksikan melalui code editor dan di code editor juga telah disediakan kode yang tidak lengkap, silakan diisi dengan yang seharusnya. Apa yang telah dicontohkan dapat dijadikan referensi.

Jika kodenya tidak ada yang salah dan dijalankan dengan tombol  maka akan memperoleh hasil berikut di console.

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

![trsfrm](../../pict/transform3_5.png)


## Transforming - Part 4
Di sub bab sebelumnya sudah mengetahui bahwa map hanya dapat digunakan untuk pandas series. Pada sub bab ini akan menggunakan method .applymap pada dataframe.

Untuk itu perhatikan contoh berikut:

![trsfrm](../../pict/transform4_1.png)

Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x

![trsfrm](../../pict/transform4_2.png)

Cara 2 dengan define function

![trsfrm](../../pict/transform4_4.png)

Setelah dijalankan dengan menekan tombol  maka diperoleh output berikut di console.

![trsfrm](../../pict/transform4_3.png)

Cara 1 dan cara 2 menunjukkan bahwa keduanya menghasilkan dataframe yang sama.

Tugas Praktek:

Dengan cara yang sama seperti diatas buatlah matriks random ukuran 3 x 4 dengan seed random-nya 1234. Kemudian gunakan kedua cara seperti di atas untuk merubah seluruh isi dengan fungsi kuadrat x**2 + 3*x + 2.

Jika kode dengan benar ditulis dan kemudian dijalankan dengan menekan tombol  diperoleh output berikut:

![trsfrm](../../pict/transform4_5.png)


## Penutup dari Andra

“Sampai di sini sudah cukup jelas, Aksara? Terutama soal manipulasi data dengan index,” ujar Andra mengonfirmasi padaku.

Aku mengangguk antusias, “Iya, ini keren banget! Kayak upgrade-an dari Excel ya.”

“Oke, kalau begitu kamu bisa coba mengerjakan kuisnya sebelum kita lanjut ke materi selanjutnya. Soalnya bakal ada proyek yang mau diberikan padamu berkaitan dengan Pandas ini.”

Proyek? Ah, pantas saja Andra yang sibuk itu mau meluangkan waktu untuk menjelaskan panjang lebar seperti tadi. Tapi tak bisa dipungkiri, aku sedikit gugup sekaligus tertantang untuk mengetahui detail proyeknya. 	
 
Klik tombol Next untuk melanjutkan.

# Handling Missing Values

## Pendahuluan
“Aksara, saya barusan kirim email lagi ya berisi link seputar handling missing values untuk Pandas. Kamu bisa belajar lebih lengkap di sana bersama isi modul.”

“Siap!”

Tanpa menunggu lagi, aku mengecek link yang diberikan Andra:

https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html

## Inspeksi Missing Value

Inspeksi Missing Value
Value yang hilang/tidak lengkap dari dataframe akan membuat analisis atau model prediksi yang dibuat menjadi tidak akurat dan mengakibatkan keputusan salah yang diambil. Terdapat beberapa cara untuk mengatasi data yang hilang/tidak lengkap tersebut.

Data COVID-19 yang akan digunakan ini diambil dari google big query, tetapi sudah disediakan datasetnya dalam format csv dengan nama https://storage.googleapis.com/dqlab-dataset/datacovid19.csv. Ini adalah studi kasus untuk meng-handle missing value. Bagaimanakah langkah-langkahnya?

Di pandas data yang hilang umumnya direpresentasikan dengan NaN.

Langkah pertama, harus tahu kolom mana yang terdapat data hilang dan berapa banyak dengan cara:

Cara 1: menerapkan method .info() pada dataframe yang dapat diikuti dari kode berikut ini:

Notes :

Dataset : https://storage.googleapis.com/dqlab-dataset/datacovid19.csv

![imv](../../pict/inspeksi_missing_value1.png)

Output baris kode kelima:

![imv](../../pict/inspeksi_missing_value2.png)

Cara 2: mengetahui berapa banyak nilai hilang dari tiap kolom di dataset tersebut dengan menerapkan chaining method pada dataframe yaitu .isna().sum(). Method .isna() digunakan untuk mengecek berapa data yang bernilai NaN dan .sum() menjumlahkannya secara default untuk masing-masing kolom dataframe.

Perhatikanlah kode berikut!

![imv](../../pict/inspeksi_missing_value3.png)

Output untuk baris kode ketujuh dan kedelapan:

![imv](../../pict/inspeksi_missing_value4.png)


Seperti kedua output di atas, artinya ada beberapa kolom yang ada null sebagian dan ada yang nilainya null semua untuk kolomnya.

Tugas Praktek:

Ketikkanlah kembali statement seperti yang ditunjukkan dalam kedua cara untuk mendeteksi missing value pada dataframe dengan mengisi tanda _ _ _ di code editor.

Jika dijalankan dengan menekan tombol  maka akan diperoleh kedua output di atas di bagian console.

## Treatment untuk Missing Value - Part 1
Treatment untuk Missing Value - Part 1
Terdapat beberapa cara untuk mengatasi missing value, antara lain:

dibiarkan saja,
hapus value itu, atau
isi value tersebut dengan value yang lain (biasanya interpolasi, mean, median, etc)

Sebelum melakukan action ke missing value pada data covid diatas, sebaiknya tampilkan beberapa row teratas dari dataset itu

![tms](../../pict/treatment_missing_value1.png)

dan dilihat kembali jumlah missing value tiap kolomnya.

![tms](../../pict/treatment_missing_value2.png)

agar dapat ditelaah terlebih dahulu.

Hanya kolom combine_key yang keseluruhan barisnya adalah missing value (1000 buah), sementara kolom country_region, date, dan confirmed tidak memiliki missing value. Untuk kolom lainnya terdapat beragam jumlah missing value. Apa yang dapat dilakukan?

Untuk memahami mana kolom yang akan di treatment dengan tiga perlakukan di atas lihat nature dari data terlebih dahulu. Contohnya pada kolom death dan recovered jika ada yang missing value maka kemungkinan terbesarnya adalah tidak ada meninggal atau sembuh pada hari tersebut. 

Untuk kolom yang seluruhnya missing yaitu combined_key dapat dibuang saja satu kolom itu karena tidak ada data yang dapat diketahui dari kolom tersebut.

Sementara, kolom yang lainnya bagaimana? Misal ambil kolom province_stat, missing value-nya dapat terjadi bahwa tidak dilaporkan itu berasal dari daerah mana di negara itu. Dapat mengisi misal dengan string 'unknown' karena tahu kolom tersebut bertipe data string.

## Treatment untuk Missing Value - Part 2
Treatment untuk Missing Value - Part 2
Sekarang dapat menerapkan dua aksi yaitu

1. Membiarkannya saja
2. Menghapus kolom

Treatment pertama (membiarkannya saja) seperti pada kolom confirmed, death, dan recovered. Akan tetapi jika tidak ada yang terkonfirmasi, meninggal dan sembuh sebenarnya dapat menukar value ini dengan angka nol. Meskipun ini lebih make sense dalam representasi datanya, tetapi untuk sub bab ini ketiga kolom tersebut diasumsikan dibiarkan memiliki nilai missing value.

Treatment kedua yaitu dengan menghapus kolom, yang mana ini digunakan jika seluruh kolom dari dataset yang dipunyai semua barisnya adalah missing value. Untuk itu dapat menerapkan method .dropna() pada dataframe, bagaimana caranya?

```
nama_dataframe.dropna(axis=1, how="all")
```

Pada method .dropna() ada dua keyword argumen yang harus diisikan yaitu axis dan how. Keyword axis digunakan untuk menentukan arah dataframe yang akan dibuang angka 1 untuk menyatakan kolom (column-based) atau dapat ditulis dalam string "column". Jika digunakan angka 0 berarti itu dalam searah index (row-based) atau dapat ditulis dalam string "index".

Sementara, keyword how digunakan untuk bagaimana cara membuangnya. Opsi yang dapat diterimanya (dalam string) adalah

* "all" artinya jika seluruh data di satu/beberapa kolom atau di satu/beberapa baris adalah missing value.
* "any" artinya jika memiliki 1 saja data yang hilang maka buanglah baris/kolom tersebut.
 

Tugas Praktek:

Cetaklah ukuran awal dari dataframe dengan atribut .shape pada dataframe yang telah dibaca.
Buanglah kolom jika memiliki seluruh data adalah missing value, kemudian cetaklah ukurannya.
Dari dataframe hasil langkah kedua buanglah baris-baris yang setidaknya memiliki satu saja missing value, dan cetak kembali ukurannya.
Jika berhasil akan ditampilkan output-nya sebagai berikut:

![tms](../../pict/treatment_missing_value2_1.png)

Notes:

Dataset: https://storage.googleapis.com/dqlab-dataset/datacovid19.csv

## Treatment untuk Missing Value - Part 3
Sekarang, akan melakukan treatment ketiga untuk melakukan handle missing value pada dataframe. Treatment ini dilakukan dengan cara mengisi missing value dengan nilai lain, yang dapat berupa :

* nilai statistik seperti mean atau median
* interpolasi data
* text tertentu
 
Akan mulai pada kolom yang missing yang tipe datanya adalah berupa object. Kolom tersebut adalah province_state, karena tidak tahu secara persis province_state mana yang dimaksud, bisa menempatkan string "unknown" sebagai substitusi missing value. Meskipun keduanya berarti sama-sama tidak tahu tetapi berbeda dalam representasi datanya.

Untuk melakukan hal demikian dapat menggunakan method .fillna() pada kolom dataframe yang dimaksud. Perhatikan kode berikut!

![tms](../../pict/treatment_missing_value3_1.png)

Jika dijalankan akan menghasilkan output berikut di console:

![tms](../../pict/treatment_missing_value3_2.png)

Terlihat bahwa unique value di kolom "province_state" yang semula ada nan telah berubah menjadi "unknown". 

**Tugas Praktek:**

Lakukanlah dengan cara yang sama dengan yang telah dicontohkan di atas, tetapi isilah missing value dengan string "unknown_province_state".

Jika dituliskan dengan benar dan dijalankan dengan  maka output di console berikut akan diperoleh. 

Notes :

Dataset: https://storage.googleapis.com/dqlab-dataset/datacovid19.csv

![tms](../../pict/treatment_missing_value3_3.png)

## Treatment untuk Missing Value - Part 4

Masih melanjutkan bagaimana melakukan handle missing value tentunya dengan jalan mengganti missing value dengan nilai lainnya. Pada bab sebelumnya telah mengganti kolom bertipe objek dengan sesuatu string/teks.

Dalam sub bab ini akan mengganti missing value dengan nilai statistik kolom bersangkutan, baik median atau mean (nilai rata-rata). Misalnya akan menggunakan kolom active. Dengan mengabaikan terlebih dahulu sebaran berdasarkan negara (univariate), jika mengisi dengan nilai rata-rata maka harus melihat terlebih dahulu data apakah memiliki outliers atau tidak. Jika ada outliers dari data maka menggunakan nilai tengah (median) data adalah cara yang lebih safe.

Untuk itu diputuskan dengan mengecek nilai median dan nilai mean kolom active juga nilai min dan max-nya. Jika data pada kolom active terdistribusi normal maka nilai mean dan median akan hampir sama.

![trtmnmsvl](../../pict/treatment_missing_value4_1.png)

Terlihat data memiliki distribusi yang skewness, karena nilai mean dan median yang cukup jauh serta range data yang cukup lebar. Di sini pada kolom active data memiliki outliers. Jadi akan mengisi missing value dengan median.

![trtmnmsvl](../../pict/treatment_missing_value4_2.png)

Jika dijalankan dengan menekan tombol  diperoleh output:

![trtmnmsvl](../../pict/treatment_missing_value4_3.png)

**Tugas Praktek:**

Carilah perbedaan nilai mean dan median kolom active untuk kondisi sebelum dan setelah missing value-nya diisi masing-masingnya dengan median dan mean.

Jika berjalan lancar maka akan diperoleh hasil seperti berikut ini di console:

![trtmnmsvl](../../pict/treatment_missing_value4_4.png)

Notes:

Dataset: https://storage.googleapis.com/dqlab-dataset/datacovid19.csv

## Treatment untuk Missing Value - Part 5

Di bagian ini akan menggunakan teknik interpolasi dalam mengisi nilai missing value pada suatu dataset.

Data yang menggunakan interpolasi untuk mengisi data yang hilang adalah time series data, yang secara default akan diisi dengan interpolasi linear.

Perhatikan kode berikut:

Jika dijalankan akan menghasilkan:

Tugas praktek:

Kerjakan kembali seperti contoh kode di atas dengan hasil output seperti yang ditujukkan berikut ini: 

## Quiz
Bagaimana cara menghapus kolom dengan sebagian missing value?

# Mini Project
## Pendahuluan
“Ndra, aku sudah cukup paham dengan teorinya,” sahutku seakan memberi kode jika aku sudah siap mengerjakan proyek yang tadi dijanjikan.

“Saya suka kepercayaan dirimu, Aksara. Kalau begitu, sudah siap kalau diberi proyek?” pancing Andra.

Aku mengangguk mantap.

“Oke, untuk proyek pertama, kamu akan melakukan ETL sebelum analisis data. Karena data yang dibutuhkan masih belum bersih, sehingga tidak bisa dilakukan analisis lebih lanjut.”

Aku menyimak pemaparan dari Andra sembari memikirkan solusi untuk ETL. Tentunya bisa aku eksekusi dengan Pandas. “Baik, Ndra. Data yang dibutuhkan apa saja nantinya?”

“Data untuk cabang perusahaan ritel kita, Aksara. Berarti kumpulan data bulan Januari 2019 untuk setiap kota dan provinsi, tanggal order-nya, customer, order-nya apa aja terkait brand, product, quantity dan item price-nya juga. Dan, yang terakhir adalah GMV/Gross Merchandise Volume (total price)-nya.”

“Banyak banget!” gumamku dalam hati.

“Saya tahu kamu pasti sudah memikirkan detlennya karena data yang dibutuhkan banyak. Jangan khawatir, saya beri tenggat waktu sampai akhir minggu ini, bukan besok. Cukup?”

Aku mengangkat ibu jari, “Langsung aku cicil dari sekarang deh, Ndra.”

“Baik, selamat bekerja Aksara!”

## Project dari Andra

Berikut adalah isi email yang ditugaskan oleh Andra:

Diberikan dataset ‘retail_raw_test.csv’

1. Baca dataset
2. Tipe data diubah menjadi tipe yang seharusnya
    - customer_id dari string ke int64,
    - quantity dari string ke int64,
    - item_price dari string ke int64
3. transform product_value supaya bentuknya seragam dengan format PXXXX, assign ke kolom baru "product_id", dan drop kolom "product_value", jika terdapat nan gantilah dengan "unknown".
4. trasnform order_date menjadi value dengan format YYYY-mm-dd
5. cek data hilang dari tiap kolom dan kemudian isi missing value
    - di brand dengan "no_brand", dan
    - cek dulu bagaimana missing value di city & province - isi missing value di city dan province dengan "unknown"
6. create column city/province dari gabungan city & province
7. membuat index berdasarkan city_provice, order_date, customer_id, order_id, product_id (cek index)
8. membuat kolom "total_price" sebagai hasil perkalian quantity dengan item_price
9. slice data hanya untuk Jan 2019

Notes :

Dataset :  https://storage.googleapis.com/dqlab-dataset/retail_raw_test.csv

Preview akhir data:

![pd](../../pict/project_dr_andra.png)



## Evaluasi Andra untuk Project yang Telah Disubmit
Aku baru saja mengumpulkan hasil kerja dari proyek pertamaku pada Andra. Lebih cepat satu hari dari tenggat waktu yang diberikan, semoga hasilnya juga memuaskan! Doaku dalam hati.

 

“Aksara, saya baru saja meninjau pekerjaanmu. Saya ada pertanyaan,” ujar Andra yang lagi-lagi sudah ada di sebelahku. Sepertinya Andra punya kemampuan teleportasi yang bisa muncul tiba-tiba.

“Ada yang salah, Ndra?”

 

“Saya ingin tahu alasanmu mengapa di langkah ketiga, kamu cari tahu terlebih dulu nilai null. Mengapa tidak kamu convert to string secara langsung?”

“Soalnya, kalau aku cek di df.info()nya masih ada yang kosong di kolom ‘product_value’, Ndra.  Kalau aku langsung convert to string, nantinya value NaN akan berubah menjadi string ‘nan’, kemudian ketika aku pad 0 di depan dan concat dengan char ‘P’, hasilnya akan menjadi ‘P0nan’ yang aneh sekali, Ndra,” jelasku.

 

“Oke. Satu lagi pertanyaanku, Aksara. Kenapa kamu memakai langkah ke-4? Mengapa tidak langsung menggunakan kolom date yang sudah ada. Bukankah format waktunya sudah ideal?”

Aku merasa tanya jawab ini tampak seperti ujian apakah aku benar-benar memahami cara kerja Pandas. Aku memantapkan diri untuk memberi jawaban, “Tidak semua format datetime yang ideal pada umumnya akan ideal di dalam pandas environment. Seenggaknya harus translate dulu menjadi format yang ideal di dalam pandas sehingga pandas bisa mengenali.”

 

“Great! Untuk materi dan proyek ini, kamu dinyatakan lulus, Aksara.”

Mendengar apresiasi ini langsung dari Andra membuat hatiku hangat. Senang sekali rasanya!

## Hasil Belajarku

Walau harus bekerja keras, aku cukup puas dengan hasil kerjaku hari ini. Aku memandangi kode final yang sudah selesai kukerjakan. Diam-diam ada perasaan bangga menyelip di benakku! YES!

Akhirnya, aku telah menyelesaikan modul Data Manipulation with Pandas - Part 1. Materi-materi yang telah kupelajari dan praktikkan dalam modul ini aku telah mendapatkan pengetahuan (knowledge) dan praktek (skill) untuk:

Memahami library Pandas dan interaksinya dengan numpy
Memahami dan mempraktekkkan bagaimana membuat series dan dataframe pada pandas dari berbagai tipe data seperti list, list of list, dict, ataupun numpy array
Memahami dan mempraktekkkan bagaimana membaca dataset dari berbagai format standar seperti csv, tsc, excel, json, sql sehingga dapat dijadikan pandas dataframe/series serta bagaimana cara menyimpannya ke format standar dataset.
Mampu memahami dan mempraktikkan proses indexing, transformasi, dan slicing pada dataframe
Mampu memahami dan mempraktikkan bagaimana cara melakukan handle missing value pada suatu dataframe
Latihan dalam mengerjakan project bisnis sederhana menggunakan pandas

Semangat!