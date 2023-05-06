# Filler3
 Open source can filler built from 3D printer, 3D printed and common home brewing items.

 Credits to <a href="https://www.youtube.com/channel/UCIIYTzYpd8D7y816diZB0Dw">HarryBrew69</a> for coming up with the idea of using an Arduino to run a can filler and sense fill level via analog inputs. And <a href="https://github.com/kloon/OpenBeerFiller">kloon</a> for his original implimentation of Harry's idea.

<a href="BOM.csv">BOM</a><br/>
<a href="/Build/">The Build</a><br/>
<a href="/Photos/">Build Photos</a><br/>
<a href="/firmware/">Firmware</a><br/>
<a href="/CQ-SRC/">CadQuery</a><br/>
<br/>

## Method of operation
<p>
    When plugged in the can filler will move the servo to the <b>SERVO_POS_IDLE</b> position, make sure the gas solenoid is disabled and raise the gantry to its home position and wait for user input.
    <br/><br/>
    Pressing the button will activate the filling process. 
    <br/><br/>
    The gantry will move to the <b>PRE_PURGE_POSITION</b> and activate the gas solenoid for the <b>PRE_PURGE_DURATION</b>.
    <br/><br/>
    After purging the gantry will move to the <b>FILL_POSITION</b>, the servo will move to the <b>SERVO_POS_FILL</b> position and the LED will start "breathing" to indicate the can is filling. 
    <br/><br/>
    If using <b>POSITIVE_PRESSURE</b> mode, the purge cap should be touching the can while filling. If not using the <b>POSITIVE_PRESSURE</b> mode, the purge cap should be positioned as close to the can as possible without touching. 
    <br/><br/>
    While filling the sensor wire is constantly being read and checking if the analog input has gone past the <b>SENSOR_TRIGGER</b> value.
    The <b>SENSOR_TRIGGER</b> value will need to be tuned if canning non still liquids.
    <br/><br/>
    Once full the servo will move back to the <b>SERVO_POS_IDLE</b> position. While the can is full and the gantry is down, the combination of <b>POSITIVE_PRESSURE</b> and <b>POST_PURGE_DURATION</b> settings will determine what happens next.
    <br/><br/>
    If using <b>POSITIVE_PRESSURE</b> mode, the LED will start "blinking" to indicate the can is full and wait for the button to be pressed before moving to the next position. This behaviour is to allow the user to grab hold of the can before the gantry moves to the next position. If the gantry moves while the purge cap is touching the can and the can is not held in position things can get very messy.
    <br/><br/>
    If <b>POSITIVE_PRESSURE</b> mode is disabled, the gantry will automatically move to the next position once the can is full. 
    <br/><br/>
    If a <b>POST_PURGE_DURATION</b> value has been set the gantry will move to the <b>POST_PURGE_POSITION</b> and activate the purge solenoid for the <b>POST_PURGE_DURATION</b> before moving the gantry back to the home position.
    <br/><br/>
    If no <b>POST_PURGE_DURATION</b> is set the gantry will move directly to the home position after filling.
    <br/><br/><br/>
    <b>NOTE: IF THE BUTTON IS PRESSED ANY TIME OTHER THAN WHILE THE GANTRY IS AT ITS HOME POSITION OR WHILE THE LED IS "BLINKING" IT IS TREATED AS AN EMERGENCY STOP AND WILL RESET THE FILLER.</b>
</p>
<img src="/Build/10_Filler3.png"/>
