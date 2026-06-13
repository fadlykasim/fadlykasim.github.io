---
layout: post
title: "wvdial: carrier signal&nbsp;lost"
date: 2007-08-05T16:19:39+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/08/05/wvdial-carrier-signal-lost/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/08/05/wvdial-carrier-signal-lost/), ditulis pada 2007-08-05.

# wvdial  
–> WvDial: Internet dialer version 1.56  
–> Initializing modem.  
–> Sending: ATZ  
ATZ  
OK[](http:// "carrier signal lost")  
–> Sending: AT+CRM=1  
AT+CRM=1  
OK  
–> Sending: AT+cso=33  
AT+cso=33  
OK  
–> Modem initialized.  
–> Idle Seconds = 300, disabling automatic reconnect.  
–> Sending: ATDT#777  
–> Waiting for carrier.  
ATDT#777  
CONNECT  
~[7f]}#@!}!}!} }3}”}&} } } } }#}%B#}%}’}”}(}”W}0~  
–> Carrier detected. Waiting for prompt.  
–> Connected, but carrier signal lost! Retrying…  
–> Sending: ATDT#777  
–> Waiting for carrier.  
===============================

Edit /etc/wvdial.conf :  
Comment this line:  
#Carrier Check = no  
Add this line:  
Stupid Mode = yes

# wvdial  
–> WvDial: Internet dialer version 1.56  
–> Initializing modem.  
–> Sending: AT+crm=1  
AT+crm=1  
OK  
–> Sending: AT+cso=33  
AT+cso=33  
OK  
–> Modem initialized.  
–> Sending: ATDT#777  
–> Waiting for carrier.  
ATDT#777  
CONNECT  
~[7f]}#@!}!}!} }3}”}&} } } } }#}%B#}%}’}”}(}”W}0~  
–> Carrier detected. Starting PPP immediately.  
–> Starting pppd at Sun Aug 5 23:49:37 2007  
–> Pid of pppd: 13779  
–> Using interface ppp0  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> pppd: �[10][06][08][18][01][06][08]  
–> local IP address 10.245.169.38  
–> pppd: �[10][06][08][18][01][06][08]  
–> remote IP address 10.64.64.64  
–> pppd: �[10][06][08][18][01][06][08]  
–> primary DNS address 202.152.165.36  
–> pppd: �[10][06][08][18][01][06][08]  
–> secondary DNS address 202.93.40.174  
–> pppd: �[10][06][08][18][01][06][08]
