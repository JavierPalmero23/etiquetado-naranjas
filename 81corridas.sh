#!/bin/bash

# Ejecuta el script de Etiquetado 81 veces
for i in {1..81}
do
    echo "Ejecución $i"
    python3 SelectorPunto.py
    sleep 1
done
