import streamlit as st
from pythainlp import word_tokenize

# กำหนดโหมดแชทบอท
MODES = {
    "คุณย่า": "โอ๋ ๆ หลานรักของย่า ย่าขอให้หนูหายเหนื่อยนะลูก 💗",
    "ฟีลแฟน": "ที่รักเหนื่อยมากเลยใช่ไหม~ มากอด ๆ นะ 💕",
    "เด็กน้อย": "งืออ พี่เหนื่อยหรอ เค้าจะเป่าความเหนื่อยออกไปให้~ ฟู่ๆ 🧸"
}

# เก็บประวัติแชท
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ส่วนหัว
st.title("🧘‍♀️ แชทบอทฮีลใจพนักงาน")
st.markdown("เลือกโหมดของแชทบอท แล้วพิมพ์ข้อความเพื่อบ่นหรือเล่าเรื่องต่าง ๆ ได้เลย~")

# ปุ่มเลือกโหมด
mode = st.radio("เลือกโหมดของแชทบอท", list(MODES.keys()), horizontal=True)

# แสดงแชทแบบ Bubble ซ้าย-ขวา (ไม่มีชื่อคนพูด)
chat_placeholder = st.container()
with chat_placeholder:
    for sender, message in st.session_state.chat_history:
        align = "flex-end" if sender == "พนักงาน" else "flex-start"
        bg_color = "#DCF8C6" if sender == "พนักงาน" else "#F1F0F0"
        st.markdown(
            f"""
            <div style='display: flex; justify-content: {align}; margin: 4px 0;'>
                <div style='background-color: {bg_color}; padding: 8px 12px; border-radius: 18px; 
                            max-width: 60%; word-wrap: break-word;'>
                    {message}
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# พิมพ์ข้อความด้านล่าง
st.markdown("---", unsafe_allow_html=True)
col1, col2 = st.columns([8, 1])
with col1:
    user_input = st.text_input(" ", placeholder="พิมพ์ข้อความที่นี่...", key="input", label_visibility="collapsed")
with col2:
    send = st.button("📩", use_container_width=True)

# วิเคราะห์อารมณ์เบื้องต้น
def detect_mood(text):
    sad_words = ["เหนื่อย", "ท้อ", "ร้องไห้", "ไม่ไหว", "เศร้า", "เครียด", "เบื่อ"]
    tokens = word_tokenize(text, engine="newmm")
    for word in sad_words:
        if word in tokens:
            return "เศร้า"
    return "ปกติ"

# เมื่อผู้ใช้กดส่ง
if send and user_input.strip() != "":
    st.session_state.chat_history.append(("พนักงาน", user_input.strip()))

    mood = detect_mood(user_input)
    if mood == "เศร้า":
        bot_reply = MODES[mode]
    else:
        bot_reply = "ฟังแล้วอบอุ่นใจ 😊 ขอให้วันนี้สดใสนะ~"

    st.session_state.chat_history.append(("แชทบอท", bot_reply))
    st.rerun()




















