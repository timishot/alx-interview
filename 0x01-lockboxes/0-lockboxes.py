#!/usr/bin/python3

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False
    
    for index, innerBox in enumerate(boxes):
        if index == len(boxes) - 1 and len(innerBox) == 0:
            return True
        if len(innerBox) == 0:
            return False
    
    return True
