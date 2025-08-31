from extract_treasure_csv import get_treasure_data


def playtime_calc(level, time_in_sec):
    if time_in_sec == 0:
        return "Invalid time!"

    level -= 1
    treasure_data = get_treasure_data()

    for treasure in treasure_data.values():
        activation_count = time_in_sec // treasure.cooldown
        if time_in_sec % treasure.cooldown < treasure.activation_time:
            activation_count -= 1

        point_total = (treasure.point_per_jelly +
                       (treasure.point_per_level * level)
                       ) * treasure.jelly_num

    return point_total
