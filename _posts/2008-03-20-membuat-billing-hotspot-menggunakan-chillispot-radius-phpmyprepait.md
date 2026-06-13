
```markdown
---
layout: post
title: "Membuat Billing Hotspot Menggunakan Chillispot, Radius&nbsp;phpmyprepait"
date: 2008-03-20T23:25:20+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/03/20/membuat-billing-hotspot-menggunakan-chillispot-radius-phpmyprepait/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/03/20/membuat-billing-hotspot-menggunakan-chillispot-radius-phpmyprepait/), ditulis pada 2008-03-20.

Perpaduan Chillispot, Freeradius dan Mysql dapat menghasilkan aplikasi Hotspot lumayan handal. Chillispot sebagai Authentifikasi, Freeradius untuk account phpmyprepait sebagai billingnya dan Mysql untuk databasenya.

Sebagai uji coba saya akan menjelaskan bagaimana cara membuat Wi-Fi Hotspot tersebut :

**A. Yang dibutuhkan :**

1. Hotspot Access Point device, dalam hal ini saya menggunakan Linksys Tipe 54 GL AP bisa di gunakan AP Tipe apa saja.  
2. Sebuah komputer yang akan di jadikan sebagai radius server.  
3. OS GNU/Linux, Saya menggunakan OpenSUSE (10.2), Ubuntu, Slackware (dijelaskan)  
4. Mysql, untuk Authentic melalui database, untuk authentic nya bisa dengan beberapa cara seperti : unix user, smb user, file user  
5. Apache dengan perl support, untuk membuat user authentic melalui web-based, serta utk membuat login authentic via web-based di cgi-bin/hotspotlogin.cgi  
6. Chillispot, sistem kerja software ini adalah apabila user belum mendapatkan authentic dari server maka ia akan ter-redirect ke halaman login  
7. Freeradius, ini berfungsi sebagai pemberi authentifikasi kepada user  
8. PhpMyPrepaid, bila anda menggukan authentic melalui database Mysql, bisa juga sebagai pembuat user prepaid untuk billingnya  
9. Rokok, bisa Djarum Super bisa juga Marlboro, Atau Fileter Sejenisnya.  
10. Kopi, biar kuat begadang. atau susu putih ajah, gak usah pake gula, biar segerrrrrrr. menulis ini aja perlu Sopi Susu :D

**B. Cara Install :**

1. Untuk OS tergantung dari distro apa yang anda pakai, kali ini saya memakai distro keluaran dari SUSE (OpenSUSE 10.2-10.3). Saya hanya akan menjelaskan cara meng-install-nya dengan cara Distro OpenSUSE, Ubuntu Slackware dan untuk yang lain itu tergantung distro apa yang anda pilih dan nantinya di bagian konfigurasi akan di samakan untuk beberapa distro di atas.
2. Install mysql
3. Install Apache
4. Download chillispot; lalu install `rpm -ivh chillispot-1.0.i386.rpm` (Keluarga RPM) silahkan di sesuaikan sesuai keluarganya masing-masing (jika menggunakan Chilli di PC).
5. Install Freeradius
6. Setelah kita mengintsall Apache dan Mysql lalu kita dapat men-download phpmyprepait; **extract ke /srv/www/htdocs**
7. Sambil menginstall semua jgn lupa ambil rokok dan di nyalakan.
8. Jangan lupa untuk menyeduh kopi atau susunya.

**C. Konfigurasi :**

1. Saya mengeset Wi-Fi Hostpot (Linksys WRT 54GL) sebagai Access Point. Kemudian Linksys tersebut di upgrede ke [OpenWRT](http://openwrt.org "Openwrt") dan install [Chillispot](http://www.google.com/url?sa=t&ct=res&cd=3&url=http%3A%2F%2Fwiki.openwrt.org%2FMiniHowtos&ei=1-ziR5KoH5ng6QO5rvzBCA&usg=AFQjCNGxK3V2xx9CyLXD_oCi8cPA-4ExgQ&sig2=wOHYSt1dxn7Wm-LYZgU7ug "ChilliSpot") di dalam Linsys WRT 54GL tersebut. setelah selesai melakukan konfigurasi 

# **nvram set wan_device=eth0**

Paket yang di perlukan dalam linksys yaitu :

* **ip_2.6.11-050330-1_mipsel.ipk**
* **libpcap_0.9.4-1_mipsel.ipk**
* **tcpdump_3.8.3-1_mipsel.ipk**
* **kmod-sched_2.4.30-brcm-3_mipsel.ipk**
* **tc_2.6.11-050330-1_mipsel.ipk**
* **chillispot_1.0RC3-1_mipsel.ipk (diperlukan jika chilli diletakkan di Linksys)**
* **kmod-tun_2.4.30-1.ipk**

Berikut konfigurasi Linksys **WRT 54GL**

> **nvram set lan_proto=static**
> **nvram set lan_ipaddr=192.168.10.254**
> **nvram set lan_netmask=255.255.255.0**

– seting wan/internet

> **nvram set wan_proto=static**
> **nvram set wan_ipaddr=XX.XX.XX.XX (berikan ip local)**
> **nvram set wan_netmask=255.255.255.0**
> **nvram set wan_gateway=XX.XX.XX.XX**
> **nvram set wan_dns="diisi" Biarkan terpasang.**
> **nvram set wan_hostname=(pengguna)**

– Seting AP

```bash
nvram set wl0_mode=ap   
nvram set wl0_ssid=disesuikan   
nvram set wl0_auth_mode=open   
nvram set wl0_wep=disabled   
nvram set wl0_channel=(pilih channel yang cocok)   
nvram commit

