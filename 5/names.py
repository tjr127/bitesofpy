NAMES = ['matt Damon','arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    newlist = []
    for name in names:
        name = name.title()
        if name not in newlist:
            newlist.append(name)
    return(newlist)

    """Should return a list of title cased names,
       each name appears only once"""
    
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    shortname = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    names = dedup_and_title_case_names(names)
    for name in names:
        firstname = name.split(" ")[0]
        if len(firstname)<len(shortname):
            shortname=firstname
    return(shortname)

if __name__=="__main__":
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(sort_by_surname_desc(PY_CONTENT_CREATORS))
    print(shortest_first_name(NAMES))
