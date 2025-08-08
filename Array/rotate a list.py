def rotate_left(ARR, D):
        n=len(ARR)
        D=D%n 
        return ARR[D:]+ARR[:D]
