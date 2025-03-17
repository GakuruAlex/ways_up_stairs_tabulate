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
    for index in range(no_stairs):
        if stairs_table[index]:
            for step in steps:
                if index + step < len(stairs_table):
                    stairs_table[index + step] += stairs_table[index]

    return stairs_table[no_stairs]

def main()-> None:
    stairs: int = 5
    steps: List[int] = [ 2, 1]
    num_ways: int = ways_stairs(steps=steps,no_stairs= stairs)

    print(f"There are {num_ways} ways up {stairs} stairs given allowed steps at a time are either of {steps}")
if __name__ =="__main__":
    main()