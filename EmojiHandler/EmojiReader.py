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

    def __init__(self, path=None):
        """
        Constructs all the necessary attributes for the EmojiReader object.

        Parameters
        ----------
            path : str
                a string representing the path to the text file
        """
        self.path = path

    def read(self, path="C:\\Users\\martyna\\PycharmProjects\\teoriaKompilatorow\\Emojii-Programming\\EmojiHandler\\emojiList"):
        """
        Reads the content of the file at the given path.

        Returns
        -------
        str
            a string representing the content of the file
        """
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def returnDict(self):
        emoji_dict = {}
        lines = self.read()
        for i, line in enumerate(lines):
            # Ignore lines that do not contain a colon

            if ':' not in line:
                continue

            # Split the line at the first colon
            emoticon, description = line.split(':', 1)

            # Strip leading and trailing whitespace from the emoticon and description
            emoticon = emoticon.strip().strip('"').strip("'").lower()
            description = description.strip().strip('"').strip("'")

            # Add the emoticon and its description to the dictionary

            emoji_dict[description] = emoticon
        del emoji_dict['**']
        emoji_dict['🖇️']=':'
        return emoji_dict

    def replace_words_with_dict_values(self, text = None):
        if text is None:
            path = self.path
            lines= self.read(path)
        else:
            lines = text.splitlines()
        dictionary = self.returnDict()
        # Iterate over elements and replace if found in the dictionary
        replaced_text = []
        for line in lines:
            # Check if element is in the dictionary
            for element in line.split():
                if element in dictionary:
                    replaced_text.append(dictionary[element])
                else:
                    replaced_text.append(element)
            replaced_text.append('\n')

        # Join the replaced elements back into a string
        replaced_text = ' '.join(replaced_text)

        return replaced_text

    def convertToFile(self, pathToFile):
        replaced_text = self.replace_words_with_dict_values()
        with open (pathToFile, 'w', encoding='utf-8') as filename:
            filename.write(replaced_text)


