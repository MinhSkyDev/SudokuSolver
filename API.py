import requests
import json

def createSudokuTable(difficulty):
    url = 'https://sugoku.herokuapp.com/board?difficulty=' + difficulty
    apiGet = requests.get(url)
    apiGet_json = apiGet.json()
    sudokuBoard = apiGet_json['board']
    return sudokuBoard
