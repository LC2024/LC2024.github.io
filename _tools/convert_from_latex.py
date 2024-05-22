from sys import argv, exit, stderr
import os
import re

shapes = {
        "em": lambda s: "**" + s + "**",
        "bfseries": lambda s: "**" + s + "**",
        "bf": lambda s: "**" + s + "**",
        "textit": lambda s: "_" + s + "_",
        "itshape": lambda s: "_" + s + "_",
        "scshape": lambda s: s,
        "it": lambda s: "_" + s + "_",
        }

def replace_shapes(s):
    pattern = "\\\\("
    for p, _ in shapes.items():
        pattern = pattern + p + "|"
    pattern = pattern[:-1] + ")[\\ ]"

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

    out = out.strip()
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

def kill_macro(s, name):
    return replace_macro(s, name, lambda x: "")

def bib_index(bib_list, s):
    try:
        return bib_list.index(s.strip())
    except:
        return "?"

source_exps = [
    '(?sm)\\\\meetemail{.*?}(.*)\\\\end{document}',
    '(?sm)\\\\maketitle(.*)\\\\end{document}',
    '(?sm)\\\\thispagestyle{empty}(.*)\\\\end{document}'
    ]

def convert(text):
    source = None
    for exp in source_exps:
        source = re.search(exp, text)
        if source:
            break

    if not source:
        print("Error: Could not find source!", file=stderr)
        exit(1)

    source = source[1]

    # Remove comments
    source = "\n".join(list(map(lambda l: l if not '%' in l else l[0:l.find('%')], source.splitlines())))

    # Remove spacers
    source = source.replace('\\\\', '  \n')
    source = re.sub("~", " ", source)
    source = re.sub("\\\\ ", " ", source)
    source = re.sub("\\\\,", " ", source)
    source = re.sub("\\\\vspace\\*?{.*?}", "", source)
    source = re.sub("\\\\medskip", "", source)
    source = re.sub("\\\\noident", "", source)
    source = re.sub("\\\\noindent", "", source)
    source = re.sub("\\\\smallskip", "", source)


    # Handle itemize and enumerate
    source = re.sub("\\\\begin{itemize}(\\[.*\\])", "", source)
    source = re.sub("\\\\begin{enumerate}(\\[.*\\])?", "", source)
    source = re.sub("\\\\end{itemize}", "", source)
    source = re.sub("\\\\end{enumerate}", "", source)
    source = re.sub("\\\\item(\\[.*?\\])?", " - ", source)

    # Properly move '     - 's to the front of the line
    lines = source.split('\n')
    lines_new = []
    for line in lines:
        if line.strip().startswith("-"):
            lines_new.append("  -" + line.strip()[1:])
        else:
            lines_new.append(line)
    source = '\n'.join(lines_new)

    # Handle theorem
    source = re.sub("\\\\begin{theorem}", "**Theorem.**", source)
    source = re.sub("\\\\end{theorem}", "", source)

    source = re.sub("\\\\vspace\\*?{.*?}", "", source)

    # Remove useless commands
    source = re.sub("\\\\bibliography\\*?{.*?}", "", source)
    source = re.sub("\\\\newblock", "", source)
    source = kill_macro(source, "bibliographystyle")
    source = kill_macro(source, "hspace")
    source = kill_macro(source, "vspace")
    source = kill_macro(source, "affil")
    source = kill_macro(source, "meetemail")
    source = kill_macro(source, "urladdr")

    # Replace bolds
    source = replace_macro(source, "emph", lambda s: "**" + s + "**")
    source = replace_macro(source, "textbf", lambda s: "**" + s + "**")

    # Replace italics
    source = replace_macro(source, "textit", lambda s: "_" + s + "_")

    # Replace do nothings
    source = replace_macro(source, "paragraph", lambda s: s)
    source = replace_macro(source, "textsc", lambda s: s)

    # Handle {\xxstyle ...}
    source = replace_shapes(source)

    # Transform $ and \[ \] into $$
    source = re.sub("\\$", "$$", source)
    source = re.sub("\\\\\\[", "$$", source)
    source = re.sub("\\\\\\]", "$$", source)
    source = re.sub("\\\\\\(", "$$", source)
    source = re.sub("\\\\\\)", "$$", source)

    # Replace `` '' and `
    source = re.sub("``", "\"", source)
    source = re.sub("''", "\"", source)
    source = re.sub("`", "'", source)

    # Special characters
    source = source.replace("\\|", "\\\\mid")
    source = source.replace("{\\'e}", "é")
    source = source.replace("{\\'a}", "á")
    source = source.replace("\\\\ss", "ß")

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
       lambda m: "[{}]".format(",".join(list(map(lambda s: "{}".format(bib_index(bib_list, s)), m[1].split(","))))),
       source)

    return source

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python {} <latex file>".format(argv[0]), file=stderr)
        exit(1)

    f = open(argv[1])
    text = f.read()
    f.close()

    converted = convert(text)
    print(converted)

