from catsim_poly.cat import generate_item_bank
from catsim_poly import plot
items = generate_item_bank(100)
plot.gen3d_dataset_scatter(items)