---
layout: post
title: "awn Desktop ubuntu&nbsp;8.04"
date: 2008-05-26T08:48:12+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/05/26/awn-desktop-ubuntu-804/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/05/26/awn-desktop-ubuntu-804/), ditulis pada 2008-05-26.

[![screenshot-desktop-fadly](https://firstly.wordpress.com/wp-content/uploads/2008/05/screenshot-desktop-fadly.jpg?w=150&h=94)](http://firstly.wordpress.com/wp-content/uploads/2008/05/screenshot-desktop-fadly.jpg) Akhirnya Ubuntuku teras Mac Os X, dengan menggunakan [AWN (avant window navigator)](http://wiki.awn-project.org/Awn-extras "AWN") untuk menginstall awn di ubuntu 8.04 berikut repositorunya

Tambahkan dua baris berikut ini di

/etc/apt/sources.lis

> **deb<http://ppa.launchpad.net/awn-testing/ubuntu> hardy main  
>  deb-src <http://ppa.launchpad.net/awn-testing/ubuntu> hardy main**

atau

> **echo “deb <http://ppa.launchpad.net/awn-testing/ubuntu> hardy main” | sudo tee -a /etc/apt/sources.list**
> 
> **echo “deb-src <http://ppa.launchpad.net/awn-testing/ubuntu> hardy main” | sudo tee -a /etc/apt/sources.list**

kemuadian lakukan perintah update dibawah ini

> **sudo apt-get update** **sudo apt-get install compizconfig-settings-manager** **sudo apt-get install emerald** **sudo apt-get install awn-manager-trunk awn-extras-applets-trunk**

untuk menjalankan AWN klik

> **(Applications - > Accessories -> Avant Window Navigator )**

Untuk customize AWN,

> **AWN Manager (System - > Preferences -> Awn Manager)**
> 
> [![awn-manager2](https://firstly.wordpress.com/wp-content/uploads/2008/05/awn-manager2.png?w=150&h=115)](http://firstly.wordpress.com/wp-content/uploads/2008/05/awn-manager2.png)[![awn-manager1](https://firstly.wordpress.com/wp-content/uploads/2008/05/awn-manager1.png?w=150&h=120)](http://firstly.wordpress.com/wp-content/uploads/2008/05/awn-manager1.png)

Install Destop screenlets

> **sudo apt-get install screenlets**

Hasil intalasi dari Screenlets ada di **System - > Preferences -> Screenlets**

> [![screenlets](https://firstly.wordpress.com/wp-content/uploads/2008/05/screenlets.png?w=150&h=84)](http://firstly.wordpress.com/wp-content/uploads/2008/05/screenlets.png)

Sampai disini mudah-mudahan Linux anda akan semakin cantik

dibawah ini adalah tampilan desktop saya

> [![desktop2-fadly](https://firstly.wordpress.com/wp-content/uploads/2008/05/desktop2-fadly.jpg?w=150&h=94)](http://firstly.wordpress.com/wp-content/uploads/2008/05/desktop2-fadly.jpg)
