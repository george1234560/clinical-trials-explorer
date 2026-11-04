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
