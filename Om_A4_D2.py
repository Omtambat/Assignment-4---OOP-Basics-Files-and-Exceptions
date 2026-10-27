def read_marks_file(filename):
    try:
        with open(filename, "r") as file:
            marks = file.read().strip()
            marks = int(marks)
            print("Marks:", marks)

    except FileNotFoundError:
        print("File not found:", filename)

    except ValueError:
        print("The contents were not a number.")

    finally:
        print("File operation finished.")


# Create test file containing "hello"
with open("hello.txt", "w") as file:
    file.write("hello")

# Create test file containing 75
with open("marks75.txt", "w") as file:
    file.write("75")


# 1. File does not exist
print("\n--- Test 1: Missing File ---")
read_marks_file("missing.txt")

# 2. File contains "hello"
print("\n--- Test 2: Invalid Content ---")
read_marks_file("hello.txt")

# 3. File contains 75
print("\n--- Test 3: Valid Marks ---")
read_marks_file("marks75.txt")