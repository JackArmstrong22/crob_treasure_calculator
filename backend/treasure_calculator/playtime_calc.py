from .extract_treasure_csv import get_treasure_data


def playtime_calc(level, time_in_sec):
    if time_in_sec == 0:
        return "Invalid time!"

    level -= 1
    treasure_data = get_treasure_data()
    result_dict = {}

    for treasure in treasure_data.values():
        activation_count = int(time_in_sec // treasure.cooldown)
        # not enough time to collect it
        if time_in_sec % treasure.cooldown < treasure.activation_time:
            activation_count -= 1

        point_value = (treasure.point_per_jelly +
                       (treasure.point_per_level * level)
                       ) * treasure.jelly_num

        point_total = point_value * activation_count

        result_dict.update(
            package_treasure(treasure, activation_count, point_value,
                             point_total)
        )

    sorted_results = sorted(
        result_dict.items(),
        key=lambda item: item[1]["point_total"],
        reverse=True
    )

    return list(sorted_results)


def package_treasure(treasure, activation_count, point_value, point_total):
    my_dict = {}
    my_dict[treasure.name] = {
            "treasure": treasure.name,
            "activation_count": activation_count,
            "point_value": point_value,
            "point_total": point_total
        }
    return my_dict
