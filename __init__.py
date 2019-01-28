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
    Generates Textile headers in format:
    line_index, header_level, header_text
    '''
    for n,i in enumerate(lines):
        level=is_head(i)
        if level:
            yield (n,level,i[3:])
