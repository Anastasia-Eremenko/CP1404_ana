"""
CP1404 - Practice
Menu-driven score exercise with writing to file
"""

def main():
 scores = []
 results = []
 number_of_scores = get_number_of_scores()
 scores = generate_scores(number_of_scores)
 determine_grade()


def determine_grade(score):
 if score < 0 or score > 100:
  print("Invalid score")
 else:
  if score > 90:
   return "Excellent"
  elif score > 50:
   return "Passable"
  else:
   return "Bad"

def generate_scores():


def get_number_of_scores():
  number_of_scores = int(input("Number of scores >>> "))
  if number_of_scores > 100 or number_of_scores <= 0:
   print("Please enter a valid number of scores")
   number_of_scores = int(input("How many scores: "))
  return number_of_scores


def process_out_file(lines):
  out_file = open("results", "w")
  for line in lines:
   print(line, file=out_file)
  out_file.close()