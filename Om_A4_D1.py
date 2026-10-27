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


# Test
read_marks_file("marks.txt")