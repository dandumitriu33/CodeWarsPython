def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    passes = 1
    h = h * bounce
    while h > window:
        passes += 2
        h = h * bounce
    return passes


print(bouncing_ball(3, 0.66, 1.5))
