# FPGA Wordle

This program runs Wordle on a DE1-SoC FPGA.<br><br>

![Start screen GIF](https://github.com/lj-watson/fpga-wordle/blob/main/images/startscreen.gif)

### Web Browser Simulation

1. Go to https://cpulator.01xz.net and select ARMv7 DE1-SoC. <br>
2. Change the language in the editor to C.<br>
3. File -> Open and choose "wordle_program.c". Press "Compile and Load" then "Continue". Wordle appears on the simulated VGA Pixel Buffer.<br>
4. To provide input, type in the "PS/2 keyboard or mouse" interface. Only the interface with IRQ 79 will work. (The DE1-SoC has two PS/2 inputs with different IRQ codes.)
