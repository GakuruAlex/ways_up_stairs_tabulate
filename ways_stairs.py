from typing import List
def ways_stairs(no_stairs: int, steps: List[int])-> int:
    """_Using tabulation to find how many ways its possible to get to the top stairs given a number of stairs to take at a time _

    Args:
        no_stairs (int): _Number of the stairs_
        steps (List[int]): _Allowed number of stairs you can move at a time_

    Returns:
        int: _Number of ways to get to the top_
    """
    stairs_table: List[int] = [0 for _ in range(no_stairs + 1)]
    stairs_table[0] = 1

    return stairs_table[no_stairs]