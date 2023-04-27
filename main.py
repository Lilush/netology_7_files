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
                     'quantity' : quantity.strip(), 
                     'measure' : measure.strip()})
            cook_book[dish_name] = ingredients
            file.readline()
        return cook_book
            


