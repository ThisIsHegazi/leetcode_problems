class Solution:
    def isValid(self, s: str) -> bool:
        par_pairs = {")": "(", "}": "{", "]": "["}
        opening_pars = {"(", "[", "{"}
        seen_stack = []
        for ch in s:
            if ch in opening_pars:
                seen_stack.append(ch)
            elif ch in par_pairs:
                if seen_stack and seen_stack[-1] == par_pairs[ch]:
                    seen_stack.pop()
                else:
                    return False
        return not seen_stack
