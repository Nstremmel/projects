from random import randint
from time import sleep
import os
import sys
import random
import click

click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
if c == 'b\'y\'':
    click.echo('We will go on')
elif c == 'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')

input()
