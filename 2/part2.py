def is_valid_report(report):
    vals = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = all(v > 0 for v in vals)
    decreasing = all(v < 0 for v in vals)
    within_limit = all(abs(v) <= 3 for v in vals)
    return (increasing or decreasing) and within_limit


def is_valid_with_level_removed(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_valid_report(new_report):
            return True
    return False


total = 0

with open('input.txt') as f:
    for line in f:
        report = list(map(int, line.split()))
        if is_valid_report(report) or is_valid_with_level_removed(report):
            total += 1

print(total)
