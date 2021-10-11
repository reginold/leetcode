from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        set = [self.calHash(i) for i in obstacles]

        x = 0
        y = 0
        # people x,y and the direction
        dir = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        ans = 0
        for command in commands:
            if command == -1:
                dir = (dir + 1) % 4
            elif command == -2:
                dir = (dir + 3) % 4
            else:
                for i in range(command):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if self.calHash([nx, ny]) in set:
                        break
                    x = nx
                    y = ny
                    ans = max(ans, x * x + y * y)
        return ans

    def calHash(self, obstacle):
        return str(obstacle[0]) + "," + str(obstacle[1])
