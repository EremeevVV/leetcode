from dataclasses import dataclass

@dataclass
class Category:
    id: int
    parend_id: int|None

def create_tree(lst:list[Category]) -> dict:
    tree = {}
    return tree