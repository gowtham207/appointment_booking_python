from models.enum import Gender


def gender_handler(val: str) -> Gender:
    value = val.lower().strip()
    if value == 'male' or value == "m":
        return Gender.MALE
    elif value == 'female' or value == 'F':
        return Gender.FEMALE
    return Gender.OTHER
