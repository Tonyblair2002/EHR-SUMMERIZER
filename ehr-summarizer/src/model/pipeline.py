from typing import Dict, List

def build_context(patient_json: Dict) -> Dict:
    labs = sorted(patient_json.get("observations", []), key=lambda x: str(x.get("DATE", "")))[-5:]
    meds = patient_json.get("medications", [])[:10]
    probs = patient_json.get("problems", [])[:10]
    encs = patient_json.get("encounters", [])[-5:]
    return {"labs": labs, "meds": meds, "problems": probs, "encounters": encs}

def rule_checks(summary: str, patient_json: Dict) -> List[str]:
    issues = []
    allergies = [a.get("DESCRIPTION","").lower() for a in patient_json.get("allergies",[])]
    if any("penicillin" in a for a in allergies) and "penicillin" in summary.lower():
        issues.append("⚠ Mentions penicillin despite recorded allergy.")
    return issues

def summarize(patient_json: Dict, specialty: str = "primary care", mode: str = "clinician") -> Dict:
    ctx = build_context(patient_json)
    problems = ", ".join({p.get("DESCRIPTION","") for p in ctx["problems"] if p.get("DESCRIPTION")}) or "None"
    meds = ", ".join({m.get("DESCRIPTION","") for m in ctx["meds"] if m.get("DESCRIPTION")}) or "None"
    tone = "clinical tone" if mode == "clinician" else "patient-friendly tone"
    summary = (
        f"Specialty: {specialty}\n"
        f"Problems: {problems}\n"
        f"Meds: {meds}\n"
        f"Mode: {tone}\n"
        "Summary generated from structured fields. (Plug in LLM next.)"
    )
    issues = rule_checks(summary, patient_json)
    return {"summary": summary, "citations": [], "timeline": [], "issues": issues}
