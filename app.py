import streamlit as st
import pandas as pd
import urllib.parse

# --- KONFİGÜRASYON ---
st.set_page_config(page_title="Emlak Vizyoner | Kira Portalı", page_icon="🏠")

# --- VERİ SETİ (ŞUBAT 2026) ---
GUNCEL_ORAN = 33.88
GUNCEL_AY = "Şubat 2026"

# --- ARAYÜZ ---
st.title("🏠 Emlak Vizyoner")
st.subheader(f"TÜİK {GUNCEL_AY} Yıllık TÜFE: %{GUNCEL_ORAN}")

st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b;">
        <b>Resmi Bilgi:</b> Borçlar Kanunu kira artış üst sınırını farklı hesaplasa da, bu uygulama piyasa gerçeklerini yansıtan 
        <b>Yıllık TÜFE (%{GUNCEL_ORAN})</b> oranını baz almaktadır.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- HESAPLAMA ---
eski_kira = st.number_input("Mevcut Kira Bedeli (TL):", min_value=1000, value=15000, step=500)
yeni_kira = eski_kira * (1 + GUNCEL_ORAN / 100)

st.success(f"### Hesaplanan Yeni Kira: {yeni_kira:,.2f} TL")

# --- WHATSAPP MESAJI ---
mesaj = f"Sayın ev sahibim, TÜİK verilerine göre yıllık TÜFE kira artışım %{GUNCEL_ORAN}'dir. Yeni kiram {yeni_kira:,.2f} TL'dir."
encoded_mesaj = urllib.parse.quote(mesaj)
whatsapp_url = f"https://wa.me/?text={encoded_mesaj}"

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 18px;">
            💬 WhatsApp ile Ev Sahibine Gönder
        </div>
    </a>
    """, unsafe_allow_html=True)

st.divider()
st.caption(f"Veriler Şubat 2026 TÜİK bültenine dayanmaktadır.")
