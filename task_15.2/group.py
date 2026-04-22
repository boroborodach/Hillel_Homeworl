class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()


    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise Exception("Group student limit exceeded")


    def delete_student(self, last_name):
        for e in self.group:
            if e.last_name == last_name:
                self.group.remove(e)
                return


    def find_student(self, last_name):
        for e in self.group:
            if e.last_name == last_name:
                return e
        return None


    def __str__(self):
        all_students = ''
        ...
        return f'Number:{self.number}\n {all_students} '