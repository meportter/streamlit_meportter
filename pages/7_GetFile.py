import streamlit as st

Youtube_URL = st.text_input("Youtube_URL", 
                        value=st.session_state.get('Youtube_URL',''))

if Youtube_URL:
    st.session_state['Youtube_URL'] = Youtube_URL


mp4_file = st.file_uploader("Upload a mp4 file", type=['mp4'], accept_multiple_files=False)
if mp4_file is not None:
    vector_store = client.beta.vector_stores.create(name="ChatPDF")
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=[mp4_file]
    )
    st.session_state.vector_store = vector_store

if 'vector_store' not in st.session_state:
    st.markdown("mp4 파일을 업로드하세요.")
    st.stop()