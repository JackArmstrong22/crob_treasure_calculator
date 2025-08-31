from playtime_calc import playtime_calc

if __name__ == "__main__":
    result = playtime_calc(1, 24)
    print(result)
    for name, data in result:
        treasure_obj = data["treasure"]
        print(treasure_obj.name, treasure_obj.cooldown,
              treasure_obj.point_per_jelly)
