---
layout: post
title: "Koneksi TelkomselFlash &amp; Nokia&nbsp;e61"
date: 2008-06-25T01:19:36+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/06/25/koneksi-telkomselflash-nokia-e61/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/06/25/koneksi-telkomselflash-nokia-e61/), ditulis pada 2008-06-25.

Hari selasa 24 juni kemarin saya meregistrasi [Karto Hallo Telkomsel](http://www.telkomsel.com/web/hot_offering "Telkomsel Unlimited"). dan akhirnya setelah konfirmasih ke 111 katanya kartu Halo saya sudah di aktif untuk fitur tambahan, yaitu paket Internet Unlimited 24 jam dengan kecepatan 256kbps. Akhirnya berniat mencoba koneksi Internet ini dengan menggunakan [Bluetooth dan Nokia e61](http://firstly.wordpress.com/2008/05/20/koneksi-bluetooth-modem-di-nokia-e61-menggunakan-hardy-heron/ "Konfigurasi wvdial menggunakan Bluetooth").

[![Hallo TElkomsel](https://firstly.wordpress.com/wp-content/uploads/2008/06/halo-telkomsel.png?w=150&h=113)](http://firstly.wordpress.com/wp-content/uploads/2008/06/halo-telkomsel.png)

1\. Konfigurasi Modem

karena saya menggunakan nokia e61 silahkan menuju ke tulisan saya sebelumnya

> [Koneksi Bluetooth Modem di Nokia e61 menggunakan Hardy Heron](https://firstly.wordpress.com/2008/05/20/koneksi-bluetooth-modem-di-nokia-e61-menggunakan-hardy-heron/)

untuk konfigurasi wvdial.conf telkomselflash saya merubah pada bagian Init3 berikut isi dari wvdial.conf

> [Dialer Defaults]  
>  Init1 = ATZ  
>  Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
>  Init3 = AT+CGDCONT=1,\”IP\”,\”internet\”  
>  Phone = *99***1#  
>  ISDN = 0  
>  Username = ”  
>  Password = ”  
>  Modem = /dev/rfcomm0  
>  Baud = 460800

Keterangan:

  * Ini adalah tambahan line baru dimana IP kita isi valuenya dengan kata ‘internet’ sebagai access pointnya



> Init3 = AT+CGDCONT=1,\”IP\”,\”internet\”

  * Username & password isi dengan tanda petik yg didefine sbg string kosong


  * Isi Phone dengan nilai *99***1# atau *99#


  * Lakukan dialup dengan mengetikkan perintah di bawah:



> $sudo wvdial

> –> WvDial: Internet dialer version 1.60  
>  –> Cannot get information for serial port.  
>  –> Initializing modem.  
>  –> Sending: ATZ  
>  ATZ  
>  OK  
>  –> Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
>  ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
>  OK  
>  –> Sending: AT+CGDCONT=1,”IP”,”internet”  
>  AT+CGDCONT=1,”IP”,”internet”  
>  OK  
>  –> Modem initialized.  
>  –> Sending: ATDT*99***1#  
>  –> Waiting for carrier.  
>  ATDT*99***1#  
>  CONNECT  
>  ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~  
>  –> Carrier detected. Waiting for prompt.  
>  ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~  
>  –> PPP negotiation detected.  
>  –> Starting pppd at Wed Jun 25 07:40:04 2008  
>  –> Pid of pppd: 12658  
>  –> Using interface ppp0  
>  –> pppd: �[06][08]�[06][08]  
>  –> pppd: �[06][08]�[06][08]  
>  –> pppd: �[06][08]��[06][08]  
>  –> pppd: �[06][08]��[06][08]  
>  –> local IP address 221.132.208.135  
>  –> pppd: �[06][08]��[06][08]  
>  –> remote IP address 10.6.6.6  
>  –> pppd: �[06][08]��[06][08]  
>  –> primary DNS address 202.3.208.10  
>  –> pppd: �[06][08]��[06][08]  
>  –> secondary DNS address 202.3.210.10  
>  –> pppd: �[06][08]��[06][08]

Setelah konek saya langsung menuju ke situ tes bandwidth

dan hasilnya seperti dibawah ini

[![Koneksi internet menggunakan 3G](https://firstly.wordpress.com/wp-content/uploads/2008/06/telkomselflash-internet.png?w=150&h=86)](http://firstly.wordpress.com/wp-content/uploads/2008/06/telkomselflash-internet.png)

Gambar di atas menggunakan koneksi 3G atau UMTS,

Pada saat saya menulis tulisan ini saya berada di [Parepare](http://www.pareparekota.go.id/ "Parepare KOTA"), karena di Parepare tidak ada fasilitas 3G maka saya menggunakan koneksi GSM (GPRS) dan hasilnya seperti di bawah ini

[![parepare GPRS](https://firstly.wordpress.com/wp-content/uploads/2008/06/telkomselflash-internet-pare.png?w=150&h=80)](http://firstly.wordpress.com/wp-content/uploads/2008/06/telkomselflash-internet-pare.png)

Dari hasil koneksi diatas silahkan anda melilih sendiri koneksi internet yang layak buat anda.

—

Salam,

Fadly Kasim
