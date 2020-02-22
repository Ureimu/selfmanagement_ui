def create_description():
    print('ok')


class mission:
    id = -1
    delete_count = -1
    count = -1

    def __init__(self, name, date_add, date_start, date_end, description):
        mission.id += 1
        mission.count += 1
        self.count = mission.count
        self.date_start = date_start
        self.date_end = date_end
        self.name = name
        self.date_add = date_add
        self.description = description
        self.id = mission.id  # 编号,不会改变

