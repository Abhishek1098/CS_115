def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''

    def editDist(first, second):
        if (first, second) in data:
            return data[(first, second)]
        if first == "" or second == "":
            value = 0
            data[(first, second)] = value
            return value
        elif first[0] == second[0]:
            value = 1 + editDist(first[1:], second[1:])
            data[(first, second)] = value
            return value
        else:
            branch = editDist(first[1:], second)
            otherBranch = editDist(first, second[1:])
            value = max (branch, otherBranch)
            data[(first, second)] = value
            return value

    data = {}
    return editDist(first, second)



