---
layout: post
title: "Install ncomputing x-300 edubuntu,&nbsp;ubuntu"
date: 2008-06-06T00:48:24+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/06/06/install-ncomputing-x-300-edubuntu/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/06/06/install-ncomputing-x-300-edubuntu/), ditulis pada 2008-06-06.

tanpa basa basi perintahnya seperti ini

> $apt-get install libqt3-mt

kemudian download [x300-linux.zip](http://www.indoasiateknologi.com/drivers/ "Driver Ncomputing for Linux")

dan jalankan

> ./lnx3inst

kalau di lihat dari hasil log instalasi akn muncul seperti ini

> root@edubuntu:/home/edubuntu/x300/x300-linux.zip_FILES# ./lnx3inst  
>  23350+0 records in  
>  23350+0 records out  
>  23910400 bytes (24 MB) copied, 0.323054 seconds, 74.0 MB/s  
>  dpkg – warning: downgrading libqt3-mt from 3.3.8really3.3.7-0ubuntu5.2 to 3.3.8really3.3.7-0ubuntu5.  
>  (Reading database … 88251 files and directories currently installed.)  
>  Preparing to replace libqt3-mt 3:3.3.8really3.3.7-0ubuntu5.2 (using libqt3-mt_3%3a3.3.8really3.3.7-0ubuntu5_i386.deb) …  
>  Unpacking replacement libqt3-mt …  
>  Setting up libqt3-mt (3.3.8really3.3.7-0ubuntu5) …
> 
> X Error: BadDevice, invalid or uninitialized input device 167  
>  Major opcode: 144  
>  Minor opcode: 3  
>  Resource id: 0x0  
>  Failed to open device  
>  X Error: BadDevice, invalid or uninitialized input device 167  
>  Major opcode: 144  
>  Minor opcode: 3  
>  Resource id: 0x0  
>  Failed to open device  
>  Session management error: Authentication Rejected, reason : None of the authentication protocols specified are supported and host-based authentication failed  
>  sh: /usr/bin/ncomputing/ncltconfig: not found
> 
> gzip: stdin: decompression OK, trailing garbage ignored  
>  tar: Child returned status 2  
>  tar: Error exit delayed from previous errors  
>  Xvnc4nc: no process killed  
>  x300: no process killed  
>  SIOCSIFADDR: No such device  
>  eth1: ERROR while getting interface flags: No such device

Setelah selesai restart komputer anda, klik

> **Applications - > Xtenda 300 -> Xtenda 300 – Administration Console**

akan tampil seperti dibawah ini

[![xtenda 300 Administrator Consule](https://firstly.wordpress.com/wp-content/uploads/2008/06/xtenda-300-administrator.jpg?w=150&h=115)](http://firstly.wordpress.com/wp-content/uploads/2008/06/xtenda-300-administrator.jpg)
