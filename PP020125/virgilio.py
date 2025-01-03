# Imported os library to work with files
import os
# Imported math library to work with math operations
import math
# Imported json library to work with json
import json

# Created a class called Virgilio

class Virgilio:
    # Created a constructor as self and directory as parameters
    def __init__(self, directory):
        self.directory = directory  
        
    # Created a method called read_canto_lines for reading the canto from file and to format it and return the lines
    def read_canto_lines(self,canto_number):
        
        # Created a class called CantoNotFoundError extends Exception for a custom error managment
        class CantoNotFoundError(Exception):
            def __init__(self, message):
               super().__init__(message)
                     
        # Verify if canto_number is an integer
        
        if not (isinstance(canto_number,int)):
            raise TypeError("canto_number must be an integer")
        
        # Verify if canto_number is between 1 and 34 for raise exeption
        if canto_number < 1 or canto_number > 34:
            raise CantoNotFoundError("canto_number must be between 1 and 34")
        # Declare a variable called strip_lines that start with False
        strip_lines = False
        # Declare a variable called num_lines that start with None
        num_lines=None
      # Created a variable called file_path for storing the path of the file
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
      # Use try-except block for error handling and read the file
        try:
            # Open the file which is in read mode and utf-8 encoding
            with open(file_path, "r", encoding="utf-8") as file:
                # Read the lines of the file
                lines = file.readlines()
                # Print the lines only for debugging and testing
                #print(lines)
                # Return the lines
            # Verify if strip_lines is True and make the lines strip for all line using for cicle
            if strip_lines:
                 lines = [line.strip() for line in lines]
                 return lines
            # Verify if num_lines is not None and take the number of lines defined on num_lines value
            if num_lines is not None:
                 
                 lines = [lines for _ in range(num_lines)]
                 return lines
            return lines    
                
        except FileNotFoundError:
            # Print a message if the file is not found or if number of canto file is not found
            
            return print(f"File not found: {file_path}")
            # Print a message if there is an generic error 
        except Exception as e:
            
            return print(f"An error occurred: {e}")
        
        
        
    # Created a method called count_verses for counting the number of verses    
    def count_verses(self,canto_number):
            # Read the lines of the canto recalling last method for do this
            lines = self.read_canto_lines(canto_number)
            # Return the number of lines
            return len(lines)
    # Created a method called count_tercedi for counting the number of terzine    
    def count_tercets(self,canto_number):
        # Recall last method for do this and get the number of verses for divide by 3
        canto_number = self.count_verses(canto_number)/3
        # Return the number of terzine around using floor method of math library
        return math.floor(canto_number)
    # Created a method called count_word for counting the number of word in canto
    def  count_word(self,canto_number,word):
            # Recall last method for do this and get the number of lines for count the number of word in that       
            lines = self.read_canto_lines(canto_number)
            # Return the count of word in lines
            return lines.content.count(word)
    # Created a method called get_verse_whit_word for counting the number of word in canto    
    def get_verse_whit_word(self,canto_number,word):
            # Define an empty list that will store the lines
            line_list = []
            # Recall submethod of my first method for get lines
            lines = self.read_canto_lines(canto_number).readlines()
            # Cicle for each line and if the word is in the line, add the line to the list
            for line in lines:
                    if word in line:
                        line_list.append(line)
                        # Return the full list
                        return line_list
    # Defined a method called get_longest_verse for get the longest verse    
    def  get_longest_verse(self,canto_number):
        # Recall submethod of my first method for get lines
        lines = self.read_canto_lines(canto_number).readlines() 
        # Calculate the length of the longest line using max method of string
        longest_line = max(lines, key=len)
        # Return the longest line
        return longest_line
    # Defined a method called get_longest_canto for get the longest canto
    def get_longest_canto(self):
        # Define a dictionary that will store the longest canto
        longest_canto = {"canto_number": None, "canto_len": 0}
        # Cicle for each canto in range of 1 to 34
        for canto_number in range(1, 34):
            # Recall submethod of my first method for get lines
            lines = self.read_canto_lines(canto_number).readlines()
            # Calculate the length of the canto
            canto_len = sum(len(line) for line in lines)
            # If the length of the canto is greater than the current longest canto, update the longest canto
            if canto_len > longest_canto["canto_len"]:
                    # Update the longest canto with the current canto key
                    longest_canto["canto_number"] = canto_number
                    # Update the longest canto with the current canto value
                    longest_canto["canto_len"] = canto_len
        return longest_canto
    # Defined a method called count_words for count the number of word and write in json file
    def count_words(self,canto_number,word):
        # Define json file name
        json_file_name = "word_counts.json"
        # Define json file path and use os library to work with files
        json_file_path = os.path.join(os.getcwd(), json_file_name)
        # Define a dictionary that will store the word counts start with 0
        words_in_canto = {word: 0}
        # Recall submethod of my first method for get lines
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the content of the file
            content = file.read()
            # Cicle for each word in the content
            for word in content:
                # If the word is in the dictionary, add 1 to the count can do also words_in_canto[word] += 1
                words_in_canto[word] = content.count(word)
                
        # Open the json file        
        with open (json_file_path, "w") as json_file:
            # Write the dictionary in the json file using json library and setting parameters
            json_file = json.dump(words_in_canto, json_file, indent=4, ensure_ascii=False)
            
                
        return words_in_canto
    # Defined a method called get_hell_verses for get all the verses
    def  get_hell_verses(self):
         # Define list of canti start with empty
         all_canti = []
         # Cicle for each canto in range of 1 to 34
         for canto_number in range(1, 35):
             # Define a file path and use os library to work with files
             file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
             with open(file_path, "r", encoding="utf-8") as file:
                 content = file.read()
                 # Add the content of the file to the string and add a new line
                 all_canti = all_canti.append(content)
                 # Return the string
                 return all_canti.split("\n")
    # Defined a method called count_hell_verses for count the number of verses 
    def count_hell_verses(self):
        # Define a string that will store all the verses recalling last method that return all verses
        all_canti = self.get_hell_verses()
        # Return the number of lines using len method of string
        return len(all_canti.split("\n"))
    # Defined a method called get_hell_verse_mean_len for get the mean length of the verses    
    def  get_hell_verse_mean_len(self):
        # Define a string that will store all the verses recalling last method that return all verses
        all_canti = self.get_hell_verses()
        # Return the number of lines using len method of string and split by new line
        all_canti = all_canti.split("\n")
        # Calculate the mean length of the verses
        mean_len = sum(len(verse) for verse in all_canti)/len(all_canti) 
        # Return the mean length in float format       
        return  float(mean_len)
    
virgilio = Virgilio("https://github.com/giovanniurso92/Programming_Principles_Exam/tree/main/PP020125/canti")
virgilio.get_hell_verses()

