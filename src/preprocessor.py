from src.scraper import scrap_web
import re

scrap_text=scrap_web('https://makemeawake.blogspot.com/2024/10/the-golden-rule-of-communication-focus.html')

def text_preprocessing(text):
    text=text.lower()
    text=re.sub('[^a-z]',' ',text)
    return text

tokens=text_preprocessing(scrap_text)
print(tokens)




