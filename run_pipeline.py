from typing import Dict, List, Optional
import networkx as nx

import foo
from multiprocessing import Process

def runInParallel(*fns):
    """
    a is taking a dependency dict and sort the jobs to be able to have parallel run.
    """    
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


def main():
    stages = {
        "Lint": [],
        "Test": [],
        "Coverage": ["Test"],
        "Docs": ["Coverage", "Lint"],
        "Benchmark": ["Coverage"],
    }

    print(list(_sort_jobs(stages)))
    # Output: [['Lint', 'Test'], ['Coverage'], ['Docs', 'Benchmark']]
    output = list(_sort_jobs(stages))

    # Execute the list stages sequentially and in parallel
    for o in output:
        if len(o) == 1:
            result = getattr(foo, o[0])()
        elif len(o) > 1:
              result2=[getattr(foo, item) for item in o]
              print("result2:- ", result2)	
              runInParallel(*result2)

def _sort_jobs(dependencies: Dict[str, List[str]]) -> List[List[str]]:
    """
    a is taking a dependency dict and sort the jobs to be able to have parallel run.
    """   
    g = nx.DiGraph(dependencies)
    print("g:- ", g)

    # detect cycling workflows
    cycles = list(nx.simple_cycles(g))
    if len(cycles) > 0:
        raise CyclingPipeline(cycles=cycles)

    # sort the stages
    out_degree_map = {v: d for v, d in g.out_degree() if d > 0}
    print("out_degree_map:- ", out_degree_map)
    zero_out_degree = [v for v, d in g.out_degree() if d == 0]
    #zero_out_degree = [getattr(foo, v)() for v, d in g.out_degree() if d == 0]
    print("zero_out_degree:- ", zero_out_degree)
    
    #result = getattr(foo, 'Test')()

    while zero_out_degree:
        yield zero_out_degree
        new_zero_out_degree = []
        for v in zero_out_degree:
            for child, _ in g.in_edges(v):
                out_degree_map[child] -= 1
                if not out_degree_map[child]:
                    new_zero_out_degree.append(child)
                    print("new_zero_out_degree:- ", new_zero_out_degree)
                    print("child:- ", child)
        zero_out_degree = new_zero_out_degree
        print("zero_out_degree:- ", zero_out_degree)


class CyclingPipeline(Exception):
    """
    CyclingPipeline is an exception raised if we detect a cycle in the pipeline.
    """
    def __init__(self, cycles=Optional[List]):
        message = f"Invalid workflow you have a cycling dependencies: {cycles}"
        super().__init__(message)


if __name__ == "__main__":
    main()