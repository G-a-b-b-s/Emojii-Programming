
import emojis

def translator(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()

    rendered = emojis.decode(file_content)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(rendered)


print(emojis.decode(":bulb: add_numbers:last_quarter_moon_with_face:a :paperclip: b:first_quarter_moon_with_face::paperclips:"))