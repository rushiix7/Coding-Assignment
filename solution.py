def is_permutation_in_text(pattern, text):
    len_p = len(pattern)
    len_t = len(text)

    if len_p > len_t:
        return "NO"

 
    pattern_count = [0] * 26
    for ch in pattern:
        pattern_count[ord(ch) - ord('a')] += 1

 
    window_count = [0] * 26
    for ch in text[:len_p]:
        window_count[ord(ch) - ord('a')] += 1

    if pattern_count == window_count:
        return "YES"


    for i in range(len_p, len_t):
        new_char = text[i]
        old_char = text[i - len_p]

        window_count[ord(new_char) - ord('a')] += 1
        window_count[ord(old_char) - ord('a')] -= 1

        if pattern_count == window_count:
            return "YES"

    return "NO"

T = int(input())
for _ in range(T):
    pattern = input().strip()
    text = input().strip()
    print(is_permutation_in_text(pattern, text))
