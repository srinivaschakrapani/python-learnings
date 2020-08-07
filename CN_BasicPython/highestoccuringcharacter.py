def highestoccuringcharacter(str):
    freq = [0] * 128
    for i in str:
        freq[ord(i)] += 1
    print(freq)
    maxfreqchar = chr(97)
    maxfreq = freq[0]
    for i in str:
        if maxfreq < freq[ord(i)]:
            maxfreqchar = i
            maxfreq = freq[ord(i)]
    print(maxfreqchar)


highestoccuringcharacter("cde")

# a = 3
# b = 4
# d = 1
# e = 1
# f = 2
# g = 1
