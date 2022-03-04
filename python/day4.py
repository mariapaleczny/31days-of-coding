def gerund_infinitive(verb: str) -> str:
    """
    Turn gerund into infinitive.
    Only gerunds (present participle - 'ing' form) without spaces are accepted as input.
    """
    vovels = ["a", "e", "i", "o", "u"]
    if ' ' in verb:
        raise ValueError('Given string contains space.')
    elif verb[-3:] != "ing":
        raise ValueError('Not a gerund.')
    else:
        if verb[-4] == 'y' and len(verb) == 5:
            return 'to ' + verb[:-4] + 'ie'
        elif verb[-5] == verb[-4]:
            return 'to ' + verb[:-4]
        elif verb[-5:-3] == 'ck':
            return 'to ' + verb[:-4] + ' OR to ' + verb[:-3]
        elif verb[-5:-3] == 'th' or (verb[-5] in vovels and verb[-4] not in vovels):
            return 'to ' + verb[:-3] + 'e OR to ' + verb[:-3]
        else:
            return 'to ' + verb[:-3]


verbs = ["doing", "tying", "trying", "getting", "picnicking", "packing", "breathing", "mouthing", "celebrating", "wondering"]

for verb in verbs:
    print(verb + ": " + gerund_infinitive(verb))

# print(gerund_infinitive("do"))
# print(gerund_infinitive("I am doing"))

