from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require('sim')

sim.setStepping(True)
duration = 1

sim.startSimulation()
while (t := sim.getSimulationTime()) < duration:
    print(f'Simulation time: {t:.2f} [s]')
    sim.step()
sim.stopSimulation()
