# Exercise-2 Vadere
This repository contains scenario files for tasks and respective generated outputs. To run these scenarios and show outut files, please check following projects:
- Vadere project: https://github.com/crowdmodeling20ss/vadere
- SIR Visualization: https://github.com/crowdmodeling20ss/sir-visualization

## Output Files
"output" directory which is automatically generated when a vadere scenario is run is ignored by default. Since a lot of tests will be needed to find a correct scenario setting, there will be huge amount of output files. Most probably, we will push all output files which also contain wrong data when a task is completed. To prevent it, output directory is ignored.

**If you want to keep output file in remote, put then into /output-remote directory.**

## AddPedestrian.py
AddPedestrian.py can take 1 or 2 system arguments depending on the functionality. 
	-First argument is the ".scenario" file name and it is mandatory.
	-Second argument is optional and it depends on whether you would like to keep the existing pedestrians in the scenario or not. If you want to keep the pedestrians and just append the new ones in "add_pedestrian.json", this argument should be 1. If you want to override the pedestrians with the new ones in "add_pedestrian.json", this argument should be 0. Not giving any arguments also overrides the pedestrians.


	Example to override:
		python AddPedestrian.py rimeaa_6.scenario
		python AddPedestrian.py rimeaa_6.scenario 0

	Exaple to keep the existing pedestrians:
		python AddPedestrian.py rimeaa_6.scenario 1
		
