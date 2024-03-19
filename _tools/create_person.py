import os
import sys
import yaml

if __name__ == "__main__":
    if "_speakers" not in os.listdir("."):
        print("Error: Needs to be executed in project root!")
        sys.exit(1)

    first = input("First name: ")
    last = input("Last name: ")
    affil = input("Affiliation: ")

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
        print("Error: File already exists!")
        sys.exit(1)

    f = open("_speakers/" + file_name, "w")
    f.write(text)
    f.close()
