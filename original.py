from multiprocessing import Process, Queue


def worker(inb, outb):
    while True:
        part = inb.get()

        if part is None:
            break

        outb.put(sorted(part))


def merge_all(parts):
    out = []

    for p in parts:
        out += p

    return out


if __name__ == "__main__":
    data = [5, 1, 9, 3, 7, 2, 8, 4, 6]

    mid = len(data) // 2

    q_in = Queue()
    q_out = Queue()

    W = [Process(target=worker, args=(q_in, q_out)) for _ in range(2)]
    for w in W:
        w.start()
    q_in.put(data[:mid])
    q_in.put(data[mid:])

    for _ in W:
        q_in.put(None)

    parts = [q_out.get(), q_out.get()]

    print(merge_all(parts))

    for w in W:
        w.join()
