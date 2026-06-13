---
layout: post
title: "Instalasi Wireless Acer Aspire 2920z di Ubuntu&nbsp;8.04"
date: 2008-07-18T13:33:26+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/07/18/instalasi-wireless-acer-aspire-2920z-di-ubuntu-804/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/07/18/instalasi-wireless-acer-aspire-2920z-di-ubuntu-804/), ditulis pada 2008-07-18.

Sangat menyesal karena secara default ubuntu versi 8.04 tidak support wireless Broadcom BCM4310 nah disini ada sedikit utak atik untuk tipe wireless jenis ini.

pertama cek driver anda. perintahnya seperti dibawah ini

> $lspci |grep Broad
> 
> 02:00.0 Ethernet controller: Broadcom Corporation NetLink BCM5787M Gigabit Ethernet PCI Express (rev 02)  
>  04:00.0 Network controller: Broadcom Corporation BCM4310 USB Controller (rev 01)
> 
> Tipe wireless yaitu BCM4310 (rev 01)

lebih jelasnya lagi saya mengecek dengan perintah

> 
>     $lshw -C network
>     description: Wireless interface
>            product: BCM4310 USB Controller
>            vendor: Broadcom Corporation
>            physical id: 0
>            bus info: pci@0000:04:00.0
>            logical name: wlan0
>            version: 01
>            serial: 00:1f:3a:bb:68:c7
>            width: 64 bits
>            clock: 33MHz
>            capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless

selanjutnya kita akan melakukan instalasi wireless dengan menggunakan pelantara ndiswrapper

> 
>     $sudo apt-get install ndiswrapper-utils-1.9
>     $sudo apt-get install cabextract

cabextract adalah file kabinet dari window$

kemudian download driver wireless

> $wget <http://myspamb8.googlepages.com/R174291-pruned.zip> $unzip R174291-pruned.zip

setelah di mekarkan maka ada beberapa file yaitu

> 
>     bcm43xx64.cat  bcmwl564.sys  bcmwl5.sys
>     bcm43xx.cat    bcmwl5.inf    R174291-pruned.zip

setelah itu maka kita akam melakukan instalasi driver menggunakan ndiswrapper

> 
>     $sudo ndiswrapper -i bcmwl5.inf
>     $ndiswrapper -l
>     $sudo depmod -a
>     $sudo modprobe ndiswrapper
>     $sudo cp /etc/network/interfaces /etc/network/interfaces.orig
>     $echo -e 'auto lo\niface lo inet loopback\n' | sudo tee /etc/network/interfaces
>     $sudo ndiswrapper -m
>     $echo 'ndiswrapper' | sudo tee -a /etc/modules
>     $echo 'ENABLED=0' | sudo tee -a /etc/default/wpasupplicant

setelah selesai di instal restart komputer anda dan nikmati wirelessnya.
    
    
    selamat mencoba.
    
    NB

setelah selesai instalasi saya maka lampu wirelessnya menyala. dan saya mengecek instalasi driver tadi dengan perintah

> 
>     $ndiswrapper -l
>     $bcmwl5 : driver installed
>     	device (14E4:4315) present
