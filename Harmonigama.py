# Mapping for sa re ga ma to harmonica hole numbers
HARMONICA_MAPPING = {
    "sa": "4",
    "re": "(4)",
    "ga": "5",
    "ma": "(5)",
    "pa": "6",
    "dha": "(6)",
    "ni": "7",
    "sa'": "(7)",
    "sa*": "1",
    "re*": "(1)",
    "ga*": "2",

}

# Mapping for sa re ga ma to Western notes in C major
WESTERN_NOTES_MAPPING = {
    "sa": "C",
    "re": "D",
    "ga": "E",
    "ma": "F",
    "pa": "G",
    "dha": "A",
    "ni": "B",
    "sa'": "C",  # Higher octave sa
}

def notes_to_harmonica(notes: str) -> str:
    """
    Convert sa re ga ma notes to harmonica hole numbers.
    """
    note_list = notes.split()
    harmonica_output = [
        HARMONICA_MAPPING.get(note, f"Unknown({note})") for note in note_list
    ]
    return " | ".join(harmonica_output)


def notes_to_western(notes: str) -> str:
    """
    Convert sa re ga ma notes to Western music notes (C, D, E, etc.).
    """
    note_list = notes.split()
    western_output = [
        WESTERN_NOTES_MAPPING.get(note, f"Unknown({note})") for note in note_list
    ]
    return " | ".join(western_output)


def main():
    print("Choose an option:")
    print("1. Convert sa re ga ma to harmonica hole numbers")
    print("2. Convert sa re ga ma to Western notes (C, D, E, etc.)")
    
    try:
        choice = int(input("Enter your choice (1 or 2): ").strip())
        notes = input("Enter notes in sa re ga ma format: ").strip()
        
        if choice == 1:
            result = notes_to_harmonica(notes)
            print("\nHarmonica translation:")
        elif choice == 2:
            result = notes_to_western(notes)
            print("\nWestern notes translation:")
        else:
            print("Invalid choice. Please select 1 or 2.")
            return
        
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number (1 or 2).")


if __name__ == "__main__":
    main()