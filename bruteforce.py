import itertools
from time import sleep
import os
import multiprocessing as mp
from threading import Thread

count = CharLength = 1

pw = input("Password: ")

chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.!?:;,")

pw = tuple(pw)

for CharLength in range(1, 25):
        passwords = (itertools.product(chars, repeat = CharLength))

        first_match = filter(lambda elm: elm == pw, passwords)
        try:
            passwd = next(first_match)
            passwd =  "".join(passwd)
            print("Password found: " + passwd)
        except StopIteration:
            pass
           
