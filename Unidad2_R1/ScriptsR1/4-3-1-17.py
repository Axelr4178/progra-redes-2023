"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""

class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, line):
        super().__init__()
        self.line = line


class FileEmpty(StudentsDataException):
    pass

def main():
    try:
        filename = input("Introduce el nombre del archivo: ")
        students = {}
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if len(line.split()) != 3:
                    raise WrongLine(line)
                student, lastname, points = line.split()
                if student not in students:
                    students[student] = 0
                students[student] += float(points)
    except FileNotFoundError:
        print("El archivo no existe")
    except WrongLine as e:
        print(f"La línea '{e.line}' es incorrecta")
    except FileEmpty:
        print("El archivo está vacío")
    else:
        for student, points in sorted(students.items()):
            print(f"{student} {lastname} {points}")


if __name__ == "__main__":
    main()

