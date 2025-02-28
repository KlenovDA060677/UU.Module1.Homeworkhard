# Дополнительное практическое задание по модулю

# Вводим исходные данные
grade = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}

# Вычисляем средний бал по оценкам из списка 'gradle' и сохраняем в 'grade_average'
# Для создания списка со средним балом используем генератор списков
grade_average = [round(sum(i)/len(i)) for i in grade] # средний бал округлен до целого


# Преобразуем множество 'students' в список и сортируем по алфавиту
students = list(students) #для преобразования множества в список используем фукц.list()
students.sort()

# Создаем словарь где,
# ключ - имя студента из списка 'student',
# значение - средний бал из списка 'grade_average'
# для создания словаря из двух списков используем функцию zip,
# которая создает zip-объект кортежей, содержащих пары элементов,
# взятых последовательно из указанных в качестве параметров списков
students_grade = dict(zip(students, grade_average)) # для создания словаря используем ф-цию
                                                    # 'dict' которой передаем zip-объект
print(students_grade)
