import pytest
#importing glass_types_data() function
from other.fetch_data import glass_types_data
#importing make_plot() function
from other.making_plots import make_plot

from other.program import get_elements


#running fetch_data
glass_types_data()

#running function to make different plots
make_plot('Na', 'Si')
make_plot('Na', 'Mg')
make_plot('Na', 'Al')

get_elements()