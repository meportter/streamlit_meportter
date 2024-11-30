import streamlit as st
import validators  # URL 유효성 검사에 사용

if 'youtube_url' not in st.session_state:
    st.session_state['youtube_url'] = ""

# 입력받은 유튜브 링크
youtube_url = st.session_state['youtube_url']
if youtube_url is None:
    if st.button("API Key를 입력하세요."):
        st.switch_page("pages/1_Setting.py")
    st.stop()

client = st.session_state.get('openai_client', None)
if client is None:
    if st.button("API Key를 입력하세요."):
        st.switch_page("pages/1_Setting.py")
    st.stop()

# 유효성 검사 함수
def is_valid_youtube_url(url):
    if not validators.url(url):
        return False
    if "youtube.com/watch" not in url and "youtu.be" not in url:
        return False
    return True

# 유효성 검사 및 처리
if not is_valid_youtube_url(youtube_url):
    st.error("Invalid YouTube URL. Please enter a valid YouTube link.")
    st.stop()  # 앱 실행 중단

# 유효한 경우 비디오 출력
st.video(youtube_url)
st.success("Video loaded successfully!")
