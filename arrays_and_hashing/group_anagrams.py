def groupAnagrams(self, strs):
    string_table = {}

    # for each string
    for string in strs:
        # sort it
        # becuase all sorted strings of anagrams
        # would be the same
        sorted_string = "".join(sorted(string))

        # check if the sorted string is in the table
        if sorted_string not in string_table:
            # if not create the list for that group
            string_table[sorted_string] = []
            
        # add string to that group
        string_table[sorted_string].append(string)

    # return the list of lists
    return list(string_table.values())

