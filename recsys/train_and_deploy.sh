#!/bin/bash

# addestramento senza spark (per pochi dati)
pio-docker train

# dopo il train, il modello ascolta sulla porta 8000
pio-docker deploy