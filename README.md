# ece243-fpga-wordle
This program runs Wordle on a DE1-SoC FPGA.<br><br>

To simulate on a web browser: <br><br>

Go to https://cpulator.01xz.net and select ARMv7 DE1-SoC to simulate the system. <br>
Change the language in the editor to C.<br>
Go to File -> Open and choose "wordle_program.c". Press "Compile and Load" then "Continue". The program will appear on the simulated VGA Pixel Buffer.<br>
To provide input, type in the "PS/2 keyboard or mouse" interface. Only the interface with IRQ 79 will work. (The DE1-SoC has two PS/2 inputs with different IRQ codes.)
