FLOWERING_SEASON = {
    1: 0.0,   # Jan
    2: 0.1,   # Feb
    3: 0.4,   # Mar
    4: 0.7,   # Apr
    5: 1.0,   # May
    6: 1.0,   # Jun
    7: 1.0,   # Jul
    8: 0.8,   # Aug
    9: 0.5,   # Sep
    10: 0.2,  # Oct
    11: 0.0,  # Nov
    12: 0.0,  # Dec
}

def flowering_score(month: int) -> float:
    return FLOWERING_SEASON[month]