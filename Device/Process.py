import psutil


class Process:

    def __init__(self):
        self.pid = 0.0
        self.name = ""
        self.memory = 0.0
        self.cpu = 0.0

    @property
    def pid(self):
        return self.pid

    @pid.setter
    def pid(self, value):
        self.pid = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def memory(self):
        return self.memory

    @memory.setter
    def memory(self, value):
        self.memory = value

    @property
    def cpu(self):
        return self.cpu

    @cpu.setter
    def cpu(self, value):
        self.cpu = value


class ProcessManager:

    def __init__(self):
        self.process_list = []
        self.top_process_cpu = []
        self.top_process_memory = []

    @property
    def process_list(self):
        return self.process_list

    @process_list.setter
    def process_list(self, value):
        self.process_list = value

    @property
    def top_process_cpu(self):
        return self.top_process_cpu

    @top_process_cpu.setter
    def top_process_cpu(self, value):
        self.top_process_cpu = value

    @property
    def top_process_memory(self):
        return self.top_process_memory

    @top_process_memory.setter
    def top_process_memory(self, value):
        self.top_process_memory = value

    def __get_process(self):
        p = Process()

        for proc in psutil.process_iter():
            p.pid = proc.as_dict(attrs=['pid'])
            p.name = proc.as_dict(attrs=['name'])
            p.memory = proc.memory_percent()
            p.cpu = proc.cpu_percent()
            self.process_list.append(p)

    def get_max_cpu(self):
        max_c = 0

        for p in self.process_list:
            if p.cpu > max_c:
                max_c = p.cpu

        return max_c

    def get_max_mem(self):
        max_m = 0

        for p in self.process_list:
            if p.memory > max_m:
                max_m = p.memory

        return max_m

    def get_both_max(self):
        max_m = 0
        max_c = 0

        for p in self.process_list:

            if p.memory > max_m:
                max_m = p.memory

            if p.cpu > max_c:
                max_c = p.cpu

        return max_c, max_m

    def get_pid_max_cpu(self):
        pid = 0
        max_c = 0

        for p in self.process_list:
            if p.cpu > max_c:
                max_c = p.cpu
                pid = p.pid

        return pid

    def get_pid_max_mem(self):
        max_m = 0
        pid = 0

        for p in self.process_list:
            if p.memory > max_m:
                max_m = p.memory
                pid = p.pid

        return pid

    def get_index_max_cpu(self):
        i = 0
        i_max = 0
        max_c = 0

        for p in self.process_list:
            if p.cpu > max_c:
                max_c = p.cpu
                i_max = i
            i = i + 1

        return i_max

    def get_index_max_memory(self):
        i = 0
        i_max = 0
        max_m = 0

        for p in self.process_list:
            if p.memory > max_m:
                max_m = p.memory
                i_max = i
            i = i + 1

        return i_max

    def __remove_process(self, index):
        del self.process_list[index]

    def build_top_list(self, list_name, size=4):
        self.__get_process()

        for i in range(0, size):

            if list_name == 'cpu':
                index = self.get_index_max_cpu()
                self.top_process_cpu.append(self.process_list[index])
            else:
                index = self.get_index_max_memory()
                self.top_process_memory.append(self.process_list[index])

            self.__remove_process(index)
