#!/usr/bin/pyton

import re

def nonrep(stg):
h = {}
for ch in stg:
if ch in h:
return ch;
else:
h[ch] = 0
return '\0'



nonrep("sidhumannesiddhardhaboby")
