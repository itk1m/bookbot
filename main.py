import sys
from stats import get_num_words, get_uniq_char, get_sort_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # get the texts from the books directory
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    uniq_dict = get_uniq_char(text)
    chars_sorted_list = get_sort_dict(uniq_dict)
    print_report(book_path, num_words, chars_sorted_list)


# reads the file and returns the file as a string
# using the relative path as the argument
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in chars_sorted_list:
        if "a" <= items["char"] <= "z":
            print(f"{items['char']}: {items['num']}")
        continue

    print("============= END =============")


main()
