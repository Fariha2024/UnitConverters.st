import streamlit as st

def load_common_unit_header():
    st.markdown(
        """
        <div style="background-color:#277e07; padding:10px; border-radius:10px; display: flex; align-items: center;">
            <h1 style="color:#eaf2e7; margin-left: 20px; display: inline;">
                📐 <span style="color:#61fe28;">Common</span> <span style="color:white;">Unit System</span>
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
