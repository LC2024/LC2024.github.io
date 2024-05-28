import os
import sys
import yaml

def create(first, last, affil):
    if "_speakers" not in os.listdir("."):
        print("Error: Needs to be executed in project root!")
        sys.exit(1)

    if not (first and last and affil):
        print("Empty; abotring!")
        sys.exit(1)

    data = {
        "name": first + " " + last,
        "first_name": first,
        "last_name": last,
        "affiliation": affil
        }

    text = (yaml.dump(data, Dumper=yaml.Dumper))
    text = "---\n" + text + "---\n"

    file_name = first.lower() + "-" + last.lower() + ".md"
    if file_name in os.listdir("_speakers"):
        # print("Note: Speaker file already exists: " + first + " " + last)
        return

    f = open("_speakers/" + file_name, "w")
    f.write(text)
    f.close()

if __name__ == "__main__":
    first = input("First name: ")
    last = input("Last name: ")
    affil = input("Affiliation: ")

    create(first, last, affil)
