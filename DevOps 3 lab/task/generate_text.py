def generate_text():
    text = "Hello, World!"
    return text


def save_text_to_file(text, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(text)


if __name__ == "__main__":
    generated_text = generate_text()
    save_text_to_file(generated_text)
    print(generated_text)
