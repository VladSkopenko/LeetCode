class Solution:
    def isValid(self, s: str) -> bool:
        open_brack = []  # Создал список для хранения открытых дужок
        mapping = {")": "(", "}": "{", "]": "["}  # Словарь соответсвий
        for char in s:
            if char in mapping:
                top_element = open_brack.pop() if open_brack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                open_brack.append(char)

        return not open_brack
