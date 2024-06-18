import os, re

# this function takes a file, renames it and saves to a new dir, and updates a record file
def uploader(file, file_name):
    #open the record file to check if the file has been uploaded before
    with open('data/resources/record.txt', 'r') as f:
        books = f.read()
        books = re.split(r',', books)
        if file_name in books:
            return "File already uploaded!"
        
        else:
            file_path = f"data/resources/{file_name}.pdf"
            with open(file_path, "wb") as f:
                f.write(file.read())
                new_directory = "data/resources/"
                new_file_path = os.path.join(new_directory, f"{file_name}.pdf")
                os.rename(file_path, new_file_path)
                with open('data/resources/record.txt', 'a') as f:
                    f.write(f",{file_name}")
            return "File saved successfully!"
        
      

