import sys
import json
import importlib
import matplotlib.pyplot as plt
from graphics import Plot2DSimulation

# Load simulation file
simulation_file = sys.argv[1].replace(".json","")
sim = importlib.import_module("simulations."+simulation_file+".simulation", package=None)

try:
    with open(simulation_file + ".json") as file:
        print("Loading graphical simulation with "+simulation_file + ".json")
        logs = json.load(file)
except IOError:
    print("Couldn't locate "+simulation_file + ".json")

print('Animating simulation...')
plotSim = Plot2DSimulation( sim.robots, sim.barrier_grid, sim.paths, sim.spline_barriers, logs, plot_config = sim.plot_config )
plotSim.main_ax.set_title("Traffic Control using CLF-CBFs", fontsize=12)


initial_time = 0
if len(sys.argv) > 2:
    initial_time = float(sys.argv[2])
plotSim.animate(initial_time)

plt.show()