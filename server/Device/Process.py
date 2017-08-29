import psutil


class Process:

    def __init__(self):
        self._pid = 0.0
        self._name = ""
        self._memory = 0.0
        self._cpu = 0.0

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        self._memory = value

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        self._cpu = value


class ProcessManager:

    def __init__(self):
        self._process_list = []
        self._top_process_cpu = []
        self._top_process_memory = []

    @property
    def process_list(self):
        return self._process_list

    @process_list.setter
    def process_list(self, value):
        self._process_list = value

    @property
    def top_process_cpu(self):
        return self._top_process_cpu

    @top_process_cpu.setter
    def top_process_cpu(self, value):
        self._top_process_cpu = value

    @property
    def top_process_memory(self):
        return self._top_process_memory

    @top_process_memory.setter
    def top_process_memory(self, value):
        self._top_process_memory = value

    def _get_process(self):
        p = Process()

        for proc in psutil.process_iter():
            p.pid = proc.as_dict(attrs=['pid'])['pid']
            p.name = proc.as_dict(attrs=['name'])['name']
            p.memory = proc.memory_percent()
            p.cpu = proc.cpu_percent()
            self._process_list.append(p)

    def get_max_cpu(self):
        max_c = 0

        for p in self.process_list:
            if p.cpu > max_c:
                max_c = p.cpu

        return max_c

    def get_max_mem(self):
        max_m = 0

        for p in self._process_list:
            if p.memory > max_m:
                max_m = p.memory

        return max_m

    def get_both_max(self):
        max_m = 0
        max_c = 0

        for p in self._process_list:

            if p.memory > max_m:
                max_m = p.memory

            if p.cpu > max_c:
                max_c = p.cpu

        return max_c, max_m

    def get_pid_max_cpu(self):
        pid = 0
        max_c = 0

        for p in self._process_list:
            if p.cpu > max_c:
                max_c = p.cpu
                pid = p.pid

        return pid

    def get_pid_max_mem(self):
        max_m = 0
        pid = 0

        for p in self._process_list:
            if p.memory > max_m:
                max_m = p.memory
                pid = p.pid

        return pid

    def get_index_max_cpu(self):
        i = 0
        i_max = 0
        max_c = 0

        for p in self._process_list:
            if p.cpu > max_c:
                max_c = p.cpu
                i_max = i
            i = i + 1

        return i_max

    def get_index_max_memory(self):
        i = 0
        i_max = 0
        max_m = 0

        for p in self._process_list:
            if p.memory > max_m:
                max_m = p.memory
                i_max = i
            i = i + 1

        return i_max

    def _remove_process(self, index):
        del self._process_list[index]

    def build_top_list(self, list_name, size=4):
        self._get_process()

        for i in range(0, size):

            if list_name == 'cpu':
                index = self.get_index_max_cpu()
                self._top_process_cpu.append(self.process_list[index])
            else:
                index = self.get_index_max_memory()
                self._top_process_memory.append(self.process_list[index])

            self._remove_process(index)
