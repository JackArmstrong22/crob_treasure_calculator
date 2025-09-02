class Treasure:
    def __init__(
            self,
            name,
            point_per_jelly, point_per_level,
            jelly_num,
            cooldown, activation_time,
            enhancement_points
            ):
        self.name = name
        self.point_per_jelly = point_per_jelly
        self.point_per_level = point_per_level
        self.jelly_num = jelly_num
        self.cooldown = cooldown
        self.activation_time = activation_time
        self.enhancement_points = enhancement_points
