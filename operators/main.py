# Do not modify these lines
__winc_id__ = "d0d3cdcefbb54bc980f443c04ab3a9eb"
__human_name__ = "operators"

# Add your code after this line

# The language spoken the most in Switzerland is the same as in Spain.
spain_language = "Castilian Spanish"
switzerland_language = "(Swiss) German"
print(spain_language == switzerland_language)

# The most prevalent religion in Switzerland is the same as in Spain.
spain_religion = "Roman Catholic"
switzerland_religion = "Roman Catholic"
print(spain_religion == switzerland_religion)

# The name length of Spain's capital does not equal that of Switzerland.
spain_capital = "Madrid"
switzerland_capital = "Bern"
print(len(spain_capital) != len(switzerland_capital))

# Switzerland's GDP is greater than Spain's GDP.
spain_gdp_billion = 1715
switzerland_gdp_billion = 590.7
print(switzerland_gdp_billion > spain_gdp_billion)

# The population growth is less than 1% in Switzerland and Spain.
spain_pop_growth = -0.03
switzerland_pop_growth = 0.65
print(spain_pop_growth < 1 and switzerland_pop_growth < 1)

# At least one of the two countries has a population count of over 10 million.
spain_pop_million = 47.3
switzerland_pop_million = 8.5
print(spain_pop_million > 10 or switzerland_pop_million > 10)

# Exactly one of the two countries has a population count of over 10 million.
print(
    (spain_pop_million > 10 and switzerland_pop_million <= 10)
    or (switzerland_pop_million > 10 and spain_pop_million <= 10)
)
