def is_palindrome(s: str) -> bool:
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    
    # Initialize a stack
    stack = []
    
    # Push all characters of cleaned_s onto the stack
    for char in cleaned_s:
        stack.append(char)
    
    # Compare each character with the one popped from the stack
    for char in cleaned_s:
        if char != stack.pop():
            return False  # Found a mismatch, so it's not a palindrome
    
    return True  # All characters matched; it's a palindrome

# Examples to test the function will be commented out to follow the guidelines
# print(is_palindrome("radar"))  # Should return True
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Should return True
# print(is_palindrome("OpenAI"))  # Should return False
