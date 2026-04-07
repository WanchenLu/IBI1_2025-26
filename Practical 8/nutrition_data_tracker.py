class food_item:
    def __init__(self,calories,protein,carbohydrates,fat):
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
def total(list):
    total_calories = sum (food.calories for food in list)
    total_protein = sum (food.protein for food in list)
    total_carbohydrates = sum (food.carbohydrates for food in list)
    total_fat = sum (food.fat for food in list)
    if total_calories > 2500:
        print ("warning:consume too much calories")
    if total_fat > 90:
        print ("warning:consume too much fat")
    return total_calories,total_protein,total_carbohydrates,total_fat
apple = food_item(60,0.3,15,0.5)
consumption = [apple]
total(consumption)
print (total(consumption))