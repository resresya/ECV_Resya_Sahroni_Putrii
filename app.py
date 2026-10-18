import streamlit as st
from pathlib import Path
import html

st.set_page_config(page_title="Resya Sahroni Putri | E-CV", page_icon="✳️", layout="wide")

# ===================== EDIT DATA HERE =====================
PROFILE = {
    "name": "Resya Sahroni Putri",
    "role": "Mahasiswa S1 Sistem Informasi",
    "university": "Universitas Bina Sarana Informatika Yogyakarta",
    "email": "@resyaputri889@gmail.com",  # Ganti dengan emailmu
    "whatsapp": "0895392711467",  # Opsional: https://wa.me/628xxxxxxxxxx
    "about": (
        "Mahasiswa Program Studi Sistem Informasi Universitas Bina Sarana Informatika Yogyakarta "
        "yang memiliki minat pada pengembangan sistem informasi, basis data, dan teknologi digital. "
        "Pernah mengikuti Praktik Kerja Lapangan di bidang fotografi serta aktif sebagai Staf Publikasi "
        "dan Dokumentasi (PDD) Himpunan Mahasiswa Sistem Informasi. Terus mengembangkan kompetensi "
        "melalui proyek, seminar, dan sertifikasi."
    ),
    "ipk": "3,96",
    "ipk_url": "",  # Tempel link Google Drive untuk bukti IPK/transkrip kumulatif di sini
}
# Isi setiap "url" dengan link Google Drive KHS semester terkait.
# Contoh: "url": "https://drive.google.com/file/d/ID_FILE/view"
SEMESTERS = [
    {"name": "Semester 1", "ip": "4,00", "url": ""},
    {"name": "Semester 2", "ip": "3,84", "url": ""},
    {"name": "Semester 3", "ip": "4,00", "url": ""},
    {"name": "Semester 4", "ip": "4,00", "url": ""},
]
HARD_SKILLS = ["HTML", "CSS", "PHP", "SQL", "MySQL / MariaDB", "Database Design", "Figma", "Microsoft Office", "Visual Studio Code"]
SOFT_SKILLS = ["Komunikasi", "Kerja Sama Tim", "Problem Solving", "Disiplin", "Cepat Belajar", "Bertanggung Jawab"]
EXPERIENCES = [
    ("Praktik Kerja Lapangan", "KOI Photography", [
        "Melayani pelanggan selama sesi pemotretan.",
        "Berkomunikasi dengan klien untuk memahami kebutuhan.",
        "Membantu proses dokumentasi dan pengelolaan hasil foto.",
        "Bekerja sama dengan tim selama kegiatan."
    ]),
    ("Staf Publikasi dan Dokumentasi (PDD)", "Himpunan Mahasiswa Sistem Informasi", [
        "Mendokumentasikan kegiatan organisasi.",
        "Membantu pembuatan materi publikasi.",
        "Berkolaborasi dalam pelaksanaan kegiatan mahasiswa."
    ])
]
PROJECTS = [
    ("Digitalisasi Pendaftaran Pasien pada Klinik untuk Meningkatkan Efektivitas Layanan Berbasis Web dengan Metode RAD",
     "Rapid Application Development (RAD)", [
         "Analisis kebutuhan sistem.", "Perancangan basis data dan antarmuka pengguna.",
         "Pengembangan sistem pendaftaran pasien berbasis web."
     ]),
    ("Sistem Informasi Manajemen Penjualan Toko Sayur Berbasis Web Menggunakan Metode Design Thinking",
     "Design Thinking", [
         "Analisis kebutuhan pengguna.", "Perancangan sistem informasi.",
         "Perancangan solusi untuk mendukung pengelolaan penjualan."
     ])
]
# Isi kolom ketiga (url) dengan link Google Drive sertifikat masing-masing.
# Contoh: ("Database Administrator – BNSP", "Sertifikasi Kompetensi", "https://drive.google.com/file/d/ID_FILE/view")
CERTIFICATES = [
    ("Database Administrator – BNSP", "Sertifikasi Kompetensi", ""),
    ("Uji Kompetensi Berbasis Industri Bidang Basis Data", "Sertifikasi Kompetensi", ""),
    ("Software Quality Assurance", "Sertifikasi Kompetensi", ""),
    ("Seminar Wajib Entrepreneur", "Seminar", ""),
    ("Seminar Sosial Pencegahan Intoleransi, Radikalisme, dan Terorisme di Lingkungan Kampus", "Seminar", ""),
    ("Akselerasi Transformasi Digital Mendukung Ekonomi Kreatif Melalui Talenta Digital", "Seminar", ""),
    ("Webinar Edukasi & Inklusi Pasar Modal", "Webinar", ""),
    ("Panitia Workshop Pemanfaatan Artificial Intelligence (AI)", "Kepanitiaan", ""),
]
PDF_PATH = Path(__file__).parent / "CV_Resya_Sahroni_Putri.pdf"
PHOTO_PATH = Path(__file__).parent / "profile.jpg"

