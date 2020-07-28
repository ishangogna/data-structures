#initial array
heros=['spider man','thor','hulk','iron man','captain america']

#insert black panther in the end.
heros.append('black panther')


#remove black panther from the end and insert black panther after thor
heros.remove('black panther')
for i in range(len(heros)):
    if heros[i] == 'thor':
        heros.insert(i+1,'black panther')

print('length of the list : ', len(heros))
print(heros)

for i in range(len(heros)):
    if heros[i]== 'thor' or heros[i] == 'hulk':
        heros[i] = 'doctor strange'

print('doctor strange : ', heros)

#sort list in alphabetical order
print('Sorted list : ', sorted(heros))