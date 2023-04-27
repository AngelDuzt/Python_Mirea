import graphviz
import os
def print_tree(path, dot, indent='    '):
    for file in os.listdir(path):
        dot.node(file)
        fullpath = path + "/" + file
        dot.edge(path.split('/')[-1], file)
        print(indent + file)
        dot.node(file)
        if os.path.isdir(fullpath):
            print_tree(fullpath, dot, indent+'    ')
            if fullpath.split('/')[-1] != file:
                dot.edge(fullpath.split('/')[-1], file)

path = r'C:/Users/dasda/PycharmProjects/pythonProject/MireaPython/Kis'
print(path.split('\\')[-1])
dot = graphviz.Digraph('diagramm')
print_tree(path, dot)
dot.render(directory='doctest-output').replace('\\', '/')