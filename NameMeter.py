import streamlit as st  
import random  
import urllib.parse  
  
st.set_page_config(page_title="NameMeter", layout="centered")  
  
st.markdown("""  
<style>  
body {  
background-color: #1e1e2f;  
color: white;  
font-family: sans-serif;  
}  
.card {  
background-color: #2e2e50;  
padding: 20px;  
border-radius: 15px;  
max-width: 400px;  
margin: 30px auto;  
text-align: center;  
}  
</style>  
""", unsafe_allow_html=True)  
  
st.title("What Your Name Really Says About You")  
  
# Mood functions  
def love(): return round(random.uniform(95, 100), 2)  
def hate(): return round(random.uniform(0, 30), 2)  
def attitude(): return round(random.uniform(60, 95), 2)  
def confidence(): return round(random.uniform(50, 90), 2)  
def jealousy(): return round(random.uniform(0, 50), 2)  
  
# Session state init  
if "result" not in st.session_state:  
    st.session_state.result = None  
if "show_share" not in st.session_state:  
    st.session_state.show_share = False  
  
name = st.text_input("Enter Your Name")  
  
# --- Generate button ---  
if st.button("Generate"):  
    st.session_state.result = {  
        "name": name,  
        "love": love(),  
        "hate": hate(),  
        "attitude": attitude(),  
        "confidence": confidence(),  
        "jealousy": jealousy(),  
    }  
    st.session_state.show_share = False  # reset share links  
  
# --- If result exists, show card ---  
if st.session_state.result:  
    r = st.session_state.result  
  
    st.markdown(f"""    
        <div class="card">    
            <h2>Vibez of {r['name']}</h2>    
            <p>💖 Love: {r['love']}%</p>    
            <p>💢 Hate: {r['hate']}%</p>    
            <p>😎 Attitude: {r['attitude']}%</p>    
            <p>💪 Confidence: {r['confidence']}%</p>    
            <p>🐍 Jealousy: {r['jealousy']}%</p>    
        </div>    
    """, unsafe_allow_html=True)    
  
    # --- Buttons under card ---    
    col1, col2 = st.columns(2)    
  
    with col1:    
        if st.button("Share Your Result", use_container_width=True):    
            st.session_state.show_share = True    
  
    with col2:    
        if st.button("Compare With Friend", use_container_width=True):    
            st.session_state.result = None    
            st.session_state.show_share = False    
            st.rerun()    
  
  
# --- Show share links if Share clicked ---    
if st.session_state.show_share:    
    share_text = f"""  
Vibez of {r['name']} 🎭  

💖 Love: {r['love']}%  
💢 Hate: {r['hate']}%  
😎 Attitude: {r['attitude']}%  
💪 Confidence: {r['confidence']}%  
🐍 Jealousy: {r['jealousy']}%  

👉 Check yours here: https://namemeterpy-2elxzmxezncqpfwtaewq5b.streamlit.app/  
"""  
    whatsapp_url = "https://api.whatsapp.com/send?text=" + urllib.parse.quote(share_text)  
    insta_url = "https://www.instagram.com/?url=" + urllib.parse.quote("https://NameMeter.com")  
    snapchat_url = "https://www.snapchat.com/scan?attachmentUrl=" + urllib.parse.quote("https://NameMeter.com")  
  
    st.markdown("<h4 style='text-align:center;'>Choose Platform</h4>", unsafe_allow_html=True)    
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">WhatsApp</a>', unsafe_allow_html=True)    
    st.markdown(f'<a href="{insta_url}" target="_blank">Instagram</a>', unsafe_allow_html=True)    
    st.markdown(f'<a href="{snapchat_url}" target="_blank">Snapchat</a>', unsafe_allow_html=True)
