from .extract_treasure_csv import get_treasure_data


def playtime_calc(level, time_in_sec):
    if time_in_sec == 0:
        return "Invalid time!"

    print("time_in_sec: ", time_in_sec)

    level -= 1
    treasure_data = get_treasure_data()
    result_dict = {}

    for treasure in treasure_data.values():
        activation_count = time_in_sec // treasure.cooldown
        # not enough time to collect it
        if time_in_sec % treasure.cooldown < treasure.activation_time:
            activation_count -= 1

        enhancement = 0

        if level == 11:
            enhancement = treasure.enhancement_points
            print("point_value if treasure lvl 11: ", enhancement)

        point_value = (treasure.point_per_jelly + enhancement + (
            treasure.point_per_level * level)
                    ) * treasure.jelly_num

        point_total = point_value * activation_count

        print(
            treasure.name,
            "level:", level,
            "point_per_jelly:", treasure.point_per_jelly,
            "point_per_level:", treasure.point_per_level,
            "jelly_num:", treasure.jelly_num,
            "activation_count:", activation_count,
            "point_value:", point_value,
            "point_total:", point_total
        )

        result_dict[treasure.name] = {
            "treasure": treasure.name,
            "activation_count": activation_count,
            "point_value": point_value,
            "point_total": point_total
        }

    sorted_results = sorted(
        result_dict.items(),
        # sort by point total first, then if tie sort by name
        key=lambda item: (item[1]["point_total"], item[0]),
        reverse=True
    )

    return sorted_results


def package_treasure(treasure, activation_count, point_value, point_total):
    my_dict = {}
    my_dict[treasure.name] = {
            "treasure": treasure.name,
            "activation_count": activation_count,
            "point_value": point_value,
            "point_total": point_total
        }
    return my_dict
