class food_item:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
def total(food_list):
    total_calories = sum (food.calories for food in food_list)
    total_protein = sum (food.protein for food in food_list)
    total_carbohydrates = sum (food.carbohydrates for food in food_list)
    total_fat = sum (food.fat for food in food_list)
    if total_calories > 2500:
        print ("warning:consume too much calories")
    if total_fat > 90:
        print ("warning:consume too much fat")
    return total_calories,total_protein,total_carbohydrates,total_fat
apple = food_item('apple',60,0.3,15,0.5)
consumption = [apple]
total(consumption)
print (total(consumption))