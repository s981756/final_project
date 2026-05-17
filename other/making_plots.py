import os
from other.fetch_data import glass_types_data
import matplotlib.pyplot as plt
import seaborn as sns

# 'sepal length' is a possible factor
def make_plot(element_1, element_2):
    
    element_1_label = element_1.replace('_', ' ')
    element_2_label = element_2.replace('_', ' ')
    
    df, target_name = glass_types_data()

    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x=element_1,
        y=element_2,
        hue=target_name,
        style=target_name,
        s=90
    )

    plt.title(f'Glass Identification: {element_1_label} vs {element_2_label}')
    plt.xlabel(f'{element_1_label} (cm)')
    plt.ylabel(f'{element_2_label} (cm)')
    plt.legend(title='Glass Type')
    plt.grid(True)
    plt.savefig(f'/workspaces/final_project/plots/{element_1_label}_v_{element_2_label}.png', dpi=150)
    plt.close()