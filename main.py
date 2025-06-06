from stats import count_words, count_characters, sorted_character_count
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

        return file_contents
    

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        
        path_to_file = sys.argv[1]
        book_text = get_book_text(path_to_file)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")

        number_of_words = count_words(book_text)
        character_counts = count_characters(book_text)
        sorted = sorted_character_count(character_counts)

        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")

        print("--------- Character Count -------")

        for dict in sorted:
            if str.isalpha(dict["char"]):
                print(f"{dict["char"]}: {dict["num"]}")

        print("============= END ===============")
    except FileNotFoundError as e:
        print(f"{path_to_file} not found")
    
    except Exception as e:
        print(e)
main()