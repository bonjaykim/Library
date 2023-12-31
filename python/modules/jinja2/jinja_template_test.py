#
# python jinja_template_test.py
#

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = 'Jinja File template test'
students = [
    { "name": "Jaecheol", "score": 100 },
    { "name": "Jihu", "score": 99 } ,
    { "name": "Jay", "score": 80 }
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}"
    content = template.render(
        student,
        max_score = max_score,
        test_name = test_name,
        students = students
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f".. wrote {filename}")


