def tournaments_schedule(number_of_teams):
    if number_of_teams < 2:
        raise Exception("Tournament must be at least 2 teams")
    teams = {num: list() for num in range(1, number_of_teams + 1)}
    schedule_DC(teams, 1, number_of_teams)
    return teams


# O(n^2)
def print_table(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[0], reverse=False)
    for i, v in sorted_teams:
        print(f"team {i}:", *v)
    print()


def length(low, high):
    return high - low + 1


# O(n)
def latin_square(low, high):
    square = []

    row = list(range(low, high + 1))

    if len(row) % 2 == 1:
        row.reverse()

    for _ in range(length(low, high)):
        square.append(row.copy())
        last = [row.pop()]
        row = last + row

    return square


def timing_2_team(teams, low):
    teams[low].append(low + 1)
    teams[low + 1].append(low)
    return


# O(n^3)
def schedule_DC(teams, low, high):
    if length(low, high) == 2:
        return timing_2_team(teams, low)

    is_odd = length(low, high) % 2 == 1
    temp = None

    if is_odd:
        high += 1
        if high in teams.keys():
            temp = teams.pop(high)
        teams[high] = list()

    mid = (low + high) // 2
    schedule_DC(teams, low, mid)
    schedule_DC(teams, mid + 1, high)

    schedule_connection(teams, low, mid, high)

    if is_odd:
        if temp is not None:
            teams[high] = temp
        else:
            teams.pop(high)

        for team in range(low, high):
            index = teams[team].index(high)
            teams[team][index] = '-'


# O(n^3)
def schedule_connection(teams, low, mid, high):
    square_up = latin_square(mid + 1, high)
    for team in range(low, mid + 1):
        teams[team] += square_up.pop(0)
        if '-' in teams[team]:
            rest_index = teams[team].index('-')
            last_game = teams[team].pop()
            teams[team][rest_index] = last_game

    for team in range(mid + 1, high + 1):
        if '-' in teams[team]:
            rest_index = teams[team].index('-')
            for other_team in range(low, mid + 1):
                if teams[other_team][rest_index] == team:
                    teams[team][rest_index] = other_team

    game = len(teams[mid]) - len(teams[mid + 1])
    for team in range(mid + 1, high + 1):
        for _ in range(game):
            game_index = len(teams[team])
            for other_team in range(low, mid + 1):
                if teams[other_team][game_index] == team:
                    teams[team].append(other_team)
