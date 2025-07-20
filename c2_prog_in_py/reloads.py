import importlib
import filechanges

def changes():
    filechanges.print_changes()


for i in range(3):
    changes()
    input('Hit enter to reload')
