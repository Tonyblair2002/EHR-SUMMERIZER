# 🩺 AI Assistant for EHR Summarization

## 📌 Project Overview
The **EHR Summarizer** is an AI-powered clinical documentation assistant that transforms raw Electronic Health Record (EHR) data into concise and meaningful medical notes. It extracts key insights like diagnoses, medications, allergies, and lab findings and generates summaries tailored for both:

- Clinicians (professional & medical)
- Patients (easy-to-understand)

This system helps reduce documentation workload and improves how patient information is communicated.

---

## 🧠 Key Features
- Converts EHR data into clinical summaries
- Two viewing modes: Clinician & Patient-friendly
- Specialty-aware summarization (Primary Care, Cardiology, etc.)
- Interactive Streamlit frontend
- FastAPI backend handling LLM communication
- Uses secured synthetic EHR data (Synthea)

---

## 🏗 Technology Architecture

**Frontend:** Streamlit  
**Backend:** FastAPI  
**LLM Models Used:**
- OpenAI **GPT-4o-mini** (initial)
- Groq **Llama-3.1-70B-Versatile** (current)

**Dataset:** Synthea Synthetic EHRs

