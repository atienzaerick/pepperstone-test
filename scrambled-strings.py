""" Pepperstone - Scrambled Strings
    Sytax for running:
    python3 scrambled-strings.py dict.txt input.txt
"""
import sys
import re

class ProcessDictionary():
    """class to process input file dictionary"""
    def __init__(self, input_file):
        self.dictionary_lookup = self.set_dictionary_lookup(input_file)

    # ----------------------------------------------------------------------#
    def set_dictionary_lookup(self, input_file) -> dict:
        """inserts lines in dictionary file to a dictionary"""
        dictionary = {}
        with open(input_file, "r") as dict_file:
            for line in dict_file:
                if dictionary.get(line.strip()):
                    print("duplicate record")
                else:
                    dictionary[line.strip()] = 1
        return dictionary

    # ----------------------------------------------------------------------#
    def get_dictionary_lookup(self,) -> dict:
        """gets dictionary lookup"""
        return self.dictionary_lookup

class ProcessInput():
    """class to process input file"""
    def __init__(self, input_file, dict_lookup) -> None:
        self.input_list = self.set_input_lookup(input_file)
        self.dictionary_input = dict_lookup.get_dictionary_lookup()
        self.output_list = self.count_word_ocurrence(self.dictionary_input)
        self.print_output(self.output_list)

    # ----------------------------------------------------------------------#
    def set_input_lookup(self, input_file) -> list:
        """appends lines from input file into a list"""
        with open(input_file, "r") as file:
            input_list = [line.strip() for line in file]

        return input_list

    # ----------------------------------------------------------------------#
    def count_word_ocurrence(self, dict_lookup) ->list:
        """Counts number of items in dictionary that's in the input"""
        output = []
        for line in self.input_list:
            print("\nLOG: *NEW INPUT LINE*")
            count = 0
            for key in dict_lookup:
                found = False
                print("\nLOG: Dictionary key =", key)
                if len(key) > len(line):
                    print("LOG: out of range!")
                    continue
                for match in re.finditer(key[0], line):
                    prospect_word = line[match.start():len(key) + match.start()]
                    if prospect_word[-1] == key[-1]:
                        if sorted(key) == sorted(prospect_word):
                            print("LOG: sorted key =  ", sorted(key))
                            print("LOG: sorted match =", sorted(prospect_word))
                            found = True
                if found:
                    print("LOG: Matched!")
                    count += 1
            output.append(count)
        return output

    # ----------------------------------------------------------------------#
    def print_output(self, output_list) -> None:
        """print final output"""
        print("\n\n\n")
        print("*FINAL OUTPUT*")
        for index, output in enumerate(output_list):
            print("Case #", index+1, ": ", output)

def main(dictionary_lookup, input_lookup):
    """Main Execution"""
    input_dictionary = ProcessDictionary(dictionary_lookup)
    ProcessInput(input_lookup, input_dictionary)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
