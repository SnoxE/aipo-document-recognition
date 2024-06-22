from datetime import datetime
import re

def extract_birthdate_from_pesel(pesel):
    """
    Extract birthdate from PESEL number.
    
    Args:
        pesel (str): The PESEL number (11 digits).
    
    Returns:
        str: The birthdate in YYYY-MM-DD format.
    
    Raises:
        ValueError: If the PESEL number is invalid.
    """
    if len(pesel) < 6:
        raise ValueError("Too few digits to read birthdate from PESEL.")
    
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    
    # Determine the century
    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    elif 81 <= month <= 92:
        year += 1800
        month -= 80
    else:
        raise ValueError("Invalid PESEL number. Month part is incorrect.")
    
    return f"{year:04d}-{month:02d}-{day:02d}"


def format_passport_date(date_str):
    month_pattern = re.compile(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', re.IGNORECASE)
    month = month_pattern.search(date_str).group(0)
    day = re.search(r'\d{1,2}', date_str).group(0)
    year = re.search(r'\d{4}', date_str).group(0)

    day = int(day)
    month = datetime.strptime(month, "%b").month
    year = int(year)
    
    return f"{year:04d}-{month:02d}-{day:02d}"


# Function to convert date from dd/mm/yyyy to yyyy-mm-dd
def format_date(date_str, document_type):
    date_to_format = date_str

    if document_type == "Dowód Osobisty":
        return datetime.strptime(date_to_format, "%d/%m/%Y").strftime("%Y-%m-%d")
    elif document_type == "Legitymacja":
        return extract_birthdate_from_pesel(date_str)
    elif document_type == "Paszport":
        return format_passport_date(date_str)
