import csv
from .treasure_class import Treasure
from pathlib import Path

file_path = Path(__file__).parent / "treasure_data.csv"


def get_treasure_data():
    treasure_dict = {}
    with file_path.open() as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            treasure = Treasure(
                name=row['name'],
                point_per_jelly=int(row['point_per_jelly']),
                point_per_level=int(row['point_per_level']),
                jelly_num=int(row['jelly_num']),
                cooldown=float(row['cooldown']),
                activation_time=float(row['activation_time']),
                enhancement_points=int(row['enhancement_points']),
                enhancement_points_per_level=int(
                    row['enhancement_points_per_level']
                )
            )
            treasure_dict[row['name']] = treasure

    return treasure_dict
