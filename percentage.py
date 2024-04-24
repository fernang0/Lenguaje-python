n = int(input())
suma = 0;
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for valor in student_marks[query_name]:
    suma += valor;

print("{:.2f}".format(suma/3))
