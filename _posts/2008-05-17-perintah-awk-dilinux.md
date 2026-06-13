---
layout: post
title: "LOOP FOR"
date: 2008-05-17T11:51:37+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/05/17/perintah-awk-dilinux/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/05/17/perintah-awk-dilinux/), ditulis pada 2008-05-17.

Tulisan ini sangat membantu buat saya. coba bertanya di om google akhirnya ketemu. berikut saya paste disini biar ngga hilang dari peredaran, tengkyu buat om Kocil.

Misalkan anda jadi administrator network kampus. Tiap tahun ajaran baru, pasti akan disuruh bikin user untuk para murid baru. Kalau muridnya ratusan … bakal pegel deh..

Level: wannabee/hacker  
Oh tidak. Justru disini hebatnya komputer. Tidak seperti manusia yang gampang bosan, komputer mampu mengulang operasi serupa berkali-kali dengan patuh. Tapi tentu saja kalau kita tahu cara menyuruhnya.

Ini contoh program bash membuat 100 user baru. Tiap user akan dibuatkan:

1\. Nama login = NIM (Nomor Induk, misal dari 13304001-13324100)  
2\. Group = murid dan angkatan (2004)  
3\. Home = /export/home/NIM  
4\. password = sandiNIM (sementara, biar tidak kosong)  
5\. Skeleton = /etc/skel (setting user awal spt .bashrc, dll)

> #!/bin/sh
> 
> ## direktori standard  
>  HOME_BASE=”/export/home”  
>  SKELETON=”/etc/skel”

> ## Murid baru akan masuk group murid dan angkatan  
>  GROUP=”murid,2004″

> ## Misal group murid sudah ada  
>  ## Tapi perlu buat group angkatan  
>  groupadd -g 2004 2004

> ## Sekarang buat 100 user  
>  ## Loop for ini artinya  
>  ## AWAL LOOP : ID = 4001  
>  ## AKHIR LOOP : 4100 >= ID  
>  ## KETERATURAN TIAP KALI LOOP: ID=ID(lama)+1

> for (( ID=4001; 4001 >= $ID; ID=ID+1 )); do

> ## Konstruksi NIM buat nama login  
>  NIM=”1330$ID”

> ## Cetak buat checking  
>  echo “useradd -b $HOME_BASE -u $ID -G $GROUP -m -k $SKELETON $NIM”

> ## Tambah user  
>  useradd -d $HOME_BASE/$NIM -u $ID -G $GROUP -m -k $SKELETON $NIM

> ## Konstruksi password  
>  PASS=”sandi$NIM”

> ## Bikin password pakai passwdx (program expect sebelumnya)  
>  ## misal passwdx ada di /sbin  
>  /sbin/passwdx $NIM $PASS

> done ## SELESAI LOOP, ULANG DARI FOR LAGI

> ## Selesai  
>  #################################################
> 
> Contoh sebelumnya memperlihatkan loop for pakai angka, yang normal kita temui di bahasa seperti BASIC, PASCAL atau C. Sekarang kita akan lihat beberapa contoh loop for yang canggih.
> 
> * FOR untuk loop beberapa string
> 
> …  
>  ##############################################  
>  ## Loop for mencetak hari senin – minggu  
>  for HARI in senin selasa rabu kamis jumat sabtu minggu; do  
>  echo “Ini hari $HARI”  
>  done  
>  …

> * FOR untuk loop file di suatu direktori

> …  
>  #############################################  
>  ## Loop mencetak file berakhiran TXT  
>  for FILE in *.txt; do  
>  echo “Ada file TXT bernama $FILE”  
>  done  
>  …
> 
> * FOR untuk membaca baris teks dari file
> 
> …  
>  #############################################  
>  ## Loop mencetak baris file /etc/passwd  
>  for BARIS in `cat /etc/passwd`; do  
>  echo “Baris = $BARIS”  
>  done  
>  …

Jadi inti di sini (moral cerita kalau kata dosenku), kalau anda ketemu masalah yang perlu mengulang-ulang operasi maka:

* Temukan keteraturan dari operasi pertama ke operasi berikutnya sampai selesai. Terus terang ini perlu IQ lumayan. Ingat kan test IQ yang menjejerkan angka terus anda suruh menebak urutan berikutnya ? Nah, programmer perlu lulus test IQ itu 🙂  
* Temukan kondisi awal dan kondisi akhir. Nah disini programmer harus jago soal logika. Banyak bug software terjadi karena salah menentukan kondisi awal dan akhir !  
* Pakai konstruksi loop yang disediakan bahasa pemrograman. Biasanya pakai kata kunci FOR, WHILE, atau REPEAT. Kadang perlu dibantu IF, BREAK dan CONTINUE.

Kata dosen saya, ada 6 PAKEM loop (pakem = bahasa jawa, artinya urutan standar yang ngak boleh diselewengkan). Kalau nggak ikut pakem, algoritma program pasti salah. Buat tahu pakem-pakem tersebut, baca buku formal bangsa Knuth, Niclaus Wirth, dll. Buku-buku praktis tidak eksplisit mengajarkan soal pakem. Saya sendiri, karena otodidak baca buku-buku praktis, tahunan memrogram pakai PASCAL, C, FORTRAN, BASIC dll tanpa kenal pakem ! Setelah diajari, baru bisa berucap, “Oooooh … gitu tho”. Rasanya, tahu pakem vs. belum tahu pakem itu seperti membandingkan cara berenang istri saya (ikut kursus) vs. saya (gara-gara kecemplung ke laut). LOL 🙂

Copyleft : Kocil, 2004  
License : GNU FDL  
Posted to: <http://www.benpinter.net>, Mei 2004.  
Testbed : Vector Linux 4.0  
Writepad : Bluefish
