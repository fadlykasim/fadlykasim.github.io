---
layout: post
title:  "Apple Container Tembus v1.0.0 — dan Blog Ini Kebetulan Jalan di Atasnya"
date:   2026-07-24 09:00:00 +0800
categories: [teknologi, container]
tags: [apple, container, macos, docker, devops]
description: >-
  Apple merilis versi stabil pertama tool `container`-nya. Saya bedah apa yang
  berubah, arsitektur "satu VM per container", dan kenapa ini bukan pengganti
  Docker Desktop.
---

Beberapa waktu lalu saya nulis post "Hello dari Makassar" — post pertama blog ini yang saya build pakai `container` CLI dari Apple. Waktu itu tool-nya masih terasa eksperimen. Sekarang statusnya berubah: per 9 Juni 2026 kemarin, Apple akhirnya melepas **`container` versi 1.0.0**, rilis stabil mayor pertamanya. Jadi kebetulan blog yang lagi kamu baca ini memang jalan di atas barang yang mau saya ceritain. Mari kita bedah.

## Apa itu `container`?

Singkatnya: tool command-line untuk menjalankan **container Linux sebagai virtual machine ringan** di macOS. Ditulis pakai Swift, dioptimalkan buat Apple silicon, dan kompatibel dengan image OCI standar — artinya bisa `pull` dan `push` ke registry biasa layaknya Docker.

Kalau kamu sudah biasa Docker, CLI-nya bakal terasa familiar:

```bash
# jalanin container
container run --rm -it ubuntu:24.04 bash

# build image dari Dockerfile
container build -t blog-jekyll .

# pull image dari registry
container image pull nginx:latest
```

Nyaris tidak ada yang perlu dihafal ulang. Ini bagian yang bikin transisinya mulus.

## Yang bikin beda: satu VM per container

Nah ini poin arsitektur yang menurut saya paling penting dipahami.

Docker Desktop menjalankan semua container kamu di dalam **satu Linux VM bersama**. Sedangkan Apple `container` menaruh **setiap container di dalam VM ringannya sendiri-sendiri**. Konsekuensinya:

- Isolasi lebih kuat — tiap container punya jatah resource dan **IP address sendiri**.
- Lebih aman buat menjalankan kode yang belum kamu percaya, karena batasnya di level VM, bukan cuma namespace.
- Trade-off-nya: overhead per container sedikit lebih berat dibanding model VM bersama.

## `container machine` — fitur yang paling menarik

Selain container sekali pakai, ada `container machine`. Ini bikin **environment Linux yang persisten** — bukan container yang sekali mati langsung hilang. Yang bikin saya suka:

- Home directory di Mac otomatis di-share ke dalam.
- Alur kerja "edit di Mac, build di dalam Linux" jadi natural.
- Bisa jalanin service pakai `systemctl` — misalnya PostgreSQL nyala terus di dalam mesin.

Buat saya yang sering butuh Linux beneran tapi malas dual-boot, ini semacam WSL versi Mac. Ditambah dukungan volume mount, konfigurasi memory/CPU, port publishing, kompatibilitas Rosetta, dan SSH agent forwarding.

## Tapi jangan buru-buru buang Docker

Biar jujur, ada beberapa lubang yang perlu kamu tahu sebelum pindah total:

- **Belum ada Docker Compose.** Kalau workflow kamu berat di `docker compose`, kamu bakal ketergantungan bridge pihak ketiga seperti `container-compose`. Belum se-mulus itu.
- **Tidak ada kompatibilitas Docker socket.** Apple malah menutup issue GitHub yang minta expose Docker Engine API. Jadi tool yang ngarep `/var/run/docker.sock` bakal ngambek.
- **Syarat OS lumayan tinggi.** Butuh Apple silicon, macOS 15+, dan pengalaman paling enak di macOS 26+. Di versi lama, fitur network isolation-nya terbatas.

## Jadi, buat siapa?

Dari pemakaian saya sejauh ini, `container` paling pas untuk:

1. **Container tunggal** buat eksperimen cepat atau nyoba-nyoba.
2. **Development Linux native di Mac** — ini use case favorit saya, dan alasan blog ini bisa jalan di atasnya.
3. **Sandboxing kode yang belum dipercaya**, memanfaatkan isolasi level-VM.

Kalau tim kamu hidup di Compose, Kubernetes, atau butuh kompatibilitas ekosistem Docker seutuhnya — Docker Desktop masih raja. Apple `container` bukan berusaha jadi pengganti drop-in; ia main di ranah **integrasi platform dan isolasi**.

Buat saya pribadi? v1.0.0 ini cukup meyakinkan untuk saya lanjut pakai buat proyek-proyek kecil. Termasuk blog ini. 🚀

---

Referensi: [Apple's container just hit v1.0.0](https://dev.to/trknhr/apples-container-just-hit-v100-mid) dan [repo resmi apple/container di GitHub](https://github.com/apple/container).
