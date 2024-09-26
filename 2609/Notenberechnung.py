def calculate_grade(points: int, max_possible_points: int) -> int:

    if type(points) != int:
        raise TypeError(" Param was not of type int")

    if type(max_possible_points) != int:
        raise TypeError("Param was not of type int")

    if points < 0:
        raise ValueError(" Param 'points' was not in range")

    if max_possible_points < 0:
        raise ValueError(" Param 'max_possible_points' was not in range")

    if points > max_possible_points:
        raise ValueError(" Please provide points that are less than the maximum")

    return int((points / max_possible_points) * 100)


def get_grade_as_text(percent: int) -> str:

    if type(percent) != int:
        raise TypeError(" Please provide an integer")

    if percent < 0 or percent > 100:
        raise ValueError(" Please provide a valid percentage")

    if percent >= 92:
        return "sehr gut"
    if percent >= 81:
        return "gut"
    if percent >= 67:
        return "befriedigend"
    if percent >= 50:
        return "ausreichend"
    if percent >= 30:
        return "mangelhaft"
    return "ungenügend"

if(__name__ == "__main__"):
    print(get_grade_as_text("132"))
    print(calculate_grade(-2, 0))
    print(get_grade_as_text(49))
