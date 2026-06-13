---
layout: post
title: "Installasi Slackware Buat Pemula&nbsp;(Banget)"
date: 2008-02-16T08:43:59+0800
categories: [archive]
tags: [wordpress, imported]
original_url: https://firstly.wordpress.com/2008/02/16/installasi-slackware-buat-pemula-banget/
---

> Tulisan ini di-import dari [blog WordPress saya yang lama](https://firstly.wordpress.com/2008/02/16/installasi-slackware-buat-pemula-banget/), ditulis pada 2008-02-16.

Slackware sebagai salah satu distro paling tua memiliki penggemar yang cukup banyak. Tapi para pemula linux entah kenapa selalu beranggapan bahwa Slackware susah untuk dipelajari, bahkan untuk installasi sekalipun slackware begitu menakutkan untuk pemula.

Sebetulnya slackware tidak lah menakutkan, bahkan installasi nya yang lebih memilih menggunakan text base masih lebih mudah dibandingkan dengan installasi distro lain yang sudah mempergunakan GUI yang cantik.

Keuntungan installasi text base adalah tidak diperlukannya resource hardware yang terlalu besar ketika installasi sehingga installsi akan berjalan lebih cepat.

Biar anda tidak takut dengan installasi text mode Slackware berikut ini saya capture langkah-langkah installasi dari nol sampai Slackware bisa login. Dan seperti biasa apabila anda klik read more maka anda akan menemukan banyak sekali gambar (68 gambar) oleh karena itu sabar aja ya kalo agak lambat buka nya.

Installasi Slackware seperti distro lainnya bisa dilakukan dengan cara boot dari CD atau DVD. Dan untuk bisa boot dari CD atau DVD tentu saja anda harus merubah susunan boot order bios anda menjadi CD atau DVD terlebih dahulu. Setelah itu anda bisa mulai memasukan CD atau DVD Slackware anda dan Installasi pun dimulai seperti berikut ini.

[![slack](https://firstly.wordpress.com/wp-content/uploads/2008/02/1.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/1.png "slack")[![slack-2](https://firstly.wordpress.com/wp-content/uploads/2008/02/2.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/2.png "slack-2")[![slack-3](https://firstly.wordpress.com/wp-content/uploads/2008/02/3.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/3.png "slack-3")

Gambar diatas adalah menu ketika pertama kali kita boot atau biasa disebut lilo (linux loader). Apabila anda tidak memiliki hardware yang memerlukan driver khusus seperti harddisk sata atau scsi maka anda bisa langsung tekan enter untuk boot. Tetapi apabila anda memiliki hardware-hardware khusus silahkan tekan **F2** untuk melihat menu bantuan dan **F3** untuk melihat daftar cheat boot Slackware.

Cara menggunakan cheat boot tersebut adalah dengan mengetikan nama yang kita inginkan. Misalkan anda menggunakan harddisk sata maka anda tinggal mengetikan sata.i dan enter.

[![slack-4](https://firstly.wordpress.com/wp-content/uploads/2008/02/4.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/4.png "slack-4")[![slack-5](https://firstly.wordpress.com/wp-content/uploads/2008/02/5.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/5.png "slack-5")

Setelah anda menekan enter maka berikutnya anda akan ditanyakan jenis dari keyboard yang anda pakai. Apabila anda menggunakan keyboard versi US maka anda tidak usah pusing lagi tinggal enter saja dan anda akan dibawa ke gambar berikutnya yaitu tampilan login. Untuk login yang harus anda masukan adalah root enter dan anda tidak akan ditanyakan password.

Setelah berhasil login yang pertama kali harus anda lakukan adalah membuat partisi untuk menginstall Slackware. Dan di Slackware anda diberi tools yang sangat mudah untuk dipakai yaitu cfdisk. Untuk memulai nya cukup ketikan cfdisk seperti digambar berikut ini:

[![slack-6](https://firstly.wordpress.com/wp-content/uploads/2008/02/6.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/6.png "slack-6")[![slack-7](https://firstly.wordpress.com/wp-content/uploads/2008/02/7.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/7.png "slack-7")[![slack-8](https://firstly.wordpress.com/wp-content/uploads/2008/02/8.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/8.png "slack-8")[![slack-9](https://firstly.wordpress.com/wp-content/uploads/2008/02/9.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/9.png "slack-9")[![slack-10](https://firstly.wordpress.com/wp-content/uploads/2008/02/10.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/10.png "slack-10")[![slack-11](https://firstly.wordpress.com/wp-content/uploads/2008/02/11.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/11.png "slack-11")

[![slack-13](https://firstly.wordpress.com/wp-content/uploads/2008/02/13.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/13.png "slack-13")[![slack-12](https://firstly.wordpress.com/wp-content/uploads/2008/02/122.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/122.png "slack-12")[![slack-14](https://firstly.wordpress.com/wp-content/uploads/2008/02/14.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/14.png "slack-14")[![slack-15](https://firstly.wordpress.com/wp-content/uploads/2008/02/15.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/15.png "slack-15")[![slack-16](https://firstly.wordpress.com/wp-content/uploads/2008/02/16.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/16.png "slack-16")[![slack-17](https://firstly.wordpress.com/wp-content/uploads/2008/02/17.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/17.png "slack-17")[![slack-18](https://firstly.wordpress.com/wp-content/uploads/2008/02/18.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/18.png "slack-18")[![slack-19](https://firstly.wordpress.com/wp-content/uploads/2008/02/19.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/19.png "slack-19")[![slack-20](https://firstly.wordpress.com/wp-content/uploads/2008/02/20.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/20.png "slack-20")[![slack-21](https://firstly.wordpress.com/wp-content/uploads/2008/02/21.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/21.png "slack-21")[![slack-22](https://firstly.wordpress.com/wp-content/uploads/2008/02/22.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/22.png "slack-22")[![slack-23](https://firstly.wordpress.com/wp-content/uploads/2008/02/23.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/23.png "slack-23")

Seperti gambar-gambar diatas anda bisa dengan mudah membuat partisi. Yang harus anda ketahui adalah untuk bergerak antar menu anda bisa menggunakan panah kiri dan kanan. Sementara untuk bergerak antar partisi menggunakan panah atas dan bawah. Untuk memilih salah satu menu anda harus menggunakan enter.

Partisi minimal yang harus anda bikin untuk bisa berhasil Install slackware adalah dua partisi yaitu root ( / ) dan swap. Untuk swap anda bisa mempergunakan maksimal dua kali besar memori yang terpasang di komputer anda apabila memori yang anda miliki kurang dari 512 Mega. Apabila RAM yang anda miliki sudah lebih dari 512 Mega anda cukup membuat swap sebesar RAM yang anda miliki. Supaya satu partisi bisa menjadi swap, anda harus merubah type dari partisi tersebut dari Linux menjadi swap. Caranya adalah dengan memilih partisi yang ingin anda rubah dengan panah atas atau bawah, kemudian pilih type dengan panah kiri atau kanan kemudian enter. Ketika ditampilkan daftar jenis-jenis partisi anda bisa enter dua kali langsung atau anda mengetikan kode dari swap partition yaitu 82.

Apabila anda membuat partisi tidak lebih dari empat partisi anda bisa membuat seluruh partisi sebagai primary partition sementara apabila sudah lebih dari 4, partisi ke 4 dan seterusnya haruslah logical.

Anda juga harus menentukan satu partisi sebagai bootable partition. Biasanya yang di set bootable partition adalah root partition.

Setelah semua selesai berikutnya adalah menuliskan perubahan yang barusan kita buat dengan memilih menu write dan enter kemudian anda harus mengetikan “yes” tanpa tanda kutip untuk konfirmasi sebelum cfdisk menuliskan hasil perubahan yang anda lakukan. Sebelum anda memilih write semua perubahan terhadap harddisk belum dilakukan. Apabila anda merasa ragu dengan perubahan yang anda lakukan anda bisa keluar tanpa write dan harddisk anda masih tetap seperti sebelumnya tidak ada data yang hilang.

Langkah terakhir dari pembuatan partisi adalah memilih quit untuk kembali ke console dan memulai installasi Slackware dengan mengetikan perintah **setup** dan enter. Anda akan dibawa ke menu installasi Slackware. Yang harus anda pilih pertama kali adalah Addswap yaitu menu untuk mengaktifkan swap partition. Dengan aktifnya swap partition maka apabila memori yang anda miliki tidak cukup besar maka akan sangat terbantu dengan swap partition sebagai memori virtual tambahan.

[![slack-24](https://firstly.wordpress.com/wp-content/uploads/2008/02/24.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/24.png "slack-24")[![slack-25](https://firstly.wordpress.com/wp-content/uploads/2008/02/25.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/25.png "slack-25")[![slack-26](https://firstly.wordpress.com/wp-content/uploads/2008/02/26.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/26.png "slack-26")

Secara otomatis Installer slackware akan mendeteksi apakah anda memiliki partisi swap atau tidak anda cukup memilih ok di windows berikutnya kemudian kalau anda tidak yakin dengan kondisi harddisk anda, anda bisa memilih check for bad block sebelum diformat, tetapi ini akan memakan waktu yang lumayan lama. Biasanya saya cukup pilih no saja untuk melanjutkan.

[![slack-27](https://firstly.wordpress.com/wp-content/uploads/2008/02/27.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/27.png "slack-27")[![slack-28](https://firstly.wordpress.com/wp-content/uploads/2008/02/28.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/28.png "slack-28")[![slack-29](https://firstly.wordpress.com/wp-content/uploads/2008/02/29.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/29.png "slack-29")[![slack-30](https://firstly.wordpress.com/wp-content/uploads/2008/02/30.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/30.png "slack-30")[![slack-31](https://firstly.wordpress.com/wp-content/uploads/2008/02/31.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/31.png "slack-31")

Langkah berikutnya adalah memilih, memformat dan mounting partisi sesuai dengan yang kita inginkan. Apabila anda membuat lebih dari satu partisi Linux maka anda akan diberi daftar partisi yang belum di format. Anda harus memilih satu partisi yang akan dimount sebagai root ( / ) partition pertama kali baru dilanjutkan dengan partisi-partisi lainnya.

File System yang biasa saya pakai dalam installasi adalah reiserfs dengan alasan terasa lebih cepat dan stabil dibandingkan ext2 atau ext3 tapi anda bisa memilih yang mana saja karena disini hanyalah masalah selera saja.

Proses selanjutnya adalah memilih source installasi. Cara paling mudah, murah dan cepat adalah dengan menggunakan CD / DVD. Anda bisa saja menggunakan media yang lain seperti http, ftp atau nfs tetapi tetap tidak akan lebih cepat dan mudah dibandingkan dengan CD / DVD paling ngga anda tidak perlu sibuk mengatur source address dan lain sebagainya. Tetapi cara installasi dari ftp atau http bisa jadi opsi apabila anda tidak memiliki CD / DVD untuk install. Berikut ini screenshoot nya.

[![slack-32](https://firstly.wordpress.com/wp-content/uploads/2008/02/32.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/32.png "slack-32")[![slack-33](https://firstly.wordpress.com/wp-content/uploads/2008/02/33.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/33.png "slack-33")[![slack-34](https://firstly.wordpress.com/wp-content/uploads/2008/02/34.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/34.png "slack-34")

Langkah selanjutnya adalah memilih paket yang akan anda install. Apabila anda tidak yakin dengan apa yang anda pilih dan anda memiliki harddisk yang cukup besar (minimal 4Gb) anda bisa memilih semua aplikasi untuk di install dan ini cukup aman bagi anda pemula, daripada memilih dari daftar tersebut, kemudian salah pilih dan Slackware anda tidak jalan ![\)](https://i0.wp.com/www.giest.org/wp-includes/images/smilies/icon_smile.gif) toh setelah beres installasi anda bisa memilih aplikasi-aplikasi apa saja yang akan di uninstall.

Disini saya hanya memilih paket-paket yang penting saja seperti base linux system, networking dan compiler karena seperti yang anda lihat sebelumnya bahwa saya hanya memiliki harddisk sebesar 2Gb saja.

[![slack-35](https://firstly.wordpress.com/wp-content/uploads/2008/02/35.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/35.png "slack-35")[![slack-36](https://firstly.wordpress.com/wp-content/uploads/2008/02/36.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/36.png "slack-36")[![slack-37](https://firstly.wordpress.com/wp-content/uploads/2008/02/37.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/37.png "slack-37")

Selanjutnya adalah anda sabar menunggu. Perlu beberapa menit untuk menyelesaikan proses installasi ini. Disini anda bisa tinggalkan sebentar komputer anda untuk sekedar membuat secangkir kopi dan cari angin di luar.

Setelah proses install aplikasi selesai selanjutnya adalah memilih source kernel yang akan anda install. Berhubung kita menginstall menggunakan CD / DVD maka anda bisa langsung saja memilih CDROM sebagai source kernel, kemudian anda pilih kernel mana yang akan anda pergunakan. Pilihan pertama yang ditampilkan (di sorot) adalah kernel yang sesuai dengan apa yang anda pilih ketika boot pertama kali menggunakan CD dan biasanya itu adalah type kernel yang paling sesuai dengan komputer anda. Tetapi apabila karena sesuatu hal anda harus merubah pilihan kernel anda bisa dengan mudah memilih jenis kernel yang anda perlukan.

[![slack-38](https://firstly.wordpress.com/wp-content/uploads/2008/02/38.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/38.png "slack-38")[![slack-39](https://firstly.wordpress.com/wp-content/uploads/2008/02/39.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/39.png "slack-39")

Di windows berikutnya anda akan ditanyakan apakah akan membuat boot disk dan apakah anda memiliki modem atau tidak. Berhubung saya tidak mau membuat boot disk dan tidak memiliki modem maka disini semua saya pilih skip dan no modem.

[![slack-40](https://firstly.wordpress.com/wp-content/uploads/2008/02/40.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/40.png "slack-40")[![slack-41](https://firstly.wordpress.com/wp-content/uploads/2008/02/41.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/41.png "slack-41")

Selanjutnya adalah menginstall linux loader atau lilo. Anda bisa memilih simple untuk installasi dengan mudah atau anda bisa memilih expert yang walaupun dibilang expert tetapi tetap sangat mudah ![\)](https://i0.wp.com/www.giest.org/wp-includes/images/smilies/icon_smile.gif) jadi jangan takut mencoba memilih expert. Untuk pilihan lokasi penginstallan lilo anda bisa memilih MBR tenang saja cukup aman koq. Kalaupun terjadi error anda masih bisa memperbaikinya nanti ![P](https://i0.wp.com/www.giest.org/wp-includes/images/smilies/icon_razz.gif) (kalo bisa)

[![slack-42](https://firstly.wordpress.com/wp-content/uploads/2008/02/42.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/42.png "slack-42")[![slack-43](https://firstly.wordpress.com/wp-content/uploads/2008/02/43.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/43.png "slack-43")[![slack-44](https://firstly.wordpress.com/wp-content/uploads/2008/02/44.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/44.png "slack-44")[![slack-45](https://firstly.wordpress.com/wp-content/uploads/2008/02/45.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/45.png "slack-45")

Berikutnya adalah memilih jenis mouse dan gpm (mouse akan aktif walaupun anda hanya menggunakan console, sangat berguna untuk copy paste text).

[![slack-46](https://firstly.wordpress.com/wp-content/uploads/2008/02/46.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/46.png "slack-46")[![slack-47](https://firstly.wordpress.com/wp-content/uploads/2008/02/47.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/47.png "slack-47")

Setelah menginstall linux loader selesai selanjutnya adalah setting network, disini anda harus mempersiapkan dulu IP address, netmask, gateway, dns, domain dan host untuk komputer anda ini. Apabila anda tidak tahu coba tanyakan kepada admin jaringan anda. Tetapi apabila anda tidak terhubung ke jaringan tetapi tetap ingin bermain-main dengan slackware anda bisa mengisi setting network disini dengan nilai seadanya asal masih mengikuti kaidah tcp/ip.

[![slack-48](https://firstly.wordpress.com/wp-content/uploads/2008/02/48.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/48.png "slack-48")[![slack-49](https://firstly.wordpress.com/wp-content/uploads/2008/02/49.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/49.png "slack-49")[![slack-51](https://firstly.wordpress.com/wp-content/uploads/2008/02/51.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/51.png "slack-51")[![slack-52](https://firstly.wordpress.com/wp-content/uploads/2008/02/52.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/52.png "slack-52")[![slack-53](https://firstly.wordpress.com/wp-content/uploads/2008/02/53.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/53.png "slack-53")[![slack-54](https://firstly.wordpress.com/wp-content/uploads/2008/02/54.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/54.png "slack-54")[![slack-55](https://firstly.wordpress.com/wp-content/uploads/2008/02/55.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/55.png "slack-55")[![slack-56](https://firstly.wordpress.com/wp-content/uploads/2008/02/56.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/56.png "slack-56")

Apabila setting network sudah selesai, selanjutnya adalah menu untuk memilih service apa saja yang ingin dijalankan ketika Linux pertama kali dijalankan. Anda bisa memilih secara default saja karena nanti setelah boot pertama anda bisa dengan mudah menghidupkan atau mematikan service ini.

[![slack-58](https://firstly.wordpress.com/wp-content/uploads/2008/02/58.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/58.png "slack-58")

Berikutnya adalah menu untuk menambah font dan pemilihan time zone. Untuk font saya tidak memilih font tambahan saya pilih no saja dan untuk timezone saya sesuaikan dengan lokasi saya, jadi saya pilih Asia/Jakarta.

[![slack-59](https://firstly.wordpress.com/wp-content/uploads/2008/02/59.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/59.png "slack-59")[![slack-60](https://firstly.wordpress.com/wp-content/uploads/2008/02/60.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/60.png "slack-60")[![slack-61](https://firstly.wordpress.com/wp-content/uploads/2008/02/61.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/61.png "slack-61")

Kemudian setelah pemilihan timezone selesai, Langkah terakhir adalah membuat password untuk root. Untuk password root ini anda disarankan menggunakan password yang bagus (tidak mudah ditebak dan mengkombinasikan hurup dan angka serta karakter khusus). Apabila anda membuat password yang terlalu lemah atau mudah ditebak maka Slackware akan memberi peringatan bahwa password anda lemah. Tetapi anda tetap bisa memaksakan untuk menggunakan password tersebut.

[![slack-62](https://firstly.wordpress.com/wp-content/uploads/2008/02/62.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/62.png "slack-62")[![slack-63](https://firstly.wordpress.com/wp-content/uploads/2008/02/63.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/63.png "slack-63")

Dengan selesainya pembuatan password root maka andapun sudah menyelesaikan seluruh tahap installasi Slackware. Selanjutnya adalah kembali ke menu utama installasi, keluar ke console dengan memilih menu exit, dan menekan kombinasi key ctrl + alt + del untuk reboot.

[![slack-64](https://firstly.wordpress.com/wp-content/uploads/2008/02/64.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/64.png "slack-64")[![slack-65](https://firstly.wordpress.com/wp-content/uploads/2008/02/65.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/65.png "slack-65")[![slack-66](https://firstly.wordpress.com/wp-content/uploads/2008/02/66.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/66.png "slack-66")

Sekarang tibalah saat nya anda berdo’a. Mudah-mudahan semua yang anda lakukan benar dan Slackware anda bisa dipakai dengan lancar :). Contoh berikut adalah hasil installasi yang sukses dimulai dari boot sampai login prompt.

[![slack-67](https://firstly.wordpress.com/wp-content/uploads/2008/02/67.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/67.png "slack-67")[![slack-68](https://firstly.wordpress.com/wp-content/uploads/2008/02/68.thumbnail.png)](http://firstly.wordpress.com/wp-content/uploads/2008/02/68.png "slack-68")

Semoga Berhasil selamat mencoba….
