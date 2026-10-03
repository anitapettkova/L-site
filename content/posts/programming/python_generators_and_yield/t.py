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
