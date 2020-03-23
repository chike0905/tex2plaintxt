#!python3.6
import sys
import re

'''
line2command function parse \newcommand line. Like followings;
\newcommand{\PF}{personal fabrication}
Output:
    cmd - command (ex. PF)
    text - texst (ex. personal fabrication)
'''
def line2command(line):
    m = re.search('\{.*\}\{', line)
    cmd = m.group()[2:-2]
    m = re.search('\}\{.*\}\n', line)
    text = m.group()[2:-2]
    return [cmd, text]

def convertplain(line, cmds):
    tmp = line
    for cmd in cmds:
        if "\\"+cmd[0] in line and "\\newcommand" not in line:
            tmp = re.sub("\~", " ", tmp)
            tmp = re.sub("\\\\"+cmd[0], cmd[1], tmp)
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
        output += convertplain(line, cmds)
    
    with open(path[:-4]+".txt", mode='w') as f:
        f.write(output)
