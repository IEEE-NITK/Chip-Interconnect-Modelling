# Modelling of On-Chip Interconnects using Physical Fabrication Parameters
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

<img src="https://github.com/IEEE-NITK/Chip-Interconnect-Modelling/blob/master/blog%20files/layer.PNG"
	title="Cascade" width="250" height="200" />
<img src="https://github.com/IEEE-NITK/Chip-Interconnect-Modelling/blob/master/blog%20files/3D_view-1.png"
	title="Cascade" width="250" height="200" align='right' />

So the model's accuracy was analyzed wrt. different interconnect lenghts. The other parameters like other dimensions of the wire, nature of materials 
and media were taken to be fixed. The actual foundry parameters and equivalently, the actual circuit behaviour was obtained using a simualtion software
'Electric Binary', which has 'LT Spice IV' on background, a primary tool for circuit simulation.

The transcient analysis on LT Spice was used as the main tool for the analysis. The model was first put on simulation using a driver-load inverter
pair(CMOS inverter pair) and the time delay(or phase delay equivalently) between the waveforms resulted from using the proposed model and the actual foundry
circuits. The model was put up between the inverters for the analysis. Various interconnect lenghts were used and the corresponding delays were plotted.

Similarly, the analysis was repeated on a 3 stage CMOS Ring Oscillator circuit and the results were analyzed.

## Results
In case of the driver-load inverter pair, various plots of td vs interconnect length were obtained on different T/H ratios(thickness to height) and found that model 
provided fairly accurate results for T/H close to 1.

In case of the 3 stage CMOS Ring OScillator, the model presented fairly accurate results. The output frequency produced by the circuit with the model was within
a range of 20% from the layout circuit(with foundry parameters).
