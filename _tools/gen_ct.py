import itertools
import subprocess
import json
import os
import sys
import math
import create_person

slots = [('2024-06-25', '16:30', '18:30'),
         ('2024-06-26', '14:00', '16:00'),
         ('2024-06-27', '17:30', '18:30'),
         ('2024-06-28', '14:00', '16:00'),
         ('2024-06-28', '16:30', '18:30'),
         ]
rooms = ['J222', 'J330', 'J335', 'J336', 'J431']
prod = list(itertools.product(slots, rooms))

joined = {}
schedule = []
chairs = {}

def add_mins(t, m):
    hrs, mins = list(map(lambda i: int(i), t.split(":")))
    mins_new = (mins + m) % 60
    hrs_new = hrs + math.floor(((mins + m) / 60))
    return "{}:{:02d}".format(hrs_new, mins_new)

def build_session(i):
    (date, start, end), room = prod[i]
    scheduled = schedule[i]
    j = i + 1

    speakers = "\n"
    talks = "\n"
    for talk in scheduled:
        speakers += "  - \"" + talk["presenter"]["name"] + "\"\n"
        talks += "  - \"" + talk["title"].replace('\\', '\\\\') + "\"\n"

    key = "{}".format(i + 1)
    chair = ""
    if key in chairs:
        c = chairs[key]

        if isinstance(c, str):
            chair = "chairs:\n  - \"" + chairs[key] + "\"\n"
        if isinstance(c, list):
            chair = "chairs:\n"
            for x in c:
                chair += "  - \"" + x + "\"\n"

    timing_notice = ""
    if i < 11 or 15 < i:
        timing_notice = "**Time allocation:** 20 minutes per speaker; 5 minutes for each changeover"

    text = """---
name: {}
speakers: {}
talks: {}
{}
categories:
  - Contributed Talk
time_start: '{}'
time_end: '{}'
talk_date: {}
room: {}
---
{}
""".format("Contributed Talks " + str(j),
           speakers,
           talks,
           chair,
           start,
           end,
           date,
           room,
           timing_notice
           )

    with open("_talks/ct{}.md".format(j), 'w') as f:
        f.write(text)

def build_talk(i, j):
    (date, start_time, _), room = prod[i]
    talk = schedule[i][j]
    sid = i + 1
    tid = j + 1
    shift = 20 if 10 <= i and i < 15 else 25 # Thursday sessions do not have formal changeover times

    start = add_mins(start_time, shift * j)
    end = add_mins(start_time, shift * (j + 1))

    presenter = talk["presenter"]
    create_person.create(presenter["first"], presenter["last"], presenter["affiliation"])

    abstract = ""
    with open("CT_data/abstracts/converted_{}.md".format(talk["id"])) as f:
        abstract = f.read()

    text = """---
name: \"{}\"
speakers:
  - \"{}\"
categories:
  - Contributed Talk
hide_talk: true
time_start: '{}'
time_end: '{}'
talk_date: {}
room: {}
---

{}

{}
""".format(talk["title"].replace('\\', '\\\\'),
           talk["presenter"]["name"],
           start,
           end,
           date,
           room,
           "**Authors:** {}".format(talk["authors"]) if talk["authors"] != talk["presenter"]["name"] else "",
           abstract
           )

    with open("_talks/ct{}-{}.md".format(sid, tid), 'w') as f:
        f.write(text)

if __name__ == "__main__":
    if "_talks" not in os.listdir("."):
        print("Error: Needs to be executed in project root!")
        sys.exit(1)

    for f in os.listdir("_talks"):
        if f.startswith("ct"):
            os.remove("_talks/" + f)

    with open("CT_data/joined_manual.json") as f:
        joined = json.load(f)

    with open("CT_data/chairs.json") as f:
        chairs = json.load(f)

    # Extract schedule from joined
    for slot in range(0, len(slots)):
        for room in range(0, len(rooms)):
            talks = []
            for ti, talk in joined.items():
                s = talk["schedule"]
                if s["slot"] == slot and s["track"] == room:
                    talk["id"] = ti
                    talks.append(talk)

            talks.sort(key=lambda t: t["schedule"]["order"])
            schedule.append(talks)

    for i, talks in enumerate(schedule):
        # (date, start, end), room = prod[i]
        # talks = schedule[i]
        # print("Scheduled on {} at {} in {}:".format(date, start, room))
        # for talk in talks:
        #     print("  {}, {}".format(talk["presenter"]["name"], talk["title"]))
        # print("")

        if talks:
            build_session(i)
            for j in range(0, len(schedule[i])):
                build_talk(i, j)
