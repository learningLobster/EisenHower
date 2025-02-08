from tabulate import tabulate

# Table left column
IMPORTANT, URGENT, NOT_URGENT, NOT_IMPORTANT = ["important"], ["urgent"], ["not urgent"], ["not important"]
matrix = []

# first_sub_list = important, second_sub_list = urgent, third_sub_list = not urgent, fourth_sub_list = not important
def add_element(main_list, first_sub_list, second_sub_list, third_sub_list, fourth_sub_list):
    """
    This method creates a EisenHower matrix.

    Parameters:
        main_list (list): The main list containing all elements.
        first_sub_list (list): table left column, first row(important).
        second_sub_list (list): table left column, second row(urgent).
        third_sub_list (list): table left column, third row(not urgent).
        fourth_sub_list (list): table left column, fourth row(not important).

    Returns:
        None.

    Action:
        - Checks if 'not' is present in the element.
        - Decides which sublist to place the element into.

    Example:
        >>> main = []
        >>> first, second, third, fourth = ["important"], ["urgent"], ["not urgent"], ["not important""]
        >>> add_element(main, first, second, third, fourth)
    """

    new_element = input("Enter the element: \n-> ").lower()
    importance = input("Enter the importance: 'important' or 'not important': \n-> ").lower()
    urgency = input("Enter the urgency: 'urgent' or 'not urgent': \n-> ").lower()

    if 'not' in importance and 'not' in urgency:
        fourth_sub_list.append(new_element)
        third_sub_list.append(new_element)

    elif 'not' in importance and 'not' not in urgency:
        fourth_sub_list.append(new_element)
        second_sub_list.append(new_element)

    elif 'not' not in importance and 'not' in urgency:
        first_sub_list.append(new_element)
        third_sub_list.append(new_element)

    else:
        first_sub_list.append(new_element)
        second_sub_list.append(new_element)

    main_list.append(IMPORTANT)
    main_list.append(URGENT)
    main_list.append(NOT_URGENT)
    main_list.append(NOT_IMPORTANT)

def display_matrix(element):
    # table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
    print(tabulate(element, tablefmt="grid"))


add_element(matrix, IMPORTANT, URGENT, NOT_URGENT, NOT_IMPORTANT)
display_matrix(matrix)