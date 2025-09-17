def main():
    import sys

    lines = sys.stdin.read().strip().splitlines()
    try:
        t = int(lines[0])
    except:
        return

    def power_sum(nums):
        if not nums:
            return 0
        first, *rest = nums
        return ((first ** 4) if first < 0 else 0) + power_sum(rest)

    def handle_case(i, remaining, results):
        if remaining == 0:
            return results
        if i >= len(lines):
            return results + [-1]
        try:
            x = int(lines[i])
        except:
            return results + [-1]
        if i + 1 >= len(lines):
            return results + [-1]
        values = lines[i + 1].split()
        if len(values) != x:
            return handle_case(i + 2, remaining - 1, results + [-1])
        try:
            arr = list(map(int, values))
        except:
            return handle_case(i + 2, remaining - 1, results + [-1])
        return handle_case(i + 2, remaining - 1, results + [power_sum(arr)])

    answers = handle_case(1, t, [])
    sys.stdout.write("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
