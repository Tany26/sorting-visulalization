import pygame 
import random 
pygame.font.init() 
  
 
screen = pygame.display.set_mode( 
            (900, 650) 
        ) 
   
pygame.display.set_caption("SORTING VISUALISER") 
  

  
run = True
  
width = 900
length = 600
array =[0]*151
arr_clr =[(0, 204, 102)]*151
clr_ind = 0
clr =[(0, 204, 102), (255, 0, 0), 
      (0, 0, 153), (255, 102, 0)] 
fnt = pygame.font.SysFont("comicsans", 30) 
fnt1 = pygame.font.SysFont("comicsans", 20) 
  
  
def generate_arr(): 
    for i in range(1, 151): 
        arr_clr[i]= clr[0] 
        array[i]= random.randrange(1, 100) 
          
generate_arr()  
  
def refill(): 
    screen.fill((255, 255, 255)) 
    draw() 
    pygame.display.update() 
    pygame.time.delay(30) 
      
# Sorting Algo:Quick sort 
def quicksort(array, l, r): 
    if l<r: 
        pi = partition(array, l, r) 
        quicksort(array, l, pi-1) 
        refill() 
        for i in range(0, pi + 1): 
            arr_clr[i]= clr[3] 
        quicksort(array, pi + 1, r) 
          
# Function to partition the array 
def partition(array, low, high): 
    pygame.event.pump()  
    pivot = array[high] 
    arr_clr[high]= clr[2] 
    i = low-1
    for j in range(low, high): 
        arr_clr[j]= clr[1] 
        refill() 
        arr_clr[high]= clr[2] 
        arr_clr[j]= clr[0] 
        arr_clr[i]= clr[0] 
        if array[j]<pivot: 
            i = i + 1
            arr_clr[i]= clr[1] 
            array[i], array[j]= array[j], array[i] 
    refill() 
    arr_clr[i]= clr[0] 
    arr_clr[high]= clr[0] 
    array[i + 1], array[high] = array[high], array[i + 1]  
      
    return ( i + 1 ) 
      

def draw(): 
    txt = fnt.render("SORT : PRESS 'ENTER'", 
                       1, (0, 0, 0)) 
      
    screen.blit(txt, (20, 40)) 
    txt2 = fnt1.render("ALGORITHM USED: QUICK SORT", 
                       1, (0, 0, 0)) 
    screen.blit(txt, (600, 60)) 
    element_width =(width-150)//150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), 
                (0, 95), (900, 95), 6) 
       
    for i in range(1, 151): 
        pygame.draw.line(screen, 
                arr_clr[i], (boundry_arr * i-3, 100),
                (boundry_arr * i-3, 
                 array[i]*boundry_grp + 100), 
                 element_width) 
                   

while run: 
    
    screen.fill((255, 255, 255)) 
        
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: 
                generate_arr()  
            if event.key == pygame.K_RETURN: 
                quicksort(array, 1, len(array)-1)      
    draw() 
    pygame.display.update() 
      
pygame.quit() 
