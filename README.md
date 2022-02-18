# Lightweight Python Pipeline

Lightweight Python Pipeline which allows to create DAGs based on dependencies without worrying the prerequisites of each node within a workflow pipeline.

### Prerequisites

Install the following python packages

```
pip install networkx
pip install multiprocess
```

# Limitations
Running the nodes based on a list does not allow to create dependencies for more than 1 degree. The list items will run sequentially only.

# Fork
* **thomaspoignant** - *Initial work* - [sort_pipeline_example.py](https://gist.github.com/garyzava/83f10a6bc0d6a4a61940fbeb95d62072)
