#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    txt = dir(hidden_4)
    for i in txt:
        if not i.startswith("__"):
            print(i)