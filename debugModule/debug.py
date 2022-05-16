def debug(*inList):
    List = list(inList)
    leng = len(List)
    for i in range(leng):
        List[i] = str(List[i])
    if leng == 0: return print("--------------------------------------------")
    elif leng == 1: return print(List[0])
    elif leng == 2:
        if 'ind' in List[0]:
            List[0] = ''
            List[1] = str(''.join(["\n" for s in range(int(List[1]) - 1)]))
            List.append('10')
            List.append('10')
        else:
            List.append('20')
            List.append('40')
    elif leng == 3:
        if(List[2] == 'short'):
            List[2] = '15'
            List.append('30')
        elif(List[2] == 'mid'):
            List[2] = '20'
            List.append('40')
        elif(List[2] == 'long'):
            List[2] = '30'
            List.append('45')
        else:
            List.append('40')
    return print(str('{:<' + List[2] + '}{:<' + List[3] + '}').format(List[0], List[1]))