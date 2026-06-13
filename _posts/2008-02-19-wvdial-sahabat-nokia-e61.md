---
layout: post
title: "Wvdial sahabat Nokia&nbsp;E61"
date: 2008-02-19T06:01:36+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/02/19/wvdial-sahabat-nokia-e61/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/02/19/wvdial-sahabat-nokia-e61/), ditulis pada 2008-02-19.

[![acer & nokia e61](https://firstly.wordpress.com/wp-content/uploads/2008/04/nokia.jpg?w=300&h=230)](http://firstly.wordpress.com/wp-content/uploads/2008/04/nokia.jpg)Hari ini saya harus berpisah dengan speedhi dan Provider lain sampai hari jumat nanti tgl 22/2/08. Saya di tugaskan ke Bandung (BantaengGunung) untuk menginstall [Ubuntu-Desktop 7.10](http://www.ubuntu-id.org/ "komunitas Ubuntu Indonesia") di Branda SSCI sebanyak 40 Unit untuk persiapan pelatihan bagi Masyarakat Bantaeng. Awalnya di Branda BCEC Menggunakan koneksi VSAT Via Indosat, dan tidak ada keraguan untuk masalah koneksi ke Internet, pada saat mau berangkat ada informasih dari Bandung bahwa di Branda BCEC tidak ada Koneksi Internet (Putus). Akhir saya memutuskan untuk menggunakan teman setiaku [Nokia E61](http://nokia.co.id) untuk bisa ber GPRS ria. Nah ternyata Ubuntuku paling bersahabat sama [nokia e61](http://nokia.co.id) untuk koneksi menggunakan [wvdial](http://www.google.com/url?sa=t&ct=res&cd=6&url=http%3A%2F%2Fwiki.linuxquestions.org%2Fwiki%2FWvdial&ei=bXC6R7-9CYbqswKqvayZCw&usg=AFQjCNFhrgaTMMTSpwMi8w7esDms8HeONw&sig2=yV3Zs2t220M_ZxMuXf6rzA "Wvdial"). singkat kata saya harus mengkonfigurasi wvdial.conf dan isinya seperti ini.

wvdial.conf

[Dialer Defaults]  
Init1 = at+cgdcont=1,”ip”,”indosatgprs”  
Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
Modem Type = USB Modem  
Phone = *99***1#  
ISDN = 0  
Username = indosat  
Password = indosat  
Modem = /dev/ttyACM0  
Baud = 460800  
jalankan wvdial

root@Firstly:/home/fadly# wvdial  
WvDial<*1>: WvDial: Internet dialer version 1.56  
WvModem<*1>: Cannot get information for serial port.  
WvDial<*1>: Initializing modem.  
WvDial<*1>: Sending: at+cgdcont=1,”ip”,”indosatgprs”  
WvDial Modem<*1>: at+cgdcont=1,”ip”,”indosatgprs”  
WvDial Modem<*1>: OK  
WvDial<*1>: Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
WvDial Modem<*1>: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0  
WvDial Modem<*1>: OK  
WvDial<*1>: Modem initialized.  
WvDial<*1>: Sending: ATDT*99***1#  
WvDial<*1>: Waiting for carrier.  
WvDial Modem<*1>: ATDT*99***1#  
WvDial Modem<*1>: CONNECT  
WvDial Modem<*1>: ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~  
WvDial<*1>: Carrier detected. Waiting for prompt.  
WvDial Modem<*1>: ~[7f]}#@!}!} } }2}#}$@#}!}$}%\\}”}&} }*} } g}%~  
WvDial<*1>: PPP negotiation detected.  
WvDial<Notice>: Starting pppd at Tue Feb 19 13:41:54 2008  
WvDial<Notice>: Pid of pppd: 12545  
WvDial<*1>: Using interface ppp0  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: local IP address 10.35.102.139  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: remote IP address 10.6.6.6  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: primary DNS address 124.195.15.100  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]  
WvDial<*1>: secondary DNS address 124.195.15.98  
WvDial<*1>: pppd: [18]�[06][08][10]�[06][08]

Akhirnya bisa konek juga. terimakasih internet.

Tulisan ini saya buat dengan menggunakan koneksi GPRS Indosat. wah mudah-mudahan GPRS Bantaeng bisa berfungsi dengan Baik.
