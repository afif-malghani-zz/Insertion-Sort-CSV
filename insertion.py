# take list from csv read as input
def Sort(list1, col):
    
#     itrate over rows
    for i in range(len(list1)):
#         skip for row 1 because it has names of columns
        if i <=1:
            continue
#         check if `col` column of current row is smaller than that of previous row
        elif list1[i][col] < list1[i-1][col]:
#         store in temporary variable
            temp = list1[i]
#     create variable j to itrate all previous rows
            j = i -1
            while j >= 1:
#             if any row with column `col` value greater than temp
                if list1[j][col]>temp[col]:
#         move it to the next index, repeat till reach a value smaller than temp[col]
                    list1[j+1] = list1[j]
#     if previous row is index 1, after moving it to next index put temp at index 1 
                    if j == 1:
                        list1[j] = temp
#                 if prev_row[col] <= temp
                else:
#         Place temp at next index
                    list1[j+1] = temp
#     breat so that this process does not repeat for higher numbers
                    break
                j -= 1
    return list1
