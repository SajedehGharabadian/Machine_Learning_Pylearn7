import numpy as np


def generate_data(SCREEN_WIDTH,SCREEN_HEIGHT,snake,apple,wall_width):

    b_up = 0
    b_right = 0
    b_down = 0
    b_left = 0

    

    if snake.center_x == apple.center_x and snake.center_y < apple.center_y:
        a_up = 1#np.abs((snake.center_x - apple.center_x )) + np.abs((snake.center_y - apple.center_y ))
    else:
        a_up = 0

    if snake.center_x == apple.center_x and snake.center_y > apple.center_y:
        a_down = 1#np.abs((snake.center_x - apple.center_x )) + np.abs((snake.center_y - apple.center_y ))
    else:
        a_down = 0

    if snake.center_x > apple.center_x and snake.center_y == apple.center_y:
        a_left = 1#np.abs((snake.center_x - apple.center_x )) + np.abs((snake.center_y - apple.center_y ))

    else:
        a_left = 0

    if snake.center_x < apple.center_x and snake.center_y == apple.center_y:
        a_right = 1#np.abs((snake.center_x - apple.center_x )) + np.abs((snake.center_y - apple.center_y ))
    else:
        a_right = 0


    for part in snake.body:
        if snake.center_x == part['x'] and snake.center_y > part['y']:
            b_down = 1#np.abs((snake.center_x - part['x'] )) + np.abs((snake.center_y - part['y'] ) )

        else:
            b_down = 0
            

        if snake.center_x == part['x'] and snake.center_y < part['y']:
            b_up = 1#np.abs((snake.center_x - part['x'] )) + np.abs((snake.center_y - part['y'] ) )

        
        else:
            b_up = 0

        if snake.center_x > part['x'] and snake.center_y ==  part['y']:
            b_left = 1#np.abs((snake.center_x - part['x'] )) + np.abs((snake.center_y - part['y'] ) )

        else:
            b_left = 0

        if snake.center_x < part['x'] and snake.center_y ==  part['y']:
            b_right = 1#np.abs((snake.center_x - part['x'] )) + np.abs((snake.center_y - part['y'] ) )

        
        else:
            b_right = 0



    return np.array([a_up,a_right,a_down,a_left,b_up,b_right,b_down,b_left]
                    ,dtype=np.float32)



