# Robo Pico Kit with Raspberry Pi Pico W

## How to Set Up
Follow the setup tutorial: [YouTube Video](https://www.youtube.com/watch?v=oLVEFHwxbaw&t=20s&ab_channel=CytronTechnologies)

### Hardware Requirements
- **Robo Pico Kit** (with Raspberry Pi Pico W)
- **Ultrasonic Sensor**
- **Line Following Sensor** (Supports both black and white line detection)
- **Light Sensor**
- **Motors & Wheels**

### Software Requirements
- **Thonny IDE** (for coding and uploading scripts)

---

## Project Files and Descriptions

| File Name | Description |
|-----------|------------|
| `Pico_movement.py` | Controls basic movement of the Pico robot (e.g., forward, backward, left, right). |
| `Ultra_sonic.py` | Implements obstacle detection using an ultrasonic sensor along with motor movement. |
| `Line_following.py` | Enables the Pico robot to follow a line. The sensor can detect both **white** and **black** lines. |
| `Light_Sensor.py` | Uses a light sensor to detect light levels and adjust the robot's movement accordingly. |
| `Mix_ultra_sonic_N_light_sensor.py` | A combination of ultrasonic and light sensors to navigate obstacles and detect objects based on darkness. |

---

## Line Following Sensor
The line-following sensor can differentiate between:
- **White Line (Colour)**: The robot detects and follows a white path.
- **Black Line (Dark)**: The robot follows a black path.

![Line Following Sensor](https://github.com/user-attachments/assets/77bb76e6-410f-4205-97ae-5e1d50b5a7d7)

---

## Mixed Sensor Behavior (`mix_ultra_sonic_N_light_sensor.py`)
- The robot starts by moving **forward**.
- If an obstacle is detected **within 20 cm** using the **ultrasonic sensor**, the robot will **turn left**.
- If no obstacle is detected, the **light sensor** is used:
  - When an object is close, the area in front becomes **darker**.
  - The light sensor detects it and makes the robot **move backward and turn left**.

---

## How to Run the Code
1. Install **Thonny IDE**.
2. Connect your **Raspberry Pi Pico W** to your computer.
3. Upload the desired `.py` script to the Pico.
4. Run the script to see the robot's behavior.

---
**Result Video:** [YouTube Video](https://youtu.be/NvJSs73UOrY)  
**Custom Function:** [YouTube Video](https://youtu.be/soNdTLq_Bb0)

