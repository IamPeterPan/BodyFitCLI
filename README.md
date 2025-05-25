# BodyFitCLI
Personal Calorie &amp; Protein Manager

A lightweight, terminal-based tool that calculates your Basal Metabolic Rate (BMR) and tracks daily calorie & protein intake from any food you log.  
Ideal for students, athletes, or anyone who prefers a no-GUI, keyboard-only workflow.

 **BMR calculator** using the Mifflin-St Jeor formula  
 **Automatic food database** (`foods.csv`) that grows as you add new foods  
 **Calorie & protein tally** with deficit/maintenance/surplus feedback  
 **CSV-only storage** – no external databases, no internet required

 ## 📦 Installation

 **Clone the repo**

   ```bash
   git clone https://github.com/<your-user>/bodyfit-cli.git
   cd bodyfit-cli

 ## 📦 How to run

 python main.py

#############################################
#    Welcome to Your Calorie Manager App!   #
#############################################

Enter your weight (kg): 70
Enter your height (cm): 175
Enter your age: 30
Enter your gender (male/female): male

ℹ️  Your BMR is: 1715.0 calories/day

Enter food eaten (or type "done" to finish): banana
Enter grams of banana eaten: 120
Enter food eaten (or type "done" to finish): chicken breast
Enter grams of chicken breast eaten: 150
Enter food eaten (or type "done" to finish): done

------------ Summary ------------
ℹ️ Total calories consumed: 390.00 kcal
ℹ️ Total protein consumed: 48.65 g
ℹ️ Your BMR: 1715.00 kcal/day
✅ You are in a significant calorie deficit.
----------------------------------

Enter food eaten (or type "done" to finish): oatmeal
"⚠️ oatmeal" not found. Add it? (yes/no): yes
Enter calories per 100 g: 389
Enter protein (g) per 100 g: 16.9




 
