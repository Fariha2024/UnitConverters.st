import streamlit as st

def load_footer():
    st.markdown(
        """
        <hr>
        <p style="text-align:center;">© 2025 Unit Converter | Built with Streamlit</p>
        """,
        unsafe_allow_html=True
    )
