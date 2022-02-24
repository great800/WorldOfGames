# Project Part 3 - Lior A
import Utils
from Utils import SCORES_FILE_NAME
import Live


def add_score(difficulty, user):
    try:
        open(Utils.SCORES_FILE_NAME, "r")
    except:
        open(Utils.SCORES_FILE_NAME, "w")
    POINTS_OF_WINNING = int(difficulty*3+5)
    f = open(SCORES_FILE_NAME, "r")
    prev_content = f.read()
    if not(prev_content.isnumeric()):
        #print("***   The SCORES file content isn't numerical. Resetting it now before continuing the calculation!   ***")
        f = open(SCORES_FILE_NAME, "w")
        f.write("0")
        prev_content = 0
    f = open(SCORES_FILE_NAME, "r+")
    new_content = int(prev_content) + POINTS_OF_WINNING
    f = open(SCORES_FILE_NAME, "w")
    f.write(f'{str(new_content)}')
    f.close()
