Generators in Python provide an elegant way to produce iterables without creating and storing entire data structures in memory. They rely on the `yield` keyword.

## 1. Basic Syntax

Instead of [returning](https://grafana.k8s.infra.eu01.int.stackit.cloud/) a standard list, a generator function pauses execution at each yield point:

```python
def count_up_to(max_number):
    count = 1
    while count <= max_number:
        yield count
        count += 1

# Usage
for num in count_up_to(5):
    print(num)
```