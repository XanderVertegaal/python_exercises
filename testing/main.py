def get_none():
    return None


results = []


def flatten_dict(mydict: dict):
    if type(mydict) is not dict:
        raise ValueError
    else:
        for key in mydict:
            try:
                flatten_dict(mydict[key])
            except ValueError:
                results.append(mydict[key])
                continue
        return [x for x in results]
