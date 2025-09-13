def get_grade(s1, s2, s3):
    mean = int((s1 + s2 + s3) / 3)
    grade = ["F", "D", "C", "B", "A"]
    return grade[(mean >= 60) + (mean >= 70) + (mean >= 80) + (mean >= 90)]
    