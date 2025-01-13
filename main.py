def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    #book_report = build_book_report(chars_dict)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    book_report_start = f"---------My book report on {book_path}---------"
    book_report_end = f"---------------------------------------------------------------"
    print(book_report_start)
    for letters in chars_sorted_list:
         #print(f"{letters[letter]} has {letters[num]} occuranced")
         print(f"{letters[0]} has {letters[1]} occuranced")
    print(book_report_end)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        elif lowered not in chars and lowered.isalpha() == True:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    return sorted(num_chars_dict.items(), key=lambda item: item[1], reverse=True)
main()