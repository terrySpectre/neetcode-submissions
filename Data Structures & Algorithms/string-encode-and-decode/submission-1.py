class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += f"{len(i)}#{i}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            start_of_the_word = j + 1
            end_of_the_word = start_of_the_word + length

            decoded_strings.append(s[start_of_the_word:end_of_the_word]) 
            i = end_of_the_word
            
        return decoded_strings
