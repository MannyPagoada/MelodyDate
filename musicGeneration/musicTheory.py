monthToKey= {
    1: "C Major",
    2: "G Major",
    3: "D Major",
    4: "A Major",
    5: "E Major",
    6: "B Major",
    7: "F# Major",
    8: "Db Major",
    9: "Ab Major",
    10: "Eb Major",
    11: "Bb Major",
    12: "F Major"
}

def getKeyForMonth(month):
    """
    Get the musical key for a given month based on the Circle of Fifths.

    Parameters:
    month (int): The month as an integer (1-12).

    Returns:
    str: The musical key corresponding to the month.
    """
    return monthToKey.get(month, "Invalid Month")