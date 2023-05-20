# fpga-wordle
This program runs a Wordle minigame on the DE1-SoC FPGA. It is written in C with some inline ARM Assembly. 

** SIMULATION INSTRUCTIONS **

To try it on a web browser, go to https://cpulator.01xz.net and select ARMv7 DE1-SoC to simulate the system.
First change the language in the editor to C.
Go to File -> Open and choose the .c file. The program will appear on the simulated VGA Pixel Buffer.
To provide user input, type in the "PS/2 keyboard or mouse" device interface. Only the interface with IRQ 79 will work.
(This is an arbitrary choice as the DE1-SoC has two PS/2 inputs with different IRQ codes.)
