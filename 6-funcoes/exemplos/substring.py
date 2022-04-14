def is_substring(str1, str2):
    esta = 0
    for i in str1:
        for j in str2:
            if i == j:
                esta += 1
                break
    if esta == len(str2): return True
    else: return False

assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')
