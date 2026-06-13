---
layout: post
title: "Configurasi Wvdial &#8220;TravelMate 2420&#8221;"
date: 2007-07-12T13:14:14+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/07/12/wvdial-di-travelmate-2420/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/07/12/wvdial-di-travelmate-2420/), ditulis pada 2007-07-12.

Hi, here is short tutorial to set up your Linux OpenSuse 10.2 and Ubuntu 7.4 get connect to CDMA modem to get internet access. I use Nokia CDMA 2116 and DKU-5 (not original) cable data. For the internet provider i use Starone.

[](http:// "Wvdial Di TravelMate 2420")

1\. Log on as root (administrator)  
2\. Connect Nokia CDMA 2116 and DKU-5 to usb port  
3\. Open Konsole and type dmesg, on my computer ( i use laptop Acer Travelmate 2420) you will find  
something like this

usb 1-1: ark3116 converter now attached to ttyUSB0

This is mean that your Linux OpenSuse 10.2 recognize your Nokia CDMA 2116 modem and the DKU-5  
cable data

4\. Then type “wvdialconf /etc/wvdial.conf”. Find someting like this :

Found a modem on /dev/ttyUSB0.  
Modem configuration written to /etc/wvdial.conf.  
ttyUSB0: Speed 230400; init “ATQ0 V1 E1 S0=0 &C1 &D2″

5\. Ok, now open the wvdial.conf (i use kwrite) and make some change on this :

Modem = /dev/ttyUSB0 —-> fill based on information on step 3  
Baud = 230400 —-> fill based on information on step 4  
Init1 = ATZ  
Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 —-> fill based on information on step 4  
Init3 = AT+cso=33 —-> if blank, fill with AT+cso=33  
Area Code =  
Phone = #777 —-> if you are in indonesia and use CDMA type #777  
Username = starone —-> ask your phone/internet provider  
Password = indosat —-> ask your phone/internet provider  
Ask Password = 0  
Dial Command = ATDT  
Stupid Mode = 1  
Compuserve = 0  
Force Address =  
Idle Seconds = 300  
DialMessage1 =  
DialMessage2 =  
ISDN = 0  
Auto DNS = 1  
Modem Type = Analog Modem

6\. Save your change and exit

7\. Open the konsole again and type wvdial

8\. The connection work fine if you find information like this :

CONNECT  
~[7f]}#@!}!}!} }3}”}&} } } } }#}%B#}%}’}”}(}”W}0~  
–> Carrier detected. Starting PPP immediately.  
–> Starting pppd at Sun May 20 17:34:43 2007  
–> pid of pppd: 4547  
–> Using interface ppp0  
–> pppd: #777  
–> pppd: #777  
–> pppd: #777  
–> pppd: #777  
–> pppd: #777  
–> local IP address 10.242.30.198  
–> pppd: #777  
–> remote IP address 10.64.64.64  
–> pppd: #777  
–> primary DNS address 202.93.40.174  
–> pppd: #777  
–> secondary DNS address 202.155.0.10  
–> pppd: #777  
–> Script /etc/ppp/ip-up run successful  
–> Default route Ok.  
–> Nameserver (DNS) Ok.  
–> Connected… Press Ctrl-C to disconnect  
–> pppd: #777

I hope this information also work with your Linux. 🙂

NB.

[wvdial: carrier signal lost](http://firstly.wordpress.com/2007/08/05/wvdial-carrier-signal-lost/ "wvdial-carrier-signal-lost")
