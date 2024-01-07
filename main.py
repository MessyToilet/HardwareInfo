import platform, psutil, cpuinfo, wmi, os

os.system('cls')
cpu_info = cpuinfo.get_cpu_info()
pc = wmi.WMI()

print(f'Architecture:     {platform.architecture()}')
print(f'Network Name:     {platform.node()}')
print(f'Operating System: {platform.platform()}')
print(f'Processor:        {platform.processor()}')
print(f'Full CPU Name:    {cpu_info["brand_raw"]}')
print()
print(f'RAM:              {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} gb')
print(f'CPU count:        {psutil.cpu_count()}')
print(f'CPU frequency     {psutil.cpu_freq()}')