import pandas as pd

print("🍹 Welcome to the Drink Recommendation System!")
print("Answer a few questions and we’ll suggest a drink for you.\n")

# Create dataset
data = {
    "drink": ["Mojito", "Cola", "Lemonade", "Iced Tea", "Coffee", "Beer", "Wine"],
    "type": ["Cocktail", "Soft Drink", "Soft Drink", "Tea", "Hot Drink", "Alcohol", "Alcohol"],
    "flavor": ["Minty", "Sweet", "Citrus", "Bitter", "Bitter", "Bitter", "Fruity"],
    "sweetness": ["Medium", "High", "High", "Low", "Low", "Low", "Medium"],
    "alcohol": ["Yes", "No", "No", "No", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

# Show available options
print("Available flavors: Sweet, Bitter, Citrus, Minty, Fruity")
print("Sweetness levels: Low, Medium, High")
print("Alcohol: Yes or No\n")

# Get user input
flavor = input("👉 What flavor do you prefer? ")
sweetness = input("👉 Preferred sweetness level? ")
alcohol = input("👉 Do you want alcohol? (Yes/No): ")

# Clean inputs
flavor = flavor.strip().lower()
sweetness = sweetness.strip().lower()
alcohol = alcohol.strip().lower()

# Recommendation logic
recommendations = df[
    (df["flavor"].str.lower() == flavor) &
    (df["sweetness"].str.lower() == sweetness) &
    (df["alcohol"].str.lower() == alcohol)
]

# Output results
if not recommendations.empty:
    print("\n✅ Recommended drink(s) for you:")
    for drink in recommendations["drink"]:
        print(f"🍸 {drink}")
else:
    print("\n⚠️ No exact match found. Showing similar options based on flavor...\n")
    
    similar = df[df["flavor"].str.lower() == flavor]
    
    if not similar.empty:
        print("👉 You might like:")
        for drink in similar["drink"]:
            print(f"🍹 {drink}")
    else:
        print("😅 No similar drinks found. Try different preferences!")

print("\n✨ Thank you for using the Drink Recommendation System!")
