"""
Garden Advice App
-----------------
An interactive app that gives gardening advice based on season and plant type.
Supports two seasons (summer, winter) and two plant types (flower, vegetable).
Includes input validation to handle incorrect entries.
"""

# Dictionaries for storing advice
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

plant_advice = { 
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

# Dictionary for recommended plants by season and plant type
recommended_plants = {
    ("summer", "flower"): ["Sunflowers", "Marigolds", "Zinnias"],
    ("summer", "vegetable"): ["Tomatoes", "Cucumbers", "Peppers"],
    ("winter", "flower"): ["Pansies", "Winter Jasmine", "Snowdrops"],
    ("winter", "vegetable"): ["Kale", "Broccoli", "Brussels Sprouts"]
}

def get_valid_input(prompt: str, valid_options: list[str]) -> str:
    """
    Repeatedly ask the user for input until a valid option is given.

    Args:
        prompt (str): The message to display to the user.
        valid_options (list[str]): A list of acceptable inputs.

    Returns:
        str: A valid input value from the user (always in lowercase).
    """
    while True:
        value = input(prompt).lower().strip()
        if value in valid_options:
            return value
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_season_advice(season: str) -> str:
    """Return gardening advice based on the season."""
    return season_advice.get(season, "No advice for this season.\n")

def get_plant_advice(plant_type: str) -> str:
    """Return gardening advice based on the type of plant."""
    return plant_advice.get(plant_type, "No advice for this type of plant.")

def get_recommended_plants(season: str, plant_type: str) -> list[str]:
    """Return a list of recommended plants for the season and plant type."""
    return recommended_plants.get((season, plant_type), [])

def main():
    """Main program flow with input validation and repeat option."""
    while True:
        season = get_valid_input(
            "Which season are you planning for? (summer/winter): ",
            list(season_advice.keys())
        )
        plant_type = get_valid_input(
            "Which type of plant are you planning for? (flower/vegetable): ",
            list(plant_advice.keys())
        )

        # Collect advice
        advice = get_season_advice(season)
        advice += get_plant_advice(plant_type)

        # Display results
        print("\n--- Gardening Advice ---")
        print(advice)

        # Show recommended plants
        plants = get_recommended_plants(season, plant_type)
        if plants:
            print(f"Recommended {plant_type}s for {season}: {', '.join(plants)}")

        # Ask if user wants to try again (case-insensitive yes/no)
        again = get_valid_input(
            "\nWould you like to get more advice? (yes/no): ",
            ["yes", "no", "y", "n"]
        )
        if again in ["no", "n"]:
            print("Thanks for using the Garden Advice App. Goodbye!")
            break

if __name__ == "__main__":
    main()
