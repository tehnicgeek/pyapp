def create_and_load_file(file_path, data):
    try:
        # Create a new file
        with open(file_path, 'w') as file:
            # Write data to the file
            file.write(data)
        print(f"File '{file_path}' created and data loaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
file_path = "example.txt"
data = "This is the data to be loaded into the file."

create_and_load_file(file_path, data)

