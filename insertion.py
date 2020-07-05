def Sort(list1, col):
    for i in range(len(list1)):
        if i <=1:
            continue
        elif list1[i][col] < list1[i-1][col]:
            temp = list1[i]
            j = i -1
            while j >= 1:
                if list1[j][col]>temp[col]:
                    list1[j+1] = list1[j]
                    if j == 1:
                        list1[j] = temp
                # elif list1[j+1] == temp:
                else:
                    list1[j+1] = temp
                    break
                j -= 1
    return list1