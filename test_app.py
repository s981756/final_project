import os
from other.program import get_elements 

def test_file_creation():

    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Al.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Mg.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Si.png")
    
def test_terminal_print(capsys):

    get_elements()
    captured = capsys.readouterr()
    assert captured.out == "Please type what elements (Ex. Al, Mg, Si, etc.) you have the concentrations of from your glass sample.\n"
