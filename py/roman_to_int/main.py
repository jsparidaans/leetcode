class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        for key in subtractions.keys():
            if key in s:
                answer += subtractions[key]
                s = s.replace(key, "", 1)
        for num in s:
            answer += numerals[num]
        return answer


numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
subtractions = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution().romanToInt("LVIII")
    print(solution)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
