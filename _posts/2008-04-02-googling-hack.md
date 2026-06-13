---
layout: post
title: "Googling Hack"
date: 2008-04-02T08:49:36+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/04/02/googling-hack/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/04/02/googling-hack/), ditulis pada 2008-04-02.

Ini saya dapat dari [Harry Chan Putra,SP](http://harrychanputra.wordpress.com "Harry Chanputra") maaf ya copy paste

Googling hack  
\” Intitle:\” ialah sintaks perintah untuk membatasi pencarian yang hanya menghasilkan judul yang mengandung informasi pada topik yang  
dimaksud. Sebagai contoh pada pencarian, ?intitle:  
password admin ? ( tanpa tanda kutip ). Pencarian akan mencari page yang mengandung kata ? password ? sebagai judulnya dengan prioritas utama ?admin? .  
Jika pada pencarian terdapat dua query pencarian utama, digunakan sintaks allintitle: untuk pencarian secara lengkap. Sebagai contoh pada pencarian ?allintitle:admin mdb?. Maka pencarian akan dibatasi pada dua subjek utama judul yaitu ?admin? dan ?mdb?.  
  
? inurl:? ialah sintaks perintah untuk membatasi pencarian yang hanya menghasilkan semua URL yang hanya berisi kata kunci informasi yang dimaksudkan. Sebagai contoh pencarian dalam pencarian,?inurl : database mdb?. Pencarian akan menghasilkan semua URL yang hanya mengandung informasi tentang ?database mdb ?.  
Hal yang sama juga berlaku pada sintaks ini, jika terdapat dua query pencarian utama, digunakan sintaks ?allinurl:? untuk mendapatkan list url tersebut.  
Sebagai contoh pencarian ?allinurl: etc/passwd? , pencarian akan menghasilkan URL yang mengandung informasi tentang ?etc? dan ?passwd?. Tanda garis miring slash (?/?) diantara dua kata etc dan passwd akan diabaikan oleh mesin pencari Google.

?site:? ialah sintaks perintah untuk membatasi pencarian suatu query informasi berdasarkan pada suatu situs atau domain tertentu. Sebagai contoh pada pencarian informasi: ?waveguide site:itb.ac.id? (tanpa tanda kutip). Pencarian akan mencari topic tentang waveguide pada semua halaman yang tersedia pada domain itb.ac.id.

?cache:? akan menunjukkan daftar web yang telah masuk kedalam indeks database Google. Sebagai contoh:  
?cache:deffcon.org?, pencarian akan memperlihatkan list yang disimpan pada Google untuk page deffcon.org

?filetype:? ialah sintaks perintah pada Google untuk pencarian data pada internet dengan ekstensi tertentu (i.e. doc, pdf or ppt etc). Sebagai contoh pada pencarian : ?filetype:doc site:go.id confidental? ( tanpa tanda kutip). Pencarian akan menghasilkan file data dengan ekstensi ?.doc? pada semua domain go.id yang berisi informasi ?confidential?.

?link:? ialah sintaks perintah pada Google yang akan menunjukkan daftar list webpages yang memiliki link pada webpage special. Sebagai contoh:?link:www.securityfocus.com? akan menunjuukan daftar webpage yang memiliki point link pada page SecurityFocus.

?related:? sintaks ini akan memberikan daftar web pages yang serupa dengan web page yang di indikasikan.  
Sebagai contoh: ?related:www.securityfocus.com?, pencarian akan memberi daftar web page yang serupa dengan homepage Securityfocus.

?intext:? sintaks perintah ini akan mencari kata kata pada website tertentu. Perintah ini mengabaikan link atau URL dan judul halaman. Sebagai contoh :  
?intext:admin? (tanpa tanda petik), pencarian akan menghasilkan link pada web page yang memiliki keyword yang memiliki keyword admin.

Beberapa query sintaks diatas akan sangat membantu dalam pencarian data dan informasi lebih detail.  
Google dapat menjadi mesin pencari untuk menggali informasi tertentu dan rahasia, informasi yang tidak diperkirakan yang dapat memberitahukan sisi lemah suatu sistem. Hal tersebut yang dimanfaatkan oleh sebagian individu untuk melakukan penetrasi suatu server atau sistem informasi .

Sintaks ?Index of ? dapat digunakan untuk mendapatkan situs yang menampilkan indeks browsing direktori.  
Webserver dengan indeks browsing yang dapat diakses, berarti siapa saja dapat melakukan akses pada direktori webserver, seperti layaknya dapat dilakukan pada lokal direktori pada umumnya.  
Pada kesempatan ini dipaparkan bagaimana penggunaan sintaks ?index of? untuk mendapatkan hubungan pada webserver dengan direktori indeks browsing yang dapat diakses.. Hal tersebut merupakan sumber informasi yang sederhana dapat diperoleh, akan tetapi isi dari informasi seringkali merupakan informasi yang sangat penting. Informasi tersebut dapat saja berupa password akses atau data transaksi online dan hal yang sangat penting lainnya.  
Dibawah ini merupakan beberapa contoh penggunaan sintaks ? indeks of? untuk mendapatkan informasi yang penting dan sensitive sifatnya.  
ex :  
Index of /admin  
Index of /passwd  
Index of /password  
Index of /mail  
\”Index of /\” +passwd  
\”Index of /\” +password.txt  
\”Index of /\” +.htaccess  
\”Index of /secret\”  
\”Index of /confidential\”  
\”Index of /root\”  
\”Index of /cgi-bin\”  
\”Index of /credit-card\”  
\”Index of /logs\”  
\”Index of /config\”  
\”Index of/admin.asp  
\”Index of/login.asp

Mencari sistem atau server yang vulnerable menggunakan sintaks ?inurl:? atau ?allinurl:?

1\. Menggunakan sintaks ?allinurl:winnt/system32/? (dengan tanda petik ) akan menampilkan daftar semua link pada server yang memberikan akses pada direktori yang terlarang seperti ?system32?. Terkadang akan didapat akses pada cmd.exe pada direktori ?system32? yang memungkinkan seseorang untuk mengambil alih kendali sistem pada server tersebut.

2\. Menggunakan ?allinurl:wwwboard/passwd.txt? ( dengan tanda petik ) akan menampilkan daftar semua link pada server yang memiliki kelemahan pada ?wwwboard Password?. Pembahasan lebih lanjut tentang vulnerability ?wwwboard Password? dapat dilihat pada site keamanan jaringan seperti <http://www.securityfocus.com> atau <http://www.securitytracker.com>

3\. Menggunakan sintaks ?inurl: bash history? (dengan tanda petik ) akan menampilkan daftar link pada server yang memberikan akses pada file ?bash history? melalui web. File tersebut merupakan command history file yang mengandung daftar perintah yang dieksekusi oleh administrator, yang terkadang menyangkut informasi sensitive seperti password sistem. Seringkali password pada sistem telah dienkripsi, untuk mendapatkan password aslinya bentuk yang dienkripsi ini harus didekripsi menggunakan program password cracker. Lama waktu untuk mendapatkan hasil dekripsi tergantung dari keandalan program dan banyaknya karakter yang terenkripsi.

4\. Menggunakan ?inurl:config.txt? (dengan tanda petik) akan menampilkan daftar semua link pada server yang memberikan akses pada file ?config.txt. File ini berisi informasi penting termasuk hash value dari password administrator dan proses autentifikasi dari suatu database.

Sintaks ?inurl:? atau ?allinurl:? dapat dikombinasikan dengan sintaks yang lainnya seperti pada daftar dibawah ini :

Inurl: /cgi-bin/cart32.exe  
inurl:admin filetype:txt  
inurl:admin filetype:db  
inurl:admin filetype:cfg  
inurl:mysql filetype:cfg  
inurl:passwd filetype:txt  
inurl:iisadmin  
inurl:auth_user_file.txt  
inurl:orders.txt  
inurl:\”wwwroot/*.\”  
inurl:adpassword.txt  
inurl:webeditor.php  
inurl:file_upload.php  
inurl:gov filetype:xls \”restricted\”  
index of ftp +.mdb allinurl:/cgi-bin/ +mailto allinurl:/scripts/cart32.exe allinurl:/CuteNews/show_archives.php  
allinurl:/phpinfo.php  
allinurl:/privmsg.php  
allinurl:/privmsg.php  
inurl:cgi-bin/go.cgi?go=*  
allinurl:.cgi?page=*.txt  
allinurul:/modules/My_eGallery  
Mencari suatu sistem atau server yang memiliki kelemahan dengan sintaks ?intitle:?  
atau ?allintitle:?

1\. Menggunakan allintitle: \”index of /root? ( tanpa tanda kutip ) akan menampilkan  
Daftar link pada webserver yang memberikan akses pada direktori yang terlarang seperti direktori root.

2\. Menggunakan allintitle: \”index of /admin? ( tanpa tanda kutip ) akan menampilkan link pada site yang memiliki indeks browsing yang dapat diakses untuk direktori terlarang seperti direktori ?admin?.

Penggunaan lain dari sintaks ?intitle:? atau ?allintitle:? yang dikombinasikan dengan sintaks lainnya antara lain :

intitle:\”Index of\” .sh_history  
intitle:\”Index of\” .bash_history  
intitle:\”index of\” passwd  
intitle:\”index of\” people.lst  
intitle:\”index of\” pwd.db  
intitle:\”index of\” etc/shadow  
intitle:\”index of\” spwd  
intitle:\”index of\” master.passwd  
intitle:\”index of\” htpasswd  
intitle:\”index of\” members OR accounts  
intitle:\”index of\” user_carts OR user_cart  
allintitle: sensitive filetype:doc  
allintitle: restricted filetype :mail  
allintitle: restricted filetype:doc site:gov  
allintitle:*.php?filename=*  
allintitle:*.php?page=*  
allintitle:*.php?logon=*

Penggunaan dan kombinasi pada sintaks tidak hanya terbatas pada contoh paparan diatas. Masih banyak lagi kombinasi dari sintaks sintaks dengan berbagai kata kunci yang dapat digunakan. Hal tersebut bergantung pada kreativitas dan kemauan untuk mencoba. Ada baiknya penggunaan wacana yang telah dipaparkan ini digunakan untuk kepentingan yang tidak menimbulkan kerugian atau kerusakan.  
Kelemahan pada suatu sistem atau server yang diketahui ada baiknya dilakukan sharing dengan administrator sistem yang bersangkutan sehingga dapat bermanfaat bagi semua pihak. Dikarenakan kemungkinan besar hasil dari pencarian informasi dapat memberikan informasi yang sensitive, yang seringkali menyangkut segi keamanan suatu sistem atau server.  
Wacana tentang sintaks yang sangat membantu dalam pencarian informasi tersebut akhirnya tergantung pada niat dan tujuan dalam pencarian data. Apakah sungguh sungguh dilakukan untuk kebutuhan pencarian data, mengumpulkan informasi dari suatu mesin target penetrasi. Tujuan akhirnya bergantung pada niat individu yang bersangkutan sehingga penulis tidak bertanggung jawab terhadap penyalahgunaan dari informasi yang telah dipaparkan. Seperti kata pepatah lama ? resiko ditanggung penumpang ?.
