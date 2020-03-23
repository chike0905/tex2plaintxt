#!python3.6
import sys
import re

def line2command(line):
    m = re.search('\{.*\}\{', line)
    cmd = m.group()[2:-2]
    m = re.search('\}\{.*\}\n', line)
    text = m.group()[2:-2]
    return [cmd, text]

def plain2latex(line, cmds):
    tmp = line
    for cmd in cmds:
        tmp = re.sub(" "+cmd[1]+" ", "~\\"+cmd[0]+"~", tmp)
        tmp = re.sub(" "+cmd[1]+",", "~\\"+cmd[0]+",", tmp)
        tmp = re.sub(" "+cmd[1]+"\.", "~\\"+cmd[0]+".", tmp)
    return tmp

if __name__ == '__main__':
    args = sys.argv
    path = args[1]
    with open(path) as f:
        l = f.readlines()
    
    commands = [i for i in l if "\\newcommand" in i and "[1]" not in i]
    cmds = [line2command(i) for i in commands]

    output = "" 
    for line in l:
        output += plain2latex(line, cmds)

    with open(path[:-4]+".fixed.tex", mode='w') as f:
        f.write(output)


