def height_prct(screen_height, percentage):
    """
        Returns a percentage.
    """
    return (screen_height / 100) * percentage

def width_prct(screen_width, percentage):
    """
        Returns a percentage.
    """
    return (screen_width / 100) * percentage


# first_sub_list = important, second_sub_list = urgent, third_sub_list = not urgent, fourth_sub_list = not important
def add_element(main_list, new_element, importance, urgency):
    """
    This method creates a EisenHower matrix.

    Parameters:
        main_list (list): The main list containing all elements.
        new_element (string): element added to the main list.
        importance (string): importance of the element.
        urgency (string): urgency of the element.

    Returns:
        None.

    Action:
        - Checks if 'not' is present in the element.
        - Decides which sublist to place the element into.

    Example:
        >>> main = []
        >>> new_element, importance, urgency= "money", "important", "urgent"
        >>> add_element(main, new_element, importance, urgency)
    """
    # import + not urgent, not important + urgent, not important + not urgent, important + urgent
    first_sub_list = main_list[0]
    second_sub_list = main_list[1]
    third_sub_list = main_list[2]
    fourth_sub_list = main_list[3]

    if 'not' in importance and 'not' in urgency:
        first_sub_list.append(new_element)

    elif 'not' in importance and 'not' not in urgency:
        second_sub_list.append(new_element)

    elif 'not' not in importance and 'not' in urgency:
        third_sub_list.append(new_element)

    else:
        fourth_sub_list.append(new_element)

