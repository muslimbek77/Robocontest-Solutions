def decode_and_find_kth(s: str, k: int) -> str:
    result = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            repeat_count = int(s[i])
            prev = ""
            # find the previous substring
            j = i - 1
            while j >= 0 and not s[j].isdigit():
                prev = s[j] + prev
                j -= 1
            result += prev * (repeat_count - 1)  # oldin bir marta qo‘shilgan bo‘ladi
            i += 1
        else:
            result += s[i]
            i += 1

        if len(result) >= k:
            return result[k - 1]
    return result[k - 1]

# Test
s = input().strip()
k = int(input())
print(decode_and_find_kth(s, k))
