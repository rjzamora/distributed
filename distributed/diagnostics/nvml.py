import pynvml

# need_pynvml_init = True
# count = None
# handles = None

pynvml.nvmlInit()
count = pynvml.nvmlDeviceGetCount()
handles = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(count)]

# def _initialize_pynvml():
#     global need_pynvml_init, count, handles
#     pynvml.nvmlInit()
#     count = pynvml.nvmlDeviceGetCount()
#     handles = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(count)]
#     need_pynvml_init = False


def real_time():
    # global need_pynvml_init, handles
    # if need_pynvml_init:
    #     _initialize_pynvml()
    return {
        "utilization": [pynvml.nvmlDeviceGetUtilizationRates(h).gpu for h in handles],
        "memory-used": [pynvml.nvmlDeviceGetMemoryInfo(h).used for h in handles],
    }


def one_time():
    # global need_pynvml_init, handles
    # if need_pynvml_init:
    #     _initialize_pynvml()
    return {
        "memory-total": [pynvml.nvmlDeviceGetMemoryInfo(h).total for h in handles],
        "name": [pynvml.nvmlDeviceGetName(h).decode() for h in handles],
    }
