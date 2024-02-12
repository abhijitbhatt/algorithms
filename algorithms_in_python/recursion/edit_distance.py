# Edit distance using recursion - https://www.geeksforgeeks.org/edit-distance-dp-5/

def edit_distance(s1:str,s2:str,i:int,j:int)->int:
    if i == 0:
        return j
    if j == 0:
        return i
    if s1[i] == s2[j]:
        return edit_distance(s1,s2,i-1,j-1)
    else:
        return min(edit_distance(s1,s2,i-1,j),
                   edit_distance(s1,s2,i-1,j-1),
                   edit_distance(s1,s2,i-1,j-1)) + 1

s1 = 'saturday'
s2 = 'sunday'
print(edit_distance(s1,s2,len(s1) - 1,len(s2) - 1))