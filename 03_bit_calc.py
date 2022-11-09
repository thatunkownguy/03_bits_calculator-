
# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text,decortation):

    # make string with five characters
    ends = decortation * 5

    # add docoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# main routine goes here
statement_generator("look - stars", "*")