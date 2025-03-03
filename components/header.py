import streamlit as st

def load_header():
    st.markdown(
        """
        <div style="background-color:#277e07; padding:10px; border-radius:10px; display: flex; align-items: center;">
            <h1 style="color:white; margin-left: 0px; display: inline;">
               <span style="color:#61fe28;">UnitConverters</span><span style="color:white;">.st</span>
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
