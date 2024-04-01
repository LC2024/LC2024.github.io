from sys import argv, exit
import yaml
import os
import re
import datetime

room_order = ['J222', 'J330', 'J335', 'J336', 'J431']

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python {} <_talks directory>".format(argv[0]))
        exit(1)

    talks_dir = argv[1]

    # Load all of the talks
    talks = []
    for talk_fn in os.listdir(talks_dir):
        f = open(os.path.join(talks_dir, talk_fn))
        talk_text = f.read()
        talk_data_text = talk_text.split("---\n")[1]
        talk_data = yaml.load(talk_data_text, Loader=yaml.Loader)

        talk_data["parsed_start"] = datetime.time.fromisoformat(talk_data["time_start"])

        talks.append(talk_data)
        f.close()

    talks = list(filter(lambda t: not t.get("hide_talk", False), talks))

    # Generate the entry for each day
    dates = set([t["talk_date"] for t in talks])
    program = {"days": []}
    while not dates == set():
        data = {}
        day = min(dates)
        dates.remove(day)

        data["name"] = day.strftime('%A')
        data["date"] = day
        data["rooms"] = []

        # The entries are generated room-wise, ordered by starting time
        talks_today = list(filter(lambda t: t["talk_date"] == day, talks))
        talks_today.sort(key=lambda t:t["parsed_start"])
        rooms = set([t["room"] for t in talks_today])
        for room in room_order:
            if not room in rooms:
                continue

            room_list = [{"name": t["name"], "time_start": t["time_start"], "time_end": t["time_end"]}
                        for t in filter(lambda t: t["room"] == room, talks_today)]
            data["rooms"].append({"name": room, "talks": room_list})

        program["days"].append(data)

    text = yaml.dump(program)
    text = text.replace("09:00", "\'09:00\'")
    text = text.replace("08:30", "\'08:30\'")

    print(text)
