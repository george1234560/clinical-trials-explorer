import pandas as pd



def flatten_study(study):
    new_dict = {}
    new_dict["nct_id"] = study["protocolSection"]["identificationModule"]["nctId"]
    new_dict["title"] = study["protocolSection"]["identificationModule"]["briefTitle"]
    new_dict["status"] = study["protocolSection"]["statusModule"]["overallStatus"]
    phases = study["protocolSection"]["designModule"].get("phases")
    if phases is not None:
        new_dict["phases"] = ", ".join(phases)
    else:
        new_dict["phases"] = None
    new_dict["startdate"] = study["protocolSection"]["statusModule"].get("startDateStruct",{}).get("date")
    new_dict["why_stopped"] = study["protocolSection"]["statusModule"].get("whyStopped")
    new_dict["enrollment"] = study["protocolSection"]["designModule"].get("enrollmentInfo",{}).get("count")
    new_dict["completion_date"] = study["protocolSection"]["statusModule"].get("completionDateStruct",{}).get("date")
    new_dict["sponsor_type"] = study["protocolSection"]["sponsorCollaboratorsModule"]["leadSponsor"]["class"]
    new_dict["has_results"] = study["hasResults"]
    return new_dict


def build_table(studies,condition_name):
    rows = []
    for study in studies:
        rows.append(flatten_study(study))
    
    df = pd.DataFrame(rows)

    df.to_csv(f"../data/processed/{condition_name}.csv",index = False)
    return df

