diamond = 5
star_count = diamond
space = 1
reverse_count = False
repeat = diamond % 2 == 0

while star_count <= diamond:
    if star_count == 1:
        reverse_count = True
        if repeat:
            print(space * " " + star_count * "* ")
            repeat = False

    if not reverse_count:
        print(space * " " + star_count * "* ")
        star_count = star_count - 1
        space = space + 1
    else:
        print(space * " " + star_count * "* ")
        star_count = star_count + 1
        space = space - 1
