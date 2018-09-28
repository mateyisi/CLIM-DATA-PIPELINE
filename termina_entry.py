#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:38:46 2018

@author: mohau
"""

import tkinter as tk
from os import system as cmd

root = tk.Tk()
termf = tk.Frame(root, height=700, width=1000)
termf.pack(fill=tk.BOTH, expand=tk.YES)
wid = termf.winfo_id()

f=tk.Frame(root)
tk.Label(f,text="/dev/pts/").pack(side=tk.LEFT)
tty_index = tk.Entry(f, width=3)
tty_index.insert(0, "1")
tty_index.pack(side=tk.LEFT)
#tk.Label(f,text="Command:").pack(side=tk.LEFT)
#e = tk.Entry(f)
#e.insert(0, "ls -l")
#e.pack(side=tk.LEFT,fill=tk.X,expand=1)

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    command="ls -l"
    tty="/dev/pts/%s" % tty_index.get()
    cmd("%s <%s >%s 2> %s" % (command,tty,tty,tty))

#e.bind("<Return>",send_entry_to_terminal)
b = tk.Button(f,text="Send", command=send_entry_to_terminal)
b.pack(side=tk.LEFT)

f.pack(fill=tk.X, expand=1)

cmd('xterm -into %d -geometry 160x50 -sb -e "tty; sh" &' % wid)

root.mainloop()