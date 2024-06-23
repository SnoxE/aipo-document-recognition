from PySide6.QtCore import QDate

def format_person_output(data, omit_keys=[]):
    output = ""
    for k, v in data.items():
        if k in omit_keys:
            continue
        
        if isinstance(v, QDate):
            data[k] = v.toString("dd.MM.yyyy")
        
        output += f"{k}: {data[k]}\n"

    return output