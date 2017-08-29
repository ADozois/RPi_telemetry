import time

import psutil

import Process


class Device:

    def __init__(self):
        self._cpu_usage = 0.0
        self. _usage_per_core = []
        self._memory_usage = 0.0
        self._cpu_temperature = 0.0
        self._pid_cpu = []
        self._pid_memory = []
        self._process_manager = Process.ProcessManager()
        self.update()

    @property
    def cpu_usage(self):
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, value):
        self._cpu_usage = value

    @property
    def usage_per_core(self):
        return self._usage_per_core

    @usage_per_core.setter
    def usage_per_core(self, value):
        self._usage_per_core = value

    @property
    def memory_usage(self):
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, value):
        self._memory_usage = value

    @property
    def cpu_temperature(self):
        return self._cpu_temperature

    @cpu_temperature.setter
    def cpu_temperature(self, value):
        self._cpu_temperature = value

    @property
    def pid_cpu(self):
        return self._pid_cpu

    @pid_cpu.setter
    def pid_cpu(self, value):
        self._pid_cpu = value

    @property
    def pid_memory(self):
        return self._pid_memory

    @pid_memory.setter
    def pid_memory(self, value):
        self._pid_memory = value

    def _get_cpu_usage(self):
        time.sleep(0.01)
        self._cpu_usage = psutil.cpu_percent(interval=None)

    def _get_core_usage(self):
        time.sleep(0.01)
        self._usage_per_core = psutil.cpu_percent(interval=None, percpu=True)

    def _get_memory(self):
        self._memory_usage = psutil.virtual_memory()[2]

    def _get_temperature(self):
        file = open("/sys/class/thermal/thermal_zone0/temp")
        self._cpu_temperature = float(file.read())/1000.0
        file.close()

    def _get_pid(self):
        self._pid_cpu = self._process_manager.build_top_list('cpu', 4)
        self._pid_memory = self._process_manager.build_top_list('memory', 4)

    def update(self):
        self._get_cpu_usage()
        self._get_core_usage()
        self._get_memory()
        self._get_pid()
        self._get_temperature()