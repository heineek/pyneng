def deduplicate_links(topology):
    '''
    if (X, Y): (N, M) and (N, M): (X, Y) are in the same dict, remove one of them
    '''
    result = topology.copy()

    # will change during dict changes in Python3
    keys = result.keys()
    values = result.values()

    for value in list(values):
        if value in keys and result[value] in keys:
            del(result[value])
    return result
