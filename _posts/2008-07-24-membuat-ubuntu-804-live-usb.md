---
layout: post
title: "Membuat Ubuntu 8.04 Live&nbsp;USB"
date: 2008-07-24T07:37:41+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/07/24/membuat-ubuntu-804-live-usb/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/07/24/membuat-ubuntu-804-live-usb/), ditulis pada 2008-07-24.

Barusan saya mencoba menginstall Ubuntu 8.04 menjadi live USB di USB 1G merek Flash.

dan akhirnya berhasil dengan sangat mengagumkan.

caranya seperti ini,

> 
>     sudo apt-get install syslinux mtools
>     wget http://www.startx.ro/sugar/isotostick.sh
>     chmod +x isotostick.sh

Siapkan file iso ubuntu 8.04 colok di pc anda lakukan pengecekan untuk melihat status usb caranya

> ##### $mount

berikut contoh dari tampilan mount di komputer saya

> ###### /dev/sdb1 on /media/disk type vfat (rw,nosuid,nodev,uhelper=hal,shortname=mixed,uid=1000,utf8,umask=077,flush)

berarti usb saya aktif di /dev/sdb1, Kemudian lakukan pemindahan file iso ke USB caranya

> 
>     sudo ./isotostick.sh ubuntu-8.04-desktop-i386.iso /dev/sdb1

sampai disini tunggu sampai ada tampilan

> ###### Installing boot loader  
>  USB stick set up as live image!

kalau sudah selesai, anda bisa menikmati usb anda dengan setting bios agar boot awal memilih USB.

selamat mencoba
