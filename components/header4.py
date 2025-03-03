import streamlit as st

def load_help_header4():
    st.markdown(
        """
        <div style="background-color:#277e07; padding:10px; border-radius:10px; display: flex; align-items: center;">
            <h1 style="color:#eaf2e7; margin-left: 20px; display: inline;">
                📚 <span style="color:#61fe28;">Help</span> <span style="color:#61fe28;">& </span><span style="color:white;">FAQs</span>
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
