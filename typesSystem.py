
from yaplWalker import yaplWalker

error = 0
def checkInferenceRule(operator, a, aType, b, bType):
    if (aType, bType) == ("INT", "INT"):
        pass
    elif ((aType, bType) == ("INT", "STRING") or (aType, bType) == ("STRING", "INT")) and operator in ("+", "-", "/"):
        error += 1
    elif ((aType, bType) == ("STRING", "STRING")) and operator in ("-", "*", "/"):
        error += 1
    elif ((aType, bType) == ("INT", "TRUE") or (aType, bType) == ("INT", "FALSE") or (aType, bType) == ("STRING", "TRUE") or (aType, bType) == ("STRING", "FALSE")):
        error += 1
    elif ((aType, bType) == ("TRUE", "TRUE") or (aType, bType) == ("TRUE", "FALSE") or (aType, bType) == ("FALSE", "TRUE") or (aType, bType) == ("FALSE", "FALSE")):
        error += 1
