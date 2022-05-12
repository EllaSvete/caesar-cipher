from corpus import word_list, name_list

def encrypt(plain, shift):
  # shift = shift % 27
  encrypted_text = ""
  for character in plain:
    if character.isalpha():
      letter_as_num = ord(character)

      baseline_index = 0

      if letter_as_num >= 65 and letter_as_num <= 90:
      ## this is the uppercase range in ascii
         letter_as_num -= 65
      ## stores how far the uppercase letters were shifted 
         baseline_index = 65
      elif letter_as_num >= 97 and letter_as_num <= 122:
      ## this is the ascii range for lowercase letters in ascii
            letter_as_num -= 97
            baseline_index = 97
      letter_as_num += shift
      letter_as_num = letter_as_num % 26
      letter_as_num += baseline_index
      shifted_letter = chr(letter_as_num)
      encrypted_text += shifted_letter
    else:
      encrypted_text += character
      
  return encrypted_text



def decrypt(encoded, shift):
    return encrypt(encoded, shift * -1)

def crack(encoded):
    phrase = "It was the best of times, it was the worst of times."
    for i in range(26):
        if encrypt(encoded, i * -1) == phrase:
            return encrypt(encoded, i * -1)

    return ""

