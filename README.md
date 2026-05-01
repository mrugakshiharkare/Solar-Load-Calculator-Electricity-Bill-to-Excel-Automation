# ⚡ Energybae: Solar Load Calculator & Bill Automator
### AI Intern Practical Task Submission

This project automates the manual process of analyzing electricity bills to determine solar system sizing. It replaces a 15–30 minute manual entry task with a high-speed AI workflow that extracts data from MSEDCL bills and populates the official Energybae Excel template.

---

## 📄 1. Project Brief
**What I Built:**
I developed an end-to-end automation tool using Python and Streamlit that uses Computer Vision (Gemini 1.5 Flash) to "read" electricity bills. The system identifies key parameters like Consumer Name, Sanctioned Load, and 12-month usage history, then programmatically maps them into the provided Excel template while preserving existing formulas.

**Tools Used:**
- **Streamlit**: For a clean, professional web interface.
- **Google Gemini 2.5 Flash**: For high-speed OCR and structured data extraction.
- **Openpyxl & Pandas**: To handle precise Excel cell mapping and data management.
- **Python-dotenv**: To securely manage API credentials.

**Future Improvements:**
Next, I would implement a "Validation Step" where the user can edit extracted data before the Excel is generated to ensure 100% accuracy. I also plan to add support for multi-page PDF bills and integrate a database to track customer history and ROI trends over time.

---

## 🛠️ 2. Tech Stack & Architecture
- **Language**: Python 3.10+
- **AI Model**: Google Gemini API (Vision-to-JSON).
- **Frontend**: Streamlit (Responsive Web UI).
- **Template Engine**: Openpyxl (preserving Excel formulas).

---

## 🚀 3. Setup & Installation

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/mrugakshiharkare/Solar-Load-Calculator-Electricity-Bill-to-Excel-Automation
   cd EnergyBae-Solar-Automation

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure API Key**:
- Create a .env file in the root directory.
- Add your key: GEMINI_API_KEY=your_key_here

4. **Run the Application**:
```bash
streamlit run app.py
```
