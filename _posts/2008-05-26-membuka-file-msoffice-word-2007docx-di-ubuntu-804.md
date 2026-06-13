---
layout: post
title: "Membuka File MsOffice Word 2007.docx di Ubuntu&nbsp;8.04"
date: 2008-05-26T16:27:20+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/05/26/membuka-file-msoffice-word-2007docx-di-ubuntu-804/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/05/26/membuka-file-msoffice-word-2007docx-di-ubuntu-804/), ditulis pada 2008-05-26.

Sudah menjadi Standart bagi **Micro$oft Office 2007** yang mana file yang disimpan dirubah menjadi file yang ber xtensi **docx** sehingga perubahan ini menjadi OpenOffice tidak bisa membukanya pada instalasi default di ubuntu 8.04 atau yang sudah mengupgrade dari 7.10 ke 8.04 untuk yang belum upgrade ke 7.10 silahkan kunjungi [disini](http://firstly.wordpress.com/2008/03/20/membuka-file-msoffice-word-2007docx-di-ubuntu/ "membuka-file-msoffice-word-2007docx-di-ubuntu")

untuk yang 8.04 kita bisa membukanya dengan menupdate fitur openoffice, cara sederhana yaitu :

untuk i386 ambil **Applications > Accessories > Terminal** ketik

> `wget [ftp://ftp-mirror.internap.com/pub/www.getdeb.net/od/odf-converter_1.0.0-2~getdeb1_i386.deb](ftp://ftp-mirror.internap.com/pub/www.getdeb.net/od/odf-converter_1.0.0-2%7Egetdeb1_i386.deb)`

untuk amd64

> `wget [http://cesium.di.uminho.pt/pub/getdeb/od/odf-converter_1.0.0-2~getdeb1_amd64.deb](http://cesium.di.uminho.pt/pub/getdeb/od/odf-converter_1.0.0-2%7Egetdeb1_amd64.deb)`

`sekarang kita akan melakukan instalasi package`

`i386 users`

> **`sudo dpkg -i odf-converter_1.0.0-2~getdeb1_i386.deb`**

`amd64 users`

> **`sudo dpkg -i odf-converter_1.0.0-2~getdeb1_amd64.deb`**

`Sampai disini ubuntu anda sudah bisa membuka menikmati file docx  
`
