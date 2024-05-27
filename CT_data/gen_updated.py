import csv
import json

slots = ["Tue", "Wed", "Thu", "Fri m", "Fri a"]

def get_slot(day):
    # try:
    return slots.index(day.strip())
    # except:
    #     return 3

if __name__ == "__main__":
    joined = {}
    with open('joined.json') as f:
        joined = json.load(f)

    schedule = {}
    with open('versione finale finale.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if not row[7] in ["WITHDRAWN", "REJECT"]:
                try:
                    schedule[int(row[0])] = {'slot': get_slot(row[9]), 'track': int(row[10]) - 1}
                except:
                    print(row)

    items = list(joined.items())
    for (i, talk) in items:
        if int(i) in schedule:
            talk["schedule"] = schedule[int(i)]
        else:
            joined.pop(i)

    for slot in range(0, 5):
        for room in range(0, 5):
            talks = []
            for ti, talk in joined.items():
                s = talk["schedule"]
                if s["slot"] == slot and s["track"] == room:
                    talk["id"] = ti
                    talks.append(talk)
            for i, talk in enumerate(talks):
                talk["schedule"]["order"] = i

    with open('joined_new.json', 'w') as f:
        f.write(json.dumps(joined, sort_keys=True, indent=2))
    # for _, talk in joined.items():
    #     print(talk["presenter"]["name"])
