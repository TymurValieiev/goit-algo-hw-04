def load_data(file_directory):
    with open(file_directory, "r", encoding='utf-8') as file:
        return file.readlines()

def clean_data(cat_data):
    cat_data = [data.strip() for data in cat_data if data.strip()]

    cleaned_data = []
    for item in cat_data:
        parts = item.strip().split(',')
        cleaned_data.extend(parts)
    return cleaned_data

