#Given N non-negative integers a1,a2,....an where each represents a point at coordinate (i, ai). N vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i,0). Find two lines, which together with x-axis forms a container, such that it contains the most water.Note : In Case of single verticle line it will not be able to hold water.
def maxArea(A,le):
    def maxArea(A,le):
        left = 0
        right = le - 1
        max_area = 0
        while left<right:
            current_area = min(A[left],A[right])*(right-left)
        
            if current_area>max_area:
                max_area = current_area
            
            if A[left]<A[right]:
                left += 1
            
            else:
                right -= 1
        return max_area
    