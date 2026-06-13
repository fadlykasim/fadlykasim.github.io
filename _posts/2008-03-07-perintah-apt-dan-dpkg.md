---
layout: post
title: "Perintah apt dan&nbsp;dpkg"
date: 2008-03-07T16:50:35+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/03/07/perintah-apt-dan-dpkg/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/03/07/perintah-apt-dan-dpkg/), ditulis pada 2008-03-07.

Debian merupakan salah satu distro tertua selain Slackware dan Redhat, karena terkenal dengan kestabilan, update package yang rutin dan komitmen selalu pada jalan yang benar [maksudnya selalu freedom and free “gratis”] maka banyak orang yang mengambil debian sebagai induk dari distro turunan, contohnya sekarang yang lagi gencar2nya ubuntu, knoppix, kanotik merupakan turunan dari debian

debian memanjakan penggunanya dalam penginstalan software dengan paket manajernya, dengan ini kita bisa menginstal paket apapun tanpa memikirkan depedensi apapun, apalagi kalo konek ke internet, apt-get merupakan pilihan yang tepat dalam menginstall applikasi, wah memang benar-benar surganya open source, nih dia perintah2 di apt dan dpkg untuk pengingat yang kudapat dari [google](http://google.com)

**Install aplikasi**

  * # apt-get install nama-aplikasi
  * Update daftar paket yang terdapat di sources.list  
# apt-get update
  * Update aplikasi  
# apt-get upgrade
  * Merubah daftar mirror apt  
# apt-setup
  * Mencari paket aplikasi  
# apt-cache search package
  * Uninstall aplikasi  
# apt-get remove software


  * menampilkan list paket yang diinstall  
# dpkg -l
  * status paket yang di install  
# dpkg -l pkg
  * menampilkan susunan paket  
# dpkg -S pattern
  * menampilkan list paket  
# dpkg -L pkg
  * status paket  
# dpkg -s pkg
  * menampilkan secara detail package  
# dpkg -p pkg
  * mencari list yang relevan package  
# apt-cache search string
  * install paket .deb  
# dpkg -i file.deb
  * purge package (and config?)  
# dpkg -P pkg
  * re-run konfigurasi package  
# dpkg-reconfigure pkg
  * download source package  
# apt-get source pkg
  * config build-deps for source and install as needed  
# apt-get build-dep
  * install package from specific release  
# apt-get -t release install pkg
  * menghapus eksekusi daemon saat bootup  
# update-rc.d -f name remove
  * upgrade the distribution  
# apt-get dist-upgrade
