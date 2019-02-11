def is_head(ln):
    if len(ln)<4:
        return False
    if not ln[0]=='h':
        return False
    if not ln[2:4]=='. ':
        return False
    if not ln[1] in '123456':
        return False
    return int(ln[1])

def get_headers(filename, lines):
    '''
    gets tuples in format
    ((x1, y1, x2, y2), level, title, icon)
    '''
    r = []
    for n,i in enumerate(lines):
        level=is_head(i)
        if level:
            r.append( ((0, n, 0, n+1), level, i[3:], -1) )
    return r
