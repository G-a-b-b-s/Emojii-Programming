import spacy


class EmojiReader:
    """
    A class used to read and process a text file with emojis.

    ...

    Attributes
    ----------
    path : str
        a string representing the path to the text file

    Methods
    -------
    read():
        Reads the content of the file at the given path.
    convertText():
        Converts the text read from the file, replacing emojis with their descriptions.
    """

    def __init__(self, path):
        """
        Constructs all the necessary attributes for the EmojiReader object.

        Parameters
        ----------
            path : str
                a string representing the path to the text file
        """
        self.path = path

    def read(self):
        """
        Reads the content of the file at the given path.

        Returns
        -------
        str
            a string representing the content of the file
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            return file.read()

    def convertText(self, output_file):
        """
        Converts the text read from the file, replacing emojis with their descriptions.

        Returns
        -------
        str
            a string representing the converted text
        """
        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("emoji", first=True)
        doc = nlp(self.read())
        new_text = []
        for token in doc:
            # If the token is an emoji, append its description to the new text in a form < >
            if token._.is_emoji:
                new_text.append(f"<{token._.emoji_desc}>")
            # If the token is not an emoji, append the token itself
            else:
                new_text.append(token.text)

        # Join the new text into a single string
        new_text = ' '.join(new_text)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(new_text)
        # Now new_text contains the original text with emojis replaced by their descriptions
        return new_text