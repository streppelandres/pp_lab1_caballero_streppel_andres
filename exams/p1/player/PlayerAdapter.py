from player.Player import Player
from player.PlayerStats import PlayerStats


def adapt_players(players: list) -> list:
    '''
    Adapts JSON players to the Players class
        returns: List of Players adapted
    '''
    return [__adapt_player(player) for player in players]


def __adapt_player(player: any) -> Player:
    '''
    Adapt JSON player to the Player class
        returns: Player adapted
    '''
    return Player(
        str(player['nombre']),
        str(player['posicion']),
        __adapt_player_stats(player['estadisticas']),
        player['logros']
    )


def __adapt_player_stats(stats: dict) -> PlayerStats:
    '''
    Adapts player JSON stats to PlayerStats class
        returns: PlayerStats adapted
    '''
    return PlayerStats(
        int(stats['temporadas']),
        int(stats['puntos_totales']),
        float(stats['promedio_puntos_por_partido']),
        int(stats['rebotes_totales']),
        float(stats['promedio_rebotes_por_partido']),
        int(stats['asistencias_totales']),
        float(stats['promedio_asistencias_por_partido']),
        int(stats['robos_totales']),
        int(stats['bloqueos_totales']),
        float(stats['porcentaje_tiros_de_campo']),
        float(stats['porcentaje_tiros_libres']),
        float(stats['porcentaje_tiros_triples'])
    )
