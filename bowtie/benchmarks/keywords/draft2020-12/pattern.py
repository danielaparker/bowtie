import string
import random

def get_benchmark():

    max_string_size = 1000000
    string_size = 1000

    benchmarks = []
    while string_size <= max_string_size:
        letters = string.ascii_letters
        random_letter_string = ''.join(random.choice(letters) for _ in range(string_size))
        benchmarks.append(dict(
            name=f"pattern_{string_size}",
            description=(
                "A benchmark for validation of the `pattern` keyword."
            ),
            schema=dict(type="string", pattern="^[a-zA-Z]+$"),
            tests=[
                dict(description="Empty String", instance=""),
                dict(description="Invalid Char at First", instance="1"+random_letter_string),
                dict(description="Invalid Char at Middle", instance=(
                        random_letter_string[:string_size//2]+"1"+random_letter_string[string_size//2:]
                )),
                dict(description="Invalid Char at Last", instance=random_letter_string+"1"),
                dict(description="Valid String", instance=random_letter_string),
            ],
        ))
        string_size *= 10

    return benchmarks
