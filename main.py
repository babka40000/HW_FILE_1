def convert_file_to_dict(file_name):
    dict_for_return = {}

    with open(file_name, "r", encoding="utf-8") as file:
        while True:
            file_line = file.readline()
            if not file_line:
                return dict_for_return

            dict_for_return[file_line.strip()] = []

            count_of_ingredients = 0
            for count_of_ingredients in range(0, int(file.readline().strip())):
                list_of_ingredient = file.readline().strip().split(" | ")
                dict_for_return[file_line.strip()].append({'ingredient_name': list_of_ingredient[0], 'quantity': list_of_ingredient[1], 'measure': list_of_ingredient[2]})
            file.readline()


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    dict_of_ingredients = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] not in dict_of_ingredients:
                dict_of_ingredients[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"], "quantity": int(ingredient["quantity"]) * person_count}
            else:
                dict_of_ingredients[ingredient["ingredient_name"]]["quantity"] += \
                    int(ingredient["quantity"]) * person_count
    return dict_of_ingredients


cook_book = (convert_file_to_dict("recipes.txt"))
ingredients = get_shop_list_by_dishes(cook_book, ["Фахитос", "Утка по-пекински"], 22)

print(cook_book)
print(ingredients)