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
## Dataset 
## Pivot 
## Pivot_table 
## Melt - Part 1 
## Melt - Part 2
## Stack & Unstack - Part 1
## Stack & Unstack - Part 2 
## Quiz
