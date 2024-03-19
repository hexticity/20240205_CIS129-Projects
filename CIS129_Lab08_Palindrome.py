# Function to check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    # Remove spaces, punctuation, and convert to lowercase to ignore case sensitivity
    normal_str = ""
    for char in s:
        if char.isalnum():  # Check if character is alphanumeric
            normal_str += char.lower()  # Convert string to lowercase and add to the normalized string

    # Step 2: Use a stack to reverse the string.
    stack = []
    for char in normal_str:
        stack.append(char)  # Push each character of the string onto the stack

    # Step 3: Create the reversed string by popping elements from the stack.
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()  # Pop the character from the stack and add it to the reversed string

    # Step 4: Compare the normalized string with the reversed string.
    # If they are the same, the string is a palindrome.
    return normal_str == reversed_str he .===