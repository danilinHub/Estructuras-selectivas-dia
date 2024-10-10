x = 28

if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20  ")

print("estudiar los sabados", end='')
print("es genial")

#parametro end y sep

print("danieal", "luis", "carlos", "camila")# agrega un espacio
print("danieal", "luis", "carlos", "camila",sep="")#quota el espacio
print("danieal", "luis", "carlos", "camila",sep=",")#agrega una coma

print("danieal", "luis", "carlos", "camila",sep="_", end="_Curso_Python")#implementacion end y sep 