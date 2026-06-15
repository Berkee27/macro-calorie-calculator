# Macro and Calorie Calculator

A simple NumPy-based project that calculates daily calories and macronutrients from meal quantities.

## Problem

Manually calculating daily calories, protein, carbs, and fat can be slow and error-prone. This project automates that process using Python and NumPy.

## Technologies

- Python
- NumPy

## How It Works

The program stores food nutrition values per 100 grams in a NumPy array.  
It also stores how many grams of each food were eaten in each meal.

Then it calculates:

- Meal totals
- Daily calorie and macro totals
- Difference from daily targets
- Target completion percentages

## Sample Foods

- Chicken Breast
- Rice
- Egg
- Oats
- Olive Oil

## Installation

```bash
git clone https://github.com/Berkee27/macro-calorie-calculator.git
cd macro-calorie-calculator
python -m venv .venv
