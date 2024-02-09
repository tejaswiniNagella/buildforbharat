# #DEPENDED LIBRARY
# # pip install --upgrade googletrans==4.0.0-rc1 translate streamlit -q

#IMPORTING LIBRARIES
import googletrans
import translate
import streamlit as st

st.title("Language Translator")

translator = googletrans.Translator()
List_LANGUAGES = googletrans.LANGUAGES

user_input = st.text_input("Enter Text..!")

# COLLECTING LANGUAGES
languages = []  

for code, name in List_LANGUAGES.items():
    languages.append({name: code})

# SEPARATING NAME & CODE
languages_name = [list(i.keys())[0] for i in languages]  
lan_codes = [list(i.values())[0] for i in languages]

selected_languages = st.selectbox('', languages_name)

code = lan_codes[languages_name.index(selected_languages)]

# TRANSLATING
def translate_text(text):
    try:
        translated = translator.translate(text, dest=code)
        translated_text = translated.text
        return translated_text
    except Exception as e:
        pass

output = translate_text(user_input)
if output ==None:
    pass
else:
    st.header(output)
