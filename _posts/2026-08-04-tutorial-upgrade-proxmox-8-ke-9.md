---
layout: post
title:  "Cara Upgrade Proxmox VE 8 ke Proxmox VE 9 (In-Place, Tanpa Install Ulang)"
date:   2026-08-04 10:00:00 +0800
categories: [teknologi, virtualisasi]
tags: [proxmox, virtualisasi, homelab, debian, tutorial]
description: >-
  Panduan lengkap upgrade Proxmox VE dari versi 8 ke 9.2.6 secara in-place,
  langkah demi langkah, termasuk cara menangani warning dan prompt konfigurasi.
  Berdasarkan pengalaman nyata.
---

Proxmox VE 9 sudah rilis, berbasis Debian 13 "Trixie" dengan kernel baru, QEMU 10, dan banyak fitur baru. Kabar baiknya, kita bisa upgrade dari Proxmox 8 ke 9 secara **in-place** — artinya tanpa install ulang, dan semua VM serta container tetap aman.

Di tutorial ini saya akan memandu prosesnya langkah demi langkah, berdasarkan pengalaman langsung mengupgrade server saya dari versi **8.0.4 hingga 9.2.6**. Saya sertakan juga cara menangani _warning_ dan _prompt_ konfigurasi yang muncul di tengah jalan — bagian yang sering dilewatkan tutorial lain, padahal justru di situ orang sering bingung.

> ⚠️ **Peringatan penting:** Backup dulu semua VM dan container Anda ke storage terpisah sebelum memulai. Upgrade in-place umumnya aman, tapi backup adalah satu-satunya jalan pulang kalau terjadi masalah. Jangan lewati langkah ini.
{: .prompt-warning }

## Apa yang Baru di Proxmox VE 9?

Sebelum mulai, sekilas perubahan besarnya:

| Komponen      | Proxmox 8      | Proxmox 9        |
|---------------|----------------|------------------|
| Basis Debian  | Bookworm (12)  | Trixie (13)      |
| Kernel        | 6.8            | 6.14 / 7.x-pve   |
| QEMU          | 9.x            | 10.x             |
| LXC           | 5.x            | 6.x              |
| ZFS           | 2.2            | 2.3              |

Beberapa fitur baru yang menarik: snapshot VM di LVM thick-provisioned, HA affinity rules yang menggantikan HA groups, tampilan web mobile baru, dan ekspansi perangkat ZFS RAIDZ tanpa downtime.

## Prasyarat: Yang Wajib Dipenuhi Dulu

Ada beberapa syarat yang **harus** dipenuhi sebelum menyentuh repository:

1. **Proxmox harus minimal versi 8.4.1.** Ini yang paling sering terlewat. Kalau Anda masih di 8.0.x, 8.1.x, atau 8.2.x seperti saya (saya mulai dari 8.0.4), Anda **wajib** update dulu ke 8.4.x sebelum lanjut ke versi 9. Jangan lompat langsung.
2. **Ruang disk cukup** — minimal 5 GB kosong di partisi root, idealnya 10 GB.
3. **Backup valid** — sekali lagi, backup dulu.
4. **Akses konsol yang stabil** — kalau lewat SSH, gunakan `tmux` atau `screen` agar proses tetap jalan meski koneksi putus. Kalau lewat Shell di web UI atau akses fisik/IPMI, ini opsional.

Catatan: kalau Anda pakai Ceph atau Proxmox Backup Server (PBS), ada langkah tambahan (Ceph harus di versi Squid, PBS harus di versi 4 dulu). Tutorial ini fokus pada setup homelab node tunggal tanpa Ceph/PBS, yang merupakan skenario paling umum.

## Langkah 1: Cek Kondisi Awal

Buka **Shell** dari node Anda (klik node → Shell), lalu cek versi dan ruang disk:

```bash
pveversion
df -h /
```

Di kasus saya, `pveversion` menampilkan `pve-manager/8.0.4`. Karena masih di bawah 8.4.1, saya harus update dulu.

