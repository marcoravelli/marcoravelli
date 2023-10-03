import pygame
pygame.init()
finestra1 = pygame.display.set_mode((400,400))
#colors
RED = (255,255,255)
BLACK=(00,00,00)
GREEN=(0,160,100)
#vars
P=(0,0)
PUNTEGGIO=0
LATI=(30,30)
gap=35
k=0
X=0
Y=0
S=35 #step tra i tasti
R=pygame.Rect
ret=pygame.draw.rect
dot=pygame.draw.circle
#lists
T=[]
zone=[]
tasti=[]
lista_pos=[]
verdi=[]
EVENTI=[]
#disegno dei tasti


for i in range(10):
        Y=i*S+gap
        for j in range(10):
                X=j*S+gap
                k+=1
                Z=(X,Y)
                tasti.append(Z)
                P=Z
                ret(finestra1,RED,R(P,LATI),1)
                DX=Z[0]+LATI[0]/2
                DY=Z[1]+LATI[1]/2
                dot(finestra1,GREEN,(DX,DY),6)
                pygame.display.update()
                T=tasti
                                   
while True:        
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        for Q in tasti:
                                      P=Q  
                                      ret(finestra1, BLACK,R(P,LATI)) #cancella tutti i pallini
                                      ret(finestra1, RED,R(P,LATI),1)  #ridisegna tutti quadrati rimasti in tasti
                        for Q in T:
                                P=Q
                                if R(P,LATI).collidepoint(event.pos): #verifica se il punto cliccato è l''interno di un quadrato disponibile

                                                          ret(finestra1, BLACK,R(P,LATI)) #cancella il quadrato scelto
                                                          PUNTEGGIO+=1
                                                          pygame.draw.rect(finestra1, BLACK,(340,0,60,34))
                                                          stile_2=pygame.font.SysFont('Aral',41)
                                                          testo_2=stile_2.render(str(PUNTEGGIO),True,GREEN)
                                                          finestra1.blit(testo_2, (350,4))      #aggiorna il punteggio
                                                          print(PUNTEGGIO)
                                                          tasti.remove(Q)               #togli il quadrato scelto dalla lista tasti
                                                          pygame.display.update()
                                                           
                                                          #MOSSE POSSIBILI
                                                          N=(0,105)
                                                          NE=(70,70)
                                                          E=(105,0)
                                                          SE=(70,-70)
                                                          S=(0,-105)
                                                          SO=(-70,-70)
                                                          O=(-105,0)
                                                          NO=(-70,70)
                                                          moves=[N,NE,E,SE,S,SO,O,NO]
                                                          print(event.pos)
                                                          T=[]                          
                                                          for m in moves:
                                                                  scelta=(event.pos[0]+m[0],event.pos[1]+m[1])
                                                                  for Q in tasti:
                                                                        P=Q  
                                                                        if R(P,LATI).collidepoint(scelta): #verifica i quadrati disponibili
                                                                                      DX=Q[0]+LATI[0]/2
                                                                                      DY=Q[1]+LATI[1]/2
                                                                                      dot(finestra1,GREEN,(DX,DY),6)    #disegna un pallino nei quadratini disponibili
                                                                                      
                                                                                      T.append(Q) #aggiorna la lista T
                                                                                      pygame.display.update()
                                                                                      
                                                          if not T:                     # se T è vuota dichiara fine del gioco
                                                                                              ret(finestra1, RED,(70,105,245,105),3)
                                                                                              ret(finestra1, BLACK,(70,105,245,105))
                                                                                              stile=pygame.font.SysFont('Arial',24)
                                                                                              t1='NO MORE MOVES'
                                                                                              t2='100 HAI VINTO !'
                                                                                              if PUNTEGGIO<100:
                                                                                                      testo=stile.render(t1 , True, RED)
                                                                                              if PUNTEGGIO==100:
                                                                                                      testo=stile.render( t2, True, RED)                                                                                                      
                                                                                              finestra1.blit(testo, (80,150))
                                                                                              pygame.display.update()

                        if R(70,105,245,105).collidepoint(event.pos):
                                print('prova')
                                                                                              
                                                                                            
                                                                                              

                                                                                                      

                                         
                                         
                                  
                                
                        
                        


