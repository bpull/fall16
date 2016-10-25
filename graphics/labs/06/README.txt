Part1:
    Case 1:
       rotate by 45degrees, then translate

    Case 2:
       translate 10, then rotate scene by 45

    Case 3:
       scale the y, then rotate

    Case 4:
       rotate the box, then scale the axis

Part2:
 a)--        --
   |1  0  0  0|   x  = x
   |0  1  0  0|   y  = y
   |0  0  1 20|   z  = z+20
   |0  0  0  1|   1  = 1
   --        --

 b) It processed the rotate transformation, then the scale transformation.

Part3:
   Since it goes backwards, I translated the square to the middle, rotated 45degrees, and moved back to its original position
    glTranslatef(0.0, 0.0, -15.0)
    glTranslatef(7.5,7.5,0)
    glRotate(45,0,0,1.0)
    glTranslatef(-7.5,-7.5,0)
    glRectf(5.0, 5.0, 10.0, 10.0)

Part4:

    glTranslatef(0,0,-15)

    glTranslatef(0,5,0)
    glutWireSphere(2.0, 10, 8)
    glTranslatef(0,-10,0)
    glutWireSphere(2.0, 10, 8)
    glTranslatef(-5,5,0)
    glutWireSphere(2.0, 10, 8)
    glTranslatef(10,0,0)
    glutWireSphere(2.0, 10, 8)
