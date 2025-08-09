#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
      if isinstance(new_value, str):
          self._value = new_value
      else:
          print("The value must be a string.")

  def __str__(self):
    return self.value
  
  def __len__(self):
    return len(self.value)
  
  def is_sentence(self):
    return self.value.endswith(('.', '!', '?'))
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    if not self.value:
      return 0
    sentences = self.value.split()
    count = 0
    for sentence in sentences:
      if sentence.endswith(('.', '!', '?')):
        count += 1
    return count
