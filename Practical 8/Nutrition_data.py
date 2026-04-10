class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

def calculate_nutrition(food_list):
    total_calories = sum(food.calories for food in food_list)
    total_protein = sum(food.protein for food in food_list)
    total_carbohydrates = sum(food.carbohydrates for food in food_list)
    total_fat = sum(food.fat for food in food_list)

    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbohydrates} g")
    print(f"Total Fat: {total_fat} g")

    if total_calories > 2500:
        print("Warning: You have exceeded your daily calorie intake.")
    if total_fat > 90:
        print("Warning: You have exceeded your daily fat intake.")

#Example
Apple = food_item("Apple", 60, 0.3, 15, 0.5)
Banana = food_item("Banana", 105, 1.3, 27, 0.3)
daily_food = [Apple, Banana,Apple, Banana, Apple]
calculate_nutrition(daily_food)