


def display_matrix(element):
    # table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
    print(tabulate(element, tablefmt="grid"))


add_element(matrix, IMPORTANT, URGENT, NOT_URGENT, NOT_IMPORTANT)
display_matrix(matrix)