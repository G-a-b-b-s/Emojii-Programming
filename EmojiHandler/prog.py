import spacy

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("emoji", first=True)
with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read()
doc = nlp(text)
assert doc._.has_emoji is True
assert doc[0]._.is_emoji is True
assert doc[1]._.is_emoji is True
for elem in doc:
     print(elem._.emoji_desc)
