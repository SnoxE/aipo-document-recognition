from datetime import datetime


# Function to convert date from dd/mm/yyyy to yyyy-mm-dd
def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date