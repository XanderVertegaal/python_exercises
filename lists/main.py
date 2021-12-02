# Do not modify these lines
__winc_id__ = "6eb355e1a60f48a28a0bbbd0c88d9ab4"
__human_name__ = "lists"

# Add your code after this line


def alphabetical_order(films):
    return sorted(films)


def won_golden_globe(film):
    return film.lower() in [
        "jaws",
        "star wars: episode iv - a new hope",
        "e.t. the extra-terrestrial",
        "memoirs of a geisha",
    ]


def remove_toto_albums(films):
    toto_albums = [
        "fahrenheit",
        "the seventh one",
        "toto xx",
        "falling in between",
        "35th anniversary - live in poland",
        "toto xiv",
        "old is new",
        "40 tours around the sun",
        "with a little help from my friends",
    ]
    return [x for x in films if x.lower() not in toto_albums]
