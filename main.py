import numpy as np


def print_line():
    print("-" * 72)


def main():
    # Besin isimleri
    food_names = np.array([
        "Chicken Breast",
        "Rice",
        "Egg",
        "Oats",
        "Olive Oil"
    ])

    # Her besinin 100 gramdaki değerleri:
    # Sütun sırası: Calories, Protein, Carbs, Fat
    nutrition_per_100g = np.array([
        [165, 31.0, 0.0, 3.6],     # Chicken Breast
        [130, 2.7, 28.0, 0.3],     # Rice
        [155, 13.0, 1.1, 11.0],    # Egg
        [389, 16.9, 66.3, 6.9],    # Oats
        [884, 0.0, 0.0, 100.0]     # Olive Oil
    ])

    # Öğün isimleri
    meal_names = np.array([
        "Breakfast",
        "Lunch",
        "Dinner"
    ])

    # Her öğünde hangi besinden kaç gram yenildi?
    # Satırlar öğünleri, sütunlar besinleri temsil eder.
    # Sütun sırası food_names ile aynıdır.
    quantities_grams = np.array([
        [0,   0,   100, 60,  0],    # Breakfast
        [200, 180, 0,   0,   10],   # Lunch
        [150, 150, 50,  0,   5]     # Dinner
    ])

    # Günlük hedef:
    # Sıra: Calories, Protein, Carbs, Fat
    daily_target = np.array([2200, 150, 250, 70])

    macro_names = np.array([
        "Calories",
        "Protein",
        "Carbs",
        "Fat"
    ])

    # Gram değerlerini 100 gram birimine çeviriyoruz.
    serving_multiplier = quantities_grams / 100

    # Vectorization:
    # quantities_grams şekli:       (3 öğün, 5 besin)
    # nutrition_per_100g şekli:     (5 besin, 4 makro)
    # Çıkan sonuç şekli:            (3 öğün, 5 besin, 4 makro)
    nutrition_by_meal_and_food = serving_multiplier[:, :, np.newaxis] * nutrition_per_100g[np.newaxis, :, :]

    # Her öğünün toplam makrosu
    meal_totals = nutrition_by_meal_and_food.sum(axis=1)

    # Günlük toplam makro
    daily_total = meal_totals.sum(axis=0)

    # Hedefle fark
    difference = daily_total - daily_target

    # Hedefin yüzde kaçına ulaştık?
    target_completion_percent = (daily_total / daily_target) * 100

    print_line()
    print("MACRO AND CALORIE CALCULATOR")
    print_line()

    print("\nFOOD DATABASE - values per 100g")
    print_line()
    print(f"{'Food':<18} {'Calories':>10} {'Protein':>10} {'Carbs':>10} {'Fat':>10}")
    print_line()

    for index, food in enumerate(food_names):
        calories, protein, carbs, fat = nutrition_per_100g[index]
        print(f"{food:<18} {calories:>10.1f} {protein:>10.1f} {carbs:>10.1f} {fat:>10.1f}")

    print("\nMEAL PLAN - quantities in grams")
    print_line()
    print(f"{'Meal':<12}", end="")
    for food in food_names:
        print(f"{food[:10]:>12}", end="")
    print()
    print_line()

    for meal_index, meal in enumerate(meal_names):
        print(f"{meal:<12}", end="")
        for quantity in quantities_grams[meal_index]:
            print(f"{quantity:>12.0f}", end="")
        print()

    print("\nMEAL TOTALS")
    print_line()
    print(f"{'Meal':<12} {'Calories':>10} {'Protein':>10} {'Carbs':>10} {'Fat':>10}")
    print_line()

    for meal_index, meal in enumerate(meal_names):
        calories, protein, carbs, fat = meal_totals[meal_index]
        print(f"{meal:<12} {calories:>10.1f} {protein:>10.1f} {carbs:>10.1f} {fat:>10.1f}")

    print("\nDAILY RESULT")
    print_line()
    print(f"{'Macro':<12} {'Total':>10} {'Target':>10} {'Diff':>10} {'Complete %':>12}")
    print_line()

    for macro_index, macro in enumerate(macro_names):
        total = daily_total[macro_index]
        target = daily_target[macro_index]
        diff = difference[macro_index]
        complete = target_completion_percent[macro_index]

        print(f"{macro:<12} {total:>10.1f} {target:>10.1f} {diff:>10.1f} {complete:>11.1f}%")

    print_line()

    calorie_difference = difference[0]

    if calorie_difference < -200:
        print("Comment: Calories are quite below the target.")
    elif calorie_difference > 200:
        print("Comment: Calories are quite above the target.")
    else:
        print("Comment: Calories are close to the target.")

    print_line()


if __name__ == "__main__":
    main()