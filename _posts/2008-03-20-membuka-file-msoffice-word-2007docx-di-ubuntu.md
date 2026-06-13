---
layout: post
title: "Membuka File MsOffice Word 2007.docx di&nbsp;Ubuntu"
date: 2008-03-20T20:04:06+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/03/20/membuka-file-msoffice-word-2007docx-di-ubuntu/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/03/20/membuka-file-msoffice-word-2007docx-di-ubuntu/), ditulis pada 2008-03-20.

Perubahan yang dilakuakan oleh Ms Office 2007 menjadi file word yang di simpan ber xtensi docx perubahan ini menjadikan openoffice tidak bisa membukanya pada instalasi default *

Jangan panik masih ada jalan menuju Ubuntu. kita bisa membukanya dengan mengupdate fitur openoffice dengan cara sederhana yaitu download file [berikut](http://blog.mypapit.net/imej/odf_filter.tar.bz2 "odf_filter.tar.bz2")

dan simpan di komputer anda.

Langka – Langkah update :

  1. klik odf_filter.tar.bz2 dan kemudian di extrak ke desktop anda

  2. setelah di extrak maka akan muncul di desktop anda dengan nama file “**files** ”

  3. klik Applications, then Accessories, then Terminal

  4. ikuti command berikut ini

  5. cd Desktop

  6. cd files

  7. sudo cp OdfConverter /usr/lib/openoffice/program/

  8. sudo cp MOOXFilter_cpp.xcu /usr/lib/openoffice/share/registry/modules/org/openoffice/  
TypeDetection/Filter/
  9. sudo cp MOOXTypeDetection.xcu /usr/lib/openoffice/share/registry/modules/org/openoffice/TypeDetection/T

  10. selesai

  11. sekarang jalankan openoffice word anda

  12. kemudia klik open dana arahkan ke file yang berxtensi.dicx tersebut



selamat mencoba

*(catatan: menggunakan ubuntu 7.10 bawaan openoffice 2.3.0).
