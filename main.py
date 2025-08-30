from extract_treasure_csv import get_treasure_data


if __name__ == "__main__":
    treasure_dict = get_treasure_data()

    for name, treasure in treasure_dict.items():
        print(name, treasure.__dict__)