## Langkah 2: Update Proxmox 8 ke Versi Terbaru (8.4.x)

Ini langkah wajib sebelum upgrade ke versi 9:

```bash
apt update && apt dist-upgrade
```

Setelah selesai, reboot lalu cek versinya lagi:

```bash
reboot
```

Setelah sistem naik kembali:

```bash
pveversion
```

Pastikan sekarang menampilkan **8.4.1 atau lebih baru**. Kalau sudah, kita bisa lanjut ke tahap berikutnya.

## Langkah 3: Jalankan Checklist Kesiapan `pve8to9`

Proxmox menyediakan tool bawaan untuk mengecek kesiapan sistem sebelum upgrade. **Ini langkah paling penting** — dia akan mendeteksi masalah yang harus diperbaiki dulu.

```bash
pve8to9 --full
```

Hasilnya berupa ringkasan seperti ini:

```
= SUMMARY =
TOTAL:    41
PASSED:   32
SKIPPED:  5
WARNINGS: 2
FAILURES: 0
```

Aturannya sederhana:

- **FAILURES harus 0.** Kalau ada FAIL, perbaiki dulu dan jalankan ulang. Jangan lanjut selama masih ada FAIL.
- **WARNINGS** boleh ada, tidak memblokir upgrade, tapi sebaiknya dibaca dan ditangani.
- **SKIPPED** artinya pemeriksaan dilewati karena tidak relevan (misalnya cek Ceph, padahal tidak pakai Ceph). Ini normal.

Di kasus saya ada 2 warning yang muncul. Mari kita tangani keduanya.

### Warning 1: Microcode CPU

```
WARN: The matching CPU microcode package 'intel-microcode' could not be found!
```

Ini artinya paket microcode CPU (tambalan keamanan level prosesor) belum terpasang. Paketnya ada di komponen `non-free-firmware` yang perlu diaktifkan dulu.

Cek dulu apakah komponen itu sudah aktif:

```bash
grep -r 'non-free-firmware' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Kalau kosong, edit `/etc/apt/sources.list`:

```bash
nano /etc/apt/sources.list
```

Tambahkan `non-free-firmware` di ujung baris repo Debian, sehingga menjadi seperti ini:

```
deb http://ftp.debian.org/debian bookworm main contrib non-free-firmware
deb http://ftp.debian.org/debian bookworm-updates main contrib non-free-firmware
deb http://security.debian.org bookworm-security main contrib non-free-firmware
```

Simpan (Ctrl+O, Enter, Ctrl+X), lalu pasang microcode-nya:

```bash
apt update && apt install intel-microcode
```

> Kalau CPU Anda AMD, paketnya bernama `amd64-microcode`.
>
> Alternatif: warning ini tidak wajib ditangani sebelum upgrade. Anda bisa melewatinya dan memasang microcode setelah sistem sudah di versi 9 (di Debian Trixie, komponen `non-free-firmware` biasanya sudah otomatis aktif). Tapi menyelesaikannya sekarang juga tidak masalah.
{: .prompt-info }

### Warning 2: systemd-boot Tidak Terpakai

```
WARN: systemd-boot package installed on legacy-boot system is not necessary, consider removing it
```

Ini **sebaiknya ditangani sebelum `dist-upgrade`**, karena paket `systemd-boot` ini punya bug yang dikenal di Debian Trixie dan bisa menghentikan proses upgrade di tengah jalan.

Hapus paketnya:

```bash
apt remove systemd-boot
```

**Perhatikan baik-baik daftar yang akan dihapus sebelum konfirmasi.** Yang boleh dihapus hanya `systemd-boot` saja. Jangan sampai ikut terhapus `systemd-boot-efi`, `systemd-boot-tools`, `proxmox-ve`, atau `grub`. Kalau daftarnya cuma `systemd-boot`, lanjutkan dengan `y`.

## Langkah 4: Ganti Repository ke Debian Trixie & Proxmox 9

Inti dari upgrade ini adalah mengganti sumber paket dari Debian 12 (bookworm) ke Debian 13 (trixie), dan dari repo Proxmox 8 ke Proxmox 9.

### 4a. Ganti repo Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
```

