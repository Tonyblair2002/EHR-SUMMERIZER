import streamlit as st, json, requests

st.set_page_config(page_title="EHR Summarizer", layout="wide")
st.title("🩺 EHR Clinical Documentation Companion")

mode = st.radio("Mode", ["Clinician", "Patient-friendly (ELI5)"])
specialty = st.selectbox("Specialty", ["primary care","cardiology","pediatrics","oncology","ED"])
raw = st.text_area("Paste patient JSON", height=300)

if st.button("Summarize"):
    try:
        payload = {
            "patient_json": json.loads(raw),
            "specialty": specialty,
            "mode": "patient" if "Patient" in mode else "clinician"
        }

        st.write("🧩 Sending request to backend...")
        st.json(payload)

        r = requests.post("http://localhost:8081/summarize", json=payload, timeout=120)

        st.write("📩 Raw backend response:")
        st.code(r.text)

        out = r.json()

        st.subheader("Summary")
        st.code(out.get("summary", "⚠️ No summary found. Check backend logs."))

        if out.get("error"):
            st.error(out["error"])
        elif out.get("issues"):
            st.warning("\n".join(out["issues"]))

    except Exception as e:
        st.error(f"❌ {str(e)}")
