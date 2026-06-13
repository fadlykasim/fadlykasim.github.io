---
layout: post
title: "Tips: Membuat SLAPT&nbsp;Package"
date: 2008-05-17T12:00:37+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/05/17/tips-membuat-slapt-package/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/05/17/tips-membuat-slapt-package/), ditulis pada 2008-05-17.

SLAPT (Slackware Advanced package Tools) adalah utilitas manajemen paket yang memungkinkan kita menginstall suatu paket berikut dependensi-dependensinya. Ini rahasia membuat paket-paketnya.

Mereka yang pakai Debian (juga derivativenya seperti UBuntu, Mepis) sudah lama menikmati fasilitas manajemen paket otomatis ini. Di Slackware, ada beberapa pilihan utilitas dengan tujuan sama, misalnya SWARET atau SLAPT. SWARET mendeteksi dependensi dengan langsung menggalinya dari file binary, lalu mengejar paket yang diperlukan dari file MANIFEST yang ada di direktori standar /packages di CDROM atau mirror Slackware. Sementara itu slapt memilih pendekatan lain, yaitu dengan menambahkan file dependency ke dalam paket Slackware. Dengan demikian, SWARET dapat bekerja dengan paket-paket asli Slackware, sedang SLAPT membutuhkan paket yang telah dimodifikasi.

Walau tidak kompatible dengan paket asli Slackware, ternyata pendekatan SLAPT lebih terpercaya (reliable). Karena itu SLAPT telah diadopsi oleh Linux-Packages, College Linux maupun Vector Linux. Sementara itu Vector Linux maju selangkah lebih jauh dengan menyediakan fasilitas untuk membuat paket yang kompatibel dengan SLAPT secara otomatis. Ini dia caranya.

Misalkan saja kita akan membuat paket sqlite (embedded SQL database memakai bahasa C).

1\. Download kode sumber paket berupa tarball dari homepagenya. Misalnya sqlite-3.2.2.tar.gz  
2\. Pergi ke direktori kompilasi, misal $HOME/src, lalu ekstrak

> $ tar -xzf /download/sqlite-3.2.2.tar.gz

3\. Pergi ke direktori sqlite yang baru

> $ cd sqlite-3.2.2

4\. Eksport FLAG kompilasi (optional, flag ini adalah standard VL 5.x)

> $ export CFLAGS=”-O2 -march=i586 -mcpu=i686″

5\. Konfigurasi paket, options prefix dan sysconfdir disini adalah standard VL 5.x

> $ ./configure –prefix=/usr –sysconfdir=/etc/sqlite

6\. Mulai kompilasi

> $ make

7\. Jadi root untuk instalasi

> $ su

8\. Bikin paket. Perhatikan, biasanya disini kita pakai “make install”, namun hal tersebut akan memasang paket sqlite ke sistem. Dengan perintah checkinstall ini, paket tidak akan dipasang namun dijadikan paket-tgz.

> $ checkinstall

9\. Nah, paket anda akan siap sebagai sqlite-2.3.3-i386-1.tgz. Kalau mau anda pasang sendiri tinggal

> $ installpkg sqlite-2.3.3-i386-1.tgz

10\. Hebatnya pakai cara ini di VL 5.x, paket yang dihasilkan otomatis mengandung informasi dependensi yang diperlukan oleh SLAPT. Untuk melihatnya coba

> root:# tar -xzf sqlite-3.2.2-i386-1.tgz install/slack-required  
>  root:# cat install/slack-required  
>  readline >= 4.3  
>  ncurses >= 5.4  
>  gpm >= 1.19.6

Itu artinya, sqlite membutuhkan paket readline, ncurses dan gpm.

Paket sqlite ini bisa anda sumbangkan ke Linux Package atau Vector Linux. Setelah diterima dan ditaruh di package repository mereka, nantinya semua orang yang terhubung ke Internet bisa memasang paket ini dengan perintah

> $slapt-get –install sqlite

Dengan satu perintah tersebut, sqlite akan dipasang berikut paket-paket dependesinya yang belum terpasang, yaitu readline, ncurses maupun gpm. Asik kan.
