def return_id(cleaned_data):
    return cleaned_data[::3]

def return_name(cleaned_data):
    return cleaned_data[1::3]

def return_age(cleaned_data):
    return cleaned_data[2::3]