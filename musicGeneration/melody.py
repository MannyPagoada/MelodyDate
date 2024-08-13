getKeyForMonth= {
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
    return getKeyForMonth.get(month, "Invalid Month")