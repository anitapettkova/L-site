---
title: "Python Generators and the Yield Key Word"
date: 2026-09-18
draft: false
tags: [zig, programming]
math: false                  # Set to true to enable KaTeX math formulas in this post
cover: "zig_c_interlop.webp"     # Cover image URL (optional, WebP format recommended, < 200KB)
toc: true                    # Show table of contents
description: "Python Generators, what are they, how they work and how does the Yield keyword tie to them?"  # Used for card summary
---

On a lot of interviews I have been asked and I have also asked interviewees about their code and why they used or didn't use a generator function on a specific place in their code.
In more cases than not, they cannot really answer what the generators are, how they work and how the `yield` keyword ties to them.
So let's get started.

## What are the `generators`?
So what are the `generators` exactly? Well, they are just functions that returns an `iterator` object, basically an object which implements the `__iter__` and `__next__` methods, that allow us to iterate over it. It is that simple. There is one small caveat though, unlike the regular functions that return one result, the generators yield many results whenever called.

## The `yield` keyword
This is where the yield keyword comes into play, it allows us to yield a value and pause the function, keeping its current state until it is called again. See the example below.

```bash
from typing import List, Generator


def fetch_n(names: List[str]) -> Generator:
    for name in names:
        yield name


our_generator = fetch_n(["Rebecca", "Theodore", "Benjamin"])
print(our_generator.__next__())
print(our_generator.__next__())
```

The result of the above is
```bash
Rebecca
Theodore
```

Benjamin is never loaded at all. If we had a regular array returned, we would have loaded all of the names in memory, which in this case is not a problem, but what if we had `1_000_000` names for example?

## Why are the generators userful?
This brings us to the next point, why are the generators useful, what advantages do we get from using them?

- Memory efficiency - The generators allow us to load only what we need into memory, depending on the data size, this can save huge amounts of RAM while processing
- No limit to the data we can process - infinite data is fully supported here, as we do not need to load all of it at once
- Lazy loading of values - compute only the values we need, whenever we need them

## When to use the generators?
I guess a great rule is to always try to implement a generator whenever we have large data samples and we care about the RAM that our program will consume ( which shuld be always ).


## The `next()` function
As shown in the example, we have the `next` function or the `__next__` dunder method, which allow us to call the generator's next element. We can see this in the example below:
```bash
from typing import Generator


def fetch_n(numbers: int) -> Generator:
    counter = 0
    while counter < numbers:
        yield counter

        counter += 1

our_generator = fetch_n(2)
print(next(our_generator))
print(next(our_generator))
print(next(our_generator))
```

Here on each call we would get the next number, but what happens when we have two numbers, but we call `next` three times? Well, we would get a `StopIteration` error raised, which we can of course handle.

## Generator expressions
The generator expressions are basically list comprehensions but instead of square brackets `[]` we would use the square ones `()` in order to get the generator. A simple example would be the below.

```bash
our_generator = (n + n * n for n in range(15))

for n in our_generator:
    print(n)
```

result:
```bash
0
2
6
12
20
30
42
56
72
90
110
132
156
182
210
```

## The two special methods when working with generators
Now, for the generators, we have two special methods attached to them `send` and `close`. 

### The send method
The send method is pretty obvious, the way we use it is a bit counterintuitive though, but it allows us to send a value to a generator.

```bash
from typing import Generator


def multiply() -> Generator:
    while True:
        number = yield
        print(number * 2)


our_generator = multiply()
next(our_generator)
our_generator.send(15)
```

### The close method
The close method can close the generator before it is fully exhausted compltely.

```bash
from typing import Generator


def fetch_names() -> Generator:
    try:
        yield "Rebecca"
        yield "Theodore"
        yield "Benjamin"
    finally:
        print("Generator is closing")


our_generator = fetch_names()
print(next(our_generator))
print(next(our_generator))
our_generator.close()
```

# Conclusion
As we see the generators are really easy once you get the underlying idea of how they work. So I hope the next time you are going through large data sets, you will remember this article and posisbly use a generator : ) . Thank you and until next time!
