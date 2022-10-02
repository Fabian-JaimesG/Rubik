'''
Por el momento le pasaremos los parametro a la matriz formada.
Como funciona el codigo:
Se creara una matriz por cada cara, el nombre corresponde al valor del centro el cual siempre es fijo en el cubo.
Ej: Cubo Rubik formada:
    caraBlanca=    [['WE1','WA1','WE2'],['WA2','WC','WA3'],[['WE3','WA4','WA4']]];
    caraAmarrilla= [['YE1','YA1','YE2'],['YA2','YC','YA3'],[['YE3','YA4','YA4']]];
    caraAzul=      [['BE1','BA1','BE2'],['BA2','BC','BA3'],[['BE3','BA4','BA4']]];
    caraVerde=     [['GE1','GA1','GE2'],['GA2','GC','GA3'],[['GE3','GA4','GA4']]];
    caraRoja=      [['RE1','RA1','RE2'],['RA2','RC','RA3'],[['RE3','RA4','RA4']]];
    caraNaranja=   [['OE1','OA1','OE2'],['OA2','OC','OA3'],[['OE3','OA4','OA4']]];
siendo la primera letra la referencia al color W = Blanco y la segunda letra referencia al tipo de la cara (E = esquina, A = Arista, C= centro).
W=Blanco,Y=Amarrillo,G=Verde,B=Azul,O=Naranja,R=Rojo,
Movimientos rubik:
F: Front - Frontal
U: Up - Superior
D: Down - Inferior
R: Right - Derecha
L: Left - Izquierda
B: Back - Posterior
': mismos movimientos sentido antihorario (en codigo se pone i para hacer referencia a invertido)
Todos los movimientos seria equivalentes a un frente en sentidoi de como esta ubicado las caras
'''
import numpy as np

caraAmarrilla = [['YE1','YA1','YE2'],['YA2','YC','YA3'],['YE3','YA4','YE4']];
caraBlanca    = [['WE1','WA1','WE2'],['WA2','WC','WA3'],['WE3','WA4','WE4']];
caraAzul      = [['BE1','BA1','BE2'],['BA2','BC','BA3'],['BE3','BA4','BE4']];
caraVerde     = [['GE1','GA1','GE2'],['GA2','GC','GA3'],['GE3','GA4','GE4']];
caraRoja      = [['RE1','RA1','RE2'],['RA2','RC','RA3'],['RE3','RA4','RE4']];
caraNaranja   = [['OE1','OA1','OE2'],['OA2','OC','OA3'],['OE3','OA4','OE4']];

# Movimiento de los cubos:

def fHorario(izquierda,abajo,frente,arriba,derecha):
   nuevaizquierda = np.copy(izquierda);
   nuevaabajo     = np.copy(abajo);
   nuevafrente    = np.copy(frente);
   nuevaarriba    = np.copy(arriba);
   nuevaderecha   = np.copy(derecha);
   for i in range(3):
    nuevaizquierda[i][2]   = abajo[0][i];
    nuevaarriba[2][i] = izquierda[2-i][2];
    nuevaderecha[i][0]      = arriba[2][i];
    nuevaabajo[0][i]    = derecha[2-i][0];
    
    for j in range(3):
     nuevafrente[i][j] = frente[3-1-j][i]
   return nuevaizquierda,nuevaabajo,nuevafrente,nuevaarriba,nuevaderecha
def fAntihorario(izquierda,abajo,frente,arriba,derecha):
   nuevaizquierda= np.copy(izquierda);
   nuevaabajo= np.copy(abajo);
   nuevafrente= np.copy(frente);
   nuevaarriba= np.copy(arriba);
   nuevaderecha = np.copy(derecha);
   for i in range(3):
    nuevaizquierda[i][2]   = arriba[2][2-i];
    nuevaarriba[2][i] = derecha[i][0];
    nuevaderecha[i][0]      = abajo[0][2-i];
    nuevaabajo[0][i]    = izquierda[i][2];
    for j in range(3):
     nuevafrente[i][j] = frente[j][3-1-i]
   return nuevaizquierda,nuevaabajo,nuevafrente,nuevaarriba,nuevaderecha
def f():
    global caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja;
    caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja = fHorario(caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja);
def fi():
    global caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja;
    caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja = fAntihorario(caraNaranja,caraBlanca,caraAzul,caraAmarrilla,caraRoja);
def u():
    global caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde;
    caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde = fHorario(caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde);
def ui():
    global caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde;
    caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde = fAntihorario(caraAzul,caraRoja,caraAmarrilla,caraNaranja,caraVerde);
def r():
    global caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde;
    caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde = fHorario(caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde);
def ri():
    global caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde
    caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde = fAntihorario(caraAzul,caraBlanca,caraRoja,caraAmarrilla,caraVerde);
def l():
    global caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul;
    caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul = fHorario(caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul);
def li():
    global caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul;
    caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul = fAntihorario(caraVerde,caraBlanca,caraNaranja,caraAmarrilla,caraAzul);
def d():
    global caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja;
    caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja = fHorario(caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja);
def di():
    global caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja;
    caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja = fAntihorario(caraNaranja,caraVerde,caraBlanca,caraAzul,caraRoja);
def b():
    global caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja;
    caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja = fHorario(caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja);
def bi():
    global caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja;
    caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja = fAntihorario(caraVerde,caraBlanca,caraVerde,caraAmarrilla,caraNaranja);
 
print('normal')

print('\ncaraAmarrilla',caraAmarrilla,'\ncaraBlanca',caraBlanca,'\ncaraAzul',caraAzul,'\ncaraVerde',caraVerde,'\ncaraRoja',caraRoja,'\ncaraNaranja',caraNaranja);

ui();

print('despues de la ui:')
    
print('\ncaraAmarrilla',caraAmarrilla,'\ncaraBlanca',caraBlanca,'\ncaraAzul',caraAzul,'\ncaraVerde',caraVerde,'\ncaraRoja',caraRoja,'\ncaraNaranja',caraNaranja);