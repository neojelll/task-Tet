import csv
import os
from collections import defaultdict
import wikipediaapi


def fetch_animal_counts():
    user_agent = "YourAppName/1.0 (https://yourwebsite.com; your-email@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent=user_agent,
        language='ru'
    )
    animal_counts = defaultdict(int)

    category_page = wiki_wiki.page("Категория:Животные_по_алфавиту")
    
    if category_page.exists():
        for animal in category_page.categorymembers.values():
            title = animal.title
            
            if "категория:" in title.lower():  
                continue

            if isinstance(title, str) and title:
                first_letter = title[0].upper()
                animal_counts[first_letter] += 1

    print("Подсчет животных по буквам:")
    for letter, count in sorted(animal_counts.items()):
        print(f"{letter}: {count}")

    return animal_counts


def save_to_csv(animal_counts):
    current_directory = os.getcwd()
    
    file_path = os.path.join(current_directory, 'beasts.csv')
    
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            count = animal_counts.get(letter, 0)
            writer.writerow([letter, count])


if __name__ == "__main__":
    animal_counts = fetch_animal_counts()
    save_to_csv(animal_counts)
    