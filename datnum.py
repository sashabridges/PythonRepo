def deeznums(stuff, stuff1, stuff2, stuff3):
    average = (stuff + stuff1 + stuff2 + stuff3) / 4
    return average

prompt = int(input("Enter numbers: "))
prompt1 = int(input("Enter numbers: "))
prompt2 = int(input("Enter numbers: "))
prompt3 = int(input("Enter numbers: "))
print(deeznums(prompt, prompt1, prompt2, prompt3))