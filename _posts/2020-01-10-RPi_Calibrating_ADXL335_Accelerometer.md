---
title: "How to calibrate your accelerometer? Some tidbits"  
date: 2020-01-08 00:26:00 +0800  
categories: [Accelerometer, Calibration]  
tags: [Accelerometer, Calibration]  
---

I had to calibrate the accelerometer ADXL335 for the robot skin project that I am doing. It gives analog output in this digital world. Good for it! No problem. So I attached MPC3208 12bit ADC converter to read that output and consequently converting them to G's. Basically G means gravitational force of the mother earth which is 9.819 m/$s^2$.

Why I have chosen MP3208? Because it has python package. Install plug and play. Easy and simple. And choosing ADXL335 wasn't totally under my control, so here we are reading this blog post. Let's cross this Styx river together shall we?

The ADXL335 outputs in the range of 0V to 3.3V. Below is a quick table:

| Voltage | G Value |   
|---------|---------|
| 0       | -3G     |   
| 3.3     | 3G      |  

[Source](https://www.adafruit.com/product/163)

Now according to the [datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL335.pdf) page 12, they say

> The ADXL335 output is ratiometric

Meaning it's a straight line and the output is dependent on supply voltage. So 0G would be (Supply Volatge)/2. Cool!

Also when you just place the accelerometer on the table, in normal position, in technical terms the Z axis direction opposite to earth's magnetic field, you should be getting what?

The answer lies in my above statement: The ADXL335 output is ratiometric. So we basically have two points (0V, -3G) and (3.3V, 3G). If we draw a co-ordinate system where Voltage is on X axis and Acceleration in G is on Y axis, we have two points, use line equation and draw a line. So the equation of the line would be:

$$

$$

Now coming back to MCP3208. We will be getting output only in digital. So the output of MCP3208 can range from [1, 4096]. Why 4096? Because it's $$2^12$$ and also because it's 12-bit ADC. Now after we get ADC value we need to convert back to voltage so that we can estimate how much acceleration in terms of G are we getting? To do that, we refer to the datasheet of [MCP3208](https://ww1.microchip.com/downloads/en/DeviceDoc/21298c.pdf).Scroll down to Page 14 and you will find a equation below:

$$

$$

So now it's very important, what we put in Vref. Now at last I have also attached the circuit diagram I am using for the project. You can see I have put Vref to 3.3V. Hence My final equation would be :

$$

$$

So just for 1G, according to equations, we would should be measuring the voltage of 2.2V in our multimeter/oscilloscope when you measure the voltage between pins Zout and ground.

But if all this world was made of roses and Taylor Swift songs, you wouldn't be measuring that.

I was measuring exactly 2V between Zout and ground. Then I thought about the all the mistakes I made in my life till now. Well couldn't find any. To my dismay I also found it was same in case of X and Y axes too. So if your sensor is giving something like this, what would you do?

Well our good friend Co-ordinate geometry comes to rescue again. Now you don't take the hypothetical points mentioned in datasheet but take real values. Now keeping the board in normal position measure the volatge. In my case it was 2V. Now reverse the board and find out what's the voltage? I got it to be (TBD). So now my I have two points (TBD) and (TBD). Plot the line again. Below is the equation of the line:

$$

$$

So now you use this equation on all axes (Honestly you have to do it for every axis, but I just did for one axis and called it a day) and then find out exact acceleration in g. And this time it will be smooth and calibrated and it will behave exactly how you want it to be.

One taking the readings make sure you spirit level to find out it's exactly flat or not, else you find yourself in trouble later, when it's not behaving the way you wanted.

Good Day!

Blog incomplete. Some details will be added shortly! Thanks for your patience.
