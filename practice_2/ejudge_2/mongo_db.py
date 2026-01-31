import sys


def main():
    input_lines = sys.stdin.read().strip().split("\n")
    n = int(input_lines[0])
    document = {}
    output = []

    for i in range(1, n + 1):
        parts = input_lines[i].split(maxsplit=2)

        if parts[0][0] == "s":
            document[parts[1]] = parts[2]
        else:
            key = parts[1]
            if key in document:
                output.append(document[key])
            else:
                output.append("KE: no key " + key + " found in the document")

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
