for i in range(1,5):
 file_path = i,"i.txt"
 

with open(file_path, 'w') as file:
   
    file.write("Hello, this is a new text file created using open() function.")
i+=1   
print(f"File '{file_path}' created successfully.")
