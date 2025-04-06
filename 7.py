import os

# Open files in read, write, and append modes
with open("text_files/_7_read.txt", "r") as fread, \
     open("text_files/_7_write.txt", "w") as fwrite, \
     open("text_files/_7_append.txt", "a") as fappend:

    print()
    print("File Read: ", fread.name, "\n")

    # Read first 10 characters
    print("First 10 characters of the file:", fread.read(10))  
    print("Current File Pointer Position (After read):", fread.tell(), "\n")  

    # Reset file pointer to beginning
    fread.seek(0)  

    # Read and print three lines
    print("3 Lines of File:", fread.readline(), fread.readline(), fread.readline())  
    print("Current File Pointer Position (After readline):", fread.tell())  

    # Reset file pointer again
    fread.seek(0)  

    # Read all lines
    print("All Lines of File:", fread.readlines())  

    # Writing to file
    fwrite.write("After This Operation \nData of Original File \nWill be Deleted")  
    fwrite.writelines([
        "\n\n", "This is Inserted \n", "\n", 
        "Through Writelines \n", "Method \n"
    ])  

    # Appending data
    fappend.write("\nThis is Appended Data: \nHello World")  

# Check if files exist
print("\nChecking if files exist:")
print("_7_read.txt Exists:", os.path.exists("text_files/_7_read.txt"))  
print("_7_write.txt Exists:", os.path.exists("text_files/_7_write.txt"))  
print("_7_append.txt Exists:", os.path.exists("text_files/_7_append.txt"))  
print("xyz.txt Exists:", os.path.exists("text_files/xyz.txt"), "\n")  

# Rename file if it exists
if os.path.exists("text_files/OS_Experimental.txt"):  
    os.rename("text_files/OS_Experimental.txt", "text_files/OS_Experimental_Renamed.txt")  

# Remove file if it exists
if os.path.exists("text_files/OS_Experimental_Renamed.txt"):  
    os.remove("text_files/OS_Experimental_Renamed.txt")  
    print("File 'OS_Experimental_Renamed.txt' deleted successfully.")  
