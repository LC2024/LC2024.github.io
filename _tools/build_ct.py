import create_person
import importlib
import webbrowser
import json
import time
import convert_from_latex

# webbrowser.open('https://dowehr.dortselb.st', new=0, autoraise=True)

def load_abstract(i):
    latex = ""
    with open("CT_data/abstracts/paper_tex_" + i + ".tex") as f:
        latex = f.read()
    with open("CT_data/current_abstract.tex", 'w') as f:
        f.write(latex)

def gen_abstract():
    importlib.reload(convert_from_latex)
    latex = ""
    with open("CT_data/current_abstract.tex") as f:
        latex = f.read()

    abstract = convert_from_latex.convert(latex)

    with open('CT_data/current.md', 'w') as f:
        f.write(abstract)

def gen_talk(i, talk):
    abstract = ""
    with open('CT_data/current.md') as f:
        abstract = f.read()

    with open('CT_data/abstracts/converted_{}.md'.format(i), 'w') as f:
        f.write(abstract)

    with open('_talks/ct_test.md', 'w') as f:
        f.write(build_talk(talk, abstract))

def build_talk(talk, abstract):
    authors = ""
    if talk["authors"] != talk["presenter"]["name"]:
        authors = "**Authors:** {}".format(talk["authors"])


    return """---
name: \"{}\"
speakers:
 - {}
categories:
 - Contributed Talk
time_start: '{}'
time_end: '{}'
talk_date: {}
room: {}
---
{}

{}
""".format(talk['title'], talk['presenter']['name'], '13:00',
           '14:00', '06-21-24', 'J333', authors, abstract)

if __name__ == "__main__":
    converted = []
    with open('CT_data/converted.json') as f:
        converted = json.loads(f.read())


    joined = {}
    with open('CT_data/joined.json') as f:
        joined = json.loads(f.read())

    for i, talk in joined.items():
        if not (int(i) in converted["converted"] or int(i) in converted["skipped"]):
            print("Handling [{}]: {}".format(i, talk["title"]))
            load_abstract(i)
            gen_abstract()
            gen_talk(i, talk)

            while True:
                choice = input("[a]ccept/[s]kip/[c]onvert/[r]eload?").strip()

                if choice == "a":
                    converted["converted"].append(int(i))
                    with open('CT_data/converted.json', 'w') as f:
                        f.write(json.dumps(converted))
                    break
                if choice == "s":
                    converted["skipped"].append(int(i))
                    with open('CT_data/converted.json', 'w') as f:
                        f.write(json.dumps(converted))
                    break
                elif choice == "c":
                    gen_abstract()
                    gen_talk(i, talk)
                elif choice == "r":
                    gen_talk(i, talk)
