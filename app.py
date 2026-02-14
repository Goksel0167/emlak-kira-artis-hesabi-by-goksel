import streamlit as st
import urllib.parse

# --- KONFİGÜRASYON ---
st.set_page_config(page_title="Emlak Kira Artış Hesabı by Goksel", page_icon="🏠")

# --- GÜNCEL VERİ TABANI ---
# 2024 Haziran ve öncesi yasal %25 sınırına sabitlenmiştir.
# Sonrası paylaştığın tablolardaki tam değerlerdir.
VERI_TABANI = {
    "2024": {
        "Ocak": 25.0, "Şubat": 25.0, "Mart": 25.0, "Nisan": 25.0, "Mayıs": 25.0, "Haziran": 25.0,
        "Temmuz": 65.07, "Ağustos": 65.93, "Eylül": 64.91, "Ekim": 63.47, "Kasım": 62.02, "Aralık": 60.45
    },
    "2025": {
        "Ocak": 58.51, "Şubat": 56.35, "Mart": 53.83, "Nisan": 51.26, "Mayıs": 48.73, "Haziran": 45.80,
        "Temmuz": 43.23, "Ağustos": 41.13, "Eylül": 39.62, "Ekim": 38.36, "Kasım": 37.15, "Aralık": 35.91
    },
    "2026": {
        "Ocak": 34.88, "Şubat": 33.98  # Görseldeki tam veri %33,98 olarak güncellendi
    }
}

# --- ARAYÜZ ---
st.title("🏠 Emlak Kira Artış Hesabı")
st.markdown("### Resmi TÜFE Verileri ile Kira Hesaplama")

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        secilen_yil = st.selectbox("Kira Artış Yılı:", ["2026", "2025", "2024"])
    with col2:
        aylar = list(VERI_TABANI[secilen_yil].keys())
        secilen_ay = st.selectbox("Kira Artış Ayı:", aylar)

    mevcut_kira = st.number_input("Mevcut Kira Bedeli (TL):", min_value=1000, value=15000, step=500)

    # Veriyi Çekme
    oran = VERI_TABANI[secilen_yil][secilen_ay]
    
    if st.button("HESAPLA"):
        yeni_kira = mevcut_kira * (1 + oran / 100)
        
        st.divider()
        st.subheader("📊 Hesaplama Sonucu")
        st.info(f"📅 **{secilen_ay} {secilen_yil}** dönemi yıllık TÜFE oranı: **%{oran}**")
        
        st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; text-align: center;">
                <p style="margin:0; font-size:18px;">Yeni Kira Bedeli</p>
                <b style="font-size:32px; color:#2e7d32;">{yeni_kira:,.2f} TL</b>
            </div>
        """, unsafe_allow_html=True)

        # --- WHATSAPP MESAJI (İSTEDİĞİN TAM FORMAT) ---
        taslak_mesaj = f"Sayın ev sahibim, TÜİK verilerine göre yıllık TÜFE kira artışım %{oran}'dir. Yeni kiram {yeni_kira:,.2f} TL'dir."
        encoded_mesaj = urllib.parse.quote(taslak_mesaj)
        whatsapp_url = f"https://wa.me/?text={encoded_mesaj}"

        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 20px; margin-top: 25px;">
                    🟢 WhatsApp ile Ev Sahibine Gönder
                </div>
            </a>
        """, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Emlak Kira Artış Hesabı by Goksel | Veriler paylaşılan resmi bülten görseline dayanmaktadır.")
