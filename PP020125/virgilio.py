# Imported os library to work with files

import os
# Imported math library to work with numbers
import math

# Created a class called Virgilio

import json


class Virgilio:
    # Created a constructor as self and directory as parameters
    def __init__(self, directory):
        self.directory = directory  
        
    # Created a method called read_canto_lines for reading the canto from file and to format it and return the lines
    def read_canto_lines(self,canto_number):
        
        class CantoNotFoundError(Exception):
            def __init__(self, message):
               super().__init__(message)
              
        
        
        
        if not (isinstance(canto_number,int)):
            raise TypeError("canto_number must be an integer")
        if canto_number < 1 or canto_number > 34:
        
            raise CantoNotFoundError("canto_number must be between 1 and 34")
        strip_lines = False
        
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
            if strip_lines:
                 lines = [line.strip() for line in lines]
                 return lines
            if num_lines is not None:
                 lines = file.readlines(num_lines)
                 return lines
                
            return lines    
                
        except FileNotFoundError:
            # Print a message if the file is not found or if number of canto file is not found
            print(f"File not found: {file_path}")
            return None
            # Print a message if there is an generic error 
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        
        
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
        # Return the number of terzine
        return math.floor(canto_number)
    def  count_word(self,canto_number,word):
        
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content.count(word)
        
    def get_verse_whit_word(self,canto_number,word):
            line_list = []
            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    if word in line:
                        line_list.append(line)
                return line_list
        
    def  get_longest_verse(self,canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            longest_line = max(lines, key=len)
            return longest_line
    def get_longest_canto(self):
        longest_canto = {"canto_number": None, "canto_len": 0}
        for canto_number in range(1, 34):
            file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                canto_len = sum(len(line) for line in lines)
                if canto_len > longest_canto["canto_len"]:
                    longest_canto["canto_number"] = canto_number
                    longest_canto["canto_len"] = canto_len
        return longest_canto
    
    def count_words(self,canto_number,word):
        json_file_name = "word_counts.json"
        json_file_path = os.path.join(os.getcwd(), json_file_name)
        words_in_canto = {word: 0}
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for word in content:
                words_in_canto[word] = content.count(word)
                
                
        with open (json_file_path, "w") as json_file:
            json_file = json.dump(words_in_canto, json_file, indent=4, ensure_ascii=False)
            
                
        return words_in_canto
           
    def  get_hell_verses(self):
         all_canti = ""
         for canto_number in range(1, 35):
             file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
             with open(file_path, "r", encoding="utf-8") as file:
                 content = file.read()
                 all_canti += (content + "\n")
         return all_canti
     
    def count_hell_verses(self):
        all_canti = self.get_hell_verses()
        return len(all_canti.split("\n"))
        
    def  get_hell_verse_mean_len(self):
        all_canti = self.get_hell_verses()
        all_canti = all_canti.split("\n")
        mean_len = sum(len(verse) for verse in all_canti)/len(all_canti)        
        return  float(mean_len)
    
virgilio = Virgilio("C:/Users/giova/Desktop/Epicode/PP020125/canti")

print(virgilio.read_canto_lines(898))