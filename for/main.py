from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    min_length = min([len(country) for country in countries])
    shortest_country_list = []
    for country in countries:
        if len(country) == min_length:
            shortest_country_list.append(country)
    return shortest_country_list


def most_vowels(countries):
    vowels_per_country = []
    for country in countries:
        vowels_per_country.append(
            len([x for x in country if x.lower() in ["a", "e", "i", "o", "u"]])
        )

    ziplist = zip(countries, vowels_per_country)

    def get_value(item):
        return item[1]

    sorted_list = sorted(ziplist, key=get_value, reverse=True)
    top_three = []
    for country in sorted_list[:3]:
        top_three.append(country[0])
    return top_three


def alphabet_set(countries):
    found_countries = []
    found_letters = set()
    while len(found_letters) < 26:
        for country in set(countries):
            unique_letters = set(
                [
                    x.lower()
                    for x in country
                    if (ord(x.lower()) >= 97 and ord(x.lower()) <= 122)
                ]
            )

            if len(unique_letters.union(found_letters)) > len(found_letters):
                found_letters = found_letters.union(unique_letters)
                found_countries.append(country)

    return found_countries

    # This block is only run if this file is the entrypoint; python main.py
    # It is not run if it is imported as a module: `from main import *`


if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    most_vowels(countries)
    print(alphabet_set(countries))
