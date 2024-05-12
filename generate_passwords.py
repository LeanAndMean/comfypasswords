import random

# Define character sets for each hand based on a standard QWERTY keyboard layout
left_hand_chars = {
    'lowercase': "qwertasdfgzxcvb",
    'uppercase': "QWERTASDFGZXCVB",
    'numbers': "123456",
    'symbols': "`~!@#$%^"
}
right_hand_chars = {
    'lowercase': "yuiophjklnm",
    'uppercase': "YUIOPHJKLNM",
    'numbers': "7890",
    'symbols': "&*()_+-=[]{}|;:'\",.<>/?\\"
}

# Function to generate a password
def generate_password(password_length:int) -> str:
    password = []
    # Order of types, shuffled to ensure randomness in type positions
    types = ['lowercase', 'uppercase', 'numbers', 'symbols']
    if password_length < len(types):
        raise ValueError(
            "Specified password_length was {}, but must be at least {} in order to contain the following character types: {}".format(
                password_length,
                len(types),
                ', '.join(types)
            )
        )
    # Add 'any' type to indicate that a random other type should be chosen.
    password_types = types + ['any'] * (password_length - len(types))
    assert len(password_types) == password_length
    random.shuffle(password_types)

    # Decide starting hand
    use_left_hand = random.choice([True, False])

    # Add characters from each type to the password, alternating hands
    for type in password_types:
        if type == 'any':
            type = random.choice(types)
        if use_left_hand:
            next_char = random.choice(left_hand_chars[type])
            password.append(next_char)
            # Switch hands
            use_left_hand = False
        else:
            next_char = random.choice(right_hand_chars[type])
            password.append(next_char)
            # Switch hands
            use_left_hand = True

    return ''.join(password)

if __name__ == '__main__':
    for _ in range(10):
        # Generate and print 10 passwords.
        print(generate_password(10))