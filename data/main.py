import streamlit as st
from prepare_data import PrepareData
from post_generator import generate_post

def main():
    st.title("LinkedIn Content Generator")
    col1, col2, col3 = st.columns(3)
    fs=PrepareData()

    with col1:
        selected_tag=st.selectbox("Title",options=fs.get_tags())

    with col2:
        selected_length=st.selectbox("Lenght", options=["Short","Medium","Large"])
    
    with col3:
        selected_language=st.selectbox("Language", options=["English", "Hinglish"])

    if st.button("Generate"):
        generated_text= generate_post(selected_length, selected_language, selected_tag)
        st.write(generated_text)


if __name__=="__main__":
    main()