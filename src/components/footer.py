import streamlit as st

def footer_home():

    st.markdown("""
        <style>
            .signature{
            display:flex; justify-content:center; align-items:center; gap:8px; margin-top:2rem; color:white; font-size:18px; font-family:Arial, sans-serif; font-weight:bold;
            }    
            .signature-name{
                font-family:"Brush Script MT","Lucida Handwriting",cursive; font-size:34px; color:#FFD1E8; font-weight:normal;
            }
        
        </style>
        <div class="signature">
            <span>Created with ❤️ by</span>
            <span class="signature-name">Paramisha</span>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():

    st.markdown("""
        <style>
            .signature{
            display:flex; justify-content:center; align-items:center; gap:8px; margin-top:2rem; color:black; font-size:18px; font-family:Arial, sans-serif; font-weight:bold;
            }    
            .signature-name{
                font-family:"Brush Script MT","Lucida Handwriting",cursive; font-size:34px; color:#ee6b6e; font-weight:normal;
            }
        
        </style>
        <div class="signature">
            <span>Created with ❤️ by</span>
            <span class="signature-name">Paramisha</span>
        </div>
    """, unsafe_allow_html=True)