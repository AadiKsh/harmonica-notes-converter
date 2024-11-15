# Mapping for notes to harmonica hole numbers with 
# Example is for a diatonic harmonica in C
NOTE_MAPPING = {
    "sa": "4",       # Blow
    "re": "(4)",    # Suck
    "ga": "5",       # Blow
    "ma": "(5)",    # Suck
    "pa": "6",       # Blow
    "dha": "(6)",   # Suck
    "ni": "7",       # Blow
    "sa'": "(7)",   # Suck (higher octave sa)
}

def notes_to_harmonica(notes: str):
    """
    Convert musical notes (sa, re, ga, ma, etc.) to harmonica hole numbers with blow/suck.
    
    Args:
        notes (str): A string of notes separated by spaces (e.g., "sa re ga ma").
    
    Returns:
        str: Harmonica hole numbers with blow/suck indications.
    """
    # Split the notes by spaces
    note_list = notes.split()
    
    # Convert notes to harmonica numbers
    harmonica_output = []
    for note in note_list:
        if note in NOTE_MAPPING:
            harmonica_output.append(NOTE_MAPPING[note])
        else:
            harmonica_output.append(f"Unknown({note})")
    
    return " | ".join(harmonica_output)


# Example Usage
if __name__ == "__main__":
    # Input notes from the user
    input_notes = input("Enter notes in sa re ga ma format: ")
    result = notes_to_harmonica(input_notes)
    print("\nHarmonica translation:")
    print(result)