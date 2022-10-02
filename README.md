# Explicacion Cubo Rubik

## Estado cubo ordenado
Por el momento le pasaremos los parametro a la matriz formada.
Como funciona el codigo:
Se creara una matriz por cada cara, el nombre corresponde al valor del centro el cual siempre es fijo en el cubo.
Ej: Cubo Rubik formada: 
- caraBlanca=    [['WE1','WA1','WE2'],['WA2','WC','WA3'],['WE3','WA4','WA4']];
- caraAmarrilla= [['YE1','YA1','YE2'],['YA2','YC','YA3'],['YE3','YA4','YA4']];
- caraAzul=      [['BE1','BA1','BE2'],['BA2','BC','BA3'],['BE3','BA4','BA4']];
- caraVerde=     [['GE1','GA1','GE2'],['GA2','GC','GA3'],['GE3','GA4','GA4']];
- caraRoja=      [['RE1','RA1','RE2'],['RA2','RC','RA3'],['RE3','RA4','RA4']];
- caraNaranja=   [['OE1','OA1','OE2'],['OA2','OC','OA3'],['OE3','OA4','OA4']];

siendo la primera letra la referencia al color W = Blanco y la segunda letra referencia al tipo de la cara (E = esquina, A = Arista, C= centro).
W=Blanco,Y=Amarrillo,G=Verde,B=Azul,O=Naranja,R=Rojo,
Movimientos rubik:
- F: Front - Frontal
- U: Up - Superior
- D: Down - Inferior
- R: Right - Derecha
- L: Left - Izquierda
- B: Back - Posterior
- ': mismos movimientos pero en sentido antihorario (en codigo se pone i para hacer referencia a invertido)

Todos los movimientos seria equivalentes a un frente en sentidoi de como esta ubicado las caras 


# Movimientos del cubo
![Movimientos Rubik](https://kubekings.com/img/cms/notacion-cubo/17.png "Movimientos Rubik")

## Hacer frente (f)

| Movimiento |  i |  j0 |  j1 |  j2 |
|     --     | -- |  -- |  -- |  -- |
| original   | i0 |(0,0)|(0,1)|(0,2)|
| rotada     | i0 |(2,0)|(1,0)|(0,0)|
| original   | i1 |(1,0)|(1,1)|(1,2)|
| rotada     | i1 |(2,1)|(1,1)|(0,1)|
| original   | i2 |(2,0)|(2,1)|(2,2)|
| rotada     | i2 |(2,2)|(1,2)|(0,2)|

**rotada[ i ][ j ]** = original[3 -1 -j ][ i ] => 3 por el tamaño de la matriz

## Hacer frente invertido (fi)
| Movimiento |  i |  j0 |  j1 |  j2 |
|     --     | -- |  -- |  -- |  -- |
| original   | i0 |(0,0)|(0,1)|(0,2)|
| rotada     | i0 |(0,2)|(1,2)|(2,2)|
| original   | i1 |(1,0)|(1,1)|(1,2)|
| rotada     | i1 |(0,1)|(1,1)|(2,1)|
| original   | i2 |(2,0)|(2,1)|(2,2)|
| rotada     | i2 |(0,0)|(1,0)|(2,0)|

**rotada[ i ][ j ]** = original[ j ][ 3-1-i ] => 3 por el tamaño de la matriz



## Rotar matriz frente:
```py
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
```
## Frente invertido:
```py
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
```

**rotada[ i ][ j ]** = original[len original -1][ i ]