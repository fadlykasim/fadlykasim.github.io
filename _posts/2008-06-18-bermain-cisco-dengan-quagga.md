---
layout: post
title: "Bermain Cisco dengan&nbsp;quagga"
date: 2008-06-18T16:14:36+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/06/18/bermain-cisco-dengan-quagga/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/06/18/bermain-cisco-dengan-quagga/), ditulis pada 2008-06-18.

Sedikit share, karena saya tidak ada cisco betulan, dan pingin sekali konfigurasi Cisco untuk itu saya mencoba pelajari setting network menggunakan quagga. awalnya saya mengintall quagga dengan cara

> $sudo apt-get install quagga quagga-doc

setelah instalasi selesai kita akan merubah file daemons didalam direktori /etc/quagga

> Konfigurasi awal quagga berada di direktori /etc/quagga
> 
> # ls /etc/quagga
> 
> daemons
> 
> debian.conf

Langkah-­langkah untuk menggunakan routing protokol :

1\. Memilih daemon routing protokol yang akan digunakan

2\. Membuat konfigurasi dasar

3\. Mengaktifkan daemon

4\. Login ke aplikasi routing protokol

5\. Melakukan distribusi jaringan pada PC router

yaitu dengan merubah sesui dengan protokal yang nantinya kita gunakan. dengan cara merubah “no” menjadi “yes” contoh:

> zebra = yes
> 
> bgpd = yes

Artinya kita mengaktifkan protokol zebra (wajib) dan protokol bgpd dan contoh tersebut bisa juga dilakukan untuk protokol routing lainnya, protokol tidak lain merupakan set rule yang memberitahu cara divice-device dalam jaringan bertukar informasih, protokal routing ini adalah protokol-protokol yang digunakan untuk merawat tabel routing pada router-router. Untuk itu ada beberapa protokol yang saya tidak aktifkan seperti dibawah ini

> ospfd=no  
>  ospf6d=no  
>  ripd=no  
>  ripngd=no  
>  isisd=no
> 
> kemudian copy file berikut ini

> cp /usr/share/doc/quagga/zebra.conf.sample /etc/quagga/zebra.conf
> 
> cp /usr/share/doc/quagga/bgpd.conf.sample /etc/quagga/bgpd.conf

begitu juga dengan daemon yang lain jika kita menggunakannya

Setelah membuat konfigurasi zebra.conf dan routing protokol (misal bgpd.conf), daemonrouting protokol perlu diaktifkan dengan cara :

> $sudo /etc/init.d/quagga start

Begitu juga untuk restart dan stop

> $sudo /etc/init.d/quagga stop
> 
> $sudo /etc/init.d/quagga restart

jika selesai silahkan melihat log file quagga yaitu dengan cara

> $sudo tail -f /var/log/quagga/bgpd.log  
>  2008/06/18 23:32:04 BGP: BGPd 0.99.9 starting: vty@2605, bgp@179

> $sudo tail -f /var/log/quagga/zebra.log  
>  2008/06/18 23:32:03 ZEBRA: Zebra 0.99.9 starting: vty@2601

diatas adalah tampilan log bgpd dan zebra di komputer saya. kemudia kita akan mengecek dengan cara melakukan perintah nmap

> $nmap localhost
> 
> 2601/tcp open zebra  
>  2605/tcp open bgpd

ternyata zebra dan protokol bgpd sudah berjalan

Untuk dapat login ke routing protokol, kita dapat menggunakan aplikasi TELNET, sedangkan untuk mengetahui port dari aplikasi routing protokol dapat dilakukan dengan perintah netstat ­nlptu untuk melihat port zebra dan routing daemon yang lainnya

> $sudo netstat -nlptu | grep zebra
> 
> 0.0.0.0:*tcp 0 0 127.0.0.1:2601 LISTEN 7567/zebra
> 
> $sudo netstat -nlptu | grepbgpd
> 
> 0.0.0.0:*tcp 0 0 127.0.0.1:2605 LISTEN 7571/bgpd

sekarang kita akan mencoba membuat static routing, sebelum membuat static routing saya akan menjelaskan mekanisme routing, setiap tabel routing pada router-router akan membutuhkan update. Jika proses update dilakukan manual, maka disebut Static Routing.

Routing berlangsung pada layer 3 (Network Layer), untuk membangun rute-rute, suatu router di antaranya harus mengetahui beberapa informasih spesifik yaitu, Address tujuan, router-router lain yang berdekatan, rute-rute yang memungkinkan ke jaringan tujuan dan rute terbaik untuk melintasinya.

untuk membangun dan merawat tabel routing, router menggunakan empat mekanisme dasar :

  * Direct Connection
  * Static Routing
  * Default Routing
  * Dynamic Routing



**Direct Connection**

Direct Connection adalah bentuk koneksi dimana router terhubung secara langsung atau ditambahkan secara otomatis ke table routing, jaringan yang terhubung langsung dengan router akan memiliki nilai Administrative Distence nol (0), ini merupakan nilai distence terendah dan sekaligus rute paling terpercaya.

