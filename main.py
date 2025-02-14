def main(path_to_file):
    char_count = {"a" : 0}

    with open(path_to_file) as f:
        file_contents = f.read().lower()
        word_number = len(file_contents.split())
        print (f"--- Begin report of {path_to_file} ---")
        print (f"{word_number} words found in the document")
        for character in file_contents:
            if character.isalpha():
                if character in char_count:
                    char_count[character] += 1
                else:
                    char_count[character] = 1

    for char, count in char_count.items():
        print(f"The '{char}' was found {count} times")
    print(f"--- End report ---")

main("./books/frankenstein.txt")