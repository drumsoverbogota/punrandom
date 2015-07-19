# punrandom
Programa que genera sonidos aleatorios utilizando una cadena de Markov para usar estados y generar la música aleatoria por medio de interfaz MIDI.

## Requerimientos 
 - Python 2.7
 - Pygame
 - Un sintetizador de software MIDI. Windows viene con uno por defecto (Microsoft GS Wavetable SW Synth) pero puede ser utilizado cualquier otro.

## Usandolo

Para usarlo, una vez abierto (o importado) para correrlo hay que escribir:
```python
run(bpm,matriz,instrumento)
```
 - bpm : Son los bits por minuto, entre mayor el valor, será menor la duración del sonido
 - matriz : Indica la matriz a ser usada; hay tres matrices de Markov implementadas:
 La primera, cuando el valor es '1', es una matriz aleatoria y sus valores de saltos son aleatorios. 
 La segunda, cuando el valor es '2' es una matriz que no va a silencios, por lo tanto siempre suena. Tiene la misma probabilidad en todos los casos.
 La tercera, cuando el valor es cualquier otro número, todos los valores, incluidos los silencios, tienen la misma probabilidad de salir seleccionados.
 - Instrumento: un número entero que escoge el instrumento a ser tocado. Una lista de instrumentos se puede ver acá: http://www.midi.org/techspecs/gm1sound.php

