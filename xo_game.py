row1=['🤩','🤩','🤩']
row2=['🤩','🤩','🤩']
row3=['🤩','🤩','🤩']
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the position where u want to pur money")
#32
rowno=int(position[0])
colno=int(position[1])
row_select=matrix[rowno-1]
row_select[colno-1]="X"
print(f"{row1}\n{row2}\n{row3}")
