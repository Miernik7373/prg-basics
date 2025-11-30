


def time_string(hours: int, minutes: int, time_format: str) -> str:

    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    period = ''
    if hours < 12:
        period = "am" 
    else:
        period = "pm"
    hour12 = hours % 12
    if hour12 == 0:
        hour12 = 12 

    return f"{hour12}:{minutes:02d}{period}"
print(time_string(8,3,'24'))
