f = open("4.txt", "r").readlines()



ans = 0

for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "X":
            right, left, up, down, ur, ul, dr, dl = (True for _ in range(8))
            for k in range(1, 4):
                # right
                if i + k >= len(f):
                    down = False
                    dl = False
                    dr = False
                if j + k >= len(f[i]):
                    right, ur, dr = (False for _ in range(3))
                if i - k < 0:
                    up, ur, ul = (False for _ in range(3))
                if j-k < 0:
                    left, ul, dl = (False for _ in range(3))
                
                if right:
                    if f[i][j+k] != "XMAS"[k]:
                        right = False
                
                if left:
                    if f[i][j-k] != "XMAS"[k]:
                        left = False
                
                if up:
                    if f[i-k][j] != "XMAS"[k]:
                        up = False

                if down:
                    if f[i+k][j] != "XMAS"[k]:
                        down = False

                if dr:
                    if f[i+k][j+k] != "XMAS"[k]:
                        dr = False

                if dl:
                    if f[i+k][j-k] != "XMAS"[k]:
                        dl = False

                if ur:
                    if f[i-k][j+k] != "XMAS"[k]:
                        ur = False
                
                if ul:
                    if f[i-k][j-k] != "XMAS"[k]:
                        ul = False


            ans += (up, down, left, right, ur, ul, dr, dl).count(True)


print(ans)
