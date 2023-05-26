from dataclasses import dataclass


@dataclass
class PlayerStats:
    seasons: int
    total_points: int
    average_points_per_game: float
    total_rebounds: float
    average_rebounds_per_game: float
    total_assists: int
    average_assists_per_game: float
    total_steals: int
    total_blocks: int
    field_goal_percentage: float
    free_throw_percentage: float
    three_point_percentage: float

    def __str__(self):
        return ''.join([
            f'Temporadas: {self.seasons}\n',
            f'Puntos totales: {self.total_points}\n',
            f'Promedio de puntos por partido: {self.average_points_per_game}\n',
            f'Rebotes totales: {self.total_rebounds}\n',
            f'Promedio de rebotes por partido: {self.average_rebounds_per_game}\n',
            f'Asistencias totales: {self.total_assists}\n',
            f'Promedio de asistencias por partido: {self.average_assists_per_game}\n',
            f'Robos totales: {self.total_steals}\n',
            f'Bloqueos totales: {self.total_blocks}\n',
            f'Porcentaje de tiros de campo: {self.field_goal_percentage}%\n',
            f'Porcentaje de tiros libres: {self.free_throw_percentage}%\n',
            f'Porcentaje de tiros triples: {self.three_point_percentage}%\n',
        ])
