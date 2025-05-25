import csv
import os

CSV_FILE = 'foods.csv'

# Create CSV with few foods if missing the file to start
if not os.path.exists(CSV_FILE):

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['food', 'calories_per_100g', 'protein_per_100g'])
        writer.writerow(['apple', '52', '0.3'])
        writer.writerow(['banana', '96', '1.3'])
        writer.writerow(['chicken breast', '165', '31.0'])
        writer.writerow(['egg', '155', '13.0'])
        writer.writerow(['salmon', '208', '20.0'])

# Load foods into a dictionary from the CSV file
def load_foods():

    foods = {}
    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            foods[row['food']] = {
                'cal_per_100g': float(row['calories_per_100g']),
                'prot_per_100g': float(row['protein_per_100g'])
            }
    return foods

# to write the new food to the CSV to use it for next time
def add_food_to_csv(food, cal100, prot100):

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([food, cal100, prot100])

# Calculate BMR for the given weight height and gender
def calculate_bmr(weight, height, age, gender):

    if gender.lower() == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# function for validated float input.
def get_valid_float(prompt):

    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠️ Invalid input. Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

# function for validated int input.
def get_valid_int(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("⚠️ Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("⚠️ Invalid input. Please enter an integer.")
    

def main():

    print("#############################################")
    print("#    Welcome to Your Calorie Manager App!   #")
    print("#############################################\n")

    # Inputs for BMR calculation
    weight = get_valid_float('Enter your weight (kg): ')
    height = get_valid_float('Enter your height (cm): ')
    age = get_valid_int('Enter your age: ')
    gender = input('Enter your gender (male/female): ')
    bmr = calculate_bmr(weight, height, age, gender)
    
    # Validate BMR if invlaid we end the program
    if bmr < 0:
        print("❌ Invalid BMR calculation. Please check your inputs.")
        return

    print("\n#############################################")
    print(f"ℹ️ Your BMR is: {bmr:.2f} calories/day")
    print("#############################################\n")

    # Load foods and track intake
    foods = load_foods()
    total_calories = 0.0
    total_protein = 0.0

    while True:
        # User input for food intake
        food = input('Enter food eaten (or type "done" to finish): ').strip().lower()
        if food == 'done':
            break

        # If food not found, we ask users to add.
        if food not in foods:
            add = input(f'"⚠️ {food}" not found. Add it? (yes/no): ').strip().lower()
            if add == 'yes':
                cal100 = get_valid_float('Enter calories per 100 g: ')
                prot100 = get_valid_float('Enter protein (g) per 100 g: ')
                add_food_to_csv(food, cal100, prot100)
                foods[food] = {
                    'cal_per_100g': cal100,
                    'prot_per_100g': prot100
                }
            else:
                continue

        qty_g = get_valid_float(f'Enter grams of {food} eaten: ')
        total_calories += foods[food]['cal_per_100g'] * qty_g / 100
        total_protein += foods[food]['prot_per_100g'] * qty_g / 100

    # Summary
    print('\n------------ Summary ------------')
    print(f'ℹ️ Total calories consumed: {total_calories:.2f} kcal')
    print(f'ℹ️ Total protein consumed: {total_protein:.2f} g')
    print(f'ℹ️ Your BMR: {bmr:.2f} kcal/day')
    print('-----------------------------------')
    # Check if in calorie deficit or surplus
    if total_calories == bmr:
        print('✅ You are at maintenance calories.')
    elif total_calories < bmr * 0.9:
        print('✅ You are in a significant calorie deficit.')
    elif total_calories > bmr * 1.1:
        print('❌ You are in a significant calorie surplus.')
    else:
        print('⚠️ You are in a moderate calorie deficit/surplus.')

if __name__ == '__main__':
    main()
