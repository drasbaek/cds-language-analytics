import argparse

def input_parse():
    # initialize parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type=str, default="John Doe")
    parser.add_argument("--age", type=int)
    # parse arguments
    args = parser.parse_args()
    return args

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old.")

def main():
    # run input parse
    args = input_parse()

    # get name and age
    name = args.name
    age = args.age

    # pass name to hello
    hello(name, age)

if __name__ == "__main__":
    main()
