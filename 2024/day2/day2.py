def is_safe(report: str) -> bool:
    levels = list(map(int, report.split()))

    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if not all(abs(diff) in range(1, 4) for diff in differences):
        return False

    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing

def is_safe_with_dampener(report: str) -> bool:
    if is_safe(report):
        return True

    levels = report.split()
    for i in range(len(levels)):
        modified_report = " ".join(levels[:i] + levels[i+1:])
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports(data, dampener=False):
    """
    Counts safe reports.
    :param data: List of report strings
    :param dampener: If True, uses Problem Dampener logic (Part 2)
    :return: Number of safe reports
    """
    if dampener:
        return sum(1 for report in data if is_safe_with_dampener(report))
    else:
        return sum(1 for report in data if is_safe(report))

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()

    safe_count_part1 = count_safe_reports(data, dampener=False)
    print(f"Number of safe reports (Part 1): {safe_count_part1}")

    safe_count_part2 = count_safe_reports(data, dampener=True)
    print(f"Number of safe reports (Part 2): {safe_count_part2}")
