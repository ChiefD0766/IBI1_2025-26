# create a new Python class 
class food_item(object):
    """
    the name of the food item and counts of its calories, protein, carbohydrates and fat
    """
    def __init__(self, item_name, calories, protein, carbohydrates, fat):
        self.name = item_name
        self.calories = calories
        self.protein = protein
        self.carbs = carbohydrates
        self.fat = fat

# a function that takes a list of items defined in the class
def total_nutrition(food_list):
    """
    Input: food_list, food_item list of instances
    Output: total nutrition, warning report
    """
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0

    for food in food_list:
        total_cal = total_cal + food.calories
        total_pro = total_pro + food.protein
        total_car = total_car + food.carbs
        total_fat = total_fat + food.fat

    print("24-hour total intake:")
    print("calories:", total_cal, "kcal")
    print("protein:", total_pro, "g")
    print("carbohydrates:", total_car, "g")
    print("fat:", total_fat, "g")

    # warning of excessive calorific or fat consumption
    if total_cal > 2500:
        print("Warning: Calories exceed 2500 kcal!")
    if total_fat > 90:
        print("Warning: Fat exceeds 90g!")

# Example
apple = food_item("apple", 60, 0.3, 15, 0.5)
rice = food_item("rice", 130, 2.7, 28, 0.3)
chicken = food_item("chicken", 165, 31, 0, 3.6)
day_eat = [apple, rice, chicken, rice, chicken]
total_nutrition(day_eat)