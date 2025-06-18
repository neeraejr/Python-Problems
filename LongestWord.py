#                   2. Find longest word in a sentence
# Input: "GenAI is extremely powerful" → Output: extremely
st = input("Enter string: ")
l = st.split()
LongestWord = ""
for word in l:
    if len(word)>len(LongestWord):
        LongestWord=word

print(f"Longest Word: {LongestWord}")    