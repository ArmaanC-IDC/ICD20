class item:
    def __init__(self,name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True

    def get_done(self):
        return self.done

    def __str__(self):
        return f"{self.name}"
    
class todolist:
    def __init__(self):
        self.item_list = []

    def add_task(self, task):
        self.item_list.append(task)

    def show_tasks(self):
        for task in self.item_list:
            if not task.get_done():
                print(task)

hw = item('math homework')
test = item('comp sci test')
my_list = todolist()

my_list.add_task(hw)
my_list.add_task(test)

my_list.show_tasks()