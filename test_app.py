import os
import ast
from other.program import get_elements 
from other.fetch_data import glass_types_data

def test_file_creation():

    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Al.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Mg.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Si.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_K.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Ca.png")
    assert os.path.isfile("/workspaces/final_project/plots/Na_v_Ba.png")
    
def test_terminal_print(capsys):

    get_elements()
    captured = capsys.readouterr()
    assert captured.out == "Please type what elements (Ex. Al, Mg, Si, etc.) you have the concentrations of from your glass sample.\n"

def test_data_input():
    assert glass_types_data() is not None

def test_element_comps():
    user_Al_comp = "4.5"
    assert type(ast.literal_eval(user_Al_comp)) is float

    user_Na_comp = "2.888"
    assert type(ast.literal_eval(user_Na_comp)) is float

    user_Mg_comp = "-2.34"
    assert type(ast.literal_eval(user_Mg_comp)) is float

    user_Si_comp = "67.2"
    assert type(ast.literal_eval(user_Si_comp)) is float

    user_K_comp = "5.8"
    assert type(ast.literal_eval(user_K_comp)) is float

    user_Ca_comp = "7"
    assert type(ast.literal_eval(user_Al_comp)) is int

    user_Ba_comp = "10"
    assert type(ast.literal_eval(user_Al_comp)) is int

    user_Fe_comp = "89"
    assert type(ast.literal_eval(user_Al_comp)) is int

test_glass_ident():
    user_Al_comp = 8.9
    user_K_comp = 10
    assert glass_identity(user_Al_comp, user_K_comp) == "tableware"

    user_Mg_comp = 23.5
    user_Si_comp = 1.5
    assert glass_identity(user_Mg_comp, user_Si_comp) == "vehicle_windows_float_processed"

    user_Fe_comp = 12.1
    user_Ca_comp = 0.54
    assert glass_identity(user_Mg_comp, user_Si_comp) == "building_windows_float_processed"

    user_Ba_comp = 27
    user_Ai_comp = 11
    assert glass_identity(user_Mg_comp, user_Si_comp) == "containers"