import os
import json

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def create_dictionary(folder_path):
    dictionary = {}
    for i in range(8000):
        file_path = os.path.join(folder_path, f"{i}.txt")
        words = list(set(read_text_file(file_path)))
        dictionary[str(i)] = words
    return dictionary

def save_to_text_file(dictionary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False)

if __name__ == "__main__":
    folder_path = "procxmu_pages"
    output_file = "dictionary2.txt"

    dictionary = create_dictionary(folder_path)
    save_to_text_file(dictionary, output_file)
