---
layout: post
title: "Instalasi &amp; Configurasi&nbsp;Nagios"
date: 2007-06-29T17:13:23+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/06/29/instalasi-configurasi-nagios/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/06/29/instalasi-configurasi-nagios/), ditulis pada 2007-06-29.

Pernahka terbesik di pikiran anda gimana caranya menjadi sorang sysadmin pada suatu perusahaan IT seperti ISP, yang hanya memonitoring semua Networ dengan menggunakan GUI. Bahkan dimana saja kita berada bisa memonitoring Network kita dengan cara menggunakan HP, SMS, etc.[](http:// "Instalasi & Configurasi Nagiso")

Banyak pertannya yang sering ditanyakan kepada saya apa nama program yang digunakan, gimana cara melakukan instalasi, gimana cara melakukan configurasi, dan masih banyak lagi pertannya yang muncul. nah disinilah saya akan mencoba memandu anda untuk melakukan Instalasi dan configurasi.

Adapun nama dari program ini yaitu [nagios](http://nagios.org "nagios"), anda juga bisa mendapatkan manual instalasi di website [nagios](http://www.nagios.org/docs "Documentasi") atau di [wiki](http://www.nagioscommunity.org/wiki/index.php/Main_Page "Nagios Community")  
sekarang kita akan mencoba melakukan instalasi, komputer yang saya gunakan P 4 Multimedia, dan menggunakan Distro OpensSUSE 10.2, dan Ubuntu 7.04.

Untuk instalasi di OpenSUSE 10.2

1\. Kita harus mendownload filenya di [nagios](http://www.nagios.org/download/ "Download Ngios") silahkan anda mengunjungi, instalasi [Apache](http://www.apache.org/ "Apache")

2\. Lakukan Perintah.  
**root@iNterNUX:~#tar xzf nagios-_version_.tar.gz**

**root@iNterNUX:~#adduser nagios**

**root@iNterNUX:~#****mkdir /usr/local/nagios** ****

**root@iNterNUX:~#****chown nagios.nagios /usr/local/nagios**

Kita akan melakukan pembuata group untuk nagios

**root@iNterNUX:~#** /usr/sbin/groupadd nagcmd

**root@iNterNUX:~#** /usr/sbin/usermod -G nagcmd apache

**root@iNterNUX:~#** /usr/sbin/usermod -G nagcmd nagios

selanjutnya kita akan melakukan compile

**#./configure –prefix=_prefix_ –with-cgiurl=_cgiurl_ –with-htmurl=_htmurl_ –with-nagios-user=_someuser_ –with-nagios-group=_somegroup_ –with-command-group=_cmdgroup_**

**#make all**

Note: Diusahakan tidak ada yang error

**#make install**

**#make install-init**

Nah sampai disini selesai deh, sekarang kita bisa mengedit filenya.

**#cd /usr/local/nagios**

sebelum kita melakukan instalasi kita akan melakukan konfigurasi dari apache, kita buat satu file didalan direktori /etc/apache2/vhost/nagios.conf isi dari file nagios.conf yaitu

********
    
    
    ****ScriptAlias /nagios/cgi-bin /usr/local/nagios/sbin <Directory "/usr/local/nagios/sbin">
        Options ExecCGI
        AllowOverride None
        Order allow,deny
        Allow from all
        AuthName "Nagios Access"
        AuthType Basic
        AuthUserFile /usr/local/nagios/etc/htpasswd.users
        Require valid-user
    </Directory>
    
    Alias /nagios /usr/local/nagios/share
    
    <Directory "/usr/local/nagios/share">
        Options None
        AllowOverride None
        Order allow,deny
        Allow from all
        AuthName "Nagios Access"
        AuthType Basic
        AuthUserFile /usr/local/nagios/etc/htpasswd.users
        Require valid-user
    </Directory>****

Selanjutnya restart apache perintahnya#rcapache2 restart sekarang kita menjalankan nagiosnya /etc/inet.d/nagios start

kalau sudah berhasil silahkan anda buka browsing anda terserserah mau menggunakan opera atau firefox. caranya

<http://localhost/nagios>

[bersambung](http://firstly.wordpress.com)
