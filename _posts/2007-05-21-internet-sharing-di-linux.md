---
layout: post
title: "Internet Sharing di&nbsp;Linux"
date: 2007-05-21T02:33:13+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/05/21/internet-sharing-di-linux/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/05/21/internet-sharing-di-linux/), ditulis pada 2007-05-21.

Duh, banyak sekali yang nanya-nanya cara internet sharing pakai Suse, Mandrake, Fedora, dll,dll. [](http:// "Internet Sharing di Linux")Ini cara sapu jagad yang pasti jalan di semua Linux.Level: wannabees Singkat saja ya, pasang Linux anda jadi gateway

{INTERNET}———–[LINUX]—————-{LAN}  
Lalu di Linux itu, cari file namanya rc.local (biasanya di /etc/rc.d/rc.local atau /etc/init.d/rc.local) lalu tambahkan 6 baris berikut (tidak termasuk comment)

# Ganti device pakai sambungan Internet: ppp0, eth0 atau eth1 DEVICE=ppp0

# Ini jalur INTERNAL ke INTERNET iptables -A FORWARD -o $DEVICE -i ! $DEVICE -j ACCEPT  
# In jalur balik dari INTERNET iptables -A FORWARD -m state –state ESTABLISHED,RELATED -j ACCEPT  
iptables -A FORWARD -f -j ACCEPT  
# Ini rahasianya internet sharing iptables -t nat -A POSTROUTING -o $DEVICE -j MASQUERADE  
# dan ini pembuka gateway-nya. echo “1” > /proc/sys/net/ipv4/ip_forward  
Kalau sudah, reboot si Linux, hidupkan modemnya (kalau pakai). Terus semua komputer di LAN, diset supaya GETEWAY=IP-DALAM nya si Linux. Sementara itu DNS masih tetap DNS dari ISP. Met nyoba.
