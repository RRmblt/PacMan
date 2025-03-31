"""
Programme réalisé par Raimbault, Romain
"""
import pygame

#definition du niveau
niveau=[[ 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,10, 5, 5, 5,10, 5, 5, 5,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2],
        [ 6,12,12,12,12,12,12,12,12,12,12,12,38,12,12,12, 6,12,12,12,38,12,12,12,12,12,12,12,12,12,12,12, 6],
        [ 6,12, 1, 2,12, 1, 2,12, 1, 5, 2,12,12,12,39,12, 6,12,39,12,12,12, 1, 5, 2,12, 1, 2,12, 1, 2,12, 6],
        [ 6,12, 3, 4,12, 3, 4,12, 3, 5, 4,12,36, 5, 4,12,38,12, 3, 5,37,12, 3, 5, 4,12, 3, 4,12, 3, 4,12, 6],
        [ 6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12, 6],
        [ 3, 5, 5, 5, 2,12,36, 5,10, 5,37,12, 1, 5, 5,37,12,36, 5, 5, 2,12,36, 5,10, 5,37,12, 1, 5, 5, 5, 4],
        [ 0, 0, 0, 0, 6,12,12,12,38,12,12,12, 6,12,12,12,12,12,12,12, 6,12,12,12,38,12,12,12, 6, 0, 0, 0, 0],
        [ 1, 5, 5, 5, 4,12,39,12,12,12,39,12, 3, 5, 5,37,12,36, 5, 5, 4,12,39,12,12,12,39,12, 3, 5, 5, 5, 2],
        [ 6,12,12,12,12,12, 3,37,12,36, 9,12,12,12,12,12,12,12,12,12,12,12, 7,37,12,36, 4,12,12,12,12,12, 6],
        [ 3, 5, 5, 5, 2,12,12,12,12,12, 6,12,36, 5, 5, 2,12, 1, 5, 5,37,12, 6,12,12,12,12,12, 1, 5, 5, 5, 4],
        [ 0, 0, 0, 0, 6,12, 1, 5,37,12, 6,12,12,12,12, 6,12, 6,12,12,12,12, 6,12,36, 5, 2,12, 6, 0, 0, 0, 0],
        [ 1, 5, 5, 5, 4,12, 6,12,12,12,38,12,36, 5, 5, 4,12, 3, 5, 5,37,12,38,12,12,12, 6,12, 3, 5, 5, 5, 2],
        [ 6,12,12,12,12,12, 3, 5,37,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,36, 5, 4,12,12,12,12,12, 6],
        [ 6,12, 1, 5, 2,12,12,12,12,12, 1, 2,12, 1, 5, 5, 5, 5, 5, 2,12, 1, 2,12,12,12,12,12, 1, 5, 2,12, 6],
        [ 6,12, 3, 5, 4,12, 1, 5, 2,12, 3, 4,12,38,12,12, 0,12,12,38,12, 3, 4,12, 1, 5, 2,12, 3, 5, 4,12, 6],
        [ 6,12,12,12,12,12, 6, 0, 6,12,12,12,12,12,12, 1, 5, 2,12,12,12,12,12,12, 6, 0, 6,12,12,12,12,12, 6],
        [ 3, 5, 5, 5, 5, 5, 4, 0, 3, 5, 5, 5, 5, 5, 5, 4, 0, 3, 5, 5, 5, 5, 5, 5, 4, 0, 3, 5, 5, 5, 5, 5, 4]]

