from sys import argv, exit, stderr
import os
import re

shapes = {
        "em": lambda s: "**" + s + "**",
        "bfseries": lambda s: "**" + s + "**",
        "textit": lambda s: "_" + s + "_",
        "itshape": lambda s: "_" + s + "_",
        "scshape": lambda s: s,
        }

def replace_shapes(s):
    pattern = "\\\\("
    for p, _ in shapes.items():
        pattern = pattern + p + "|"
    pattern = pattern[:-1] + ")"
    print(pattern)

    m = re.search(pattern, s)
    while m:
        i = m.start()
        found, j_open = find_open(s, i)
        if found:
            found, j_close = match_parens(s[j_open + 1:])
            if found:
                inside = s[j_open + 1: j_open + 1 + j_close]
                s = s[:j_open] + process_shapes(inside) + s[j_open + 2 + j_close:]
            else:
                return s
        else:
            return s

        m = re.search(pattern, s)
    return s

def process_shapes(s):
    stack = 0
    ops = []
    out = ""

    while s != '':
        c = s[0]

        if c == '{':
            stack += 1
        if c == '}':
            stack -= 1

        if stack == 0 and c == '\\':
            for (shape, g) in shapes.items():
                if s.startswith('\\' + shape):
                    ops = [g] + ops
                    s = s[len(shape):]
                    break

        else:
            out += c

        s = s[1:]

    for f in ops:
        out = f(out)
    return out

def match_parens(s):
    i = 0
    stack = 0
    while i < len(s):
        c = s[i]

        if c == '{':
            stack += 1
        elif c == '}':
            if stack == 0:
                return True, i
            else:
                stack -= 1

        i += 1

    return False, None

def find_open(s, i):
    stack = 0
    while 0 <= i:
        c = s[i]

        if c == '}':
            stack += 1
        elif c == '{':
            if stack == 0:
                return True, i
            else:
                stack -= 1

        i -= 1

    return False, None


def replace_macro(s, name, f):
    i = s.find('\\' + name)
    while i >= 0:
        inside = s[i + 1 + len(name):]
        if inside[0] == '{':
            inside = inside[1:]
            m, j = match_parens(inside)

            if m:
                inside = inside[:j]
                # Do something to inside
                s = s[:i] + f(inside) + s[i + 3 + len(name) + j:]
            else:
                print("No match! " + inside)

        else:
            print("No paren! " + inside)

        i = s.find('\\' + name)

    return s

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python {} <latex file>".format(argv[0]), file=stderr)
        exit(1)

    f = open(argv[1])
    text = f.read()
    f.close()

    source = re.search("(?sm)\\\\meetemail{.*?}(.*)\\\\end{document}", text)
    # source = re.search("(?sm)\\\\maketitle(.*)\\\\end{document}", text)
    # source = re.search("(?sm)\\\\thispagestyle{empty}(.*)\\\\end{document}", text)
    if not source:
        print("Error: Could not find source!", file=stderr)
        exit(1)

    source = source[1]

    # Remove comments
    source = "\n".join(list(map(lambda l: re.sub("^(.*)%(.*)$", "\\1", l), source.split("\n"))))

    # Remove spacers
    source = re.sub("~", " ", source)
    source = re.sub("\\\\ ", " ", source)
    source = re.sub("\\\\,", " ", source)
    source = re.sub("\\\\hspace{.*?}", " ", source)
    source = re.sub("\\\\vspace{.*?}", "", source)
    source = re.sub("\\\\vspace\\*?{.*?}", "", source)


    # Replace bolds
    source = replace_macro(source, "emph", lambda s: "**" + s + "**")

    # Replace italics
    source = replace_macro(source, "textit", lambda s: "_" + s + "_")

    source = replace_shapes(source)

    # Transform $ and \[ \] into $$
    source = re.sub("\$", "$$", source)
    source = re.sub("\\\\\\[", "$$", source)
    source = re.sub("\\\\\\]", "$$", source)

    # Replace `` '' and `
    source = re.sub("``", "\"", source)
    source = re.sub("''", "\"", source)
    source = re.sub("`", "'", source)

    # Special characters
    source = re.sub("\\\\ss", "ß", source)

    # Deal with Bibliographies
    bibs = re.findall("(?ms)\\\\bibitem{(.*?)}(.*?)(?=(\\\\bibitem)|(\\\\end{thebibliography}))", source)
    bib_map = {}
    bib_list = [""]
    for bib in bibs:
        tag = bib[0]
        bib_list.append(tag)

        text = bib[1]
        text = text.replace("\n", "")
        text = text.replace("\t", "")

        bib_map[tag] = text

    # Build the bibliography in the end
    source = re.sub("(?ms)\\\\bibitem{(.*?)}(.*?)(?=(\\\\bibitem)|(\\\\end{thebibliography}))", lambda m: "{}. {}\n".format(bib_list.index(m[1]), bib_map[m[1]]),  source)
    source = re.sub("\\\\begin{thebibliography}{.*?}", "## Bibliography", source)
    source = re.sub("\\\\end{thebibliography}", "", source)

    # Replace citations
    source = re.sub("\\\\cite{(.*?)}",
       lambda m: "[{}]".format(",".join(list(map(lambda s: "{}".format(bib_list.index(s.strip())), m[1].split(","))))),
       source)

    print(source)
