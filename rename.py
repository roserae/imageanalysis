import os

PrevName = raw_input('current filename = ')
NewName = raw_input('new filename = ')

os.rename(PrevName, NewName)
