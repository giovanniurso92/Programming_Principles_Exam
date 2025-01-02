# Imported os library to work with files

import os

# Created a class called Virgilio

class Virgilio:
    # Created a constructor as self and directory as parameters
    def __init__(self, directory):
        self.directory = directory  
        
    # Created a method called read_canto_lines for reading the canto from file and to format it and return the lines
    def read_canto_lines(self,canto_number):
      # Created a variable called file_path for storing the path of the file
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
   # Use try-except block for error handling and read the file
        try:
            # Open the file which is in read mode and utf-8 encoding
            with open(file_path, "r", encoding="utf-8") as file:
                # Read the lines of the file
                lines = file.readlines()
                # Print the lines only for debugging and testing
                print(lines)
                # Return the lines
                return lines
        except FileNotFoundError:
            # Print a message if the file is not found or if number of canto file is not found
            print(f"File not found: {file_path}")
            return None
            # Print a message if there is an generic error 
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        
    
virgilio = Virgilio("C:/Users/giova/Desktop/Epicode/PP020125/canti")

canto = virgilio.read_canto_lines(1)

