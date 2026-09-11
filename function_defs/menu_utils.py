"""Menu utility functions for input validation and selection."""

from function_defs.helper_functions import typewriter


def get_menu_selection(items, show_items=True):
    """
    Safely get menu selection from user input.
    
    Args:
        items: List of items to select from
        show_items: Whether to display items before getting input
    
    Returns:
        Selected item or None if invalid selection
    """
    if not items:
        typewriter("Your options are empty.")
        return None
    
    if show_items:
        for i, item in enumerate(items, 1):
            typewriter(f"{i}. {item}")
    
    choice = input("> ")
    
    if not choice.isdigit():
        return None
    
    index = int(choice) - 1
    
    if 0 <= index < len(items):
        return items[index]
    
    return None


def get_menu_index(items, show_items=True):
    """
    Get the index of selected menu item.
    
    Args:
        items: List of items to select from
        show_items: Whether to display items before getting input
    
    Returns:
        Index of selected item or None if invalid selection
    """
    if not items:
        typewriter("Your options are empty.")
        return None
    
    if show_items:
        for i, item in enumerate(items, 1):
            typewriter(f"{i}. {item}")
    
    choice = input("> ")
    
    if not choice.isdigit():
        return None
    
    index = int(choice) - 1
    
    if 0 <= index < len(items):
        return index
    
    return None
