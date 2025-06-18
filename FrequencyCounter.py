#                     ✅ Problem 2: Count frequency of each word in a sentence
# Input: "hello world hello"
# Output:
#     hello = 2  
#     world = 1

st = input("Enter String: ")
words = st.split()
for w in set(words):
    print(f"{w} = {words.count(w)}")