### 4b. Tambahkan repo Proxmox 9 (no-subscription, untuk homelab)

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

### 4c. Pastikan tidak ada repo lama yang menunjuk bookworm

Periksa semua file repo:

```bash
ls /etc/apt/sources.list.d/
grep -r 'bookworm\|trixie' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Pastikan **tidak ada baris `bookworm` yang masih aktif** (tanpa `#` di depannya). Biasanya file seperti `pve-enterprise.list` dan `ceph.list` sudah dalam keadaan dikomentari (`#`) secara default, jadi aman. Kalau ada yang masih aktif menunjuk bookworm, komentari atau ubah ke trixie.

> **Tips:** Kalau baris repo Proxmox muncul dua kali (di `sources.list` _dan_ di `proxmox.sources`), hapus yang di `sources.list` agar tidak duplikat:
> ```bash
> sed -i '/download.proxmox.com/d' /etc/apt/sources.list
> ```
{: .prompt-tip }

### 4d. Refresh daftar paket

```bash
apt update
```

Pastikan **tidak ada error merah**. Anda akan melihat repo `trixie` termuat semua, dan di akhir muncul pesan seperti `582 packages can be upgraded`. Angka ratusan paket ini normal — itulah paket yang akan di-upgrade ke Proxmox 9.

## Langkah 5: Jalankan Upgrade Utama (`dist-upgrade`)

Ini proses intinya:

```bash
apt dist-upgrade
```

Sistem akan menampilkan ringkasan (misalnya "582 upgraded, 158 newly installed, 59 to remove"). Selama tidak ada peringatan `proxmox-ve would be removed`, ketik `Y` untuk lanjut.

Proses ini memakan waktu 5–30 menit tergantung kecepatan disk. **Jangan diputus di tengah.** Selama proses, akan muncul beberapa layar dan prompt. Berikut cara menanganinya:

### Layar berita (apt-listchanges)

Kalau muncul layar informasi berwarna yang menampilkan catatan rilis (misalnya perubahan OpenSSH), dan di pojok kiri bawah ada tanda `:`, cukup tekan **`q`** untuk menutupnya dan melanjutkan. Ini cuma informasi, bukan pertanyaan.

### Prompt konfigurasi file

Ini bagian yang paling sering bikin bingung. Sistem akan bertanya apakah mau memakai file konfigurasi versi baru atau versi lama Anda. **Prinsipnya:** file yang tidak pernah Anda edit manual → pilih versi maintainer (baru); file yang pernah Anda ubah sendiri → pertahankan versi Anda.

Panduan cepat untuk file yang umum muncul:

| File                       | Pilihan                                            |
|----------------------------|----------------------------------------------------|
| `/etc/issue`               | **N** (keep) — hanya teks layar login, aman        |
| `/etc/lvm/lvm.conf`        | **Y** (install versi maintainer)                   |
| `/etc/ssh/sshd_config`     | **Y** kalau tak pernah diedit; **N** kalau pernah  |
| `/etc/default/grub`        | **N** kalau pernah diedit; **Y** kalau default     |
| `/etc/chrony/chrony.conf`  | **Y** kalau tak pernah diedit                      |

### Prompt "Restart services without asking?"

Akan muncul dialog biru menanyakan apakah layanan boleh di-restart otomatis tanpa bertanya setiap kali. **Pilih `<Yes>`.** Ini membuat proses berjalan mulus tanpa terus-terusan berhenti menanyakan setiap library. Gunakan panah/Tab untuk pindah ke `<Yes>`, lalu Enter.

### Error postfix (aman diabaikan)

Di akhir proses, Anda mungkin melihat error seperti ini:

```
Failed to restart postfix.service: Transaction contains conflicting jobs...
```

