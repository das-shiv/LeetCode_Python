class Solution:
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        common_length = gcd(len(str1), len(str2))
        return str1[:common_length]

# Example usage:
solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
result = solution.gcdOfStrings(str1, str2)
print(result)
