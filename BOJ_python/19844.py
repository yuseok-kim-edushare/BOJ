fr_vowel = ['a','e','i','o','u','h']
pre_words = ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu']

source1 = input().replace('-',' ').split()
ans=len(source1)

for a in source1:
    if a[0] == """'""":
        a = a[1:]
    if a[-1] == """'""":
        a = a[:-1:]
    t = a.split("""'""")
    if len(t)>1:
        if t[0] in pre_words and t[1][0] in fr_vowel:
            ans+=1 #count를 올리지 않고, 분리한 단어를 이 logic으로 굴리면 null array도 카운트 될 수 있더라아아...
        else:
            pass
    else:
        pass
print(ans)
