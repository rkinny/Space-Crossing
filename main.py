import pygame, sys
level_map = [
'                                                ',
'                                                ',
'                                                ',
' XX                                             ',
' XX P                                           ',
' XXXX                                           ',
' XXXX       XX                                  ',
' XX    X  XXXX    XX  XX        XXXXX           ',
'       X  XXXX    XX  XXX                       ',
'    XXXX  XXXXXX  XX  XXXX  XXXX     XXXXXX     ',
'XXXXXXXX  XXXXXX  XX  XXXX  XXXXXX              ']

tile_size = 48 #64
screen_width = 1500
screen_height = len(level_map) * tile_size