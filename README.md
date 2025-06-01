# Evolution Simulator
A simple neural network + genetic algorithm based evolution simulation

## Algorithm Description

### Generation Steps

At each new generation, $30$ blobs and $20$ food units are spawed at random positions.

Each blob needs to take as much food as possible.

At the end of the generation, $60$% of the population are replaced with a mutated form of the best performing blob.

### Blob

Each blob has a neural network (nn) as decision power. The nn is composed of $4$ input numbers, $2$ hidden layers of size $10$ and $2$ output neurons with the $X$ direction and the $Y$ direction.

As input for the nn, each blob gets his position as input $x, y$ and the position of the closest food unit's position $xf, yf$, so the input will be $[x, y, xf, yf]$

At each tick of the simulation each blob makes forward propagation through the nn so that it's position can be updated.

### Mutation

As mentions above, after each generation $60$% of the population are replaced with a mutated form of the best performing blob.

The mutation refers strictly to the brain (nn), so each weight is updated by a random value.

## How to run?

Install the libraries:
```
pip install -r req.txt
```
and then:

```
python3 main.py
```

Notes: 
* a venv is required
* the tested python version is $3.13.3$
