class Solution:
    def encode(self, strs: list[str]) -> str:
        parts = []

        for word in strs:
            parts.append(str(len(word)) + "#" + word)

        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the end of the length field
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end

        return result