[1. Pengantar](#1-pengantar)
- [Pengantar](#pengantar)
- [Project yang Akan Dikerjakan](#project-yang-akan-dikerjakan)

[2. Transform Data](#2-transform-data)
[Extract](#extract)
[Transform](#transform)
[Transform Bagian I - Kode Pos](#transform-bagian-i---kode-pos)
[Transform Bagian II - Kota](#transform-bagian-ii---kota)
[Transform Bagian III - Github](#transform-bagian-iii---github)
[Transform Bagian IV - Nomor Handphone](#transform-bagian-iv---nomor-handphone)
[Transform Bagian V - Nama Tim](#transform-bagian-v---nama-tim)
[Transform Bagian VI - Email](#transform-bagian-vi---email)
[Transform Bagian VII - Tanggal Lahir](#transform-bagian-vii---tanggal-lahir)
[Transform Bagian VII - Tanggal Daftar Kompetisi](#transform-bagian-vii---tanggal-daftar-kompetisi)
[Kesimpulan](#kesimpulan)
[Load](#load)


# 1. Pengantar
## Pengantar

Di masa pandemi seperti ini, kompetisi coding seperti Competitive Programming maupun Hackathon banyak diselenggarakan karena sangat memungkinkan untuk dilakukan secara online.

Hackathon merupakan kompetisi membuat perangkat lunak (software) yang dilaksanakan secara marathon yang biasanya diikuti secara tim. Umumnya, peserta hackathon diminta untuk mengembangkan platform (mobile, web, desktop, dll.) dalam kurun waktu tertentu untuk menyelesaikan permasalahan yang sudah ditetapkan/didefinisikan oleh penyelenggara ataupun berdasarkan tema yang dipilih oleh tim tersebut.

Untuk bisa mengikuti hackathon dari suatu instansi, calon peserta diwajibkan untuk mendaftarkan diri mereka pada situs/form tertentu dengan memasukkan beberapa informasi yang diminta oleh penyelenggara tersebut.

Extract, Transform dan Load (ETL) merupakan kumpulan proses untuk "memindahkan" data dari satu tempat ke tempat lain.
Tempat yang dimaksud adalah dari sumber data (bisa berupa database aplikasi, file, logs, database dari 3rd party, dan lainnya) ke data warehouse.

Apa itu data warehouse?

Singkatnya, data warehouse merupakan database yang berisi data-data (tabel-tabel) yang sudah siap untuk dilakukan analisis oleh Data Analyst maupun Data Scientist.

Lebih lengkapnya bisa dilihat di:
https://en.wikipedia.org/wiki/Data_warehouse.

Pada modul ini kita akan mempelajari masing-masing dari proses tersebut.

## Project yang Akan Dikerjakan

Pada proyek kali ini, Anda diminta untuk mengolah data pendaftar hackathon yang diselenggarakan oleh DQLab bernama DQThon.

Dataset ini terdiri dari 5000 baris data (5000 pendaftar) dengan format CSV (Comma-separated values) dan memiliki beberapa kolom diantaranya:

- participant_id: ID dari peserta/partisipan hackathon. Kolom ini bersifat unique sehingga antar peserta pasti memiliki ID yang berbeda
- first_name: nama depan peserta
- last_name: nama belakang peserta
- birth_date: tanggal lahir peserta
- address: alamat tempat tinggal peserta
- phone_number: nomor hp/telepon peserta
- country: negara asal peserta
- institute: institusi peserta saat ini, bisa berupa nama perusahaan maupun nama universitas
- occupation: pekerjaan peserta saat ini
- register_time: waktu peserta melakukan pendaftaran hackathon dalam second
Namun pada proyek ini nantinya Anda diminta untuk menghasilkan beberapa kolom dengan memanfaatkan kolom-kolom yang ada, sehingga akhir dari proyek ini berupa hasil transformasi data dengan beberapa kolom baru selain dari 10 kolom diatas.

Sebagai pemanasan dalam proyek ini, Anda dipersilakan untuk membuka isi datasetnya dan melihat values-nya. Jika sudah siap dengan perjalanan di proyek ini, silakan klik Next.

# 2. Transform Data
## Extract

## Transform

Transform merupakan proses melakukan transformasi data, atau perubahan terhadap data. Umumnya seperti:

1. Merubah nilai dari suatu kolom ke nilai baru,
2. Menciptakan kolom baru dengan memanfaatkan kolom lain,
3. Transpose baris menjadi kolom (atau sebaliknya),
4. Mengubah format data ke bentuk yang lebih standard (contohnya, kolom date, maupun datetime yang biasanya memiliki nilai yang tidak standard maupun nomor HP yang biasanya memiliki nilai yang tidak sesuai format standardnya), dan lainnya. 

## Transform Bagian I - Kode Pos

Ada permintaan datang dari tim logistik bahwa mereka membutuhkan kode pos dari peserta agar pengiriman piala lebih mudah dan cepat sampai. Maka dari itu buatlah kolom baru bernama postal_code yang memuat informasi mengenai kode pos yang diambil dari alamat peserta (kolom address).

Diketahui bahwa kode pos berada di paling akhir dari alamat tersebut.

Note:
Jika regex yang dimasukkan tidak bisa menangkap pattern dari value kolom address maka akan menghasilkan NaN.

## Transform Bagian II - Kota

Selain kode pos, mereka juga membutuhkan kota dari peserta.

Untuk menyediakan informasi tersebut, buatlah kolom baru bernama city yang didapat dari kolom address. Diasumsikan bahwa kota merupakan sekumpulan karakter yang terdapat setelah nomor jalan diikuti dengan \n (newline character) atau dalam bahasa lainnya yaitu enter.

## Transform Bagian III - Github

Salah satu parameter untuk mengetahui proyek apa saja yang pernah dikerjakan oleh peserta yaitu dari git repository mereka.

Pada kasus ini kita menggunakan profil github sebagai parameternya. Tugas Anda yaitu membuat kolom baru bernama github_profile yang merupakan link profil github dari peserta.

Diketahui bahwa profil github mereka merupakan gabungan dari first_name dan last_name yang sudah di-lowercase. 

## Transform Bagian IV - Nomor Handphone

Jika kita lihat kembali, ternyata nomor handphone yang ada pada data csv kita memiliki format yang berbeda-beda. Maka dari itu, kita perlu untuk melakukan cleansing pada data nomor handphone agar memiliki format yang sama. Anda sebagai Data Engineer diberi privilege untuk menentukan format nomor handphone yang benar. Pada kasus ini mari kita samakan formatnya dengan aturan:

Jika awalan nomor HP berupa angka 62 atau +62 yang merupakan kode telepon Indonesia, maka diterjemahkan ke 0.
Tidak ada tanda baca seperti kurung buka, kurung tutup, strip⟶ ()-
Tidak ada spasi pada nomor HP nama kolom untuk menyimpan hasil cleansing pada nomor HP yaitu cleaned_phone_number

## Transform Bagian V - Nama Tim

Dataset saat ini belum memuat nama tim, dan rupanya dari tim Data Analyst membutuhkan informasi terkait nama tim dari masing-masing peserta.

Diketahui bahwa nama tim merupakan gabungan nilai dari kolom first_name, last_name, country dan institute.

Tugas Anda yakni buatlah kolom baru dengan nama team_name yang memuat informasi nama tim dari peserta.

## Transform Bagian VI - Email
## Transform Bagian VII - Tanggal Lahir
## Transform Bagian VII - Tanggal Daftar Kompetisi
## Kesimpulan
## Load