---
layout: post
title: "Lupa Password root&nbsp;MySQL"
date: 2007-10-06T17:49:34+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/10/06/lupa-password-root-mysql/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/10/06/lupa-password-root-mysql/), ditulis pada 2007-10-06.

Bila anda lupa password root MySQL? tidak perlu Panik! berikut ini adalah caranya. Adalah beberapa langkah yang harus anda lakukan untuk mengatasi masalah kelupaan passwd root mysql anda yaitu:

  * Stop service MySQL server
  * Start MySQL dengan –skip-grant-tables option
  * Koneksikan diri anda ke MySQL sebagai root
  * Buat passwd baru dan restart MySQL server



tentunya anda bertanya teknisnya bagaimana? jangan kawatir. mari kita mulai

  1. `# /etc/init.d/mysql stop`
  2. `# mysqld_safe --skip-grant-tables &`
  3. `# mysql -u root`
  4. `mysql> use mysql;  
mysql> update user set password=PASSWORD("NEW-ROOT-PASSWORD") where User='root';  
mysql> flush privileges;  
mysql> quit`
  5. `# /etc/init.d/mysql stop`
  6. `# /etc/init.d/mysql start`



Coba sekarang anda login dengan passwd baru. berhasil bukan?
