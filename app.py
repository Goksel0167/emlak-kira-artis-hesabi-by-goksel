import streamlit as st
import urllib.parse

# --- KONFİGÜRASYON ---
st.set_page_config(page_title="Emlak Kira Artış Hesabı by Goksel", page_icon="🏠")

# --- GÜNCEL VERİ TABANI (GÖRSELLERİNE GÖRE) ---
VERI_TABANI = {
    "2026": {"Şubat": 33.98, "Ocak": 34.88},
    "2025": {
        "Aralık": 35.91, "Kasım": 37.15, "Ekim": 38.36, "Eylül": 39.62, "Ağustos": 41.13, "Temmuz": 43.23,
        "Haziran": 45.80, "Mayıs": 48.73, "Nisan": 51.26, "Mart": 53.83, "Şubat": 56.35, "Ocak": 58.51
    },
    "2024": {
        "Aralık": 60.45, "Kasım": 62.02, "Ekim": 63.47, "Eylül": 64.91, "Ağustos": 65.93, "Temmuz": 65.07,
        "Haziran": 25.0, "Mayıs": 25.0, "Nisan": 25.0, "Mart": 25.0, "Şubat": 25.0, "Ocak": 25.0
    }
}

st.title("🏠 Emlak Kira Artış Hesabı")
st.markdown("### Resmi TÜFE Verileri ile Çift Taraflı Hesaplama")

# --- HESAPLAMA ALANI ---
with st.container():
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        yil = st.selectbox("Yıl Seçiniz:", ["2026", "2025", "2024"])
    with c2:
        ay = st.selectbox("Ay Seçiniz:", list(VERI_TABANI[yil].keys()))

    kira = st.number_input("Mevcut Kira Bedeli (TL):", min_value=1000, value=15000, step=500)
    oran = VERI_TABANI[yil][ay]

    if st.button("HESAPLA"):
        yeni_kira = kira * (1 + oran / 100)
        
        st.divider()
        st.info(f"📅 **{ay} {yil}** dönemi yıllık TÜFE oranı: **%{oran}**")
        st.success(f"### Yeni Kira Bedeli: {yeni_kira:,.2f} TL")

        st.write("### 📲 WhatsApp Mesaj Seçeneği")
        st.write("Gönderen kişinin rolüne göre mesajı seçiniz:")

        # --- MESAJ TASLAKLARI ---
        msj_kiraci = f"Sayın ev sahibim, TÜİK verilerine göre yıllık TÜFE kira artışım %{oran}'dir. Yeni kiram {yeni_kira:,.2f} TL'dir."
        msj_evsahibi = f"Merhaba, TÜİK tarafından açıklanan resmi yıllık TÜFE oranı %{oran} olarak belirlenmiştir. Bu doğrultuda yeni dönem kira bedelimiz {yeni_kira:,.2f} TL olmuştur. Bilgilerinize sunarım."

        col_k, col_e = st.columns(2)

        with col_k:
            url_k = f"https://wa.me/?text={urllib.parse.quote(msj_kiraci)}"
            st.markdown(f'<a href="{url_k}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366;color:white;padding:12px;border-radius:10px;text-align:center;font-weight:bold;">🙋‍♂️ Kiracı Mesajı</div></a>', unsafe_allow_html=True)
            st.caption(f"Önizleme: {msj_kiraci}")

        with col_e:
            url_e = f"https://wa.me/?text={urllib.parse.quote(msj_evsahibi)}"
            st.markdown(f'<a href="{url_e}" target="_blank" style="text-decoration:none;"><div style="background-color:#128C7E;color:white;padding:12px;border-radius:10px;text-align:center;font-weight:bold;">🏡 Ev Sahibi Mesajı</div></a>', unsafe_allow_html=True)
            st.caption(f"Önizleme: {msj_evsahibi}")

st.divider()
st.caption("© 2026 Emlak Kira Artış Hesabı by Goksel | Veriler resmi TÜİK bültenlerine dayanır.")
