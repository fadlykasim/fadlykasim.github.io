---
layout: post
title: "Koneksi Bluetooth Modem di Nokia e61 menggunakan Hardy&nbsp;Heron"
date: 2008-05-20T14:59:47+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/05/20/koneksi-bluetooth-modem-di-nokia-e61-menggunakan-hardy-heron/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/05/20/koneksi-bluetooth-modem-di-nokia-e61-menggunakan-hardy-heron/), ditulis pada 2008-05-20.

Untuk koneksi ini saya menggunakan _Nokia e61_ dan menggunakan device _USB Bluetooth_ , jadi disini ada dua cara untuk setingannya yaitu menggunakan [CLI](http://en.wikipedia.org/wiki/Command_line_interface "CLI") dan menggunakan _KPPP_ , yang dibutuhkan yaitu aplikasi _Bluetooth_ dan _wvdial_ , secara _default_ keduanya sudah terpasang pada _Ubuntu Hardy Heron_ . berikut langkah-langkahnya sampai selesai.Menggunakan [CLI](http://en.wikipedia.org/wiki/Command_line_interface "CLI")

Lakukan perintah lsusb

> _root@firstly:/home/fadly# lsusb_ _Bus 004 Device 003: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)_

tampilan di atas menunjukkan tipe _Bluetooth_ yang saya gunakan.

  * kemudian konfigurasi file hcid.conf vi /etc/bluetooth/hcid.conf, yang perlu di rubah adalah pada bagian _options_ yaitu _security_ di set menjadi **_security auto;_** dan **_passkey “1234”_** atau _passkey_ diset sesuai dengan selera anda, ini maksudnya ketika kita inisiasi pairing dari device ubuntu akan secara otomatis menerima dengan _passkey_ yang sudah kita tentukan tadi.

  * Lakukan pairing dari device, dalam hal ini nokia e61. Dan nantinya akan di tanyakan passkey, isi dengan passkey yang sudah kita tentukan dilangkah pertama.
  * Berikutnya kita akan mencari tau MAC address dari nokia e61 yang sudah di set mode discoverable, menggunakan perintah hcitool scan. Catat alamat yang didapat, sebagai contoh alamat MAC Nokia E61 saya adalah




> root@firstly:/home/fadly# hcitool scan Scanning … 00:12:D1:D4:80:55 Fadly 

  * Mencari tahu _channel_ number yang digunakan oleh _device_ untuk _dialup networking_ , dengan menggunakan perintah _sdptool browse <mac-address-kamu>_ sebagai contoh _  
_



_sdptool browsing 00:12:D1:D4:80:55_ cari bagian “ _Service Dial-Up Networking_ ” lihat “ _RFCOMM_ ” dibawahnya ada tulisan _channel_ catat angka _channel_ ini, ingat tiap ponsel _channelnya_ selalu berbeda-beda, berikut adalah tampilan dari komputer saya setelah melakukan perintah dibawah ini :

> #sdptool browsing 00:12:D1:D4:80:55 Service Name: Dial-Up Networking  Service RecHandle: 0x10001 Service Class ID List: “Dialup Networking” (0x1103) Protocol Descriptor List: “L2CAP” (0x0100) “RFCOMM” (0x0003) Channel: 2 

  * Edit file **rfcomm.conf** isinya saya punya seperti ini



> vi /etc/bluetooth/rfcomm.conf rfcomm0 { bind yes; device 00:12:D1:D4:80:55; <<<< MAC Address HP Nokia Saya  
>  channel 2; <<<< Channel 2 yang di gunakan  
>  comment “Bluetooth device Nokia e61”; }

  * Restart _service bluetooth_ , **sudo /etc/init.d/bluetooth restart** , lalu cek dengan perintah _rfcomm_



> hasilnya akan tampil seperti ini **rfcomm0: 00:12:D1:D4:80:55 channel 2 closed**

  * Edit file _wvdial.conf_ , **vi /etc/wvdial.conf**



> karena saya menggunakan mentari maka isinya seperti ini : [Dialer Defaults] Modem = /dev/rfcomm0 Init1 = AT+CGDCONT=1,”IP”,”indosatgprs” Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 Modem Type = Analog Modem FlowControl = crtscts Phone = *99***1# ISDN = 0 Username = indosat Password = indosat Dial Command = ATDT Baud = 460800 

  * Jika semua berjalan dengan lancar seharusnya kita sudah bisa ber Internet dengan menggunakan _bluetooth_ sebagai _device_.
  * Berikut tampilan koneksi saya, setelah menjalankan perintah _wvdial_



> root@firstly:/home/fadly# wvdial –> WvDial: Internet dialer version 1.60 –> Cannot get information for serial port. –> Initializing modem. –> Sending: AT+CGDCONT=1,”IP”,”indosatgprs” AT+CGDCONT=1,”IP”,”indosatgprs” OK –> Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 OK –> Modem initialized. –> Sending: ATDT*99***1# –> Waiting for carrier. ATDT*99***1# CONNECT ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~ –> Carrier detected. Waiting for prompt. ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~ –> PPP negotiation detected. –> Starting pppd at Tue May 20 19:13:03 2008 –> Pid of pppd: 5435 –> Using interface ppp0 –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> local IP address 10.35.128.117 –> pppd: ��[06][08]��[06][08] –> remote IP address 10.6.6.6 –> pppd: ��[06][08]��[06][08] –> primary DNS address 124.195.15.100 –> pppd: ��[06][08]��[06][08] –> secondary DNS address 124.195.15.98 –> pppd: ��[06][08]��[06][08] Caught signal 2: Attempting to exit gracefully… –> Terminating on signal 15 –> pppd: ��[06][08]��[06][08] –> Connect time 0.4 minutes. –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> pppd: ��[06][08]��[06][08] –> Disconnecting at Tue May 20 19:13:26 2008 


  * Ini hasil _capture IP_ yang terkoneksi ke indosatgprs dengan kodeksi **ppp0**



> root@firstly:/home/fadly# ip r 10.6.6.6 dev ppp0 proto kernel scope link src 10.35.128.117 192.168.1.0/24 dev eth1 proto kernel scope link src 192.168.1.196 169.254.0.0/16 dev eth1 scope link metric 1000 default via 192.168.1.254 dev eth1

  * sekarang kita akan mensetting menggunakan kppp, sebelum melakukan instalasi yakinkan bahwa **kppp** sudah terinstall dikomputer anda, jika belum ada anda bisa melakukan instalasi dengan cara Klik **Applications >> Add/Remove** kemuadia **search kppp** dan tinggal di centangseperti gambar di bawah ini :


[![Instalasi KPPP](https://firstly.wordpress.com/wp-content/uploads/2008/05/install-kppp.jpg?w=150&h=111)](http://firstly.wordpress.com/wp-content/uploads/2008/05/install-kppp.jpg)

setelah selesai di install maka akan tampil di menu _Applications >>> Internet >>> kppp _maka akan tampil menu _kppp_

[![configurasi-kppp](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-1.jpg?w=150&h=61)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-1.jpg)

kemudian klik _configure_ maka akan muncul dialog dibawah ini

[![configuratisi-kppp-2](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-2.jpg?w=109&h=150)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-2.jpg)

klik _new >> add_ dan masukkan no _Dial-Up Indosat_ (_Phone_) yaitu *99***1# kemudian klik oke, seperti gambar dibawah ini, untuk _connection name_ saya beri nama indosat-bluetooth.

[![configurasi-kppp-4](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-4.jpg?w=123&h=150)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-4.jpg)

kemudian klik oke dan akan muncul seperti gambar dibawah ini.

![configurasi-kppp-6](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-6.jpg?w=106&h=150)

kemudian klik _modem_ dan klik _new_ seperti gambar dibawah ini

[![configurasi-kppp-7](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-7.jpg?w=122&h=150)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-7.jpg)

untuk _modem name_ saya tulis **Indosat-Bluetooth** dan moden device saya pilih _/dev/rfcomm0_ kemudian klik lagi _modem_ pada bagian atas dan pilih menu **Modem Commands** maka akan tampil dialog seperti dibawah ini

[![configurasi-kppp-5](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-5.jpg?w=117&h=150)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-5.jpg)

nah pada gambar diatas ada sedikit _configurasi_ yaitu pada init1 dan init2 untuk init 1 saya tambahkan

initialization string 1 **AT+CGDCONT=1, ”IP”,”indosatgprs”** ****

initialization string 1 **ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0**

kemudian klik oke dan oke dan oke lagi. sampai muncul gambar dibawah ini

[![configurasi-kppp-5-konek](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-5-konek.jpg?w=150&h=67)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-5-konek.jpg)

kemudian masukkan **Login ID = indosat dan Password = indosat** klik _connect_

sampai disini muda-mudahan koneksi anda bisa berjalan seperti tampilan pada komputer saya.

[![configurasi-kppp-6-konek](https://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-6-konek.jpg?w=150&h=54)](http://firstly.wordpress.com/wp-content/uploads/2008/05/configurasi-kppp-6-konek.jpg)

selamat mencoba semoga berhasil ….
