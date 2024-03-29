import numpy as np
import prettytable as prettytable

first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ'] + \
              ['კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'ემა'] + \
              ['იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული'] + \
              ['კახა', 'როზა', 'რუსუდან', 'ბადრი', 'მადონა', 'ირინე', 'მინДია', 'ნათია', 'გულნარა', 'სიმონ', 'ნელი',
               'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა',
              'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა'] + \
             ['ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი',
              'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი'] + \
             ['მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე',
              'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა',
              'რევაზიშვილი']
subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ფიზიკა', 'ქიმია']

n_students = 100

first_names_chosen = np.random.choice(first_names, size=n_students, replace=True)
last_names_chosen = np.random.choice(last_names, size=n_students, replace=True)

grades = np.random.randint(low=1, high=101, size=(n_students, len(subjects)))

students = np.char.add(np.char.add(first_names_chosen[:, np.newaxis], " "), last_names_chosen[:, np.newaxis])

my_table = prettytable.PrettyTable(["Name", "ქართული", "მათემატიკა", "ინგლისური", "ფიზიკა", "ქიმია"])
my_table.horizontal_char = '='

for i, name in enumerate(students.flatten()):
    my_table.add_row([name, *grades[i, :]])


# ცხრილის დასაბეჭდად
# print(my_table)


def find_max_average(grades_lst, students_lst):
    means = [np.mean(sublist) for sublist in grades_lst]
    if not means:
        return None
    max_mean = max(means)
    max_index = means.index(max_mean)
    return "მაქსიმალური საშუალო ქულა ყველა საგანში: " + str(students_lst[max_index])[2:-2] + " - " + str(max_mean)


print(find_max_average(grades, students))


def get_min_max_mathematics_grade(grades_lst, students_lst):
    min_math_grade = min(grades_lst[:, 1])
    max_math_grade = max(grades_lst[:, 1])

    min_math_index = np.argwhere(grades_lst[:, 1] == min_math_grade).flatten()
    max_math_index = np.argwhere(grades_lst[:, 1] == max_math_grade).flatten()

    students_with_min_math_grade = [', '.join(students_lst[i].tolist()) for i in min_math_index]
    students_with_max_math_grade = [', '.join(students_lst[i].tolist()) for i in max_math_index]

    students_with_min_math_grade = ', '.join(students_with_min_math_grade)
    students_with_max_math_grade = ', '.join(students_with_max_math_grade)

    result = f"\nმინიმალური ქულა მათემატიკაში: {min_math_grade} (სტუდენტები: {students_with_min_math_grade})\n"
    result += f"მაქსიმალური ქულა მათემატიკაში: {max_math_grade} (სტუდენტები: {students_with_max_math_grade}) \n"

    return result


print(get_min_max_mathematics_grade(grades, students))


def get_students_with_higher_english_grade(grades_lst):
    average_english_grade = np.mean(grades_lst[:, 2])
    students_with_higher_english_grade = grades_lst[grades_lst[:, 2] > average_english_grade]

    students_index = np.arange(len(students_with_higher_english_grade))

    students_with_higher_score = []
    for i in students_index:
        students_with_higher_score.append(str(students[i])[2:-2])

    return students_with_higher_score


print("სტუდენტები საშუალოზე მაღალი ქულით ინგლისურში:")
print(get_students_with_higher_english_grade(grades))
