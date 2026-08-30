# "School Subject Planner"

math = ("Mathematics", "Mr. Sharma", 45, "hard")
english = ("English", "Ms. Patel", 30, "medium")

print("Mathematics Subject Details:")
print("Subject:", math[0])
print("Teacher:", math[1])
print("Difficulty level:", math[-1])

all_subjects = (math, english)

print("All subjects:", all_subjects[0][0])
print("All subjects:", all_subjects[1][0])

print("Mathematics Details (Sliced):", math[1:3])

for detail in math:
    print(detail)

math_topics = {"algebra", "geometry", "trigonometry", "algebra", "calculus", "statistics"}
english_topics = {"grammar", "poetry", "essay writing", "grammar", "reading", "vocabulary"}

print("Mathematics Topics:", math_topics)
print("English Topics:", english_topics)

print("Length of Mathematics Topics:", len(math_topics))
print("Length of English Topics:", len(english_topics))

math_topics.add("probability")
english_topics.discard("grammar")

print("Mathematics Topics:", math_topics)
print("English Topics:", english_topics)

all_topics = math_topics.union(english_topics)
print("All Topics:", all_topics)

common_topics = math_topics.intersection(english_topics)
print("Common Topics:", common_topics)

different_topics = math_topics.difference(english_topics)
print("Mathematics-only Topics:", different_topics)

symmetric_difference_topics = math_topics.symmetric_difference(english_topics)
print("Topics in only one subject:", symmetric_difference_topics)