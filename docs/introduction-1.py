from catsim_poly import plot
from catsim_poly.cat import generate_item_bank

item = generate_item_bank(1)[0]
plot.item_curve(item[0], item[1], item[2], item[3], ptype="both")
