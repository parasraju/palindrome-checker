def is_palindrome(text):
    text = text.lower().replace(" ", "")  # Make lowercase and remove spaces
    return text == text[::-1]  # Check if it reads the same backwards

# Get input from user
user_input = input("Enter a word or sentence: ")

if is_palindrome(user_input):
    print("Yes! It's a palindrome.")
else:
    print("No, it's not a palindrome.")
