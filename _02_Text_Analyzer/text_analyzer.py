import streamlit as st

st.set_page_config(
    page_title="Text Analyzer Web",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Text Analyzer Web")
st.markdown("## This web application allows you to analyze text using the Text Analyzer library.")
st.markdown("---")

text = st.text_area("Enter your text here:", height=100)
split_text = text.split()
word_count = len(split_text)
char_count = len(text)

if text:
    st.markdown("## Word Count")
    st.write(f"### Number of words in the above paragraph:", str(word_count))
    st.markdown("## Character Count")
    st.write(f"### Number of characters in the above paragraph:", str(char_count))

    st.markdown("## Vowel Count")
    st.write(f"### Number of vowels in the above paragraph:", str(sum(1 for char in text.lower() if char in 'aeiou')))
    st.markdown("## Average Word Length")
    st.write(f"### Your paragraph average word length is: {round(char_count / word_count,2)}")
else: 
    st.warning("Please enter some text to analyze.")
st.markdown("---")
st.markdown("## Word Search")
word_search = st.text_input("Enter the word to search: ", key="word_search")

if word_search:
    st.write(f"### Your word found at index: {text.find(word_search)}")
else:
    st.warning("Please enter a word to search.")

st.markdown("---")
st.markdown("## Word Replacement")
word_replace = st.text_input("Enter the word to replace: ")

if word_search and word_replace:
    st.success(f"### Your word replaced: {text.replace(word_search, word_replace)}")
else:
    st.warning("Please enter a word to search and replace.")

st.markdown("---")
st.markdown("## Case Conversion")
case_conversion = st.radio("Select case conversion:", (None,"Uppercase", "Lowercase"))
if case_conversion == "Uppercase":
    st.write(f"### Uppercase: {text.upper()}")
elif case_conversion == "Lowercase":
    st.write(f"### Lowercase: {text.lower()}")
else:
    st.warning("Please select a case conversion.")

st.markdown("---")
st.markdown("## Word Search in Paragraph using *comparison* operator '=='")  
para_search = st.text_input("Enter the word to search: ", key="para_search")
if para_search:
    for word in split_text:
        if word.lower() == para_search.lower():
            st.success(f"### Your paragraph contains word {para_search}")

st.markdown("---")
if para_search:
    st.markdown("## Word search using *in* membership operator")
    if para_search.lower() in text.lower():
        st.success(f"### Your text contains the word {para_search}")
