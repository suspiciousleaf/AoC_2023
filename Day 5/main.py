import time

t0 = time.perf_counter()
# Import data
with open("Day 5/input.txt", "r") as infile:
    input = infile.read().split("\n\n")

seeds = [int(num) for num in input[0].replace("seeds: ", "").split()]
input = input[1:]


def find_location(seeds):
    """Takes a list of seeds and transforms them to location, returns the final locations and the initial seed numbers

    Args:
        seeds (list): Seed numbers to be transformed

    Returns:
        (locations[list], seeds[list])
    """
    s_s_input = input[0].replace("seed-to-soil map:\n", "").split("\n")

    # Indices match both lists, contain range objects, loop to check which range the seed is in.
    s_s_source = []
    s_s_output = []

    for line in s_s_input:
        split_line = [int(num) for num in line.split()]
        s_s_source.append(range(split_line[1], split_line[1] + split_line[2]))
        s_s_output.append(range(split_line[0], split_line[0] + split_line[2]))

    soils = []

    for seed in seeds:
        soil = None
        for i, source_range in enumerate(s_s_source):
            if seed in source_range:
                soil = s_s_output[i][0] + (seed - source_range[0])
                break
        if soil is None:
            soil = seed
        soils.append(soil)

    # print("Soils:", soils)

    #############################################################################

    s_f_input = input[1].replace("soil-to-fertilizer map:\n", "").split("\n")

    s_f_source = []
    s_f_output = []

    for line in s_f_input:
        split_line = [int(num) for num in line.split()]
        s_f_source.append(range(split_line[1], split_line[1] + split_line[2]))
        s_f_output.append(range(split_line[0], split_line[0] + split_line[2]))

    # seeds = []
    fertilizers = []
    for soil in soils:
        fertilizer = None
        for i, source_range in enumerate(s_f_source):
            if soil in source_range:
                fertilizer = s_f_output[i][0] + (soil - source_range[0])
                break
        if fertilizer is None:
            fertilizer = soil
        fertilizers.append(fertilizer)

    # print("Fertilizers:", fertilizers)

    #############################################################################

    f_w_input = input[2].replace("fertilizer-to-water map:\n", "").split("\n")

    f_w_source = []
    f_w_output = []

    for line in f_w_input:
        split_line = [int(num) for num in line.split()]
        f_w_source.append(range(split_line[1], split_line[1] + split_line[2]))
        f_w_output.append(range(split_line[0], split_line[0] + split_line[2]))

    soils = []
    waters = []
    for fertilizer in fertilizers:
        water = None
        for i, source_range in enumerate(f_w_source):
            if fertilizer in source_range:
                water = f_w_output[i][0] + (fertilizer - source_range[0])
                break
        if water is None:
            water = fertilizer
        waters.append(water)

    # print("Waters:", waters)

    #############################################################################

    w_l_input = input[3].replace("water-to-light map:\n", "").split("\n")

    w_l_source = []
    w_l_output = []

    for line in w_l_input:
        split_line = [int(num) for num in line.split()]
        w_l_source.append(range(split_line[1], split_line[1] + split_line[2]))
        w_l_output.append(range(split_line[0], split_line[0] + split_line[2]))

    fertilizers = []
    lights = []

    for water in waters:
        light = None
        for i, source_range in enumerate(w_l_source):
            if water in source_range:
                light = w_l_output[i][0] + (water - source_range[0])
                break
        if light is None:
            light = water
        lights.append(light)

    # print("Lights:", lights)

    #############################################################################

    l_t_input = input[4].replace("light-to-temperature map:\n", "").split("\n")

    l_t_source = []
    l_t_output = []

    for line in l_t_input:
        split_line = [int(num) for num in line.split()]
        l_t_source.append(range(split_line[1], split_line[1] + split_line[2]))
        l_t_output.append(range(split_line[0], split_line[0] + split_line[2]))

    waters = []
    temps = []

    for light in lights:
        temp = None
        for i, source_range in enumerate(l_t_source):
            if light in source_range:
                temp = l_t_output[i][0] + (light - source_range[0])
                break
        if temp is None:
            temp = light
        temps.append(temp)

    # print("Temps:", temps)

    #############################################################################

    t_h_input = input[5].replace("temperature-to-humidity map:\n", "").split("\n")

    t_h_source = []
    t_h_output = []

    for line in t_h_input:
        split_line = [int(num) for num in line.split()]
        t_h_source.append(range(split_line[1], split_line[1] + split_line[2]))
        t_h_output.append(range(split_line[0], split_line[0] + split_line[2]))

    lights = []
    hums = []

    for temp in temps:
        hum = None
        for i, source_range in enumerate(t_h_source):
            if temp in source_range:
                hum = t_h_output[i][0] + (temp - source_range[0])
                break
        if hum is None:
            hum = temp
        hums.append(hum)

    # print("Hums:", hums)

    #############################################################################

    h_l_input = input[6].replace("humidity-to-location map:\n", "").split("\n")

    h_l_source = []
    h_l_output = []

    for line in h_l_input:
        split_line = [int(num) for num in line.split()]
        h_l_source.append(range(split_line[1], split_line[1] + split_line[2]))
        h_l_output.append(range(split_line[0], split_line[0] + split_line[2]))

    temps = []
    locations = []

    for hum in hums:
        location = None
        for i, source_range in enumerate(h_l_source):
            if hum in source_range:
                location = h_l_output[i][0] + (hum - source_range[0])
                break
        if location is None:
            location = hum
        locations.append(location)

    return (locations, seeds)


# Inputs all seeds to be transformed, and finds the lowest value for location
print(f"Part One: {min(find_location(seeds)[0])}")

#############################################################################

# The above is too inefficient for Part Two, single it requires many billions of seeds to be tested. Run time would be approx 6 days. Instead I initially ran every 1 in 100,000 seeds through to identify the range that holds the lowest value, then tested every 10,000 seeds in that range to identify a narrow range, and finally tested every seed +/- 10,000 in that identified range. This tool approx 25 seconds to run.

seeds_two = []

for i in range(0, len(seeds), 2):
    seeds_two.append(range(seeds[i], seeds[i] + seeds[i + 1], 100000))


lowest_location = 9999999999999

# Find approx value of lowest seed (1 in 100,000)
for i, seed_range in enumerate(seeds_two):
    for single_seed in seed_range:
        loc = find_location([single_seed])
        if loc[0][0] < lowest_location:
            lowest_location = loc[0][0]
            lowest_seed = loc[1][0]

# Identify the range that holds that seed
for x in seeds_two:
    if x[0] <= lowest_seed <= x[-1]:
        test_range_min, test_range_max = x[0], x[-1]

# Test 1 in 10,000 seeds in that range to create a narrow range
for single_seed_10000 in range(test_range_min, test_range_max, 10000):
    loc = find_location([single_seed_10000])
    if loc[0][0] < lowest_location:
        lowest_location = loc[0][0]
        lowest_seed = loc[1][0]

# Test every seed +/- 10,000 in that narrow range to find exact value
for single_seed in range(lowest_seed - 10000, lowest_seed + 10000):
    loc = find_location([single_seed])
    if loc[0][0] < lowest_location:
        lowest_location = loc[0][0]
        lowest_seed = loc[1][0]

print(f"Part Two: {lowest_location}")


print(f"Time taken: {time.perf_counter() - t0:.2f} s")
