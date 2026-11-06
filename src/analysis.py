import pandas as pd

def phase_termination(phase,df):
    mask = df["phases"] == phase
    phase_number = df[mask]
    phase_number_terminated = (phase_number["status"].value_counts(normalize = True)*100).round(2)
    return phase_number_terminated.get("TERMINATED",0)

def termination_by_phase(df):
    phases = df["phases"].value_counts()
    rates_temp = {}
    for phase in phases.index:
        phase_number_terminated =phase_termination(phase,df)
        rates_temp[phase] = phase_number_terminated

    rates = pd.Series(rates_temp).sort_values(ascending = False)
    return rates


def categorize_text(text):
    if pd.isna(text):
        return "missing"
    if "efficacy" in text or "futility" in text:
        return "efficacy"
    if "safety" in text or "adverse" in text or "death" in text:
        return "safety"
    if "pi " in text or "investigator" in text:
        return "investigator"
    if "covid" in text:
        return "covid"
    if "administrative" in text:
        return "administrative"
    if "enrol" in text or "recruit" in text or"accrual" in text or "particip" in text:
        return "recruitment"
    if "sponsor" in text or "business" in text or "fund" in text or "strateg" in text or "focus" in text:
        return "funding"   
    if "description" in text:
        return "see description"
    else:
        return "other"
    
