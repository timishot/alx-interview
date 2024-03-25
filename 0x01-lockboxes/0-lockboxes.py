#!/usr/bin/python3
"""
lockboxes in python3
"""


def canUnlockAll(boxes):
    """
    Function that checks with a boolean value if the list type and
    length to invoke two for iterations: one to traverse the list
    and the other to compare if the key is idx or not in order to open
    """
    if not isinstance(boxes, list):
        return False

    for key in range(1, len(boxes) - 1):
        boxes_checked = any(key in box and key != idx for idx,
                            box in enumerate(boxes))
        if not boxes_checked:
            return False

    return True