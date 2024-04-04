import os


def random_symbols_string(length=5):
    import random
    import string

    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    return res


def save_text_to_file(filename: str, text: str) -> str:
    output_filename = f"{filename}_{random_symbols_string()}.txt"
    print(f"Saving text to a file {output_filename}...")

    path = os.path.join('generated', output_filename)

    # Save the text to a .txt file
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Done.\n")

    return output_filename


def read_text_from_file(filename: str) -> str:
    path = os.path.join('generated', filename)

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text
