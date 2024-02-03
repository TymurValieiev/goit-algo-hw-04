from data import load_data, clean_data
from processing import calculate_average_salary, calculate_total_salary
import os

def total_salary(file_directory):
    raw_data = load_data(file_directory)
    salaries = clean_data(raw_data)

    total = calculate_total_salary(salaries)
    average = calculate_average_salary(salaries)

    return (int(total),int(average))

if __name__ == "__main__":

    total, average = total_salary("/Users/timur/Desktop/ph/goit-algo-hw-04/task_1/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
