# Modul Content : Manipulation with Pandas Part 2
[1. Penggabungan Series/Dataframe](#1-penggabungan-seriesdataframe)
- [Pendahuluan](#pendahuluan)
- [Bagaimana Cara Menggabungkan Pandas Series/Dataframe?](#bagaimana-cara-menggabungkan-pandas-seriesdataframe)
- [Append](#append)
- [Concat](#concat)
- [Merge - Part 1](#merge---part-1)
- [Merge - Part 2](#merge---part-2)
- [Join](#join)
- [Quiz](#quiz)

[2. Pivot, Melt, Stack & Unstack](#pivot-melt-stack--unstack)
- [Pendahuluan](#pendahuluan-1)
- [Dataset](#dataset) 
- [Pivot](#pivot) 
- [Pivot_table](#pivot_table) 
- [Melt - Part 1](#melt---part-1) 
- [Melt - Part 2](#melt---part-2)
- [Stack & Unstack - Part 1](#stack--unstack---part-1)
- [Stack & Unstack - Part 2](#stack--unstack---part-2) 
- [Quiz](#quiz-1)

[3. Aggregation & GroupBy](#aggregation--groupby)
- [Pendahuluan](#pendahuluan-2)
- [Review Inspeksi Data](#review-inspeksi-data)
- [Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 1](#groupby-dan-aggregasi-dengan-fungsi-statistik-dasar---part-1)
- [Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 2](#groupby-dan-aggregasi-dengan-fungsi-statistik-dasar---part-2)
- [Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 3](#groupby-dan-aggregasi-dengan-fungsi-statistik-dasar---part-3)
- [Groupby dengan Multiple Aggregations](#groupby-dengan-multiple-aggregations)
- [Groupby dengan Custom Aggregations](#groupby-dengan-custom-aggregations)
- [Groupby dengan Custom Aggregations by dict](#groupby-dengan-custom-aggregations-by-dict)
- [Quiz](#quiz-2)

# 1. Penggabungan Series/Dataframe
## Pendahuluan

“Aksara, sedang apa?”

Aku pun mengalihkan perhatianku dari layar laptop ke Andra. Pagi-pagi sekali ia sudah menghampiriku. Diam-diam aku menebak materi baru apa lagi yang harus kupelajari ataukah ada proyek dadakan lagi yang perlu diselesaikan?

“Lagi latihan pakai Pandas, Ndra.”

“Oh, masih modul Pandas part 1 kemarin?”

Aku mengangguk.

“Pas banget, pagi ini saya mau ngirim ke kamu lanjutan modulnya. Lagipula modul kemarin kamu sudah lulus kok. Sekarang fokus ke Pandas part 2 saja. Kali ini materinya lebih dalam mengenai interaksi dengan tabular data menggunakan Pandas. Nanti kamu baca dan pelajari saja dulu.”

“Oh, oke.” 

Setelah obrolan tadi, aku langsung menerima pesan dengan lampiran materi lanjutan dari Andra. Penasaran dengan apa yang bisa Pandas lakukan lagi, aku pun segera membuka dan mencernanya:

Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

## Bagaimana Cara Menggabungkan Pandas Series/Dataframe?

Sebagai seorang praktisi data, pasti sering kali bertemu dengan banyak file sekaligus dan data yang dibutuhkan tersebar di berbagai file tersebut dan membutuhkan metode untuk menggabungkan semua informasi yang dibutuhkan dari setiap file itu.

Dengan menggunakan excel atau tools pengolah spreadsheet lain hal itu bisa terjadi mungkin dengan menggunakan copy paste file satu ke file lainnya atau yang agak canggih menggunakan method importRange di google sheets. Tetapi tentu hal itu tidak bisa diandalkan ketika berurusan dengan big data yang datanya bisa miliaran rows dengan informasi yang tidak terbatas, Python dan Pandas adalah satu-satunya cara untuk mengatasinya.

Terdapat beberapa metode untuk menggabungkan Series/Dataframe di Pandas, yaitu:

* append
* concat
* merge
* join
Akan dibahas satu persatu dalam subbab berikutnya.

## Append

Method .append() dapat digunakan pada dataframe/series yang ditujukan untuk menambah row-nya saja. Jika di SQL memiliki 2 tabel atau lebih maka dapat menggabungkannya secara vertikal dengan Union. Jadi SQL Union ekuivalen dengan method .append() di Pandas. 

Perhatikan contoh berikut, mulai dengan method .append pada series.

![append](../../pict/append1.png)

Output-nya adalah:

![append](../../pict/append2.png)

Untuk dataframe:

![append](../../pict/append3.png)

Outputnya adalah

![append](../../pict/append4.png)

Tugas Praktek:

Untuk praktiknya terapkanlah method append dengan series s1 dan dataframe df1 ditempatkan setelah series s2 dan dataframe df2 masing-masingnya.

Jika dijalankan dengan menekan tombol  diperoleh output di console seperti berikut ini:

![append](../../pict/append5.png)

## Concat

Method .concat() dapat digunakan pada dataframe yang ditujukan untuk penggabungan baik dalam row-wise (dalam arah) atau column-wise.

Perhatikan contoh berikut, mulai dengan method .concat pada row-wise.

![append](../../pict/concat1.png)

Output-nya:

![append](../../pict/concat2.png)

Untuk penerapan concat pada column-wise:

![append](../../pict/concat3.png)

Output-nya:

![append](../../pict/concat4.png)

Dapat juga menambahkan identifier dari dataframe untuk data yang ditambahkan.

![append](../../pict/concat5.png)

Output-nya:

![append](../../pict/concat6.png)

Tugas Praktik:

Balikkanlah posisi kedua dataframe yang akan digabungkan dengan concat. 

Jika dijalankan dengan menekan tombol , output berikut yang akan diperoleh pada console

![append](../../pict/concat7.png)

## Merge - Part 1

Method .merge() untuk menggabungkan Series/Dataframe yang bentuknya mirip dengan syntax join di SQL, specify left and right tables, join key, dan how to join (left, right, inner, full outer).

Mari kita perhatikan contoh berikut:

![merge](../../pict/merge1_1.png)

pd.merge yang ekivalen dengan SQL left join.

![merge](../../pict/merge1_2.png)

output:

![merge](../../pict/merge1_3.png)

pd.merge yang ekivalen dengan SQL right join.

![merge](../../pict/merge1_4.png)

output:

![merge](../../pict/merge1_11.png)


pd.merge yang ekivalen dengan SQL inner join.

![merge](../../pict/merge1_5.png)

output:

![merge](../../pict/merge1_6.png)

pd.merge yang ekivalen dengan SQL outer join.

![merge](../../pict/merge1_7.png)

output:

![merge](../../pict/merge1_8.png)

Tugas Praktik:

Pada contoh di atas keyword argument left=df1 dan right=df2, untuk praktik gunakanlah keyword argument untuk left dan right masing-masingnya adalah df2 dan df1.

Jika dijalankan dengan menekan tombol  dan tidak ada kesalahan, output berikut yang kamu peroleh di console.

![merge](../../pict/merge1_9.png)

## Merge - Part 2

Penggunaan method .merge yang telah dipelajari pada part 1 adalah untuk dataframe dengan index tunggal.

Bagaimana jika salah satu dataframe atau keseluruhan dataframe yang akan digabungkan tersebut memiliki multi index?

![merge2](../../pict/merge2_1.png)

dengan df1 dan d2 di console:

![merge2](../../pict/merge2_2.png)

Jika digabungkan secara langsung seperti yang telah dilakukan pada bagian sebelumnya.

![merge2](../../pict/merge2_3.png)

akan menghasilkan:

![merge2](../../pict/merge2_4.png)


terjadi kegagalan dalam merging kedua dataframe yang memiliki multi index.

Cara mengatasinya adalah dengan me-reset index pada kedua dataframe, kemudian merge akan mendeteksi common single/multi column di kedua dataframe dan melakukan merge.

![merge2](../../pict/merge2_5.png)

dengan output-nya:

![merge2](../../pict/merge2_6.png)

Tugas Praktik:

Kerjakanlah di code editor dengan cara mengisi kode yang tidak lengkap (_ _ _) sesuai dengan yang telah dicontohkan.


## Join
Method .join() digunakan pada dataframe untuk menggabungkan kedua data dengan set index pada kedua tabel tersebut sebagai join key, tanpa index, hal ini tidak akan berhasil.

Coba lihat kasusnya.

![join](../../pict/join1.png)

dengan output:

![join](../../pict/join2.png)

Terdapat error berupa:

```
ValueError: columns overlap but no suffix specified: Index(['key'], dtype='object')
```
 
Untuk itu, jika dilakukan seperti ini:

![join](../../pict/join3.png)

akan menghasilkan:

![join](../../pict/join4.png)

secara default, fungsi join ini akan mengeksekusi left join.

Untuk tipe join yang lain (contoh=inner), harus men-specify keyword how='inner' seperti yang dicontohkan berikut ini:

![join](../../pict/join5.png)

dengan output:

![join](../../pict/join6.png)

Tugas Praktek:


Lakukanlah seperti yang dicontohkan tetapi penggabungan dengan method join berupa outer join.

Jika berhasil dijalankan hasil berikut yang akan diperoleh:

![join](../../pict/join7.png)

## Quiz
Diberikan dataframe sebagai berikut:
```
df1 = pd.DataFrame({
   'key':['k1','k2','k3','k4','k5'],
   'val1':[200, 500, 0, 500, 100],
   'val2':[30, 50, 100, 20, 10],
  
})
df2 = pd.DataFrame({
   'key':['k1','k1','k5','k7','k10'],
   'val3':[1,2,3,4,5],
   'val4':[6,7,8,8,10]
})
```

Apa yang akan dihasilkan oleh code ini?
```
pd.merge(df1, df2, validate="1:1")
```

# Pivot, Melt, Stack & Unstack
## Pendahuluan
Kotak masuk email-ku tak hentinya menerima sejumlah link baru dari Andra untuk bab-bab yang akan kupelajari di modul Pandas part 2 ini. Banyak sekali referensi dari Andra!

“Pivot, Melt, Stack, dan Unstack, apa ini?” gumamku sendiri membaca subject email Andra.

Aku pun bergegas mengaksesnya:

Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html

Melakukan format ulang pada dataset itu sangatlah penting, biasanya hal ini dilakukan untuk mengetahui keseluruhan data secara cepat dengan chart atau visualisasi. Untuk orang yang sudah mahir menggunakan spreadsheet pastilah tau banyak tentang fitur pivot ini.

Di Pandas, ada beberapa teknik untuk melakukan pivot atau unpivot yang biasa disebut as melt di Pandas, terdapat pula konsep stack yang artinya menumpuk data dengan kolom yang lebih sedikit (stack) sama seperti konsep melt dan ada pula yang memperluas data dengan kolom yang lebih banyak (unstack) sama seperti konsep pivot.

## Dataset
Untuk memahami konsep pivot, melt, stack, dan unstack pada Pandas mari persiapkan dataset sederhana terlebih dahulu.

![ds](../../pict/dataset1.png)

dengan output:

![ds](../../pict/dataset2.png)

Tugas Praktek:

Carilah unique records/value pada keempat kolom dataframe 'data'.

Jalankanlah dengan menekan tombol . Jika berjalan dengan lancar maka akan memperoleh output di console seperti yang ditunjukkan berikut ini:

![ds](../../pict/dataset3.png)

## Pivot 

Untuk menerapkan menerapkan method .pivot() pada dataframe dapat dilakukan pada dataframe yang memiliki index tunggal ataupun index-nya adalah multi index.

Untuk dataset yang masih sama, yaitu data.

![ds](../../pict/pivot1.png)

Pivoting dengan single column measurement.

![ds](../../pict/pivot2.png)

dengan output:

![ds](../../pict/pivot3.png)

Pivoting dengan multiple column measurement.

![ds](../../pict/pivot4.png)

dengan output:

![ds](../../pict/pivot5.png)

Penjelasan:

Apa yang berbeda dari kedua code di atas? Pada code pertama di specify values mana yang akan dilakukan pivot sedangkan di kedua tidak specific mana yang akan dilakukan pivot maka Pandas secara default men-treat kolom yang ada selain yang telah di specify as index dan columns as values instead.

Tugas Praktik:

Ketikkanlah kembali kode-kode yang diberikan di atas agar dapat lebih memahami konsep pivoting yang telah diberikan.

## Pivot_table 
Apa yang terjadi kalau output pivot tabel memiliki duplicate index? Seperti yang diketahui, index di dataframe adalah unique identifier untuk setiap row, jadi tidak boleh ada duplikat dan setiap membuat pivot tabel, harus specify index as kolom yang mana dan columns-nya memakai kolom yang mana.

Perhatikan contoh yang diilustrasikan berikut ini!

![pvttbl](../../pict/pivot-table1.png)

dengan output:

![pvttbl](../../pict/pivot-table2.png)

Hal ini dapat diatasi dengan melakukan method .pivot_table() pada dataframe. Metode ini sama seperti melakukan pivot pada tabel tapi juga melakukan groupby dan aggregation (aggfunc) pada level rows sehingga dipastikan tidak ada duplicate index di rows (secara default aggfunc = 'mean').

Perhatikan cuplikan berikut ini!

![pvttbl](../../pict/pivot-table3.png)

dengan output:

![pvttbl](../../pict/pivot-table4.png)

Keyword aggfunc yang digunakan pada method .pivot_table() dapat menggunakan nilai berikut:

* sum
* *'mean'*
* *'median'*

Tugas Praktek:

Seperti yang dicontohkan untuk meng-create pivot tabel dengan method .pivot_table() tetapi aggfunc yang digunakan adalah 'mean' dan 'median'.

Jalankanlah kode yang telah dibuat dengan menekan , jika tidak ada kesalahan maka output berikut akan diperoleh di console.

![pvttbl](../../pict/pivot-table5.png)

## Melt - Part 1

Teknik melt melalui pd.melt() digunakan untuk mengembalikan kondisi data yang sudah dilakukan pivot menjadi sebelum pivot.

Mari diperhatikan kembali dataframe yang telah digunakan sebelumnya dan dataframenya sudah di pivot.

![melt](../../pict/melt1_1.png)

dengan bentuk dataframe dari output baris ke-11.

![melt](../../pict/melt1_2.png)

Akan melakukan teknik melting pada dataframe output di atas.

[1] Melting dataframe

![melt](../../pict/melt1_3.png)

yang menghasilkan output:

![melt](../../pict/melt1_4.png)

[2] Dengan menspesifikasi keyword argument id_vars yang ditujukan untuk membuat fix kolom yang sebagai id tiap barisnya.

![melt](../../pict/melt1_5.png)

dengan output:

![melt](../../pict/melt1_6.png)

Tugas Praktik:

Kerjakanlah di code editor dengan cara mengisi kode yang tidak lengkap (_ _ _) sesuai dengan yang telah dicontohkan.

## Melt - Part 2
Mari melanjutkan ke bagian kedua dari penggunaan teknik melt ini. Mari lihat kembali dataframe yang telah diperoleh melalui pivoting

![melt2](../../pict/melt2_1.png)

dengan bentuk dataframe dari output baris ke-11.

![melt2](../../pict/melt2_2.png)

Lanjutkan dengan melakukan teknik melting pada dataframe output di atas untuk keyword argumen lainnya, yaitu

[3] Dengan menspesifikasikan keyword argument value_vars yang digunakan untuk menampilkan variasi value apa saja yang perlu dimunculkan di kolom variable. 

dengan output:

![melt2](../../pict/melt2_3.png)

[4] Dengan spesifikasikan keyword argument var_name dan value_name yang digunakan untuk menampilkan nama kolom untuk variable dan value.

![melt2](../../pict/melt2_4.png)

dengan output di console:

![melt2](../../pict/melt2_5.png)

Tugas Praktik:

Kerjakanlah di code editor dengan jalan mengisi kode yang tidak lengkap (_ _ _) sesuai dengan yang telah dicontohkan.

## Stack & Unstack - Part 1
Konsep stacking dan unstacking sama dengan melt dan pivot secara berurutan, hanya saja tidak memasukkan index sebagai parameter di stack/unstack tapi harus set index terlebih dahulu, baru bisa melakukan stacking/unstacking dengan level yang bisa ditentukan sendiri.

Perhatikan kembali dataframe berikut dengan multi index-nya.

![stackunstack](../../pict/stact_unstack1_1.png)

dengan output:

![stackunstack](../../pict/stact_unstack1_2.png)

Mari terapkan bagaimana menggunakan teknik stacking dan unstacking ini pada dataframe multi index 'data':

[1] Unstacking dataframe

![stackunstack](../../pict/stact_unstack1_3.png)

dengan output:

![stackunstack](../../pict/stact_unstack1_4.png)

[2] Unstacking dengan specify level name

![stackunstack](../../pict/stact_unstack1_5.png)

dengan output-nya di console:

![stackunstack](../../pict/stact_unstack1_6.png)

[3] Unstacking dengan specify level position

![stackunstack](../../pict/stact_unstack1_7.png)

dengan output yang diperoleh di console:

![stackunstack](../../pict/stact_unstack1_8.png)

Tugas Praktik:

Kerjakanlah di code editor dengan jalan mengisi kode yang tidak lengkap (_ _ _) sesuai dengan yang telah dicontohkan.

## Stack & Unstack - Part 2

Dalam bagian kedua dari Stack & Unstack ini akan membahas stacking dataframe. Untuk itu, mari diperhatikan dataframe berikut ini:

![stackunstack2](../../pict/stact_unstack2_1.png)

dengan dataframe yang dicetak pada langkah ke-11.

![stackunstack2](../../pict/stact_unstack2_2.png)

[1] Stacking dataframe 

![stackunstack2](../../pict/stact_unstack2_4.png)

dengan output di console:

![stackunstack2](../../pict/stact_unstack2_3.png)

[2] Tukar posisi index setelah stacking dataframe

![stackunstack2](../../pict/stact_unstack2_5.png)

dengan output:

![stackunstack2](../../pict/stact_unstack2_6.png)

[3] Melakukan sort_index pada stacking dataframe

![stackunstack2](../../pict/stact_unstack2_7.png)


dengan output yang diperoleh di console:

![stackunstack2](../../pict/stact_unstack2_8.png)

Tugas Praktik:

Kerjakanlah di code editor dengan jalan mengisi kode yang tidak lengkap (_ _ _) sesuai dengan yang telah dicontohkan.

 
## Quiz
Diberikan dataframe:

![quiz](../../pict/quiz_1.png)

Bagaimana cara untuk menghasilkan output seperti di bawah ini?

![quiz](../../pict/quiz_2.png)

# Aggregation & GroupBy
## Pendahuluan
Teknik agregasi diperlukan ketika mau melihat dataset dengan view yang berbeda, bisa set data tersebut akan dikelompokkan seperti apa, yang kemudian juga bisa menerapkan beberapa fungsi atau metode statistik ke hasil group dataset itu untuk mengetahui behavior dari data tersebut secara summary/overview.

**Basic Concept of Groupby & Aggregation**

![agg](../../pict/pend_aggre.png)

Groupby memiliki konsep untuk:

Split: melakukan indexing/multi-indexing dengan apa yang di specify as groupby menjadi kelompok
Apply: menerapkan fungsi pada masing-masing kelompok tersebut
Combine: mengumpulkan semua hasil fungsi dari tiap kelompok kembali menjadi dataframe

## Review Inspeksi Data

## Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 1
## Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 2
## Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 3
## Groupby dengan Multiple Aggregations
## Groupby dengan Custom Aggregations
## Groupby dengan Custom Aggregations by dict
## Quiz