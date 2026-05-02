import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
import json
from process_excel import update_excel_template

# 1. Configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Energybae AI", page_icon="⚡", layout="wide")

# 2. The Header Section 
try:

    banner = Image.open("energybae_banner.png") 
    st.image(banner, use_container_width=True)
except:
    st.error("Banner image 'energybae_banner.png' not found.")

st.markdown("<h1 style='text-align: center; color: white;'>Solar Load Calculator — Electricity Bill to Excel Automation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>AI-Powered Electricity Bill Analysis System</p>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Upload Bill")
    uploaded_file = st.file_uploader("Choose an MSEDCL bill image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    with col1:
        st.image(img, caption="Preview of Uploaded Bill", use_container_width=True)
    
    with col2:
        st.subheader("Analysis")
        if st.button("Start AI Processing"):
            with st.spinner("AI is analyzing the bill..."):
                model = genai.GenerativeModel('gemini-2.5-flash')

                prompt = """
                Analyze this electricity bill image and extract:
                1. Consumer Name
                2. Consumer Number
                3. Sanctioned Load (numeric value in kW)
                4. Monthly Units Consumed for the last 12 months.
                
                Return ONLY a JSON object with these keys: 
                "name", "number", "load", "units" (where units is a dictionary of Month: Value).
                """
                
                try:
                    response = model.generate_content([prompt, img])
                    
                    # Clean and parse JSON
                    clean_json = response.text.replace('```json', '').replace('```', '').strip()
                    data = json.loads(clean_json)
                    
                    st.success("Analysis Complete!")
                    st.json(data)
                    
                    # 4. Generate & Download Excel
                    output_path = update_excel_template(data)
                    
                    with open(output_path, "rb") as file:
                        st.download_button(
                            label="Download Solar Analysis Excel",
                            data=file,
                            file_name="Energybae_Report.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                except Exception as e:
                    st.error(f"Processing error: {e}")
