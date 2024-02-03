from data import load_data, clean_data
from processing import return_id, return_name, return_age
import os

def main():

    def get_cats_info(cats_file_directory):
        try:
            cat_data = load_data(cats_file_directory)
            cleaned_data = clean_data(cat_data)
            id_list = return_id(cleaned_data)
            name_list = return_name(cleaned_data)
            age_list = return_age(cleaned_data)

            return [{'id': i, 'name': n, 'age': a} for i, n, a in zip(id_list, name_list, age_list)]
            
        except FileNotFoundError:
            return f"Файл за директорією: {cats_file_directory} не знайдено."

            

    print(get_cats_info("C:\\Users\\valieiet\\Documents\\My files\\py\\task_2\\cats_file.txt"))

if __name__ == "__main__":
    main()