**[Static Routing](http://id.wikipedia.org/wiki/Router "Static Routing"), [Default Routing](http://id.wikipedia.org/wiki/Alamat_IP_versi_4 "Default Routing"), [Dynamic Routing](http://id.wikipedia.org/wiki/Router "Dynamic Routing")**

Untuk Arsitektur Quagga dibagi menjadi 2 yaitu :

1\. Zebra – merupakan bagian penghubung antara linux kernel dengan aplikasi routing protokol

2\. Routing Daemon – merupakan aplikasi pengatur routing protokol. Misal: ospfd, adalah aplikasi yang mengatur routing protokol OSPF, RIPD adalah aplikasi yang mengatur routing protokol RIP, begitu juga dengan bgpd.

Perintah Quagga, mirip dengan perintah yang ada di CISCO router.

Untuk zebra menggunakan port 2601 dan untuk ospfd 2604, bgpd 2605, artinya kita dapat masuk keaplikasi tersebut melalui port­-port tersebut

> $telnet localhost 2601
> 
> Trying 127.0.0.1…Connected to localhost.localdomain.
> 
> Escape character is ‘^]’.
> 
> Hello, this is Quagga (version 0.98.3).
> 
> Copyright 1996-2005 Kunihiro Ishiguro, et al.
> 
> User Access Verification
> 
> Password:

Untuk login kita gunakan password awalnya “zebra” (tanpa petik dua, sesuai dengankonfigurasi). Sehingga muncul “Router >” atau “ospfd>” dan “bgpd>”

Yang merupakan prompt awal pada quagga. Begitu juga apabila menggunakan ripd atau lainnya.

Contoh Gambar 1

[![](https://firstly.wordpress.com/wp-content/uploads/2008/06/1.png?w=300&h=116)](http://firstly.wordpress.com/wp-content/uploads/2008/06/1.png)

gambar.1

Dengan kondisi topologi diatas, apabila kita berada di network A, kita hanya dapat mengetahui bahwa kita memiliki 2 jaringan 10.252.108.0/24 dengan 192.168.1.0/24. Dapat dipastikan bahwa kita belum tentu tahu jaringan yang berada dibalik Router B. Begitu juga sebaliknya. Supaya network A bisa menghubungi network B, pada router A harus ditambahkan table routing yang menuju ke Network B. Dengan perintah

> RouterA#ip route add 192.168.2.0/24 via 10.252.108.15

Itu dapat dilakukan apabila kita mengetahui IP jaringan dibalik router B, dan apabila jumlah jaringan yang dituju cuma 1. Bagaimana bila yang dituju ada 1000Router ???? ….

Untuk itu antar router harus saling bertukar informasi table routing dengan menggunakanrouting protokol.

Pada quagga kita dapat lakukan pendistribusian dengan cara :­ Login ke aplikasi routing protokol (misal: ospfd dengan port 2604) dengan password“zebra”

> Router# telnet localhost 2604
> 
> Trying 127.0.0.1…
> 
> Connected to localhost.localdomain.
> 
> Escape character is ‘^]’.
> 
> Hello, this is Quagga (version 0.98.3).
> 
> Copyright 1996-2005 Kunihiro Ishiguro, et al.
> 
> User Access Verification
> 
> Password:
> 
> ospfd>­
> 
> Naik ke privillages berikutnya dengan perintah “enable”
> 
> ospfd> en­

– Masuk ke mode configurasi dengan perintah “configure terminal”

> ospfd# conf t

– Mengaktifkan tipe routing

> ospfd(config)#router ospf­

– Mendistribusikan jaringan yang dimiliki oleh route

> rospfd(config-router)# network 10.252.108.0/24 area 0
> 
> ospfd(config-router)# network 192.168.1.0/24 area 0

– Simpan konfigurasi dengan perintah:

> Ctrl­-Z
> 
> ospfd# wr

PC Router harus diaktifkan ip forwardingnya melalui terminal dengan cara:

> $ sudo echo 1 > /proc/sys/net/ipv4/ip_forward

Atau dengan cara mengaktifkan melalui zebra, dengan password “zebra”

Telnet ke port 2601

> $telnet localhost 2601
> 
> Trying 127.0.0.1…
> 
> Connected to localhost.localdomain.
> 
> Escape character is ‘^]’.
> 
> Hello, this is Quagga (version 0.98.3).
> 
> Copyright 1996-2005 Kunihiro Ishiguro, et al.
> 
> User Access Verification
> 
> Password:

Lakukan “enable” dengan password “zebra”

> Router> en
> 
> Password:

Masuk ke mode configurasi dengan perintah “configure terminal”

> Router# conf t

Mengaktifkan ip forwarding

> Router(config)# ip forwarding

Simpan dengan kembali ke mode enable dengan menekan CTRL­+Z, kemudian lakukan

perintah “write memory”

> Router(config)#
> 
> Router# wr
