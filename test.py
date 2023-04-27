import os
from pprint import pprint

from main import parse_recipes, get_shop_list_by_dishes


file_path = os.path.join('files', 'recipes.txt')

cook_book = parse_recipes(file_path)
ingredients = get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 2)

pprint(cook_book, width=100)
print()
pprint(ingredients, width=100)
