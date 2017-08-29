import Device

if __name__ == '__main__':
    pc = Device.Device()
    print(pc.cpu_usage)
    print(pc.usage_per_core)
    print(pc.pid_cpu)
    print(pc.pid_memory)
    print(pc.cpu_temperature)