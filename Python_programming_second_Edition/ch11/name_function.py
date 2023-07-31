def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = str(first + ' ' + middle + ' ' + last).title()
    else:
        full_name = str(first + ' ' + last).title()
    return full_name
