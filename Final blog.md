# Modelling of On-Chip Interconnects using Physical Facbrication Parameters
## Team Members

* Sahith S R
* Iteesha V A
* A Shrikant

## Guides
* Aditya Kulkarni

## Objectives

* Analyzing the Lower metal layers of the On-Chip interconnects using the proposed model.
* Calculating the efficiency and accuracy of the proposed model against the foundry parameters.
* Designing a GUI for displaying the results acquired from the model for any interconnect lengths.

## Methodology

The lower metal layer wires were modelled using the proposed pi-model RLC network. The RLC values of the pi-network was carefully 
chosen to match the actual characteristics of the wire under test. The lengths of the interconnects was chosen as the parameter of interest.
So the model's accuracy was analyzed wrt. different interconnect lenghts. The other parameters like other dimensions of the wire, nature of materials 
and media were taken to be fixed. The actual foundry parameters and equivalently, the actual circuit behaviour was obtained using a simualtion software
'Electric Binary', which has LT Spice IV on background, a primary tool for circuit simulation. 
The model was first put on simulation using a driver-load inverter pair(CMOS inverter pair) and the time delay(or phase delay equivalently) between the waveforms
resulted from using the proposed model and the actual foundry circuits 
