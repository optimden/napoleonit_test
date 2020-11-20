class Solution:
    def __init__(self):
        self.arabic = []
        self.matching = {"I": 1, "V": 5, "X": 10,
                        "L": 50, "C": 100, "D": 500,
                        "M": 1000}

    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            raise Exception("Incorrect string length.")
        # преобразовываю римские цифры в арабские
        for i, number in enumerate(s[::-1]):
            if number not in self.matching.keys():
                raise Exception("Incorrect letter at {} position.".format(i+1))
            self.arabic.append(self.matching[number])
            # если число в исходной строке меньше идущего
            # после него, тогда берем его со знаком минус
            if (i > 0) and (self.arabic[i]<self.arabic[i-1]):
                self.arabic[i] *= -1
        # вычисляю итоговое арабское число
        result = sum(self.arabic)
        if result < 1 or result > 3999:
            raise Exception("Arabic number is out of defined range.")
        return sum(self.arabic)
