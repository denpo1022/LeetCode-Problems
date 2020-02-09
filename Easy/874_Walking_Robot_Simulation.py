class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curX, curY, direction, ans = 0, 0, 0, 0
        obstacles = set([tuple(i) for i in obstacles])
        for command in commands:
            if(command == -2):
                direction -= 1
            elif(command == -1):
                direction += 1
            else:
                for _ in range(command):
                    if(direction % 4 == 1):
                        if((curX + 1, curY) in obstacles):
                            break
                        else:
                            curX += 1
                    elif(direction % 4 == 2):
                        if((curX, curY - 1) in obstacles):
                            break
                        else:
                            curY -= 1
                    elif(direction % 4 == 3):
                        if((curX - 1, curY) in obstacles):
                            break
                        else:
                            curX -= 1
                    else:
                        if((curX, curY + 1) in obstacles):
                            break
                        else:
                            curY += 1
                ans = max(ans, curX**2 + curY**2)
        return ans