__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }


def add_stamp(passport: dict, country: str):
    if country != passport["nationality"]:
        if "stamps" not in passport:
            passport["stamps"] = [country]
        else:
            passport["stamps"].append(country)
    return passport


def check_passport(
    passport,
    country,
    admitted,
    denied,
):
    if "stamps" in passport:
        visited_countries = [*passport["stamps"]]
        visited_countries.append(passport["nationality"])
    else:
        visited_countries = passport["nationality"]

    if country in denied:
        bad_countries = denied[country]
    else:
        bad_countries = []

    unpermitted_trips = [c for c in visited_countries if c in bad_countries]

    if len(unpermitted_trips) == 0:
        stamped_passport = add_stamp(passport, country)
        return stamped_passport
    else:
        return False