**Ini aman.** Postfix (server email lokal untuk notifikasi) hanya gagal _restart_ sementara, bukan rusak. Error ini akan hilang sendiri setelah reboot.

## Langkah 6: Reboot

Setelah `dist-upgrade` selesai dan prompt kembali ke `root@pve:~#`, reboot untuk masuk ke kernel Proxmox 9 yang baru:

```bash
reboot
```

Tunggu 1–2 menit sampai sistem naik kembali.

## Langkah 7: Verifikasi Hasil

Setelah reboot, sambungkan kembali dan verifikasi:

```bash
pveversion
uname -r
```

Kalau berhasil, Anda akan melihat output seperti ini:

```
pve-manager/9.2.6/7f8d010005bd72cb (running kernel: 7.0.14-8-pve)
7.0.14-8-pve
```

- `pve-manager/9.2.6` → Proxmox sudah di versi 9. ✅
- `running kernel: 7.0.14-8-pve` → sudah pakai kernel baru. ✅

Terakhir, buka web UI Proxmox di browser dan tekan **Ctrl+Shift+R** (hard refresh) agar tampilan baru versi 9 termuat dengan benar. Header di kiri atas seharusnya sekarang menampilkan **Virtual Environment 9.2.6**. Cek juga semua VM dan container Anda bisa start dan berjalan normal.

## Langkah 8: Bersih-Bersih (Opsional)

Hapus paket dan kernel lama yang sudah tidak terpakai untuk membebaskan ruang disk:

```bash
apt autoremove
```

Ini biasanya akan menawarkan menghapus kernel lama (misalnya kernel 6.2.x dari era Proxmox 8 awal). **Aman dihapus** selama Anda masih punya kernel baru yang berfungsi. Sistem otomatis me-regenerate konfigurasi GRUB setelahnya, dan Anda tetap punya beberapa kernel cadangan di menu boot.

## Ringkasan Semua Perintah

```bash
# 1. Cek kondisi awal
pveversion
df -h /

# 2. Update ke 8.4.x terbaru
apt update && apt dist-upgrade
reboot
pveversion          # pastikan 8.4.1+

# 3. Checklist kesiapan
pve8to9 --full      # bereskan semua FAIL

# 4. Tangani warning (contoh)
apt install intel-microcode   # setelah aktifkan non-free-firmware
apt remove systemd-boot       # cek daftarnya dulu!

# 5. Ganti repository
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list

cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF

grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/   # pastikan bersih

# 6. Upgrade utama
apt update
apt dist-upgrade
reboot

# 7. Verifikasi
pveversion          # harus 9.x
uname -r            # harus kernel baru

# 8. Bersih-bersih
apt autoremove
```

## Troubleshooting Umum

**"proxmox-ve would be removed"** — masih ada repo bookworm yang aktif. Cari dan komentari:
```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

**systemd-boot menghentikan upgrade** — hapus meta-package-nya (bukan yang -efi/-tools):
```bash
apt remove systemd-boot
```

**LVM thin pool minta repair:**
```bash
lvconvert --repair pve/data
```

**PCI passthrough bermasalah dengan kernel baru** — sematkan kernel lama sementara:
```bash
proxmox-boot-tool kernel pin 6.8.12-39-pve
```

## Penutup

Selesai! Server Anda sekarang berjalan di Proxmox VE 9 dengan Debian 13. Prosesnya mungkin terlihat panjang, tapi sebenarnya inti alurnya sederhana: **update ke 8.4.x dulu → jalankan `pve8to9` dan bereskan semua FAIL → ganti repo bookworm ke trixie → `dist-upgrade` → reboot.**

Kunci upgrade yang mulus ada di persiapan: backup dulu, jalankan checker, dan tangani setiap warning. Lakukan itu, dan Anda akan menikmati semua fitur baru Proxmox 9 tanpa drama.

Semoga bermanfaat. Kalau ada pertanyaan, silakan tinggalkan komentar di bawah.

---

*Referensi: [Dokumentasi resmi Proxmox — Upgrade from 8 to 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)*
