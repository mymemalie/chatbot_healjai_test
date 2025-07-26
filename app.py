import streamlit as st
from pythainlp import word_tokenize

# โหมดแชทบอท
MODES = {
    "คุณย่า": "โอ๋ ๆ หลานรักของย่า ย่าขอให้หนูหายเหนื่อยนะลูก 💗",
    "ฟีลแฟน": "ที่รักเหนื่อยมากเลยใช่ไหม~ มากอด ๆ นะ 💕",
    "เด็กน้อย": "งืออ พี่เหนื่อยหรอ เค้าจะเป่าความเหนื่อยออกไปให้~ ฟู่ๆ 🧸"
}

# เก็บประวัติแชท
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ส่วนหัว
st.markdown("<h1 style='text-align:center;'>🧘‍♀️ แชทบอทฮีลใจพนักงาน</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>เลือกโหมด แล้วพิมพ์ข้อความได้เลย~</p>", unsafe_allow_html=True)

# ปุ่มเลือกโหมด
mode = st.radio("เลือกโหมดของแชทบอท", list(MODES.keys()), horizontal=True)

# พื้นที่แสดงแชท
chat_box = st.container()
with chat_box:
    for sender, msg in st.session_state.chat_history:
        align = "flex-end" if sender == "พนักงาน" else "flex-start"
        bg = "#DCF8C6" if sender == "พนักงาน" else "#F1F0F0"
        chat_html = f"""
        <div style='display: flex; justify-content: {align}; margin: 5px 0;'>
            <div style='background: {bg}; padding: 10px 14px; border-radius: 16px;
                        max-width: 75%; word-wrap: break-word; font-size: 15px;'>
                {msg}
            </div>
        </div>"""
        st.markdown(chat_html, unsafe_allow_html=True)

# กล่องพิมพ์ข้อความด้านล่าง
with st.container():
    st.markdown("---", unsafe_allow_html=True)
    col1, col2 = st.columns([9, 1])
    with col1:
        user_input = st.text_input("พิมพ์ข้อความ", placeholder="พิมพ์ที่นี่...", label_visibility="collapsed")
    with col2:
        send_btn = st.button("📩", use_container_width=True)

# ฟังก์ชันวิเคราะห์เบื้องต้น
def detect_mood(text):
    sad_words = ["เหนื่อย", "ท้อ", "ร้องไห้", "ไม่ไหว", "เศร้า", "เครียด", "เบื่อ"]
    tokens = word_tokenize(text, engine="newmm")
    for word in sad_words:
        if word in tokens:
            return "เศร้า"
    return "ปกติ"

# ตอบกลับเมื่อกดส่ง
if send_btn and user_input.strip():
    st.session_state.chat_history.append(("พนักงาน", user_input.strip()))
    mood = detect_mood(user_input)
    reply = MODES[mode] if mood == "เศร้า" else "ฟังแล้วอบอุ่นใจ 😊 ขอให้วันนี้สดใสนะ~"
    st.session_state.chat_history.append(("แชทบอท", reply))
    st.rerun()  # rerun ปลอดภัย ไม่มี experimental แล้ว





















