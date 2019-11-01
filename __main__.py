#!/usr/bin/python3

from queue import Queue
from threading import Thread
from srcs.brain import Brain


def get_input(queue):
    while True:
        try:
            line = input()
        except (EOFError, KeyboardInterrupt):
            queue.put(["END"])
            break
        if line.endswith('\r\n'):
            line = line[:-2]
        elif line.endswith('\n'):
            line = line[:-1]
        if len(line.split(" ")) == 0:
            continue
        queue.put(line.split(" "))
        if line == "END":
            break
    return 0


def main():
    b = Brain()
    queue = Queue()
    x = Thread(target=get_input, args=(queue,), daemon=True)
    x.start()
    while True:
        if not queue.empty():
            stdin_input = queue.get()
            if stdin_input[0] == "END":
                break
            try:
                decision = b.think(stdin_input)
            except (IndexError):
                decision = "ERROR"
            finally:
                if decision:
                    print(decision, end="\r\n")
    return 0


if __name__ == "__main__":
    exit(main())
