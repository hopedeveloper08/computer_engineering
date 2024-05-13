def tournaments_schedule(number_of_teams):
    if number_of_teams < 2:
        raise Exception("Tournament must be at least 2 teams")

    teams = {num: list() for num in range(1, number_of_teams + 1)}
    _schedule_DC(teams, 1, number_of_teams)

    return teams


def print_table(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[0], reverse=False)

    for i, v in sorted_teams:
        print(f"team {i}:", *v)
    print()


def _schedule_DC(teams, low, high):
    if _length(low, high) == 2:
        return _timing_2_team(teams, low)

    is_odd = _length(low, high) % 2 == 1
    temp = None

    if is_odd:
        high += 1
        if high in teams.keys():
            temp = teams.pop(high)
        teams[high] = list()

    mid = (low + high) // 2
    _schedule_DC(teams, low, mid)

    for team in range(mid + 1, high + 1):
        teams[team] += [0] * _length(low, high - 1)

    _schedule_next(teams, low, mid, high)
    _schedule_down(teams, low, mid, high)

    if is_odd:
        if temp is not None:
            teams[high] = temp
        else:
            teams.pop(high)

        for team in range(low, high):
            index = teams[team].index(high)
            teams[team][index] = '-'


def _length(low, high):
    return high - low + 1


def _timing_2_team(teams, low):
    teams[low].append(low + 1)
    teams[low + 1].append(low)


def _schedule_next(teams, low, mid, high):
    square_up = _latin_square(mid + 1, high)

    for team in range(low, mid + 1):
        square = square_up.pop(0)
        teams[team] += square

        if '-' in teams[team]:
            rest_index = teams[team].index('-')
            last_game = teams[team].pop()
            teams[team][rest_index] = last_game

        for opponent in square:
            game = teams[team].index(opponent)
            teams[opponent][game] = team


def _schedule_down(teams, low, mid, high):
    size = len(teams[mid]) // 2
    for team in range(mid + 1, high + 1):
        for game in range(size + 1):
            teams[team][game] = (teams[team - mid][game] + mid)
            if teams[team][game] > high:
                teams[team][game] = teams[team][game] % high


def _latin_square(low, high):
    square = []

    row = list(range(low, high + 1))

    if len(row) % 2 == 1:
        row.reverse()

    for _ in range(_length(low, high)):
        square.append(row.copy())
        last = [row.pop()]
        row = last + row

    return square
