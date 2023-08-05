# PDF TO SPEECH

#### Description: Web ini dibuat menggunakan Flask, yang memungkinkan pengguna mengunggah file PDF, memilih kata untuk diterjemahkan, dan mengeluarkan audio.


### Feature :
1. *Upload* : Fitur unggah memungkinkan pengguna untuk mengunggah file PDF ke dalam aplikasi. Setelah file PDF diunggah, pengguna dapat melihat isi file tersebut dan menggunakan fitur lain yang tersedia di web, seperti fitur Terjemahan dan Audio.

2. *Translate* : Fitur Terjemahkan memungkinkan pengguna menerjemahkan teks yang dipilih dari bahasa asli ke bahasa yang diinginkan. Fitur ini sangat berguna bagi pengguna yang ingin memahami isi dokumen dalam bahasa yang tidak mereka kuasai.

3. *Audio* : Fitur audio memungkinkan pengguna untuk mendengarkan teks yang dipilih dalam bentuk audio. Fitur ini sangat berguna bagi pengguna yang ingin mendengarkan isi dokumen tanpa harus membaca teksnya secara langsung.


### Programming language :
1. *python*
2. *Javascript*

### library dan framework Python :

1. *Flask* :  digunakan untuk membangun aplikasi web dengan python.
Cara install : `pip install flask`.

3. *pymupdf*: digunakan untuk membaca dan mengkonversi file PDF ke dalam format HTML, sehingga konten dari file PDF dapat diakses oleh javascript dan ditampilkan ke dalam web.
Cara install:  `pip install pymupdf`.

3. *googletrans*: digunakan untuk menerjemahkan teks yang dipilih pengguna ke bahasa yang diinginkan. Library ini menghubungkan aplikasi dengan layanan Google Translate.
Cara install : `pip install googletrans`.

4. *gtts*: digunakan untuk mengkonversi teks ke dalam format audio. Library ini menghubungkan aplikasi dengan layanan Google Text-to-Speech.
Cara install: `pip install gtts`.


### Library and framework on the frontend :
1. *CSS Bootstrap* : to design web pages.
2. *Ajax* : send request to flask and receive response.



### How to run:
1. Make sure to install all the required frameworks and libraries.
2. Run in terminal : `flask run`.