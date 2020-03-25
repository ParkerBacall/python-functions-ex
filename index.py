x_pos = 0
e_pos = -1

def move():
    global x_pos
    x_pos += 1

move()

def move_by(amount):
    global x_pos
    x_pos += amount

move_by(-2)

def check_collision():
    global x_pos
    global e_pos
    if x_pos == e_pos:
        return True
    else:
        return False

did_collide = check_collision()
    
print(x_pos)
print(did_collide)
    
