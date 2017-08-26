import psutil
import time
import Process


class Device:

    def __init__(self):
        self.cpu_usage = 0.0
        self.pid = []
        self.memory_usage = 0.0
        self.cpu_temperature = 0.0
        self.pid_cpu = []
        self.pid_memory = []
        self.process_manager = Process.ProcessManager()

    @property
    def cpu_usage(self):
        return self.cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, value):
        self.cpu_usage = value

    @property
    def usage_per_core(self):
        return self.usage_per_core

    @usage_per_core.setter
    def usage_per_core(self, value):
        self.usage_per_core = value

    @property
    def memory_usage(self):
        return self.memory_usage

    @memory_usage.setter
    def memory_usage(self, value):
        self.memory_usage = value

    @property
    def cpu_temperature(self):
        return self.cpu_temperature

    @cpu_temperature.setter
    def cpu_temperature(self, value):
        self.cpu_temperature = value

    @property
    def pid(self):
        return self.pid

    @pid.setter
    def pid(self, value):
        self.pid = value

    def __get_cpu_usage(self):
        time.sleep(0.01)
        self.cpu_usage = psutil.cpu_percent(interval=None)

    def __get_core_usage(self):
        time.sleep(0.01)
        self.usage_per_core = psutil.cpu_percent(interval=None, percpu=True)

    def __get_memory(self):
        self.memory_usage = psutil.virtual_memory()[2]

    def __get_temperature(self):
        file = open("/sys/class/thermal/thermal_zone0/temp")
        self.cpu_temperature = float(file.read())/1000.0
        file.close()

    def __get_pid(self):
        pass