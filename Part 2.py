def write_substrings(filename):
    # Read the entire contents of the original file
    with open(filename, "r") as f:
        original_file_content = f.read()

    # Find the first comma in the original file content
    comma_index = original_file_content.find(",")

    # Extract the first part of the original file (before the comma)
    part1_content = original_file_content[:comma_index]

    # Extract the second part of the original file (after the comma)
    part2_content = original_file_content[comma_index + 1 :]

    # Write the first part of the original file to part_1.txt
    with open("part_1.txt", "w") as f:
        f.write(part1_content)

    # Write the second part of the original file to part_2.txt
    with open("part_2.txt", "w") as f:
        f.write(part2_content)

    # Print the name and content of each file
    print(f"File name: part_1.txt")
    with open("part_1.txt", "r") as f:
        part1_content = f.read()
        print(f"Content: {part1_content}")

    print(f"File name: part_2.txt")
    with open("part_2.txt", "r") as f:
        part2_content = f.read()
        print(f"Content: {part2_content}")


if __name__ == "__main__":
    filename = "string.txt"
    write_substrings(filename)