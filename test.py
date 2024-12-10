from pypower.runpf import runpf
from pypower.case300 import case300
from pypower.case9 import case9

if __name__ == '__main__':
    results = runpf(case300())
    # results = runpf(case300())
    # print(results['bus'][:, 7])