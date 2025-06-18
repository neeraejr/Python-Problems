#                 ✅ Problem 1: Reverse words in a sentence
# Input: "I love GenAI"
# Output: "GenAI love I"

st= input("Enter your String: ")
words = st.split()
rev = words[::-1]
st2 = " ".join(rev)
print(st2)