ParcoursFantomeRouge=  [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 61, 60, 59,  0,  0,  0,  0,  0, 47, 46, 45, 44, 43, 42, 41,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 62,  0, 58, 57, 56,  0,  0,  0, 48,  0,  0,  0,  0,  0, 40,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 63,  0,  0,  0, 55,  0,  0,  0, 49,  0,  0,  0,  0,  0, 39,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 65, 64,  0,  0,  0, 54, 53, 52, 51, 50,  0, 34, 35, 36, 37, 38,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 33,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0, 76, 77, 78,  0,  0,  0, 32,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 68,  0,  0,  0,  0, 75,  0, 79, 80,  0,  0, 31,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 69, 70, 71, 72, 73, 74,  0,  0, 81,  0,  0, 30,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 83, 82,  0,  0, 29,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  2,  3,  4,  0, 84,  0,  0,  0, 28,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0, 85, 86, 87,  0, 27,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  7,  8,  0,  0,  0, 26, 25, 24, 23, 22,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10, 11, 12, 13,  0,  0,  0, 21,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 14,  0,  0,  0, 20,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 16, 17, 18, 19,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

ParcoursFantomeBleu=   [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,  0, 12, 11, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 73,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 14, 13,  0,  9,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 72,  0,  0,  0,  0,  0,  0,  0,  0,  0, 16,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 71, 70, 69, 68, 67,  0,  0,  0,  0,  0, 17,  0,  0,  0,  7,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0, 18,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 65,  0,  0,  0,  0,  0, 19,  0,  1,  2,  3,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 64,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 63,  0,  0,  0,  0,  0, 21, 22, 23, 24, 25, 26,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 62,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 27,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 61,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 28,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 60,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 29,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 55, 56, 57, 58, 59,  0,  0,  0,  0,  0,  0, 34, 33, 32, 31, 30,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 54,  0,  0,  0, 46, 45, 44, 43, 42,  0,  0, 35,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 53,  0,  0,  0, 47,  0,  0,  0, 41,  0,  0, 36,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0, 52, 51, 50, 49, 48,  0,  0,  0, 40, 39, 38, 37,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

ParcoursFantomeRose=   [[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 68, 69, 70, 71, 72, 73, 74, 75,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0, 76,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 77,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  0,  0,  0,  0, 65,  0,  0,  0,  0,  0, 79, 78,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0, 18,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0, 64,  0,  0,  0,  0,  0, 80,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0, 19,  0,  0,  0, 29, 30, 31,  0,  0,  0,  0,  4,  3,  2,  1,  0, 63,  0,  0,  0, 83, 82, 81,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0, 20,  0,  0, 27, 28,  0, 32,  0,  0,  0,  0,  0,  0,  0,  0,  0, 62,  0,  0, 85, 84,  0,  0,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0, 21,  0,  0, 26,  0,  0, 33,  0,  0,  0,  0, 56, 57, 58, 59, 60, 61,  0,  0, 86,  0,  0,113,114,115,116,117,  0],
                        [  0,  0,  0,  0,  0, 22, 23, 24, 25,  0,  0, 34,  0,  0,  0,  0, 55,  0,  0,  0,  0,  0,  0, 88, 87,  0,  0,112,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 35,  0,  0,  0,  0, 54,  0,  0,  0,  0,  0,  0, 89,  0,  0,  0,111,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 36,  0,  0,  0,  0, 53,  0,  0,  0,  0,  0,  0, 90,  0,  0,  0,110,  0,  0,  0,  0,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0, 39, 38, 37, 48, 49, 50, 51, 52,  0,  0,  0,  0,  0,  0, 91,  0,  0,  0,109,108,107,106,105,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0, 40,  0,  0, 47,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 92, 93, 94, 95, 96,  0,  0,  0,104,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0, 41,  0,  0, 46,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 97,  0,  0,  0,103,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0, 42, 43, 44, 45,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 98, 99,100,101,102,  0],
                        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

ParcoursFantomeJaune=  [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0, 74, 73, 72, 71,  0,  0,  0,  0,  0, 59, 58, 57,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0, 75,  0,  0, 70,  0,  0,  0, 62, 61, 60,  0, 56,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0, 76,  0,  0, 69,  0,  0,  0, 63,  0,  0,  0, 55,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0, 77, 78,  0, 68, 67, 66, 65, 64,  0,  0,  0, 54, 53,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 79,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 52,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0, 80, 81, 82,  0,  0,  0,  0,  0,  0,  0,  0, 51,  0,  0,  0,  0, 42, 41, 40,  0, 36, 35, 34,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0, 83, 84,  0,  0,  0,  0,  0,  0,  0, 50,  0,  0,  0,  0, 43,  0, 39, 38, 37,  0, 33,  0,  0,  0,  0,  0],
                        [ 0,116,115,114,113,112,  0,  0, 85,  0,  0,  0,  0,  0,  0,  0, 49, 48, 47, 46, 45, 44,  0,  0,  0,  0,  0, 32,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,111,  0,  0, 86, 87,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 27, 28, 29, 30, 31,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,110,  0,  0,  0, 88,  0,  4,  3,  2,  1,  0,  0,  0,  0,  0,  0,  0,  0, 26,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,109,  0,  0,  0, 89,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,104,105,106,107,108,  0,  0,  0, 90,  0,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,  0,  0, 24,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,103,  0,  0,  0, 95, 94, 93, 92, 91,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 16,  0,  0, 23,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,102,  0,  0,  0, 96,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 17,  0,  0, 22,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,101,100, 99, 98, 97,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 18, 19, 20, 21,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

#variables du niveau
NB_TILES = 42       #nombre de tiles à charger
TILE_SIZE=32       #definition du dessin (carré)
largeur=33          #hauteur du niveau
hauteur=17          #largeur du niveau
tiles=[]            #liste d'images tiles
numeroTile=0        #numéro du tile sur lequel le pacman est - défini pour éviter le plantage lorsque l'on quitte sans avoir bouger 1 fois


#variables de gestion du pacman
pacX=16                     #position x y du pacman dans le niveau
pacY=14
compteurBilles=0
directionPacman=18          #direction du pacman selon la valeur 14=droite 15=gauche 16=haut 17=bas 18=neutre
viesPacman=3                #nombre de vies du pacman
pixelPacmanX=pacX*TILE_SIZE #compteur de pixels pour la fluidite du pacman
pixelPacmanY=pacY*TILE_SIZE
stopPacman=False            #valeur booléenne qui sert à définir si le pacman est en court de déplacement ou non
pixelRatePacman=2           #définit le nombre de pixels qu'il parcourt entre chaque itération de la boucle pour son animation (forcément un diviseur de 32 : 1,2,4,8,16,32), plus la valeur est grande moins l'animation sera fluide

"""
DEFINITIONS VARIABLES FANTOMES DES LISTES :

FRAMERATE_FANTOME           -> vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME      -> le nombre de cases sur lesquelles le fantome se deplace
positionFantome             -> position du fantome dans la liste ParcoursFantome
frameRateCounterFantome     -> compteur servant à ralentir le fantome en la comparant avec FRAMERATE_FANTOME
posfX                       -> position en X du fantome
posfY                       -> position en Y du fantome
directionFantome            -> direction où le fantome regarde
sensFantome                 -> défini si le fantome va en avant ou en arrière dans son parcours, par défaut à 1 pour aller en avant
pixelFantomeX               -> coordonnées X du fantome en pixels
pixelFantomeY               -> coordonnées Y du fantome en pixels
stopFantome                 -> valeur booléenne, elle sert à indiquer comme pour le pacman si le fantome est en cours de déplacement ou non (fluidité)
directionDynamiqueF         -> sert à configurer la direction des fantomes, doit être enregistrée dans la liste car lorsque le stopFantome est en true, elle n'est pas redéfinie dans la fonction
posfDiffX                   -> futur position X du fantome (positionFantome +1 ou -1 selon le sensFantome), les posfDiff doivent aussi être enregistrées dans la liste quand le stopFantome = True
posfDiffY                   -> futur position X du fantome (positionFantome +1 ou -1 selon le sensFantome)
"""


#Variables et listes de gestion des fantomes
FRAMERATE_FANTOME=32   #définit la vitesse à laquelle le fantome va de case en case ( /!\ : prendre en compte le pixelRateFantome qui prend 1 à 32 itérations selon sa valeur, si on défini un framerate inférieur au nombre d'itérations minimum au déplacement des fantomes, ils ne bougeront pas)
pixelRateFantome=2     #définit le nombre de pixels qu'il parcourt entre chaque itération de la boucle pour son animation (forcément un diviseur de 32 : 1,2,4,8,16,32), plus la valeur est grande moins l'animation sera fluide

###ParcoursFantome,NB_DEPLACEMENT_FANTOME,positionFantome,frameRateCounterFantome,posfX,posfY,directionFantome,sensFantome,pixelFantomeX,pixelFantomeY,stopFantome,directionDynamiqueF,posfDiffX,posfDiffY
#             [                    0,  1,2,3, 4, 5, 6,7,           8,           9,   10,11,12,13]
fantomeRouge= [ ParcoursFantomeRouge, 87,1,0,18,10,19,1,18*TILE_SIZE,10*TILE_SIZE,False, 0, 0, 0]
fantomeBleu=  [  ParcoursFantomeBleu, 84,1,0,13, 6,23,1,13*TILE_SIZE, 6*TILE_SIZE,False, 0, 0, 0]
fantomeRose=  [  ParcoursFantomeRose,117,1,0,19, 6,28,1,19*TILE_SIZE, 6*TILE_SIZE,False, 0, 0, 0]
fantomeJaune= [ ParcoursFantomeJaune,116,1,0,14,10,32,1,14*TILE_SIZE,10*TILE_SIZE,False, 0, 0, 0]



#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TILE_SIZE, (hauteur+1)*TILE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)
pygame_icon = pygame.image.load('data/14.png')
pygame.display.set_icon(pygame_icon)


#Chargement des tiles
def chargetiles(tiles):
    for n in range(0,NB_TILES):
        print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png'))


#Affichage niveau grâce à la liste niveau[][]
def afficheNiveau(niveau):
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TILE_SIZE,y*TILE_SIZE))


#Affichage Pacman
def affichePac(numero,pixelX,pixelY):
    fenetre.blit(tiles[numero],(pixelX,pixelY))


#Retourne une valeur booléenne si le pacman est sur la même case qu'un des 4 fantomes
def contactPacmanFantome():
    if (pacX,pacY)==(fantomeRouge[4],fantomeRouge[5]):
        return True
    elif (pacX,pacY)==(fantomeBleu[4],fantomeBleu[5]):
        return True
    elif (pacX,pacY)==(fantomeRose[4],fantomeRose[5]):
        return True
    elif (pacX,pacY)==(fantomeJaune[4],fantomeJaune[5]) :
        return True


def SupprBilles():                                      #fonction permettant de supprimer toutes les billes sauf 1 pour tester le programme
    global compteurBilles
    for y in range(hauteur):
        for x in range(largeur):
            if niveau[y][x]==12:
                if compteurBilles!=223:
                    compteurBilles+=1
                    niveau[y][x]=0
                else:
                    compteurBilles+=1
    compteurBilles-=1


def frameRateCounterFantomeReset():
    fantomeRouge[3]=0
    fantomeBleu[3]=0
    fantomeRose[3]=0
    fantomeJaune[3]=0


#Affichage score
def afficheScoreVie(score,vies):
    scoreAafficher = font.render("Score : " + str(score), True, (255, 255, 255))
    viesAafficher = font.render("Vies : " + str(vies), True, (255, 255, 255))
    fenetre.blit(scoreAafficher,(32,544))
    fenetre.blit(viesAafficher,(960,544))


#Recherche la position du fantome en fonction du numéro de sa position dans le parcours
def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    #print("POSITION",position)         #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coordFantome=x,y
    return coordFantome                  #les coord du fantome x et y sont dans un tuple coordFantome


#Assossie la bonne direction du fantome à la bonne couleur
def couleurDirectionFantome(parcoursF,directionF):
    global ParcoursFantomeRouge
    global ParcoursFantomeBleu
    global ParcoursFantomeRose
    global ParcoursFantomeJaune

    if parcoursF==ParcoursFantomeRouge:             #il s'agit du fantome rouge
        if directionF==1:                           #haut
            direction=21
        elif directionF==2:                         #bas
            direction=22
        elif directionF==3:                         #droite
            direction=19
        elif directionF==4:                         #gauche
            direction=20

    if parcoursF==ParcoursFantomeBleu:              #il s'agit du fantome bleu
        if directionF==1:                           #haut
            direction=25
        elif directionF==2:                         #bas
            direction=26
        elif directionF==3:                         #droite
            direction=23
        elif directionF==4:                         #gauche
            direction=24

    if parcoursF==ParcoursFantomeRose:              #il s'agit du fantome rose
        if directionF==1:                           #haut
            direction=29
        elif directionF==2:                         #bas
            direction=30
        elif directionF==3:                         #droite
            direction=27
        elif directionF==4:                         #gauche
            direction=28

    if parcoursF==ParcoursFantomeJaune:             #il s'agit du fantome jaune
        if directionF==1:                           #haut
            direction=33
        elif directionF==2:                         #bas
            direction=34
        elif directionF==3:                         #droite
            direction=31
        elif directionF==4:                         #gauche
            direction=32

    return direction


#Incrémente ou décrémente la positionFantome en fonction du sens dans lequel il va
def gestionPositionFantome(sensF,posF):
    if sensF==1:
        posF += 1
    elif sensF==0:
        posF -= 1
    return posF


#Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
def deplaceFantome(fantome):
    ParcoursFantome,NB_DEPLACEMENT_FANTOME,positionFantome,frameRateCounterFantome,posfX,posfY,directionFantome,sensFantome,pixelFantomeX,pixelFantomeY,stopFantome,directionDynamiqueF,posfDiffX,posfDiffY=fantome
    global FRAMERATE_FANTOME
    global pixelRateFantome
    global TILE_SIZE

    if frameRateCounterFantome==FRAMERATE_FANTOME and stopFantome==False:                   #ralenti la vitesse du fantome + vérifie qu'il n'est pas déjà en déplacement
        if positionFantome==NB_DEPLACEMENT_FANTOME:                                         #un tour est fait donc le fantome refait son parcours en sens inverse
            sensFantome=0
        elif positionFantome==1:                                                            #lorsque le fantome démarre à la première tile de son parcours ou y retourne, il repart dans le sens du parcours
            sensFantome=1

        if sensFantome==1:
            posfDiffX,posfDiffY=rechercheFantome(ParcoursFantome,positionFantome+1)         #déballage du tuple des futurs coordonnées du fantome
        elif sensFantome==0:
            posfDiffX,posfDiffY=rechercheFantome(ParcoursFantome,positionFantome-1)
        DeplacementX=posfDiffX-posfX                                                        #différence entre le point de départ et le point d'arrivée, pour définir si le fantome va à gauche ou à droite
        DeplacementY=posfDiffY-posfY                                                        #différence entre le point de départ et le point d'arrivée, pour définir si le fantome va en haut ou en bas


        if DeplacementY==-1:                                                                #déplacement en haut
            directionDynamiqueF=1                                                           #on définie une direction qui peut être appliquée à tous les fantomes, utilisée pour l'animation qui suit
            directionFantome=couleurDirectionFantome(ParcoursFantome,directionDynamiqueF)   #on définie la vraie direction du fantome, en prenant en compte la couleur et la futur direction
            stopFantome=True                                                                #on rend impossible le lancement d'un autre déplacement pour que celui en cours se termine


        elif DeplacementY==1:                                                               #déplacement en bas
            directionDynamiqueF=2
            directionFantome=couleurDirectionFantome(ParcoursFantome,directionDynamiqueF)
            stopFantome=True


        elif DeplacementX==1:                                                               #déplacement à droite
            directionDynamiqueF=3
            directionFantome=couleurDirectionFantome(ParcoursFantome,directionDynamiqueF)
            stopFantome=True


        elif DeplacementX==-1:                                                              #déplacement à gauche
            directionDynamiqueF=4
            directionFantome=couleurDirectionFantome(ParcoursFantome,directionDynamiqueF)
            stopFantome=True


        frameRateCounterFantome=0                                                           #compteur de vitesse à zero

    frameRateCounterFantome += 1                                                            #incrémentation du compteur de vitesse


    if (stopFantome==True):                             #déplacement pacman en cours, impossible que l'utilisateur en lance un autre avant que celui là soit terminé

        if directionDynamiqueF==1:                      #haut
            pixelFantomeY-=pixelRateFantome             #on incrémente ou décrémente selon la direction le nombre de pixel
            if pixelFantomeY==posfDiffY*TILE_SIZE:      #est-ce que le fantome est arrivé à la case voulue ?
                stopFantome=False                       #on met fin au déplacement en cours, le fantome peut recommencer à avancer/reculer d'une case
                if sensFantome==1:                      #on met à jour la réelle position du fantome en fonction de son sens après l'animation
                    positionFantome += 1
                else:
                    positionFantome -= 1

        elif directionDynamiqueF==2:                    #bas
            pixelFantomeY+=pixelRateFantome
            if pixelFantomeY==posfDiffY*TILE_SIZE:
                stopFantome=False
                if sensFantome==1:
                    positionFantome += 1
                else:
                    positionFantome -= 1

        elif directionDynamiqueF==3:                    #droite
            pixelFantomeX+=pixelRateFantome
            if pixelFantomeX==posfDiffX*TILE_SIZE:
                stopFantome=False
                if sensFantome==1:
                    positionFantome += 1
                else:
                    positionFantome -= 1

        elif directionDynamiqueF==4:                    #gauche
            pixelFantomeX-=pixelRateFantome
            if pixelFantomeX==posfDiffX*TILE_SIZE:
                stopFantome=False
                if sensFantome==1:
                    positionFantome += 1
                else:
                    positionFantome -= 1

    posfX,posfY=rechercheFantome(ParcoursFantome,positionFantome)                               #deballage du tuple coordonnées du fantome après incrémentation ou décrémentation de la positionFantome

    #mise à jour des valeurs dans la liste fantome:
    fantome[2], fantome[3], fantome[4], fantome[5], fantome[6], fantome[7], fantome[8], fantome[9], fantome[10], fantome[11], fantome[12], fantome[13] = positionFantome, frameRateCounterFantome, posfX, posfY, directionFantome, sensFantome, pixelFantomeX, pixelFantomeY, stopFantome, directionDynamiqueF, posfDiffX, posfDiffY
    fenetre.blit(tiles[directionFantome],(pixelFantomeX,pixelFantomeY))                         #affichage du fantome après animation


#Déplace les 4 fantômes en une seule ligne de code (voir boucle while), permet de tous les désactiver si besoin
def deplace4Fantomes():
    deplaceFantome(fantomeRouge)        #déplace le fantome rouge
    deplaceFantome(fantomeBleu)         #déplace le fantome bleu
    deplaceFantome(fantomeRose)         #déplace le fantome rose
    deplaceFantome(fantomeJaune)        #déplace le fantome jaune


chargetiles(tiles)  #chargement des images


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False                                            #fermeture de la fenetre (croix rouge)


        elif (event.type == pygame.KEYDOWN) and stopPacman==False : #une touche a été pressée...laquelle ? + pacman est-t-il en cours de déplacement ?

            if event.key == pygame.K_UP:                            #est-ce la touche UP
                posY = pacY - 1                                     #on deplace le pacman virtuellement
                posX = pacX
                numeroTile = niveau[posY][posX]                     #on regarde le numéro du tile
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0):           #si le tile est une bille ou un fond noir alors le déplacement est possible
                    directionPacman=16                              #la direction du pacman est donc définie
                    stopPacman=True                                 #on passe la variable stopPacman en true pour rendre les déplacements impossibles
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")


            elif event.key == pygame.K_DOWN:                        #est-ce la touche DOWN
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                print("down",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0):
                    directionPacman=17
                    stopPacman=True
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")


            elif event.key == pygame.K_RIGHT:                       #est-ce la touche RIGHT
                posY = pacY
                posX = pacX + 1
                numeroTile = niveau[posY][posX]
                print("right",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0):
                    directionPacman=14
                    stopPacman=True
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")


            elif event.key == pygame.K_LEFT:                        #est-ce la touche LEFT
                posY = pacY
                posX = pacX - 1
                numeroTile = niveau[posY][posX]
                print("left",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0):
                    directionPacman=15
                    stopPacman=True
                    print("deplacement possible",pacX,pacY)
                else:
                    print("deplacement impossible")

            elif event.unicode == 'x':
                SupprBilles()

            elif event.key == pygame.K_ESCAPE or event.unicode == 'q':  #touche q pour quitter
                loop = False

            if (numeroTile==12):                                        #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1                                       #alors on incrémente le score
                niveau[posY][posX]=0                                    #et on efface la bille dans le niveau
                print("nouvelle bille")

            else:
                print("fond noir")

    if stopPacman==True:                                                #déplacement pacman en cours, impossible que l'utilisateur en lance un autre avant que celui en cours soit terminé

        if directionPacman==16:                                         #haut
            pixelPacmanY-=pixelRatePacman                               #on incrémente ou décrémente selon la direction le nombre de pixel
            if pixelPacmanY==posY*TILE_SIZE:                            #est-ce que le pacman est arrivé à la case voulue lors de l'appuie de la touche ?
                stopPacman=False                                        #on met fin au déplacement en cours, l'utilisateur peut relancer un déplacement ailleurs
                pacY-=1                                                 #on met à jour la réelle position du pacman après l'animation

        if directionPacman==17:                                         #bas
            pixelPacmanY+=pixelRatePacman
            if pixelPacmanY==posY*TILE_SIZE:
                stopPacman=False
                pacY+=1

        if directionPacman==14:                                         #droite
            pixelPacmanX+=pixelRatePacman
            if pixelPacmanX==posX*TILE_SIZE:
                stopPacman=False
                pacX+=1

        if directionPacman==15:                                         #gauche
            pixelPacmanX-=pixelRatePacman
            if pixelPacmanX==posX*TILE_SIZE:
                stopPacman=False
                pacX-=1



    if contactPacmanFantome()==True:                                #pacman a-t-il les mêmes coordonnées qu'un des fantomes ?
        directionPacman=18                                          #on lui donne une direction neutre
        viesPacman-=1                                               #on lui retire une vie
        if (viesPacman!=0):
            pacX,pacY=16,14                                         #on remet le pacman à ses coordonnées initiales
            pixelPacmanX,pixelPacmanY=pacX*TILE_SIZE,pacY*TILE_SIZE #on actualise également les valeurs pixelPacmanX et pixelPacmanY
        else:
            loop=False
            print("Vous avez perdu")


    elif compteurBilles==251:
        loop=False
        print("Vous avez gagné")

    fenetre.fill((0,0,0))                                   #efface la fenetre
    afficheNiveau(niveau)                                   #affiche le niveau
    affichePac(directionPacman,pixelPacmanX,pixelPacmanY)   #affiche la pacman
    afficheScoreVie(compteurBilles,viesPacman)              #affiche le score
    deplace4Fantomes()                                      #déplace les 4 fantômes
    pygame.display.update()                                 #met à jour la fenêtre graphique
pygame.quit()
