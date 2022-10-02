#!/usr/bin/python3
"""markdownhtml"""
from sys import argv, stderr
from os import path

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)

    if path.exists(argv[1]) == False:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)

    with open(argv[1], "r") as fd:
        lines = fd.readlines()

        html_list = []
        ul_list = []
        ol_list = []
        for line in lines:
            sentence = line.split(" ")
            chtr = sentence[0]
            text = " ".join(sentence[1:]).replace("\n", "")

        if chtr[0] == "-":
            ul_flag = True
            ol_flag = False
            ul_list.append("<li>{}</li>\n".format(text))

        if chtr[0] == "*":
            ol_flag = True
            ul_flag = False
            ol_list.append("<li>{}</li>\n".format(text))

        if len(ul_list) >= 1:
            if ul_flag == False or line == lines[-1]:
                str_ul = "".join(ul_list)
                str_ul = "<ul>\n" + str_ul + "</ul>\n"
                html_list.append(str_ul)

        if len(ol_list) >= 1:
            if ol_flag == False or line == lines[-1]:
                str_ol = "".join(ol_list)
                str_ol = "<ol>\n" + str_ol + "</ol>\n"
                html_list.append(str_ol)

        if chtr[0] == "#":
            ul_flag = False
            ol_flag = False
            html_list.append("<h{0}>{1}</h{0}>\n".format(len(chtr), text))

    with open (argv[2], "w") as nfd:
        nfd.writelines(html_list)

    exit(0)
