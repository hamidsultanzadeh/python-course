len_figure = int(input("Type length figure : "))


def draw_space(len_space):
    for l in range(len_space):
        print(end=" ")


def draw_slash(len_space):
    draw_space(len_figure - len_space)
    print("/", end="")
    draw_space(len_space-1)


def draw_backslash(len_space):
    draw_space(len_space-1)
    print("\\", end="")
    draw_space(len_figure - len_space)


for i in range(1, len_figure*2+1):
    if i <= len_figure:
        draw_slash(i)
        draw_backslash(i)
    else:
        draw_backslash(i-len_figure)
        draw_slash(i-len_figure)
    print()

