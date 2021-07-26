#copas ke main.py


f = open('all_possible_moves.json',)
data = json.load(f)
f.close()
list_all_state = list(data.values())

lenlist = []
for i in list_all_state:
    lenlist.append(len(i))

count = 0
for i in range(len(lenlist)):
    if lenlist[i] == 7:
        print_snapshot(list(data.keys())[i])