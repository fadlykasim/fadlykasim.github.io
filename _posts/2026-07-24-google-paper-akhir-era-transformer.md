---
layout: post
title:  "Google Merilis Paper yang Katanya Mengakhiri Era Transformer — Benarkah?"
date:   2026-07-24 15:00:00 +0800
categories: [teknologi, ai]
tags: [google, transformer, rnn, machine-learning, paper]
description: >-
  Sebuah paper Google, "Memory Caching: RNNs with Growing Memory", viral
  disebut bakal mengakhiri era Transformer. Saya baca jurnalnya langsung —
  ini mana yang benar dan mana yang lebay.
---

Beberapa hari ini timeline saya rame satu narasi: *"Google baru saja merilis paper yang bisa mengakhiri era Transformer."* Katanya, selama 7 tahun semua AI besar — ChatGPT, Claude, Gemini — dibangun di atas arsitektur yang sama, Transformer, dan sekarang ada penggantinya.

Karena penasaran, saya tidak baca thread-nya doang — saya unduh dan baca jurnalnya langsung: **"Memory Caching: RNNs with Growing Memory"** (Behrouz dkk., Google Research / Cornell / USC, Feb 2026). Mari kita bedah: mana yang benar, mana yang lebay.

## Masalahnya memang nyata

Ini bagian yang benar dari narasi viral itu, dan penting dipahami dulu:

- **Transformer** jago mengingat konteks panjang, tapi harus membandingkan setiap kata dengan setiap kata lain. Namanya *quadratic complexity* — `O(L²)`. Makin panjang prompt, biaya komputasi meledak.
- **RNN** (Recurrent Neural Network) itu murah dan cepat — `O(L)` — tapi memorinya **ukuran tetap**. Kasih dokumen panjang, dia "amnesia": informasi lama ketimpa yang baru.

Jadi selama ini kita seolah dipaksa pilih: murah tapi pelupa, atau pintar tapi mahal.

## Ide intinya: tombol "save" buat RNN

Analogi yang saya suka dari paper ini: alih-alih RNN punya memori tetap yang terus menimpa dirinya sendiri, Google memberinya **tombol save**.

Teknik **Memory Caching (MC)** memotong urutan input jadi beberapa segmen, lalu **menyimpan snapshot (checkpoint) dari state memori tiap segmen**. Saat menjawab, model tidak cuma baca memori aktif, tapi juga sekumpulan memori lama yang sudah di-cache. Hasilnya: **kapasitas memori RNN bisa tumbuh** seiring panjang teks.

Yang menarik, biayanya bukan `O(L)` dan bukan `O(L²)`, tapi **`O(NL)` — sebuah dial yang bisa diatur**:

```text
N = 1   ->  jadi RNN biasa      (O(L),  memori tetap)
N = L   ->  mirip Transformer   (O(L²), akses ke tiap token)
1 < N < L  ->  jalan tengah, bisa kamu setel
```

Mereka bikin **empat varian**, termasuk **Sparse Selective Caching (SSC)** — pakai *router* gaya Mixture-of-Experts yang secara aktif memilih checkpoint mana yang paling relevan. Jadi AI-nya benar-benar milih "ingatan mana yang penting" buat pertanyaan saat ini.

## Hasilnya bagus — tapi baca angkanya baik-baik

Ini dari tabel di jurnalnya (model 760M–1.3B parameter, dilatih 30B–100B token):

- Di tugas **long-context** dan **recall-intensif**, varian Memory Caching **menutup jarak** ke Transformer.
- MC secara konsisten **mengalahkan RNN state-of-the-art** lain.
- Di **Needle-in-a-Haystack** konteks 16K, RNN polos anjlok, sedangkan varian MC bertahan tinggi.

Semua itu dicapai **tanpa biaya kuadratik penuh** ala Transformer. Sejauh ini, keren.

## Nah, ini bagian yang lebay

Setelah baca, klaim "mengakhiri era Transformer" itu clickbait berjas lab. Beberapa catatan jujur:

1. **Papernya sendiri bilang sebaliknya.** Teksnya jelas: *Transformer masih mencapai akurasi terbaik* di tugas recall. MC **mempersempit** jarak, bukan menghapusnya. Mempersempit gap ≠ mengakhiri era.
2. **"Tanpa biaya kuadratik" itu pakai tanda bintang.** `O(NL)` itu dial, bukan gratis. Kalau resolusinya dinaikkan (`N → L`), kamu balik mendekati `O(L²)`. Ini tombol antara RNN dan Transformer, bukan cara dapat kualitas Transformer di harga RNN.
3. **Skalanya masih kecil.** 760M–1.3B parameter. Belum ada bukti ini bertahan di skala frontier seperti Gemini atau GPT.
4. **MC ini ditempel ke RNN yang sudah ada** (Linear Attention, Titans, Sliding Window). Bahkan papernya menunjukkan **attention itu kasus khusus dari memory caching** — jadi ini menggeneralisasi Transformer, bukan membunuhnya.

## Yang saya bawa pulang

> Memory Caching adalah cara cerdas dan bisa-disetel untuk memberi RNN efisien sebuah memori yang *tumbuh*. Progres nyata di trade-off efisiensi vs konteks panjang, dan ia mengalahkan RNN lain. Tapi ia **mempersempit** jarak ke Transformer, bukan menghapusnya — dan masih tahap awal di skala kecil.

Buat saya yang suka ngoprek, ini riset yang layak diikuti. Tapi kalau ada yang bilang "Transformer sudah mati" — santai. Yang sebenarnya terjadi lebih halus, dan justru lebih menarik: kita mungkin memang tidak perlu memproses seluruh riwayat setiap saat. Kita cuma butuh cache yang lebih pintar.

---

Sumber: [Memory Caching: RNNs with Growing Memory (arXiv 2602.24281)](https://arxiv.org/abs/2602.24281), Behrouz dkk., Google Research.