```

2. Setelah melakukan flashing dan Install OS nya seperti kebutuhan diatas dan di sesuaikan, pertama kita harus mematikan service dhcpd yang ada di server kita, biarkan chillispot yang menangani dhcp.
3. # **pico /etc/chilli.conf** isi dari chilli saya (konfigurasi ini bisa di gunakan di Linksys 54GL atau di Komputer PC)



```text
############################################################################## 
# Sample ChilliSpot configuration file @ Fadly Kasim 
############################################################################## 
net 192.168.154.0/24 
dynip 192.168.154.0/24 
statip 192.168.154.0/24 
domain (domain isp anda) 
dns1 202.X.X.X (DNS Anda) 
dns2 202.X.X.X (DNS Anda) 

#Radius parameters 
radiusauthport 1812 
radiusacctport 1813 
radiuslisten 127.0.0.1 
radiusserver1 127.0.0.1 
radiusserver2 127.0.0.1 
radiussecret testing123 

#dhcpmac 00:00:5E:00:02:00 
dhcpif eth0 
uamserver [https://192.168.154.1/cgi-bin/hotspotlogin.cgi](https://192.168.154.1/cgi-bin/hotspotlogin.cgi) 

########################################### 
#Untuk meng allow domain yang bisa di akses 
uamallowed [http://www.google.com](http://www.google.com) 
########################################## 
uamsecret theuamsecret 
uamlisten 192.168.154.1 
uamallowed 192.168.154.1 
uamport 3990 
#======Selesai=============#

```

4. Konfigurasikanlah **chilli.conf** sesuai kebutuhan anda, disini ada beberapa point penting dalam konfigurasinya, yaitu:

> **radiussecret**, ini dibutuhkan untuk komunikasi antara radius server dan chillispot
> **uamserver**, dimana file **hotspotlogin.cgi** di simpan. Biasanya di letakkan di **/var/www/cgi-bin**
> **dhcpif**, di sesuikan ethx yang nantinya di gunakan untuk client
> Untuk itu bisa melakukakan copy file **hotspotlogin.cgi** dari **/usr/share/doc/chillispot-1.0/hotspotlogin.cgi** ke **/var/www/cgi-bin**, jadi nanti utk URL redirect nya akan menjadi **https://192.168.0.254/cgi-bin/hotspotlogin.cgi (lihat uamserver)**, ingat harus dalam secure line **ssl**.

5. Konfigurasi radius :

Setelah install Freeradius lalu masuk ke direktori radius dimana konfigurasinya berada, bila anda menggunakan OpenSuse dan memakai RPM dalam menginstallnya maka anda masuk ke direktori **/etc/raddb/** dan apabila anda menginstall dengan cara meng-compile sendiri secara default direktori nya ada di **/usr/local/etc/raddb/** atau terserah dimana –prefix=PREFIX anda diletakan.

# **pico client.conf** isinya seperti ini :

> **client 192.168.0.254**
> **secret = //ini untuk membuat komunikasi dalam chillispot dan radius (seperti pada point C.3.d)**
> **shortname = localhost**
> **radius = other**
> **radius password = "blablabla"**

# **pico sql.conf**, ini diedit karena kita akan menggunakan mysql sebagai database user authentic, ada beberapa point penting yaitu :

> **driver = "rlm_sql_mysql"** // Modul yang digunakan untuk koneksi ke mysql server
> **driver/lib** yang digunakan apabila kita menggunakan Mysql, ada beberapa tipe driver disini yaitu : **rlm_sql_mysql, rlm_sql_postgresql, rlm_sql_iodbc, rlm_sql_oracle, rlm_sql_unixodbc, rlm_sql_freetds**
> **server = "localhost"** //server mysql berada.
> **login = "root"** //login access ke mysql dan memiliki GRANT ke database radius
> **password = "blablabla"** //password dari database-user yang memiliki GRANT ke database radius
> **radius_db = "radius"** //database-name dimana user radius berada

**# pico radius.conf** lalu tambahkan perintah dibawah ini, sesudah baris **sqlcounter monthlycounter {** sampai tanda **}** dan ditambah sesudah tanda **}** isinya :

{% raw %}

```text
$INCLUDE ${confdir}/sql.conf  

sqlcounter noresetcounter { 
    counter-name = Max-All-Session-Time 
    check-name = Max-All-Session 
    sqlmod-inst = sql 
    key = User-Name 
    reset = never 
    query = "SELECT SUM(AcctSessionTime) FROM radacct WHERE UserName='%{%k}'" 
}

```

{% endraw %}

untuk **authorize** ganti dengan :

> **authorize {**
> **preprocess**
> **chap**
> **mschap**
> **suffix**
> **eap**
> **sql**
> **noresetcounter**
> **}**

dan untuk **Authentication** ganti dengan:

> **authenticate {**
> **Auth-Type PAP {**
> **pap**
> **}**
> **Auth-Type CHAP {**
> **chap**
> **}**
> **Auth-Type MS-CHAP {**
> **mschap**
> **}**
> **unix**
> **eap**
> **}**

6. Sekarang kita akan mencoba men-setting konfigurasi di PhpMyPrepaid sebagai user administrator sekaligus bisa sebagai pembuat prepaid card login serta billing nya.
7. Extract ke folder apache berada, default ada di **/var/www/**
8. Masuk ke folder phpmyprepaid
9. # pico **config.inc.php** disini ada beberapa point penting:



> **$dbName="radius"**; //database yang di pakai
> **$fpdfdir="/var/www/phpmyprepaid/fpdf"**; //lokasi dari direktori fpdf berada, tanpa "/" (slash)
> **$radius_server="192.168.0.254"**; //server radius berada
> **$radius_server_port="1812"**; //port yang dipakai oleh radius server
> **$radiussecret=" "**; //huruf rahasia yang dipakai oleh radius server untuk dapat berkomunikasi

> # **pico dbconnect.php** // edit seperti yang di edit di radius server
> 
> 
> **$my_host = "localhost";**
> **$my_user = "root";**
> **$my_pass = "PASS-MYSQL-ANDA";**
> **$my_dbase = "radius";**

7. Jalankan **http://192.168.0.254/phpmyprepaid/index.php** maka akan muncul tampilan instalasi phpmyprepaid, isi kolom databases dan di sesuikan dengan databases pada radius **dbconnect.php** secara otomatis menginstall dengan sendiri.
8. Masukan username **admin** dan password **admin**, setelah semua database terinstall. Maka dengan berakhir nya point terakhir maka selesai jugalah pekerjaan kita.

di edit ulang tgl 13-05-2008
Komputer P 4
Instalasi OS Linux OpenSUSE 10.2
Instalasi

```

```
