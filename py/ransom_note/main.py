class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        if 1 <= len(ransom_note) <= 10 ** 5 and 1 <= len(magazine) <= 10 ** 5:
            reference = magazine
            for letter in ransom_note:
                if letter not in reference:
                    return False
                reference = reference.replace(letter, "", 1)
            return True
        return False


if __name__ == '__main__':
    solution = Solution().can_construct(ransom_note="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
    print(solution)
