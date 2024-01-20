class Solution:
    def mergeAlternately(self, word1, word2):
        # Initialize an empty list to store the merged characters
        merged_chars = []

        # Determine the length of the shorter word
        min_len = min(len(word1), len(word2))

        # Iterate through the characters of both words up to the length of the shorter word
        for i in range(min_len):
            # Add the character from word1
            merged_chars.append(word1[i])
            # Add the character from word2
            merged_chars.append(word2[i])

        # Check if word1 is longer than word2
        if len(word1) > len(word2):
            # Append the remaining characters of word1 to the merged list
            merged_chars.extend(word1[min_len:])
        # Check if word2 is longer than word1
        elif len(word2) > len(word1):
            # Append the remaining characters of word2 to the merged list
            merged_chars.extend(word2[min_len:])

        # Join the merged characters into a string and return the result
        result = ''.join(merged_chars)
        return result

# Example usage:
solution_instance = Solution()
param_1 = "Hello"
param_2 = "hi"
ret = solution_instance.mergeAlternately(param_1, param_2)
print(ret)
