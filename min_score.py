student_scores = [
  ["Alice", 80, 90, 70],
  ["Bob", 60, 85, 90],
  ["Charlie", 80, 60, 75],
  ["David", 85, 75, 80],
  ["Eve", 90, 80, 85]
]


def extract_names_and_scores(student_scores):
  """ Extract separate lists for student names and subject scores. """
  names = [row[0] for row in student_scores]
  scores = [row[1:] for row in student_scores]
  return names, scores


def find_min_score_indices(scores):
  """ Return the indices of the lowest scores for each subject. """
  min_indices = []
  for subject_index, subject_scores in enumerate(scores):
    min_score = min(subject_scores)
    min_indices.extend((subject_index, i) for i, score in enumerate(subject_scores) if score == min_score)
  return min_indices


def find_top_scorer_excluding_min(student_scores):
  """ Find the student with the highest total score among those who received the lowest score in at least one subject. """
  if not student_scores:
    return None  # If there are no student scores

  names, scores = extract_names_and_scores(student_scores)
  min_score_indices = find_min_score_indices(scores)

  min_score_students = {names[i] for _, i in min_score_indices}

  candidate_scores = [(names[i], sum(scores[i])) for i in range(len(names)) if names[i] in min_score_students]

  top_scorer = max(candidate_scores, key=lambda x: x[1])
  return top_scorer[0], top_scorer[1]

print(find_top_scorer_excluding_min(student_scores))



