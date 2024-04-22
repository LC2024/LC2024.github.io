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

    # source = re.search("(?sm)\\\\meetemail{.*?}(.*)\\\\end{document}", text)
    # source = re.search("(?sm)\\\\maketitle(.*)\\\\end{document}", text)
    source = re.search("(?sm)\\\\thispagestyle{empty}(.*)\\\\end{document}", text)
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
    source = re.sub("\\\\emph{(.*?)}", "**\\1**", source)
    source = re.sub("{\\\\em (.*?)}", "**\\1**", source)
    source = re.sub("{\\\\bfseries (.*?)}", "**\\1**", source)

    # Replace italics
    source = re.sub("\\\\textit{(.*?)}", "_\\1_", source)
    source = re.sub("{\\\\itshape (.*?)}", "_\\1_", source)

    source = re.sub("{\\\\scshape (.*?)}", "\\1", source)

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
