from sys import argv, exit, stderr
import os
import re

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python {} <latex file>".format(argv[0]), file=stderr)
        exit(1)

    f = open(argv[1])
    text = f.read()
    f.close()

    source = re.search("(?sm)\\\\meetemail{.*?}(.*)\\\\end{document}", text)
    if not source:
        print("Error: Could not find source!", file=stderr)
        exit(1)

    source = source[1]

    # Remove comments
    source = "\n".join(list(map(lambda l: re.sub("^(.*)%(.*)$", "\\1", l), source.split("\n"))))

    # Replace emphs
    source = re.sub("\\\\emph{(.*?)}", "**\\1**", source)

    # Remove ~s
    source = re.sub("~", " ", source)

    # Transform $ and \[ \] into $$
    source = re.sub("\$", "$$", source)
    source = re.sub("\\\\\\[", "$$", source)
    source = re.sub("\\\\\\]", "$$", source)

    # Replace `` '' and `
    source = re.sub("``", "\"", source)
    source = re.sub("''", "\"", source)
    source = re.sub("`", "'", source)

    print(source)
