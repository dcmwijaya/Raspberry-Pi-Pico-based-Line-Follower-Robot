[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?style=flat)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=github&color=%23F7DF1E)](https://opensource.org/licenses/MIT)
![GitHub last commit](https://img.shields.io/github/last-commit/devancakra/Smart-Green-House-Berbasis-IoT-Mobile-Apps)
![Project](https://img.shields.io/badge/Project-Raspberry%20Pi%20Pico-light.svg?style=flat&logo=raspberrypi&logoColor=white&color=%23F7DF1E)

# Raspberry-Pi-Pico-based-Line-Follower-Robot
<strong>Solo Project Raspberry Pi Pico-Based Line Follower Robot</strong><br><br>
This project discusses how a robot can move along a line automatically. This robot has been equipped with an infrared sensor of the type ``` TCRT5000 ```. In the process, this sensor works on the principle of light reflection to determine its output value. If the light reflection on the dark or black colored object is judged to be less or non-existent, then the phototransistor will be in the ``` OFF ``` condition and the module will give an output of ``` HIGH ```, in which case the led indicator will not light up. If the light reflection on the light-colored or white surface is judged to be sufficient, the phototransistor will be in the ``` ON ``` state and the module will give an output of ``` LOW ```, in which case the led indicator will light up.
<br><br>

## Project Requirements
| Media | Description |
| --- | --- |
| Board Development | Raspberry Pi Pico |
| Code Editor | Thonny IDE |
| Bootloader | MicroPython UF2 |
| Programming Language | MicroPython |
| Packages | machine & utime |
| Actuators | Gear Motor / Motor DC (x2) |
| Sensor | KR08200: 3-Way Line Tracking IR Sensor, Brand: Funduino (x1) |
| Switch | KCD11: Rocker Switch SPST (x1) |
| Other Components | Micro usb cable (x1), Jumper cable, Li-ion battery 18650 (x2), 2-Slot series battery holder (x1), Robot wheels (x2), Caster wheel (x1), Motor driver L298N (x1), Car robot frame (x1), ETC |

<br><br>

## Download & Install
1. Thonny IDE

   ```
   https://thonny.org/
   ```
<br>

2. MicroPython UF2

   ```
   https://bit.ly/MicroPython_UF2
   ```
   
<br><br>

## Project Designs
<table>
<tr>
<th width="420">Block Diagram</th>
<th width="420">Pictorial Diagram</th>
</tr>
<tr>
<td><img src="https://github.com/devancakra/Raspberry-Pi-Pico-based-Line-Follower-Robot/assets/54527592/2d13dd05-7f81-45cb-9e72-9e8d3ff9a8ef" alt="Block-Diagram"></td>
<td><img src="https://github.com/devancakra/Raspberry-Pi-Pico-based-Line-Follower-Robot/assets/54527592/0ea2429f-f0d8-4db1-96f8-85622942111c" alt="Pictorial-Diagram"></td>
</tr>
</table>
<table>
<tr>
<th width="840">Wiring</th>
</tr>
<tr>
<td><img src="https://github.com/devancakra/Raspberry-Pi-Pico-based-Line-Follower-Robot/assets/54527592/9ce8539c-03ad-4e31-a5c7-bd44dabc9517" alt="Wiring"></td>
</tr>
</table>

<br><br>

## MicroPython Bootloader Setup
1. ``` Upload the firmware ``` :

   - Press and hold the ``` BOOTSEL ``` button on the Raspberry Pi Pico board while connecting to the computer via a micro USB cable.

   - After the Raspberry Pi Pico is recognized by the computer (connected), then immediately release the ``` BOOTSEL ``` button.
   
   - When successfully connected, a new drive called ``` RPI-RP2 ``` will open.
   
   - ``` Drag -> Drop ``` or ``` Copy -> Paste ``` the ``` MicroPython UF2 ``` firmware file into the ``` RPI-RP2 ``` drive.<br><br>

2. After the process is successful, the ``` RPI-RP2 ``` drive will automatically close.

<br><br>

## Thonny IDE Setup
1. Open ``` Thonny IDE ``` first.<br><br>

2. Click ``` Tools ``` -> then select ``` Options... ``` -> then select :<br><br>
   
   • ``` Interpreter Menu ```, then change the part:

      - ``` Interpreter ``` -> ``` MicroPython (Raspberry Pi Pico) ```
        
      - ``` Port ``` -> ``` Board CDC @ COM... ```
  
      - ``` Restart interpreter before running a script ``` -> ``` uncheck ```<br><br>
   
   • ``` Editor Menu ```, then check all the options except: ``` Indent with tab characters ```.<br><br>

3. If the file view does not exist in Thonny IDE, then please click the ``` View ``` -> section and select ``` Files ``` to display it.<br><br>

4. Then look for a file called ``` main.py ``` in the directory: ``` Raspberry-Pi-Pico-based-Line-Follower-Robot/Src ```.<br><br>
   
5. Right click on the file -> select ``` Upload to / ```.<br><br>

6. Open the file ``` main.py ``` which is in the ``` Raspberry Pi Pico ``` storage -> then click ``` Run current script (F5) ```.<br><br>

7. Program code executed successfully -> sign: ``` %run -c $EDITOR_CONTENT ```.

<br><br>

## Get Started
1. Download and extract this repository.<br><br>
   
2. Make sure you have the necessary electronic components.<br><br>
   
3. Make sure your components are designed according to the diagram.<br><br>
   
4. Configure your device according to the settings above.<br><br>

5. Please enjoy [Done].

<br><br>

## Highlights
<img src="https://github.com/devancakra/Raspberry-Pi-Pico-based-Line-Follower-Robot/assets/54527592/09f8d93b-ae48-4ad9-a3ef-3b69fd152945" alt="robot-line-follower">

<br><br>

## LICENSE
MIT License - Copyright (c) 2023 - Devan C. M. Wijaya, S.Kom

Permission is hereby granted without charge to any person obtaining a copy of this software and the software-related documentation files to deal in them without restriction, including without limitation the right to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons receiving the Software to be furnished therewith on the following terms:

The above copyright notice and this permission notice must accompany all copies or substantial portions of the Software.

IN ANY EVENT, THE AUTHOR OR COPYRIGHT HOLDER HEREIN RETAINS FULL OWNERSHIP RIGHTS. THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, THEREFORE IF ANY DAMAGE, LOSS, OR OTHERWISE ARISES FROM THE USE OR OTHER DEALINGS IN THE SOFTWARE, THE AUTHOR OR COPYRIGHT HOLDER SHALL NOT BE LIABLE, AS THE USE OF THE SOFTWARE IS NOT COMPELLED AT ALL, SO THE RISK IS YOUR OWN.
