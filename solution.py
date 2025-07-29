def check_function(pat, txt):
    n, m = len(pat), len(txt)
    if n > m:
        return "NO"
        
    freq_pat = [0] * 26
    for c in pat:
        freq_pat[ord(c) - ord('a')] += 1
        
    freq_win = [0] * 26
    for c in txt[:n]:
        freq_win[ord(c) - ord('a')] += 1

    if freq_pat == freq_win:
        return "YES"

    for idx in range(n, m):
        freq_win[ord(txt[idx]) - ord('a')] += 1
        freq_win[ord(txt[idx - n]) - ord('a')] -= 1
        if freq_win == freq_pat:
            return "YES"
    return "NO"

tests = int(input())
for _ in range(tests):
    pat = input().strip()
    txt = input().strip()
    print(check_function(pat, txt))
