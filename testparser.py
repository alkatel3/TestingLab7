def parse_output(output):
    iperf = {
        'Interval': [],
        'Transfer': [],
        'Bandwidth': [],
    }

    data = output[6:]
    for line in data:
        sliced = line[6:]
        parts = sliced.split()
        iperf['Interval'].append(parts[0])
        iperf['Transfer'].append(parts[2])
        iperf['Bandwidth'].append(parts[4])

    return iperf
