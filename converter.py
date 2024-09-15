from openpyxl import *

# '$' signals a lower octave
# '&' signals a natural

CONVERSION_TABLE = {
    "$F#": 0,
    "$G": 1,
    "$G#": 2,
    "$A": 3,
    "$A#": 4,
    "$B": 5,
    "$C": 6,
    "$C#": 7,
    "$D": 8,
    "$D#": 9,
    "$E": 10,
    "$F": 11,
    "$F#": 12,
    "G": 13,
    "G#": 14,
    "A": 15,
    "A#": 16,
    "B": 17,
    "C": 18,
    "C#": 19,
    "D": 20,
    "D#": 21,
    "E": 22,
    "F": 23,
    "F#": 24,
    "-": 99
}

# (work in progress)
COORDINATES = {
    "": ""
}

class Converter:
    def __init__(self, filename, scale, scaletype):
        self.filename = filename
        self.scale = scale
        self.scaletype = scaletype

    def get_notes(self, sheet_name):
        workbook = load_workbook(self.filename, sheet_name)
        sheet = workbook[sheet_name]

        notes = []
        for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):
            value = row[0]  # Get the value in column A
            if value != None:
                notes.append(value)

        return notes
    
    def convert_notes_to_numbers(self, notes):
        toReturn = []
        for note in notes:
            corresponding_number = CONVERSION_TABLE[note.replace("&", "")]
            if note.replace("$", "") in self.scale:
                if self.scaletype == "flat":
                    corresponding_number -= 1
                elif self.scaletype == "sharp":
                    corresponding_number += 1
            toReturn.append(corresponding_number)
        return toReturn
    
    def return_five_bit_binary(self, n):
        return self.do_five_bits(n, [], 4)

    def do_five_bits(self, n, bits, digit):
        if digit < 0:
            return bits
        else:
            if n - 2 ** digit >= 0:
                bits.append(1)
                return self.do_five_bits(n - 2 ** digit, bits, digit - 1)
            else:
                bits.append(0)
                return self.do_five_bits(n, bits, digit - 1)


if __name__ == '__main__':
    c = Converter("songs.xlsx", ['B', 'E'], "flat") # b flat major
    notes = c.get_notes("SuperIdol")
    print(notes)
    numbers = c.convert_notes_to_numbers(notes)
    print(numbers)