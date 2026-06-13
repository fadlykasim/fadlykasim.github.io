---
layout: post
title: "Perintah Dasar Linux yang sering&nbsp;digunakan"
date: 2007-08-23T04:59:06+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2007/08/23/perintah-dasar-linux-yang-sering-digunakan/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2007/08/23/perintah-dasar-linux-yang-sering-digunakan/), ditulis pada 2007-08-23.

Perintah 						Keterangan
    
    
    ==========================================================================
    
    
    any_command --help 		Menampilkan keterangan bantu tentang pemakaian
    
    
                                    perintah. "--help" sama dengan perintah pada
                                    DOS "/h".[](http://Perintah%20Dasar%20Linux%20yang%20sering%20digunakan "Perintah Dasar Linux yang sering digunakan")
    
    
    ls 				Melihat isi file dari direktori aktif. Pada linu
                                    x perintah "dir" hanya berupa alias dari perin-
                                    tah "ls". Untuk perintah "ls" sendiri sering di-
                                    buatkan alias "ls --color", agar pada waktu di
                                    "ls" ditampilkan warna-warna sesuai dengan file-
                                    filenya, biasanya hijau untuk execute, dsb.
    
    
    ls -al				Melihat seluruh isi file pada direktori aktif be
                                    serta file hidden, lalu ditampilkan layar per-
                                    layar.
    
    
    cd (directory)		       	Change directory. Menggunakan "cd" tanpa nama di
                                   	rektori akan menghantarkan anda ke home direktor.
                                   	Dan "cd -" akan menghantarkan anda ke direktori
                                   	sebelumnya.
    
    
    cp (source destination)		Mengopi suatu file.
    
    
    mcopy source destination 	Mengcopy suatu file dari/ke dos filesystem.
    				Contoh mcopy a:autoexec.bat/junk .
    				Gunakan "man mtools" untuk command yang sejenis
                                    : mdir, mcd, mren, move, mdel, mmd, mrd, mformat
                                    ....
    mv source destination 		Memindahkan atau mengganti nama file
    
    
    ln -s source destination      	Membuat Simbolic Links,
                                 	contoh ln -sf /usr/X11R6/bin/XF86_SVGA /etc/X11/X,
                                  	membuat Simbolic link dari file XF86_SVGA ke X
    
    
    rm files 		 	Menghapus file
    
    
    mkdir directory 		Membuat direktori baru
    
    
    rmdir directory 		Menghapus direktori yang telah kosong
    
    
    rm -r files (recursive remove)	Menghapus file, direktori dan subdirektorinya.
                                    Hati-hati menggunakan perintah ini apabila anda
                                    login sebagai root, karena root dengan mudah
                                    dapat menghapus seluruh file pada sistem dengan
                                    perintah di atas, tidak ada perintah untuk un-
                                    delete di Linux (belum)
    
    
    more 				Untuk melihat isi suatu file, dengan tambahan
    				perintah more, maka isi file tersebut ditampil-
    				kan layar per layar.
    
    
    less filename 			Melihat suatu file layar per layar, dan tekan
    				tombol "q" apabila ingin keluar,pico filename
    				Edit suatu text file.
    
    
    pico -w filename 		Edit suatu text file, dengan menonaktif-
    				kan fungsi word wrap, sangat berguna untuk meng-
    				edit file seperti /etc/fstab.
    
    
    lynx file.html 			Melihat file html atau browse ke net dengan text
    			 	mode, dimana gambar/image tidak dapat ditampil-
    				kan, tapi lynx adalah suatu browser yang sangat
     				cepat, sangat berguna bila anda hanya mengingin-
    				kan suatu artikel tanpa image.
    
    
    tar -zxvf filename.tar.gz 	Meng-untar sebuah file tar sekaligus meng-uncomp
    				ress file tersebut (*.tar.gz or *.tgz), untuk me
    				letakkannya direktori yg diinginkan tambahkan
    				option -C direktori,
    				contoh tar -zxvf filename.tar.gz -C /opt
    				(meletakkan file tersebut di direktori /opt
    
    
    tar -xvf filename.tar 		Meng-untar sebuah file tar yang tidak terkom-
    				press (*.tar).
    
    
    gunzip filename.gz 		Meng-uncompress sebuah file zip (*.gz" or *.z).
    				dengan menggunakan gzip (juga zip atau compress)
    				jika anda menginginkan mengompress file.
    
    
    bunzip2 filename.bz2 		Meng-uncompress file dengan format (*.bz2)
    				dengan utiliti "bzip2", digunakan pada file
    				yang besar.
    
    
    unzip filename.zip 		Meng-uncompress file dengan format (*.zip) deng-
    				an utiliti "unzip" yang	kompatibel dengan pkzip
    				for DOS.
    
    
    find / -name "filename" 	Mencari "namafile" pada komputer anda dimulai de
    				ngan direktori /. Namafile tersebut mungkin saja
    				berisi wildcard (*,?).
    
    
    locate filename 		Mencari file dengan string "filename". Sangat mu
    				dah dan cepat dari perintah di atas.
    
    
    pine 				Email reader yang sangat mudah digunakan, dan
    				menjadi favorit banyak pemakai 	mesin Unix.
    				Atau anda bisa pakai email yang sangat customize
    				 yaitu "mutt",
    
    
    talk username1 			Berbicara dengan keyboard dengan user lain yg se
    				dang login pada mesin kita (atau gunakan "talk
    				username1@machinename" untuk berbicara dengan
    				komputer lain) . Untuk menerima undangan perca
    				kapan, ketikkan"talk username2". Jika seseorang
    				mencoba untuk berbicara dengan anda dan itu dira
    				sakan mengganggu, anda bisa menggunakan perinta
    				"mesg n" untuk 	menolak pesan tersebut. Dan guna
    				kan perintah "who" atau "rwho" untuk melihat
    				siapa user yang mengganggu tersebut.
    
    
    mc				Menjalankan "Morton Commander" ... eh... salah
    				maksudnya "Midnight Commander" sebagai file
    				manager, cepat dan bagus.
    
    
    telnet server 			Untuk menghubungkan komputer kita ke komputer la
    				in dengan menggunakan protokol TELNET. Gunakan
    				nama mesin atau Nomor IP mesin, dan anda akan
    				mendapatkan prompt login name dari mesin terse-
    				but, masukkan passwordnya, oh ya .. anda juga
    				harus punya account di mesin remote tersebut.
    				Telnet akan menghubungkan anda dengan komputer
    				lain dan membiarkan anda untuk mengoperasikan
    				mesin tersebut. Telnet sangat tidak aman, setiap
    				yang anda ketik menjadi "open text", juga dengan
    				password anda! Gunakan ssh alih-alih telnet
    				untuk mengakses mesin secara remote.
    
    
    rlogin server (=remote login) 	Menghubungkan anda ke komputer lain. Loginname
    				dan password, tetapi apabila account anda terse-
    				but telah dipakai, maka anda akan mendapatkan
    				pesan kesalahan pada password anda. Sangat tidak
    				aman juga, gunakan ssh  sebagai gantinya. rsh
    				server (=remote shell) Jalan lain untuk menghu-
    				bungkan anda ke remote machine. Apabila login
    				name/password anda sedang dipakai di remote
    				mesin tsb, maka password anda tidak akan berla-
    				ku. Idem dengan rlogin, gantikan dengan ssh. ftp
    				server Ftp ke mesin lain, ini sangat berguna un-
    				tuk mengopy file ke/dari remote mesin. Juga
    				tidak aman, gunakan scp dari keluarga ssh  seba-
    				gai gantinya.
    
    
    minicom 			Program Minicom (dapat dikatakan seperti
    				"Procomm/Hyperterminal for Linux").
    
    
    ./program_name 			Menjalankan program pada direktori aktif, yang
    				mana tidak terdapat pada PATH anda
    
    
    xinit 				Menjalankan X-window server (tanpa windows
    				manager).
    
    
    startx 				Menjalankan X-window server dan meload default
    				windows manager. Sama seperti perintah "win"
    				under DOS dengan Win3.1
    
    
    startx -- :1 			Menjalankan sesi X-windows berikutnya pada
    				display 1 (default menggunakan display 0).
    				Anda dapat menjalankan banyak GUI terminal
    				secara bersamaan, untuk pindah antar GUI
    				gunakan , , etc,
    				tapi ini akan lebih banyak memakan memori.
    
    
    x-term 		              	(pada X terminal) ,menjalankan X-windows terminal.
    			      	Untuk keluar ketikkan "exit"
    
    
    xboing 				(pada X terminal). Sangat lucu deh ...., seperti
    				games-games lama .....
    
    
    gimp 				(pada X terminal) Program image editor yang
    				sangat bagus, bisa disamakan dengan Adobe Photo-
    				shop, yang membedakan adalah program ini gratis.
    
    
    netscape 			(pada X terminal) menjalankan netscape, versi
    				pada waktu tulisan ini dibuat telah mencapai
    				versi 4.7
    
    
    netscape -display host:0.0 	(pada X terminal) menjalankan netscape pada me-
    				sin yang aktif dan menampilkan outputnya pada me
    				sin yang bernama "host" display 0 screen 0. And
     				harus memberikan akses untuk mesin aktif untuk
    				menampilkannya pada mesin "host" dengan perintah
    				"xhost"
    
    
    shutdown -h now 		(sebagai root) Shut down sistem. Umumnya diguna-
    				kan untuk remote shutdown. Gunakan
    				untuk shutdown pada konsol (dapat dijalankan
    				oleh user).
    
    
    halt 				reboot (sebagai root) Halt atau reboot mesin.
    				Lebih simple dari perintah di atas.
    
    
    man topic 			Menampilkan daftar dari sistem manual pages
    				(help) sesuai dengan topic. Coba "man man". lalu
    				tekan "q" untuk keluar dari viewer. Perintah "in
    				fo topic" Manual pages dapat dibaca dilhat de-
    				ngan cara "any_command --help".
    
    
    apropos topic 			Menampilkan bantuan manual berdasarkan topik..
    
    
    pwd 				Melihat direktori kerja saat ini
    
    
    hostname 			Menampilkan nama local host (mesin dimana anda
    				sedang bekerja). Gunakan perintah " netconf"
    				(sebagai root) untuk merubah nama host dari
    				mesin tersebut, atau edit file /etc/hosts
    
    
    whoami 				Mencetak login name anda
    
    
    id username 			Mencetak user id (uid) atau group id (gid)
    
    
    date 				Mencetak atau merubah tanggal dan waktu pada
    				komputer, contoh merubah tanggal dan waktu ke
    				2000-12-31 23:57 dengan perintah;
    				date 123123572000
    
    
    time 				Melihat jumlah waktu yg ditangani untuk penyele-
    				saian suatu proses + info lainnya. Jangan dibin-
    				gungkan dengan perintah "date"
    
    
    who 				Melihat user yang login pada komputer kita.
    
    
    rwho -a 			Melihat semua user yg login pada network anda.
    				Layanan perintah rwho ini harus diaktifkan,
    				jalankan setup sebagai root utk mengaktifkannya.
    finger username 		Melihat informasi user, coba jalankan; finger
    				root
    last				Melihat user sebelumnya yang telah login di kom-
    				puter.
    
    
    uptime 				Melihat jumlah waktu pemakaian komputer oleh se-
    				seorang, terhitung proses reboot terakhir.
    
    
    ps (=print status) 		Melihat proses-proses yang dijalankan oleh user
    
    
    ps axu 				Melihat seluruh proses yang dijalankan,
    				walaupun tanpa terminal control, juga ditampil-
    				kan nama dari user untuk setiap proses.
    
    
    top 				Melihat proses yang berjalan, dengan urutan
    				penggunaan cpu.
    uname -a 			Informasi system kernel anda
    
    
    free 				Informasi memory (dalam kilobytes).
    
    
    df -h 				(=disk free) Melihat informasi pemakaian disk
    				pada seluruh system (in human-readable form)
    
    
    du / -bh 			(=disk usage) Melihat secara detil pemakaian
    				disk untuk setiap direktori, dimulai dari root
    				(in human legible form).
    
    
    cat /proc/cpuinfo 		Cpu info. Melihat file pada /proc directori yang
    				bukan merupakan file nyata (not real files).
    
    
    cat /proc/interrupts 		Melihat alamat interrupt yang dipakai.
    
    
    cat /proc/version 		Versi dari Linux dan informasi lainnya.
    
    
    cat /proc/filesystems 		Melihat filesystem yang digunakan.
    
    
    cat /etc/printcap 		Melihat printer yang telah disetup
    
    
    lsmod 				(as root) Melihat module-module kernel yang
    				telah di load.
    
    
    set 				Melihat environment dari user yang aktif
    
    
    echo $PATH 			Melihat isi dari variabel "PATH". Perintah ini
    				dapat digunakan untuk menampilkan variabel
    				environmen lain dengan baik. Gunakan "set" untuk
    				melihat environmen secara penuh.
    
    
    dmesg 				Mencetak pesan-pesan pada waktu proses boot.
    				(menampilkan file: /var/log/dmesg).
    
    
    clear 				Membersihkan layar.
    
    
    adduser 			Menambah pengguna.
