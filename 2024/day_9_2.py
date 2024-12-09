class Bucket:
    def __init__(self, capacity, value="."):
        self.capacity = int(capacity)
        self.content = [value] * self.capacity
        self.filled = 0
        self.used = False

    def can_fit(self, new_bucket):
        if not new_bucket.used:
            return self.capacity - self.filled >= new_bucket.capacity
        else:
            return False

    def store(self, new_bucket):
        self.content[self.filled:self.filled + new_bucket.capacity] = new_bucket.content
        self.filled += new_bucket.capacity

    def reset(self):
        self.filled = self.capacity
        self.content = ["."] * self.capacity
        self.used = True


if __name__ == '__main__':
    with open("input_day_9_1.txt", "r") as f:
        lines = f.readlines()

    lines = [c for c in lines[0]]

    values = lines[:: 2]
    spaces = lines[1:: 2]
    if len(values) > len(spaces):
        spaces.append("0")

    ids = [i for i in range(len(values))]

    empty_buckets = [Bucket(s) for s in spaces]
    filled_buckets = [Bucket(v, id) for id, v in zip(ids, values)]
    message = []
    for fill, empty in zip(filled_buckets, empty_buckets):
        message += fill.content + empty.content

    for i, filled_bucket in enumerate(reversed(filled_buckets)):
        for j, bucket in enumerate(empty_buckets):
            if j >= len(filled_buckets) - i - 1:
                break
            if bucket.can_fit(filled_bucket):
                bucket.store(filled_bucket)
                filled_bucket.reset()

    message = []
    for fill, empty in zip(filled_buckets, empty_buckets):
        message += fill.content + empty.content

    total = 0
    for i in range(len(message)):
        if message[i] != ".":
            total += i * int(message[i])

    print(total)

