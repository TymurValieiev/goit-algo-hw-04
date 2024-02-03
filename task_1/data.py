def load_data(file_directory):
    with open(file_directory, 'r') as file:
        return file.readlines()

def clean_data(salary_data):
    cleaned_data = []

    for item in salary_data:
        salary = [char for char in item if char.isdigit()]
        
        if len(salary) > 2:
            cleaned_data.append(int(''.join(salary)))

    return cleaned_data