def collect_collectable(instance):
    staggs_to_remove = []
    sambuccas_to_remove = []

    # Check collect Staggs
    for key in instance.staggs:
        if (instance.game_player.get_pos()[0] + 16 > instance.staggs[key].pos[0] and
                instance.game_player.get_pos()[0] < instance.staggs[key].pos[0] + 16 and
                instance.game_player.get_pos()[1] + 16 > instance.staggs[key].pos[1] and
                instance.game_player.get_pos()[1] < instance.staggs[key].pos[1] + 16):
            instance.debug_string = f'Got Stagg {key}'
            instance.game_player.alter_energy(instance.staggs[key].energy_modifier)
            staggs_to_remove.append(key)

    # Check collect Sambuccas
    for key in instance.sambuccas:
        if (instance.game_player.get_pos()[0] + 16 > instance.sambuccas[key].pos[0] and
                instance.game_player.get_pos()[0] < instance.sambuccas[key].pos[0] + 16 and
                instance.game_player.get_pos()[1] + 16 > instance.sambuccas[key].pos[1] and
                instance.game_player.get_pos()[1] < instance.sambuccas[key].pos[1] + 16):
            instance.game_player.alter_energy(instance.sambuccas[key].energy_modifier)
            sambuccas_to_remove.append(key)
            instance.debug_string = f'Got Sambuccas {key}'

    # Remove collected
    if len(staggs_to_remove) > 0:
        for key in staggs_to_remove:
            del instance.staggs[key]
    if len(sambuccas_to_remove) > 0:
        for key in sambuccas_to_remove:
            del instance.sambuccas[key]
