from catsim_poly.cat import generate_item_bank
from catsim_poly import plot
from catsim_poly.initialization import RandomInitializer
from catsim_poly.selection import MaxInfoSelector
from catsim_poly.estimation import NumericalSearchEstimator
from catsim_poly.stopping import MaxItemStopper
from catsim_poly.simulation import Simulator

s = Simulator(generate_item_bank(100), 10)
s.simulate(RandomInitializer(), MaxInfoSelector(), NumericalSearchEstimator(), MaxItemStopper(20))
plot.item_exposure(title='Exposures', simulator=s, hist=True)
plot.item_exposure(title='Exposures', simulator=s, par='b')