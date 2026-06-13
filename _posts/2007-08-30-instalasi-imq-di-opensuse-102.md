---
layout: post
title: "Instalasi imq di OpenSuSe&nbsp;10.2"
date: 2007-08-30T04:16:45+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/08/30/instalasi-imq-di-opensuse-102/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/08/30/instalasi-imq-di-opensuse-102/), ditulis pada 2007-08-30.

Alhamdullih akhirnya saya punya waktu untuk ngoprek juga. Hri ini aku disuruh install OpenVPN, Bandwidth Manager (menggunakan htb), Proxy Server Squid, Sedikit search di omgoogle key imq OpenSuSe, akhirnya ketemu site ftp://ftp.mantech.ro/opensuse.org/distribution/10.2/kernel-IMQ ternyata imq di OpenSuSe 10.2 sudah tidak perlu repot-2 mengcompile kernel dan patch imq. tinggal jalankan rpm -i <namafile>[](http:// "Instalasi imq di OpenSuSe 10.2")

sebelum melakukan download terlebih dahulu saya mengecek versi kernel yang saya gunakan.

openvpn:~ # uname -a

Linux openvpn 2.6.18.2-34-default #1 SMP Mon Nov 27 11:46:27 UTC 2006 i686 i686 i386 GNU/Linux  


ternyata kernel saya masih menggunakan versi 2.6.18.2, kebetulan di Kernel IMQ ada versi 2.6.20.x langsung aja saya download filenya.

openvpn# wget ftp://ftp.mantech.ro/opensuse.org/distribution/10.2/kernel-IMQ/kernel-bigsmp-2.6.20.4-1.i586.rpm

karena IMQ membutuhkan petch iptables maka saya downlod iptables untuk IMQ di

openvpn#wget ftp://ftp.mantech.ro/opensuse.org/distribution/10.2/kernel-IMQ/iptables-1.3.6-21.i586.rpm

openvpn#ls -l  
total 19420  
-rw-r–r– 1 root root 259101 2007-08-30 11:02 iptables-1.3.6-21.i586.rpm  
-rw-r–r– 1 root root 19592576 2007-08-30 11:04 kernel-bigsmp-2.6.20.4-1.i586.rpm

setelah selesai melakukan download mari kita melakukan instalasi kedua file tersebut.

openvpn#rpm -ivh kernel-bigsmp-2.6.20.4-1.i586.rpm  
Preparing… ########################################### [100%]  
1:kernel-bigsmp ########################################### [100%]  
Setting up /lib/modules/2.6.20.4-1-bigsmp  
Root device: /dev/hda2 (mounted on / as ext3)  
Module list: processor thermal sis5513 fan jbd ext3 edd (xennet xenblk)

Kernel image: /boot/vmlinuz-2.6.20.4-1-bigsmp  
Initrd image: /boot/initrd-2.6.20.4-1-bigsmp  
Shared libs: lib/ld-2.5.so lib/libacl.so.1.1.0 lib/libattr.so.1.1.0 lib/libblkid.so.1.0 lib/libc-2.5.so lib/libcom_err.so.2.1 lib/libdl-2.5.so lib/libext2fs.so.2.4 lib/libhistory.so.5.1 lib/libncurses.so.5.5 lib/libpthread-2.5.so lib/libreadline.so.5.1 lib/librt-2.5.so lib/libutil-2.5.so lib/libuuid.so.1.2 lib/libvolume_id.so.0.73.0 lib/libnss_files-2.5.so lib/libnss_files.so.2 lib/libgcc_s.so.1  
Driver modules: ide-core ide-disk processor thermal sis5513 fan edd  
Filesystem modules: jbd mbcache ext3  
Including: initramfs fsck.ext3  
Bootsplash: SuSE (1280×1024)  
13424 blocks

openvpn#rpm -ivh iptables-1.3.6-21.i586.rpm  
Preparing… ########################################### [100%]

untuk melihat apakah imq sudah terinstal maka kita harus mereboot komputer

kalau tidak ada kesalahan maka komputer anda sudah bisa menggunakan imq

sekarang kita pastikan apakah imq sudah jalan.

openvpn#ip a

1: lo: <LOOPBACK,UP,10000> mtu 16436 qdisc noqueue  
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00  
inet 127.0.0.1/8 scope host lo  
inet6 ::1/128 scope host  
valid_lft forever preferred_lft forever  
2: eth0: <BROADCAST,MULTICAST,UP,10000> mtu 1500 qdisc pfifo_fast qlen 1000  
link/ether 00:c0:26:2d:c9:06 brd ff:ff:ff:ff:ff:ff  
inet xxx.xxx.xxx.xxx/xx brd xxx.xxx.xxx.xxx scope global eth0  
inet6 fe80::2c0:26ff:fe2d:c906/64 scope link  
valid_lft forever preferred_lft forever  
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 1000  
link/ether 00:08:a1:33:66:6d brd ff:ff:ff:ff:ff:ff

ternyata img belum jalan, jangan panik ini karena pada saat linix melakukan boot imqnya tidak di panggil dari kerner. untuk menjalankan imq dari kernel silahkan ketik

openvpn#modprobe imq

coba ulangi melakukan #ip a

1: lo: <LOOPBACK,UP,10000> mtu 16436 qdisc noqueue  
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00  
inet 127.0.0.1/8 scope host lo  
inet6 ::1/128 scope host  
valid_lft forever preferred_lft forever  
2: eth0: <BROADCAST,MULTICAST,UP,10000> mtu 1500 qdisc pfifo_fast qlen 1000  
link/ether 00:c0:26:2d:c9:06 brd ff:ff:ff:ff:ff:ff  
inet xxx.xxx.xxx.xxx/xx brd xxx.xxx.xxx.xxx scope global eth0  
inet6 fe80::2c0:26ff:fe2d:c906/64 scope link  
valid_lft forever preferred_lft forever

3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 1000  
link/ether 00:08:a1:33:66:6d brd ff:ff:ff:ff:ff:ff  
4: imq0: <NOARP> mtu 1500 qdisc noop qlen 30  
link/void  
5: imq1: <NOARP> mtu 1500 qdisc noop qlen 30  
link/void  
wow ternyata imq ku sudah bisa di gunakan. selamat mencoba. continue
