#! /usr/bin/env python3

# add the required function(s) here

if __name__ == "__main__":
    input_numbers = [int(_) for _ in input().split()]
    result = round(variance(input_numbers),2)
    print(result)
