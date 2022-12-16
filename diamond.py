star = 4
n = 1
count = star
reverse_count = False
repeat = star % 2 == 0

while n > 0:
    if n == star:
        reverse_count = True
        if repeat:
            print(count * " " + n * "* ")
            repeat = False

    if not reverse_count:
        print(count * " " + n * "* ")
        n = n + 1
        count = count - 1
    else:
        print(count * " " + n * "* ")
        n = n - 1
        count = count + 1
