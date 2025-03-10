"""Determing how many smart students a class has based on their test scores"""

# Making the student_score list
student_scores = []
# Minimun a student must score to be smart
MIN_SCORE = 80
# Counter for how many smart students are in the class
counter = 0

while True:
    try:
      score = input('Enter a score, or type "done" to exit: ')
      if score == 'done':
          break
      else:
         score = int(score)
         student_scores.append(score)
    except ValueError:
        print('Invalid score!')
for score in student_scores:
    if score >= MIN_SCORE:
        counter += 1
if counter == 1:
    print('This class has 1 smart student!')
else:
    print(f'This class has {counter} smart students!')
        