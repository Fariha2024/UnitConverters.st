import streamlit as st

def load_sidebar():
    st.markdown(
        """
        <style>
            /* Sidebar Background & Styling */
            [data-testid="stSidebar"] {
                background-color: #277e07 !important;
                padding: 20px;
            }

            /* Sidebar Text */
            [data-testid="stSidebar"] h1, 
            [data-testid="stSidebar"] h2, 
            [data-testid="stSidebar"] h3, 
            [data-testid="stSidebar"] p, 
            [data-testid="stSidebar"] label {
                color: #eaf2e7 !important;
                font-weight: bold;
            }

            /* Radio Buttons */
            [role="radiogroup"] label {
                color: #eaf2e7 !important;
            }

            /* Active Selection */
            [role="radiogroup"] input:checked + div {
                background-color: #61fe28 !important;
                border-radius: 5px;
                padding: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("📂 Conversion Categories")
    st.sidebar.markdown("---")

    # Options for conversion categories
    options = ["Length", "Weight", "Temperature", "Currency", "Time", "Speed", "Energy"]
    choice = st.sidebar.radio("Select a category:", options)

    return choice
