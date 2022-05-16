def merge(*infer):
    List = list(infer)
    leng = len(List)
    src = ''
    for i in range(leng):
        infor = str(List[i])
        if(i == 0):
            src = infor
        else:
            src = src + ' ' + infor
    return src