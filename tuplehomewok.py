tpl=(12,25,36,92,47,53,68,79,84,91)
chotu_sq_list=[]
chotu_cube_list=[]
for i in range(len(tpl)):
    if i%2==0:
        chotu_sq_list.append(tpl[i]**2)
    else:
        chotu_cube_list.append(tpl[i]**3)
print("Original List:",tpl)   # [23,25,63,45,12,78,90]
print("Chotu Square List:",chotu_sq_list)   # [529, 3969, 144, 8100]
print("Chotu Cube List:",chotu_cube_list)