def parse_recipes(file_path):
    with open(file_path) as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for ingrediend in range(ingredients_count):
                temp_data = file.readline().strip()
                name, quantity, measure = temp_data.split('|')
                ingredients.append(
                    {'ingredient_name' : name.strip(), 
                     'quantity' : int(quantity.strip()), 
                     'measure' : measure.strip()})
            cook_book[dish_name] = ingredients
            file.readline()
        return cook_book
    
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish not in cook_book:
            return "Рецепт не найден"
        for ingredient in cook_book[dish]:
            ingradient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']
            ingredients.setdefault(ingradient_name, {'measure': measure, 'quantity': 0})
            ingredients[ingradient_name]['quantity'] += quantity * person_count
    return ingredients
            


