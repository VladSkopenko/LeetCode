"""You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old."""
from typing import List

inp = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
inp2 = ["1313579440F2036", "2921522980M5644"]


class Solution:
    @classmethod
    def countSeniors(cls, details: List[str]) -> int:
        count = 0
        for element in details:
            if int(element[11:13]) > 60:
                print(element[11:13])
                count += 1
        return count


if __name__ == "__main__":
    print(Solution.countSeniors(inp2))
