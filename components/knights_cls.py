import pygame
from components.pieces_cls import Pieces

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

class Knights(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self):
        possible_moves = [(self.x-2*tile_size, self.y+tile_size),
                            (self.x-2*tile_size, self.y-tile_size),
                            (self.x-tile_size, self.y+2*tile_size),
                            (self.x-tile_size, self.y-2*tile_size),
                            (self.x+tile_size, self.y+2*tile_size),
                            (self.x+tile_size, self.y-2*tile_size),
                            (self.x+2*tile_size, self.y+tile_size),
                            (self.x+2*tile_size, self.y-tile_size)
                            ]

        index_list = []

        lenght_array = len(possible_moves)

        for i in range(lenght_array):
            for piece in Pieces.all_pieces_list:
                bool1 = bool(possible_moves[i][0] == piece.x)
                bool2 = bool(possible_moves[i][1] == piece.y)
                bool3 = bool(self.farbe == piece.farbe)

                if bool1 and bool2 and bool3:
                    index_list.append(i)
                    break

        for del_index in index_list:
            possible_moves.pop(del_index)
            #nasty shit
            for i in range(len(index_list)):
                index_list[i] -= 1
        
        finite_moves = []

        if Pieces.white_is_checked or Pieces.black_is_checked:
            enemy_moves = Pieces.checking_piece.attacted_tiles()
            for possible_move in possible_moves:
                for enemy_move in enemy_moves:
                    if enemy_move == possible_move:
                        finite_moves.append(possible_move)

        else:
            finite_moves = possible_moves


        return finite_moves
    
    def attacted_tiles(self):
        possible_moves = [(self.x-2*tile_size, self.y+tile_size),
                            (self.x-2*tile_size, self.y-tile_size),
                            (self.x-tile_size, self.y+2*tile_size),
                            (self.x-tile_size, self.y-2*tile_size),
                            (self.x+tile_size, self.y+2*tile_size),
                            (self.x+tile_size, self.y-2*tile_size),
                            (self.x+2*tile_size, self.y+tile_size),
                            (self.x+2*tile_size, self.y-tile_size)
                            ]
        return possible_moves