# ===================== CREATIVE WARM THEME =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap');
:root { --cream:#fff5f2; --paper:#fffdfb; --ink:#493238; --terra:#d77f83; --rose:#f6cbd0; --sage:#c9858c; --mauve:#e7a6aa; --line:#f0d6d5; }
html, body, [class*="css"] {font-family:'DM Sans',sans-serif;}
.stApp {background:var(--cream); color:var(--ink);}
.block-container {max-width:1120px;padding-top:1.4rem;padding-bottom:4rem;}
header[data-testid="stHeader"] {background:rgba(255,245,242,.9);}
h1,h2,h3 {color:var(--ink);}
.hero {background:var(--paper);border:1px solid var(--line);border-radius:28px;padding:2.8rem 2.5rem;margin:.5rem 0 1.4rem;position:relative;overflow:hidden;}
.hero:after {content:"✳";position:absolute;right:2rem;top:-2.5rem;font-size:12rem;color:#f2c6c744;line-height:1;}
.kicker {color:var(--terra);font-weight:800;text-transform:uppercase;letter-spacing:3px;font-size:.75rem;}
.hero-name {font-family:'Playfair Display',serif;font-size:clamp(2.5rem,6vw,4.6rem);line-height:1.03;color:var(--ink);font-weight:800;max-width:780px;margin:.7rem 0;}
.hero-role {font-size:1.15rem;font-weight:700;color:var(--sage);}
.hero-sub {color:#8a6d70;margin-top:.4rem;max-width:700px;}
.hero-mark {display:inline-block;background:var(--terra);color:#fffaf2;border-radius:999px;padding:.55rem 1rem;font-weight:700;margin-top:1.2rem;}
.section-heading {font-family:'Playfair Display',serif;font-size:2rem;font-weight:800;color:var(--ink);margin:2.4rem 0 1rem;}
.section-note {color:#9a777a;font-size:.92rem;margin-top:-.7rem;margin-bottom:1rem;}
.paper-card {background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:1.25rem 1.35rem;margin-bottom:.8rem;height:100%;box-shadow:0 8px 24px #b96c7210;}
.paper-card h3 {font-family:'Playfair Display',serif;color:var(--terra);font-size:1.17rem;line-height:1.35;margin:.15rem 0 .45rem;}
.eyebrow {font-size:.75rem;text-transform:uppercase;letter-spacing:1.5px;font-weight:800;color:var(--sage);}
.ipk-card {background:var(--sage);color:#fffaf2;border-radius:22px;padding:1.4rem 1.5rem;margin-bottom:1rem;}
.ipk-card .number {font-family:'Playfair Display',serif;font-size:3rem;font-weight:800;line-height:1.1;}
.ipk-card .small {color:#f8f1ff;}
.semester {background:#fff0e8;border:1px solid #f2d4cb;border-radius:18px;padding:1rem;text-align:center;margin-bottom:.5rem;}
.semester .value {font-family:'Playfair Display',serif;font-size:2rem;color:var(--terra);font-weight:800;}
.chip {display:inline-block;padding:.42rem .75rem;margin:.22rem .2rem .1rem 0;border-radius:999px;background:#fbe2e3;color:#8b4f58;border:1px solid #f0c5ca;font-size:.83rem;font-weight:600;}
.stButton>button,.stLinkButton>a,.stDownloadButton>button {background:var(--terra)!important;color:#fffaf2!important;border:0!important;border-radius:999px!important;font-weight:700!important;padding:.55rem 1.15rem!important;}
.stButton>button:hover,.stLinkButton>a:hover,.stDownloadButton>button:hover {background:#bd626c!important;color:white!important;}
a {color:var(--terra)!important;}
hr {border-color:var(--line)!important;}
.footer {border-top:1px solid var(--line);margin-top:3rem;padding-top:1.4rem;text-align:center;color:#8a7d98;font-size:.85rem;}
div[data-testid="stAlert"] {background:#fff0ed;border:1px solid var(--line);color:var(--ink);}
@media(max-width:700px){.hero{padding:1.7rem 1.25rem}.hero:after{right:-1rem;top:-1rem;font-size:7rem}.section-heading{font-size:1.7rem}}
</style>
""", unsafe_allow_html=True)

def safe(text):
    return html.escape(str(text))

def heading(title, note=""):
    st.markdown(f'<div class="section-heading">{title}</div>', unsafe_allow_html=True)
    if note:
        st.markdown(f'<div class="section-note">{note}</div>', unsafe_allow_html=True)

# HERO
st.markdown(f"""
<div class="hero">
  <div class="kicker">✳ Digital Curriculum Vitae</div>
  <div class="hero-name">{safe(PROFILE['name'])}</div>
  <div class="hero-role">{safe(PROFILE['role'])}</div>
  <div class="hero-sub">{safe(PROFILE['university'])}</div>
  <div class="hero-mark">Belajar · Berkembang · Berkarya</div>
</div>
""", unsafe_allow_html=True)
left, right = st.columns([1, 2], gap="large")
with left:
    if PHOTO_PATH.exists():
        st.image(str(PHOTO_PATH), use_container_width=True)
    else:
        st.markdown('<div class="paper-card" style="text-align:center;padding:2rem 1rem;"><div style="font-size:4rem;">✿</div><div class="eyebrow">Tambahkan foto</div><p style="color:#9a777a;">Unggah foto sebagai <b>profile.jpg</b> ke repository agar tampil di sini.</p></div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="ipk-card"><div class="small">IPK Kumulatif</div><div class="number">3,96 <span style="font-size:1rem;">/ 4,00</span></div><div class="small">S1 Sistem Informasi · Semester 1–4</div></div>', unsafe_allow_html=True)
    if PROFILE["ipk_url"].strip():
        st.link_button("Lihat Bukti IPK ↗", PROFILE["ipk_url"], use_container_width=True)
    if PDF_PATH.exists():
        st.download_button("↓  Download CV (PDF)", data=PDF_PATH.read_bytes(), file_name="CV_Resya_Sahroni_Putri.pdf", mime="application/pdf")
    else:
        st.info("Tambahkan file `CV_Resya_Sahroni_Putri.pdf` ke repository untuk mengaktifkan tombol unduh.")

heading("01 / Tentang Saya", "Sekilas tentang minat dan perjalanan saya.")
st.markdown(f'<div class="paper-card">{safe(PROFILE["about"])}</div>', unsafe_allow_html=True)

heading("02 / Pendidikan", "Perjalanan akademik dan capaian setiap semester.")
st.markdown('<div class="paper-card"><div class="eyebrow">Pendidikan Tinggi</div><h3>Universitas Bina Sarana Informatika Yogyakarta</h3><b>S1 Sistem Informasi</b><div style="color:#9a777a;">2024 – Sekarang</div></div>', unsafe_allow_html=True)
cols = st.columns(4)
for col, sem in zip(cols, SEMESTERS):
    with col:
        st.markdown(f'<div class="semester"><div class="eyebrow">{safe(sem["name"])}</div><div class="value">{safe(sem["ip"])}</div></div>', unsafe_allow_html=True)
        if sem["url"].strip():
            st.link_button("Lihat KHS ↗", sem["url"], use_container_width=True)
st.markdown('<div class="paper-card"><h3>SMK Negeri 1 Pengasih</h3>Jurusan Multimedia <span style="color:#9a777a;">· Lulus 2024</span></div>', unsafe_allow_html=True)

heading("03 / Keahlian", "Perangkat dan kemampuan yang mendukung pekerjaan.")
c1,c2=st.columns(2,gap="medium")
with c1:
    st.markdown('<div class="paper-card"><div class="eyebrow">01 — Technical</div><h3>Hard Skill</h3>'+''.join(f'<span class="chip">{safe(x)}</span>' for x in HARD_SKILLS)+'</div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="paper-card"><div class="eyebrow">02 — Personal</div><h3>Soft Skill</h3>'+''.join(f'<span class="chip">{safe(x)}</span>' for x in SOFT_SKILLS)+'</div>',unsafe_allow_html=True)

heading("04 / Pengalaman", "Pengalaman praktik dan kontribusi organisasi.")
for title, place, items in EXPERIENCES:
    st.markdown(f'<div class="paper-card"><div class="eyebrow">{safe(place)}</div><h3>{safe(title)}</h3><ul>'+''.join(f'<li>{safe(x)}</li>' for x in items)+'</ul></div>',unsafe_allow_html=True)

heading("05 / Proyek Pilihan", "Proyek akademik yang pernah dikerjakan.")
for i,(title,method,items) in enumerate(PROJECTS,1):
    st.markdown(f'<div class="paper-card"><div class="eyebrow">PROJECT 0{i}</div><h3>{safe(title)}</h3><p style="color:#78866b;font-weight:700;">Metode: {safe(method)}</p><ul>'+''.join(f'<li>{safe(x)}</li>' for x in items)+'</ul></div>',unsafe_allow_html=True)

heading("06 / Sertifikasi & Kegiatan", "Sertifikat kompetensi, seminar, webinar, dan kepanitiaan.")
for title, category, url in CERTIFICATES:
    col1,col2=st.columns([4,1],vertical_alignment="center")
    with col1:
        st.markdown(f'<div class="paper-card"><div class="eyebrow">{safe(category)}</div><h3>{safe(title)}</h3></div>',unsafe_allow_html=True)
    with col2:
        if url.strip():
            st.link_button("Lihat ↗",url,use_container_width=True)

heading("07 / Kontak", "Terbuka untuk terhubung dan berkolaborasi.")
st.markdown(f'<div class="paper-card"><div class="eyebrow">Email</div><h3>{safe(PROFILE["email"])}</h3></div>',unsafe_allow_html=True)
if PROFILE["whatsapp"].strip():
    st.link_button("Hubungi via WhatsApp ↗",PROFILE["whatsapp"])

st.markdown('<div class="footer">Dibuat dengan teliti · E-CV Resya Sahroni Putri · Warm editorial palette</div>',unsafe_allow_html=True)
