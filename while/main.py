from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.


def unique_koala_facts(int):
    koala_fact_list = []
    iterations = 0
    while len(koala_fact_list) < int and iterations < 1000:
        new_fact = random_koala_fact()
        if new_fact not in koala_fact_list:
            koala_fact_list.append(new_fact)
        iterations += 1
    return koala_fact_list


def num_joey_facts():
    seen_facts = {}
    joey_facts = set()
    while 10 not in seen_facts.values():
        new_fact = random_koala_fact()
        if "joey" in new_fact:
            joey_facts.add(new_fact)

        if new_fact in seen_facts:
            seen_facts[new_fact] += 1
        else:
            seen_facts[new_fact] = 1
    return len(joey_facts)


def koala_weight():
    found = 0
    while found == 0:
        new_fact = random_koala_fact()
        if "kg" in new_fact:
            sliced = new_fact[: new_fact.find("kg")]
            weight = sliced[sliced.rfind(" ") + 1:]
            found = 1
    return int(weight)


if __name__ == "__main__":
    print(random_koala_fact())
    num_joey_facts()
    koala_weight()
