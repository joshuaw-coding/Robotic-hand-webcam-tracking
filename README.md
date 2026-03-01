# Robotic-Hand-Webcam-Tracking
This is a documentation of my first engineering project. This repository contains the Arduino code, Python code, 3d models, and all the physical parts I used that aren't 3d printed.
## Table of Contents
- [Demonsration](#demonstration)
- [Assembly](#assembly)
- [Wiring](#wiring)
- [Installation](#installation)
- [Coding](#coding)
- [Parts To Buy](#parts-to-buy)
- [Credits](#credits)

## Demonstration
[![Watch the video](https://img.youtube.com/vi/7y8TXPDOa_8/hqdefault.jpg)](https://www.youtube.com/watch?v=7y8TXPDOa_8)

## Assembly

[![Watch the video](https://img.youtube.com/vi/L2ddw3MQl9g/hqdefault.jpg)](https://www.youtube.com/watch?v=L2ddw3MQl9g)

## Wiring

[![Watch the video](https://img.youtube.com/vi/GDnmAI_7lOk/hqdefault.jpg)](https://www.youtube.com/watch?v=GDnmAI_7lOk)

## Installation
Download the STL files(Fingers, Thumb, Hand, Servo Cage, Servo Horn, Upper Forearm, and Wrist) on [Thingiverse](https://www.thingiverse.com/thing:2269115/files) by [Grossrc](https://www.thingiverse.com/grossrc/designs)                                                                                              
Download the STL files(Lower Forearm and Upper Forearm Cover) on [Thingiverse](

## Coding

#### Step 1: Download Arduino IDE and Python 3.6+ (make sure to enable PATH and pip in install settings).                                              
#### Step 2: Launch cmd and download the dependencies. Do this by running: pip install mediapipe opencv-python pyserial                             
#### Step 3: Create a project folder in file explorer.                                                                                              
#### Step 4: Download hand_landmarker.task and put it into your project folder.                                                                        
#### Step 5: Download the python code (hand_tracking_servo_control.py) and put it into your project folder.                                            
#### Step 6: Open Arduino IDE and download the adafruit pca library.                                                                                                                                                        
#### Step 7: Upload Arduino code via data cable(make sure data cable is plugged into com3 and you selected board and port in Arduino IDE)          
#### Step 8: Launch python and enter the correct cd by running: cd C:\projectfilename (ex:cd C:\handtrackingrobot)                                     
#### Step 9: Run the python(make sure the data cable is plugged into com3) by using: py hand_tracking_servo_control.py

## Parts To Buy
[-Arduino Uno](https://www.amazon.com/Gomass-R3-Board-Arduino-Compatible-Arduino/dp/B0F1DBB61D/ref=sr_1_10?crid=14RL04S0PDSM3&dib=eyJ2IjoiMSJ9.MazmhFfn-DF8W5oyX_S-tDFAqLRDaMJSkroaZhdQMdjrBJn--6GmjWoUnZKfH5OaBGaeyZhzdZU8lFsqqd8UDj7BqEP2_A51LD6bueNk1Da8T3Qr4cocpJ0WPIawGld1JrO0Z3V4-d98zkTuCC7_rtJC8reBSM9LomYAlnxkQWgmFWwY5Nf5QuOQ7aDJLm5cAMjniclmBDMzt-B3Pkclv6Fz5YtTsnhNHdHRbFn0HDs.gHXaAZERh-HBN-eMlEufs5tZmiST5YWHRaf4SJ2fcB0&dib_tag=se&keywords=arduino+uno&qid=1772301224&sprefix=ardui%2Caps%2C1771&sr=8-10)                                  
[-PCA9685 PWM](https://www.amazon.com/Zodazoqa-PCA9685-Channel-12-bit-Driver/dp/B0FBFZNT9H/ref=sr_1_11?crid=3LQDBDDCGSRUL&dib=eyJ2IjoiMSJ9.os3aVLN8-3BtpzxM7kRBbhEv3dvlkv54Qij-mX5Mq8f1nlMgDCSg6WD1xLgjfv3d55FbuojiarW2GTEiUG8XVpPRBscqfM-VGg0cMejMqtCLKX8G27xzNdZ-POhOxBJaMUv49K94IJp_XtNTsptckOXVvt05DSiSuEHxfok9T7rDoStcUGzb3-OiGTEGYNqD50bAL-K6mhFpwaz03olAjhjcrQHGlH64dOpGtbif2h0.8zdT65MSRW3P1YdIt-PXOW5ixKQR-h4jByr6ixh8FWM&dib_tag=se&keywords=pwm+motor+driver+16+channel+pca9865&qid=1772301365&sprefix=pwm+motor+driver+16+channel+pca9865%2Caps%2C672&sr=8-11)                                                                                                                                              
[-Mini Servo Motor](https://www.amazon.com/Miuzei-Geared-Helicopter-Arduino-Project/dp/B0BWJ4RKGV/ref=sr_1_9?dib=eyJ2IjoiMSJ9.MVOp3uTW8X144WJ_CqYOeUurdvj8MGFHhgFJWhnJQ_NpqkygXTNFPXTl_2YqVhNutQWcjXKN87c57BnoQXWKeghmJqS9rpNCCnWTgxEV1RZHh-VTU8OYdNCaYwyb_plk_GbLW9R-vO4W3aopovecC4fDblk-9DjQOcWcIpi3Er0oR7jT7GdA_5-_1oWUutzm40YKkB0aZ4awY2su39kjONjEgH9fCNZ0rWYZwRvR0Xj5HZZX07NPdJXAPvl1NO-WTgBUYM13_R7_pkf6lifJYjkAs2chwLgGHoaiO4OaNSA.sV2VueS72q_XRIXoCO4XfaQdh57ue5I47myyNzFUTmY&dib_tag=se&keywords=mini%2Bservo%2Bmotor&qid=1772320780&sr=8-9&th=1)                                                                                                                                       
[-Servo Motors](https://www.amazon.com/Deegoo-FPV-Servo-MG995-Metal-Gear/dp/B07NQJ1VZ2/ref=sr_1_5?crid=295T57F6TSC0X&dib=eyJ2IjoiMSJ9.GZTh7uRHzBI7vNpZM5S4-5iPMo3gbJVoqt_jmRsloYnbIi0_iyu1BjvVbI0FQ07QUkf_Zy42xoFx8yaJkcuYDf4CzeAZfNjsvP-ld09BY1xDL00-qhCw7Af1uXwSnAGtaKV_QBCO81B4aTGExa_jSrCIfxSNSn5kd8MRxFdTTyP-Bbh4v4kWrCefOowJruAFZK2_NhbiZ9OXCKOffa092D9nx6cIvLf2gxiDBzIijNso-SiOwCwxL_1vFg-K5VQgj9ZUFsjWZcyRCC7ZuxO11qYzRmCHFfLRP1gTfMwtvsw.78HDUJ4CED-0SAztdj4LEbGjY90lMQ8iiA-wmCBPpAE&dib_tag=se&keywords=servo%2Bmotors%2B4%2Bpack&qid=1772315570&sprefix=servo%2Bmotors%2B4%2Bpack%2Caps%2C177&sr=8-5&th=1)                  
[-Generic Fishing Line(Select Size: 327yrd 15lb)](https://www.amazon.com/RIKIMARU-Abrasion-Resistant-Superline-Diameter/dp/B07Q4NC9RV/ref=sr_1_8?crid=16DDJJWU5O9WB&dib=eyJ2IjoiMSJ9.dqWLZi6FFjGUlZKQyOCwPVBNm4bCKu94D8gUi6lnQsl_hhm4c_4ObQzXFX8ERL2qPMRsA1i6oz0Mx_LpyEdqx2PycPn678wrxpbb967U00-nkTtHTGUAolRCl423Cqtl1SLrnwnAIZQ-SnpFjILFc_4BF8TfpjeOA5FQkZVKzZCshq0PiBaCdsjUYwbuj0aVycXDvE0ZaL9MrrSiNqv3cNmRdbKJ7VzOUxgsvmMS6v1brVgbnbNVIsbC5ICgH3orUX5RSJOuigG2GJZH4oQ9aFCcyZqimXL-nUQV6PyrFCk.kdHYMlZdVyszRMnYjCwgOJayg-m-uFYH2JUssDYvlAc&dib_tag=se&keywords=rikimaru%2B300m%2B.12mm%2B15lb%2Bfishing%2Bline&qid=1772301722&sprefix=rikimaru%2B300m%2B.12mm%2B15lb%2Bfishing%2Bline%2Caps%2C176&sr=8-8&th=1&psc=1)                                                                                                           
[-Elastic 1/8 inch paracord](https://www.amazon.com/dp/B00HNYJAWU/ref=twister_B0CX5XM9Z9?_encoding=UTF8&th=1)                                     
[-Dupont Jumper Wires Variety](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_1?crid=U5OX9E3IXVC1&dib=eyJ2IjoiMSJ9.SszVHKRXXxbEIG2ErBYriTYR5PGk9WL9Ph5J0Uu87uFyAvNhOPpbUvIFmUr8s7n0RYZQ19M_z85qbOiLmn9M4fmjjduIDglzxHSXrAAZWN-RbTMxBiXDBgJt7_6USOzBy3KqvgGnGVYI9UKUREi1keUWDKpJE4V2dlnRNiFwWMNFPatujQHQq0bGZROstitm0xYPFahorvaMPobsLtfIJBUIzcmXFofn3RXh4oMC-Zw.dwLq2Kn1KoLDQVfwp2QMpMVps70Uz81roxvpPcqpDvM&dib_tag=se&keywords=dupont+wires+variety&qid=1772301518&sprefix=dupont+wires+variety%2Caps%2C149&sr=8-1)                                                                                                                                             
[-Super Glue](https://www.amazon.com/Gorilla-Super-Glue-Gram-Clear/dp/B00OAAUAX8/ref=sr_1_3?crid=1HE9KCWRPDGK1&dib=eyJ2IjoiMSJ9.tSpIGY6rFGUb59rroPvWzAfXWehP2qGd1Z_V-XE0mW4hEFD36RYlPsUhxV4uDERE_Rk6XjqNchZnwD15rpdeQVzRsoOzC0xvv1pPYye3bfas1LBMNzNXAnAMn38DGd7ubU65lLpR18t5POMCjtR8T383VwGDLb71ajzBfCV1vwi7_xp0XVSn8OiA6PY-A2A155lcj1WsL5x2mwo5SSnbDwRk8-ytC8evy7bX07my_I0BkDbHPKswK5B7FLOHcgJPbo2khziFj_4LsquFZdJgon9oASb9POrMu5ylDVxsvcM.XvdwTNMUcqA_nP9SjQy3UPjdxqsYy7VSuEuR5C1Pg6Y&dib_tag=se&keywords=super+glue&qid=1772315855&s=home-garden&sprefix=super+glue%2Cgarden%2C167&sr=1-3)                                             
[-External Power Supply 10A 5V](https://www.amazon.com/CENTROPOWER-Transformer%EF%BC%8C-Surveillance-Cameras%EF%BC%8CRouter-Connector%EF%BC%8CUL-Listed/dp/B0BZHH3HVR/ref=sr_1_22_sspa?crid=KK79HTRCIO5E&dib=eyJ2IjoiMSJ9.uvuiR3PjXOxaI3f-GywZNSc-lfuYRBHIcpCOP0DtuHaFOkU2WSACwbRWNehHTHveWyoYEPscJvftIxc5M7zReE91b4Rhzc-LZlfnP44j8rxrAwVq9AIUQyb8KP_L8xr69eECJI6d7s0q63eSKJTmiS4fvbIbaSjAj7VI5kbOa1RV0AxVxo_Q8l0kEY10G6C0ndNuSdKwoO67HZe1yXhi-SvntalHOIQxrsR0cZLvFDY.uLAf0q3zTbNCsHUBO91HwTVIe98VHCjugIrfEjHw5VA&dib_tag=se&keywords=10+amp+5+v+power+supply&qid=1772328035&sprefix=10+amp+5+v+power+suppl%2Caps%2C224&sr=8-22-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1)
## Credits
3d Printed Files(Fingers, Hand, Thumb, Servo Cage, Servo Horn, Wrist, and Upper Forearm) by [Grossrc](https://www.thingiverse.com/grossrc/designs) liscenced under [Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)
