from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    list_a = a.split("\n")
    list_b = b.split("\n")


    return list_compare(list_a, list_b)


def sentences(a, b):
    """Return sentences in both a and b"""

    list_a = sent_tokenize(a)
    list_b = sent_tokenize(b)

    return list_compare(list_a, list_b)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    list_a = get_substrings(a, n)
    list_b = get_substrings(b, n)

    return list_compare(list_a, list_b)

def get_substrings(list, length):

    output = []

    temp = len(list) - length + 1

    for i in range(temp):
        output.append(list[i:length + i])

    return output

def list_compare(a, b):

    output = []

    for i in a:
        for j in b:
            if i == j and j not in output:
                output.append(j)


    return output
