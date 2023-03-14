# Data Quality with Python for Beginner

1. [Data Profiling](#data-profiling)
- [Pengantar](#pengantar)
- [Apa itu Data Profiling](#apa-itu-data-profiling)
- [Import Data](#importing-data)
- [Inspeksitipe data](#inspeksi-tipe-data)
- [Descriptive Statistic - Part 1](#descriptive-statistics---part-1)
- [Descriptive Statistic - Part 2](#descriptive-statistics---part-2)
- [Descriptive Statistic - Part 3](#descriptive-statistics---part-3)
- [Descriptive Statistic - Part 4](#descriptive-statistics---part-4)
- [Descriptive Statistic - Part 5](#descriptive-statistics---part-5)
- [Descriptive Statistic - Part 6](#descriptive-statistics---part-6)
- [Penggunaan Profiling Libraries](#penggunaan-profiling-libraries)

2. [Data Cleansing](#data-cleansing)
- [Apa itu Data Cleansing?](#apa-itu-data-cleansing)
- [Missing Data](#missing-data)
- [Tugas Praktek](#tugas-praktek)
- [Outliers](#outliers)
- [Tugas Praktek](#tugas-praktek-1)
- [Deduplakasi Data](#deduplikasi-data)
- [Tugas Praktek](#tugas-praktek-2)

3. [Mini Project](#mini-project)
- [Pendahuluan](#pendahuluan)
- [Case Studi: Data Profiling](#case-studi-data-profiling)
- [Case Studi: Data Profiling - Part 1](#case-study-data-cleansing---part-1)
- [Case Studi: Data Profiling - Part 2](#case-study-data-cleansing---part-2)
- [Penutup/Kesimpulan](#penutupkesimpulan)


# Data Profiling
## Pengantar
Aku dipanggil ke ruangan Kroma, sang kepala divisi! Gugup? Pastinya. Penasaran? Apalagi. Setelah diam beberapa saat, Kroma menunjukkan lembar kerjaku di layar laptopnya.

“Setelah mengecek hasil analisis kamu, saya rasa ini perlu sedikit revisi. Coba lakukan analisis terhadap datanya secara lebih mendalam menggunakan EDA, termasuk data profiling. Bisa?” pinta Kroma di ruangannya.

Aku memang sudah terbiasa mendengar kata ‘revisi’ dari Senja dan Andra, tapi tetap saja kali ini lebih menegangkan karena langsung dari Kroma, si kepala divisi! Aku hendak mengangguk tapi kuingat kalau aku belum sempat mempelajari mengenai data profiling bersama Senja. Seperti mampu membaca keraguanku, Kroma mencondongkan tubuhnya ke arahku dan berujar, “Sekaligus saya kirimkan referensi lengkap dan contoh bagaimana data profiling dilakukan.”

Aku pun keluar dari ruangan membawa ‘kado’ berupa revisi.

Senangnya kalau punya kepala divisi yang memberikan revisi sekaligus solusi. Setelah kembali ke meja, aku langsung membuka tautan referensi yang diberikan Kroma. Aku memutuskan untuk mempelajarinya dulu sebelum melakukan revisi pekerjaan.

## Apa itu Data Profiling?

Pada bagian sebelumnya, aku sudah mempelajari mengenai exploratory data analysis, dimana Exploratory Data Analysis (EDA) adalah menggunakan pendekatan statistik yang bertujuan untuk menemukan dan meringkas sebuah dataset, mengetahui struktur dan hubungan antar variabel dalam dataset. EDA merupakan proses pre-analysis baik untuk descriptive analysis maupun predictive analysis.

Dalam bab ini, aku akan fokus pada satu aspek EDA, yaitu: Data Profiling!

Data profiling adalah kegiatan merangkum dataset menggunakan statistik deskriptif. Tujuan dari pembuatan data profiling adalah untuk memiliki pemahaman yang kuat tentang data sehingga dapat mulai menyusun framework analisis  dan memvisualisasikan data.

![dq](../../pict/Screenshot%202023-03-08%20144724.png)

Wah, seru sekali referensi materi dari Kroma yang kudapatkan ini. Aku akan melanjutkan ke materi berikutnya supaya lebih memahami dan bisa memenuhi tugas dari Kroma. 

## Importing Data

Sebagai langkah pertama yang harus dilakukan adalah inisialisasi Library dan mengimport dataset tersebut ke dalam Python menggunakan library Pandas dan diassign sebagai retail_raw.

Library yang perlu diimport adalah: (1) pandas, (2) numpy, (3) io, dan (4) pandas_profiling. Untuk dua libray yang pertama importlah sebagai aliasnya.

Datasetnya tersedia di: 'https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv'.

## Inspeksi tipe data
Dengan library Pandas, dapat menjalankan fungsi .dtypes untuk melihat data untuk setiap kolom termasuk tipe datanya.

Dengan menekan  untuk mengeksekusi baris program di code editor, diperoleh output di console berupa:

![dq](../../pict/Screenshot%202023-03-08%20150016.png)

## Descriptive Statistics - Part 1
Di bagian ini, aku akan mempelajari berbagai statistik deskriptif yang dapat digunakan untuk lebih memahami struktur data.

*Length*

Fungsi len menghitung jumlah pengamatan dalam suatu series/column. Fungsi len akan menghitung semua pengamatan, terlepas dari apakah ada null-value atau tidak (include missing value).

![dq](../../pict/Screenshot%202023-03-08%20150423.png)

Contoh penggunaan untuk mengetahui length dari kolom city dari dataframe retail_raw!

![dq](../../pict/Screenshot%202023-03-08%20150543.png)

Jika dijalankan kode dengan baris yang ditunjukkan akan menghasilkan output:

![dq](../../pict/Screenshot%202023-03-08%20150642.png)

### Tugas Praktek:

Setelah membaca modul referensi Kroma, aku coba memulai analisis dengan menginspeksi length dari kolom product_id dari dataframe retail_raw! Aku akan membuat syntaks Python untuk mencapai hal tersebut di code editor. Berikut cara yang akan kulakukan:

Jika dijalankan dengan  akan menghasilkan:

![dq](../../pict/Screenshot%202023-03-08%20150751.png)

## Descriptive Statistics - Part 2
Aku melanjutkan mempelajari ke fungsi berikutnya, yaitu Count.

**Count**

Fungsi count menghitung jumlah pengamatan non-NA/non-null dalam suatu series/column. Di lain pihak, fungsi len akan hanya menghitung jumlah elemen dari kolom baik kolom bersangkutan memiliki atau tidak memiliki missing value (include missing value).

![dq](../../pict/Screenshot%202023-03-08%20153329.png)

Contoh penggunaan untuk mengetahui count dari kolom city dari dataframe retail_raw!

![dq](../../pict/Screenshot%202023-03-08%20153422.png)

Jika dijalankan dengan  akan menghasilkan:

![dq](../../pict/Screenshot%202023-03-08%20153553.png)

**Tugas Praktek:**

Setelah yang tadi cukup lancar, aku berniat mengetahui jumlah non-null value dari kolom product_id dari dataframe retail_raw agar hasil analisisnya lebih lengkap.

Jika dijalankan dengan menekan  akan diperoleh output di console:

![dq](../../pict/Screenshot%202023-03-08%20153632.png)

## Descriptive Statistics - Part 3
Lanjut ke bagian berikutnya. 

**Missing Value**

Dengan Length dan Count, sekarang dapat menghitung jumlah missing-value. Jumlah nilai yang hilang adalah perbedaan antara Length dan Count.

![dq](../../pict/Screenshot%202023-03-08%20153938.png)

Jika dijalankan dengan  akan menghasilkan persentase data yang missing:

![dq](../../pict/Screenshot%202023-03-08%20154008.png)

Tugas Praktek:

Yes! Aku berhasil mendapatkan length dan count dari product_id, sekarang  aku perlu mengetahui jumlah missing-value dari kolom tersebut. Ini artiya aku perlu membuat syntaks untuk menghitung persentase missing-value dari product_id. Kerjakanlah di code editor pada baris 7 s/d 11.

Jika telah ditulis dengan benar dan dijalankan dengan  diperoleh output berupa:
![dq](../../pict/Screenshot%202023-03-08%20154033.png)

## Descriptive Statistics - Part 4
**Maximum dan Minimum**

Fungsi **max** dan **min** digunakan untuk mengetahui elemen terbesar dan terkecil dari suatu kolom di dataframe.

![dq](../../pict/Screenshot%202023-03-08%20155105.png)

Mean, Median, Modus dan Standard Deviasi

Fungsi mean, median, modus dan standard deviasi digunakan untuk mengetahui pemusatan data dan persebarannya.

![dq](../../pict/Screenshot%202023-03-08%20155127.png)

Contohnya:

![dq](../../pict/Screenshot%202023-03-08%20155147.png)

Jika dijalankan dengan  akan menghasilkan:

![dq](../../pict/Screenshot%202023-03-08%20155209.png) 

**Tugas praktek:**

Buatlah statistics deskriptif untuk data item_price dari dataframe retail_raw! Berupa max, min, mean, median, dan std!

Jika telah selesai ditulis dengan benar dan dijalakan dengan menekan  diperoleh output berikut:

![dq](../../pict/Screenshot%202023-03-08%20155230.png)

## Descriptive Statistics - Part 5

**Quantile Statistics**

Quantiles adalah titik potong yang membagi distribusi dalam ukuran yang sama. Jika akan membagi distribusi menjadi empat grup yang sama, kuantil yang dibuat dinamai quartile. Jika dibagi kedalam 10 sepuluh grup yang sama dinamakan percentile. Dalam kasus di bawah ini, ingin membagi distribusi menjadi empat grup atau quartile.

![dq](../../pict/Screenshot%202023-03-08%20175352.png)

**Contoh:**

![dq](../../pict/Screenshot%202023-03-08%20175528.png)

Jika dijalankan dengan  akan menghasilkan:

![dq](../../pict/Screenshot%202023-03-08%20175548.png)

### Tugas Praktek:

Baiklah, sekarang saatnya lanjut untuk membuat distribusi quartile dari item_price dari dataframe retail_raw. Kalau ini sih seharusnya mudah, aku mulai menyusun kodenya di code editor.

Dengan menekan  diperoleh output:

![dq](../../pict/Screenshot%202023-03-08%20175610.png)

## Descriptive Statistics - Part 6
**Correlation**

Korelasi adalah cara yang tepat untuk menemukan hubungan antara variabel numerik. Koefisien korelasi berkisar antara -1 hingga 1. Korelasi 1 adalah korelasi positif total, korelasi -1 adalah korelasi negatif total dan korelasi 0 adalah korelasi non-linear.

![dq](../../pict/Screenshot%202023-03-08%20182504.png)

### Tugas Praktek:

“Hmmm, korelasi antara quantity dan item_price apa ya?” batinku. Aku perlu tahu untuk melengkapi syntaks. Aku coba cari di modul yang Kroma berikan tadi deh. Aku mengetikkan kode yang kupelajari sebelumnya di code editor.

Jika dengan benar ditulis dan dijalankan dengan  maka akupun memperoleh hasil berikut:

![dq](../../pict/Screenshot%202023-03-08%20182528.png)

## Penggunaan Profiling Libraries

Seperti yang terlihat di atas, mengumpulkan statistik deskriptif dapat menjadi proses yang panjang. Pandas Profiling library memiliki function yang dapat membuat profiling data secara otomatis.

Untuk dapat menggunakannya, cukup dengan memanggil library:

![dq](../../pict/Screenshot%202023-03-08%20182837.png)

Syntax:

![dq](../../pict/Screenshot%202023-03-08%20182856.png)


Contoh penggunaan untuk dataset retail_raw:

![dq](../../pict/Screenshot%202023-03-08%20182917.png)

Mengingat output yang ditampilkan kaya akan penggunaan javascript, maka silakan klik tautan berikut ini untuk dibuka di tab baru browser kamu:

Retail_Profiling.html

untuk melihat profiling report dari data frame retail_raw yang telah DQLab buatkan.

Akan dapat memahami proses profiling data yang menerapkan EDA (exploratory data analysis) dari report yang di-generate menggunakan library pandas_profiling melalui method ProfileReport.



# Data Cleansing
## Apa itu Data Cleansing?
Fiuh! Materi tadi benar-benar penuh dengan latihan-latihan. Walaupun latihannya singkat, kalau jumlahnya banyak, ternyata menguras energi dan pikiranku juga. Apa mungkin Kroma sengaja memberikan referensi yang penuh latihan agar revisian aku nantinya bisa lebih lancar? Bisa juga caranya.

Aku mengecek sisa materi referensi yang diberikan, masih terdapat pembahasan seputar “Data Cleansing” lengkap dengan latihan-latihan singkat seperti sebelumnya. Baiklah, akan kujalani! Sisa ini saja kok, aku pasti bisa, batinku percaya diri.

Data Cleansing berarti proses mengidentifikasi bagian data yang salah, tidak lengkap, tidak akurat, tidak relevan atau hilang dan kemudian memodifikasi, mengganti atau menghapusnya sesuai dengan kebutuhan. Data Cleansing dianggap sebagai elemen dasar dari Data Science

Pada bagian ini, akan membahas data cleansing dari treatment terhadap missing data, treatment outliers, sampai deduplikasi data.

## Missing Data
Dataset yang ditemui di real-world biasanya akan memiliki banyak missing value. Kemampuan untuk treatment missing value sangat penting karena jika membiarkan missing value itu dapat memengaruhi analisis dan machine learning model. Sehingga jika menemukan nilai yang hilang dalam dataset, harus melakukan treatment sedemikian rupa. Cara check kolom yang mempunyai missing value:

![md](../../../pict/missingdata1.png)

Cara treatment terhadap missing-value antara lain:

1. Leave as it is (dibiarkan)
2. Filling the missing value (imputasi)
3. Drop them (hapus row yang mengandung missing value)

**Imputasi** merupakan suatu metode treatment terhadap missing value dengan mengisinya menggunakan teknik tertentu. Bisa menggunakan mean, modus ataupun menggunakan predictive modelling. Pada modul ini akan membahas mengenai pemanfaatan function **fillna** dari Pandas untuk imputasi ini, yaitu

![md](../../../pict/missingdata2.png)

.function() yang dimaksud pada syntax di atas adalah penggunan fungsi .mean() atau .mode(). Penggunaan fungsi .mean() atau .mode() ini bergantung pada kondisi yang mengharuskan menggunakan nilai rata - rata atau modus dari kolom yang akan diimputasi, seperti
```
nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.mean())
```
atau
```
nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.mode())
 ```

Drop row yang mengandung missing value. Dapat menggunakan function dropna dari Pandas.

![md](../../../pict/missingdata3.png)

Untuk menangani missing data pada retail_raw, 

1. Ceklah jika terdapat missing value pada variabel dataframe, dan kemudian cetak ke console
2. Imputasi missing value pada kolom quantity dengan menggunaan nilai rataan (mean), dan kemudian cetak ke console
3. Drop-lah missing value pada kolom quantity, dan kemudian cetak ke console

Jika ditulis dengan benar dan dijalankan dengan menekan  diperoleh output berikut: 

![md](../../../pict/missingdata4.png)


**Note**: Screen shoot untuk "Filling the missing value (imputasi):" dan "Drop missing value:" menunjukkan jumlah baris yang berbeda pada kolom quantity. Proses imputasi tentunya akan mempertahankan jumlah baris dari data karena missing value diisi dengan suatu nilai yang pada kasus kita ini menggunakan nilai rata-rata kolom bersangkutan. Sementara drop missing value tentu akan membuang baris yang memiliki missing value yang mengakibatkan jumlah baris data berkurang.

## Tugas Praktek
"Bagaimana, Aksara? Sudah dicoba dari modul yang saya kasih?” sapa Kroma. Kulihat ia baru keluar dari ruang meeting. Sedikit terkejut karena Kroma langsung menyapa dan menanyai prosesku, aku butuh beberapa detik sebelum menjawab.

“Sudah, sejauh ini paham sih. apalagi tiap subbab ada latihan singkatnya, banyak banget lagi! Cuma sedikit kendala saja soal missing value,” ujarku. Missing value memang bagian yang paling membuat penasaran karena sedari tadi aku berkutat dengan persoalan ini.

“Oke, bagus kalau memang lancar. Bisa temui saya di ruangan kalau dibutuhkan ya, Aksara.”

Aku mengangguk mantap. Aku tak mungkin bertanya pada Kroma dan memintanya mengajariku soal letak missing value-ku. Dan, tidak enak rasanya kalau merepotkan Senja lagi. Aku harus bisa mengandalkan diriku sendiri kali ini. Aku pun mengutak-atik dataku kembali selama hampir setengah jam dan menemukan jika missing value aku ada pada kolom item_price.

“Ah, akhirnya!” Dengan cepat aku melengkapi missing value tersebut dengan mean dari item_price. Berikut caranya:

Jika dengan benar telah dituliskan kodenya dan dijalankan dengan  diperoleh output seperti berikut:

![md](../../../pict/tugas_missing_data1.png)

## Outliers
Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim. Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai yang jauh atau beda sama sekali dengan sebagian besar nilai lain dalam kelompoknya.

Cara treatment terhadap outliers antara lain:

1. Remove the outliers (dibuang)
2. Filling the missing value (imputasi)
3. Capping
4. Prediction

Pada umumnya, outliers dapat ditentukan dengan metric IQR (interquartile range).

Rumus dasar dari IQR: Q3 - Q1, dan data suatu observasi dapat dikatakan outliers jika memenuhi kedua syarat dibawah ini:

* "< Q1 - 1.5 * IQR"
* "> Q3 + 1.5 * IQR"

Syntax di Python:

![dc](../../../pict/outliers1.png)


Kemudian untuk membuang outliers-nya:

![dc](../../../pict/outliers2.png)

Mari melihat penggunaannya pada dataframe retail_raw untuk kolom quantity:

![dc](../../../pict/outliers3.png)

Ukuran dataframe retail_raw sebelum dan setelah dibuang outliers pada kolom quantity yaitu:

![dc](../../../pict/outliers4.png)

Note: Langsung di-submit saja ya tanpa di-run :)

## Tugas Praktek
Setelah berhasil mengatasi missing value tadi, aku memutuskan untuk mencoba menemukan sejumlah outliers menggunakan IQR. Dengan begitu, aku bisa mengetahui berapa IQR dari variabel item_price. 

Caranya dengan mengetikkan bagian yang kosong pada live code editor. 

## Deduplikasi Data
Duplikasi data merupakan data dengan kondisi pada row-row tertentu memiliki kesamaan data di seluruh kolomnya. Tentunya ada data yang duplikat dalam dataset yang dimiliki. Kondisi duplikasi harus diatasi dengan jalan mengeliminir baris yang mengalami duplikasi, sehingga proses ini dikenal dengan deduplikasi.

Untuk mengecek duplikasi data:

![dc](../../../pict/deduplikasi_data.png)

Syntax untuk membuang duplikasi:

![dc](../../../pict/deduplikasi_data2.png)

## Tugas Praktek
Terakhir lagi menuju selesai! Aku tinggal membuang duplikasi data dari dataset retail_raw.

Aku akan melengkapi kode pada live code editor berikut. 


# Mini Project
## Pendahuluan

“Revisianmu sudah saya pelajari kembali. Hasilnya cukup memuaskan. Kamu berhasil menganalisisnya dengan tepat dan mendalam. Saya jadi tertarik untuk memberikanmu sebuah proyek,” ujar Kroma setelah mengecek satu per satu hasil revisi pekerjaanku.

Aku tidak tahu harus senang atau gugup saat ini. Proyek yang dipercayakan langsung dari Kroma? Jujur saja, aku cukup gelisah. Beragam kemungkinan menggantung di dadaku, apakah aku mampu? Aku hanya anak baru yang selama ini banyak dibimbing Senja dan dibantu Andra. 

Tanpa sadar aku terdiam lama. “Jangan khawatir. Saya yakin proyek ini sesuai dengan program belajarmu selama ini bersama Senja dan Andra. Jika ada penyesuaian dan pengembangan, hanya beberapa. Saya yakin kamu bisa melakukan improvisasi dengan baik,” lanjut Kroma.

Aku curiga atasanku ini memang bisa mendengar suara hati! Tapi mengetahui Kroma menaruh harapan dan kepercayaan padaku, aku seharusnya bangga. Dengan mengumpulkan kepercayaan diriku, aku mengiyakan proyek tersebut. 


“Baik. Lima menit lagi saya akan mengirimkan data dari cabang kita di daerah G. Tolong bersihkan saja dulu datanya, detailnya yang harus kamu lakukan akan saya arahkan juga di email.”


“Baik.”


Aku pun keluar dari ruangan. Setelah mengatur napas sejenak, aku bergegas kembali ke meja. Apalagi setelah aku mendengar notifikasi email masuk di ponselku. Dan tahu kalau itu pasti dari Kroma.

## Case Studi: Data Profiling
Dear Aksara, 

Tolong proses dataset terlampir yang  disimpan dalam bentuk csv bernama 'https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv'.

Kamu bisa memprosesnya dengan cara berikut:

1. Import dataset csv ke variable bernama uncleaned_raw
2. Inspeksi dataframe uncleaned_raw
Check kolom yang mengandung missing value. Jika ada, kolom apakah itu dan berapa persen missing value pada kolom tersebut?
3. Mengisi missing value tersebut dengan mean dari kolom tersebut!
4. Setelah membaca email tersebut, aku pun memulai kode programnya di code editor.

## Case Study: Data Cleansing - Part 1
```
Info: Predefined code telah diperbarui pada tanggal 6 Juni 2022, pastikan kode yang telah ditulis disesuaikan kembali.
```

Untuk memprosesnya bisa dilakukan dengan cara berikut:

5. Mengetahui kolom yang memiliki outliers! Gunakan visualisasi dengan boxplot pada dataframe uncleaned_raw.

## Case Study: Data Cleansing - Part 2
Langkah selanjutnya bisa dilakukan dengan cara berikut:

6. Melakukan proses removing outliers pada kolom UnitPrice.
7. Checking duplikasi dan melakukan deduplikasi dataset tersebut!

## Penutup/Kesimpulan
Congratulations! Aku telah menyelesaikan modul Data Quality with Python for Beginner. Berdasarkan materi-materi yang diberikan Kroma yang telah kupelajari dan praktekkan dalam modul ini, aku telah mendapatkan pengetahuan (knowledge) dan praktek (skill) yang diantaranya :

Mampu melakukan profiling data baik untuk data angka maupun teks
Mampu membuat rule untuk data cleansing (standarisasi data, value lookup, dan treatment duplikasi data)
 

Keep fighting!