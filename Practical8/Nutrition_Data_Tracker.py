class food_item:
    def set_details(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

def nutrition_summary(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrate = 0
    total_fat = 0

    for item in food_list:
        total_calories = total_calories + item.calories
        total_protein = total_protein + item.protein
        total_carbohydrate = total_carbohydrate + item.carbohydrate
        total_fat = total_fat + item.fat

    print("Nutrition summary for 24 hours:")
    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrate:", total_carbohydrate, "g")
    print("Total fat:", total_fat, "g")

    if total_calories > 2500:
        print("Warning: calorie intake is above 2500 calories.")

    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")

apple = food_item()
apple.set_details("Apple", 60, 0.3, 15, 0.5)
burger = food_item()
burger.set_details("Burger", 700, 25, 50, 40)
foods_eaten = [apple, burger]
nutrition_summary(foods_eaten)