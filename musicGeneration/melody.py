from musicTheory import getKeyForMonth

def generateMelody(birthday):
    """
    Generate a melody based on the user's birthday.

    Parameters:
    birthday (str): The user's birthday in YYYY-MM-DD format.

    Returns:
    str: A description of the melody.
    """
    month = int(birthday.split('-')[1])
    key = getKeyForMonth(month)
    
    # Additional logic to generate melody based on the key
    # ...
    
    return f"Generated melody in {key}"