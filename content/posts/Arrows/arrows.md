---
Title: Arrow Ballistics Calculation
Date: 2021-08-21
Slug: arrow-ballistics
JS: arrowcalc.js (bottom), https://d3js.org/d3.v4.js (top)
Category: Fun Stuff
---
# Arrow Ballistics Calculation

This post was inspired by a couple of videos[1] on the excellent 
YouTube channel _Tod's Workshop_ involving testing the maximum range
of crossbow bolts. Comments discussed whether 45 degrees was really 
the optimal angle for firing crossbow bolts for maximum range, and
most agreed that an angle between 30 and 40 degrees was ideal. However,
physical testing revealed that maximum range was achieved at close to
45 degrees.

This seemed like an interesting physics problem that could reasonably
be written in JavaScript or TypeScript, so I decided to take it on. 
The partial differential equations are as follows:


$$m \frac{d v}{dt} = -D(\psi) - m g \sin{\theta}$$
$$m v \frac{d \theta}{dt} = L(\psi) - m g \cos{\theta}$$
$$I \frac{d^2 \psi}{dt^2} = M(\psi)$$
$$D = C_D(\psi) A_D(\psi) v^2 \rho$$
$$L = C_L(\psi) A_L(\psi) v^2 \rho \sin{\psi}$$

with the following definitions:

|          |                            |
|----------|----------------------------|
| $m$      | Mass                       |
| $v$      | Speed                      |
| $\psi$   | Angle of attack            |
| $\theta$ | Angle of motion            |
| $g$      | Gravitational acceleration |
| $I$      | Moment of inertia          |
| $D$      | Drag force                 |
| $C_D$    | Coefficient of drag        |
| $A_D$    | Drag area                  |
| $L$      | Lift force                 |
| $C_L$    | Coefficient of lift        |
| $A_L$    | Lift area                  |
| $\rho$   | Air density                |
| $M$      | Pitching moment            |


The lift and drag forces depend on the angle of attack. This relationship is
approximated by finding the projected area of the body in the direction of
motion. Motion is calculated with a 4-th order Runge Kutta integrator.

Lift was added for completeness and doesn't have much of an effect at close to
zero angle of attack. However, setting a high lift area and a low mass leads to
interesting results.


<div id="controls"></div>
<div id="graph"></div>
<div id="angle"></div>

<table>
    <tr>
    <td><label for="total_distance">Total Distance</label></td>
    <td><output id="total_distance"></td>
    </tr>
    <tr>
    <td><label for="time_of_flight">Time of Flight</label></td>
    <td><output id="time_of_flight"></td>
    </tr>
    <tr>
    <td><label for="energy">Energy</label></td>
    <td><output id="energy"></td>
    </tr>
    <tr>
    <td><label for="momentum">Momentum</label></td>
    <td><output id="momentum"></td>
    </tr>
</table>


I liked learning TypeScript for this project. It was easy to learn coming from a
python background and npm made it easy to manage the build environment. However,
I found a lot of documentation and community around JavaScript and TypeScript to
be a bit _industrial_. The focus is not on helping people make little
calculators for their personal blogs. Finding how to get a slider to interact
with a JavaScript object was a chore, because almost all of the results were
something to the effect of _use the [] framework on your webserver running
node_. 


The source code for this is available on [github](https://github.com/Jason-S-Ross/arrow-ballistics).

[1]: [Distance - Which angle is best?](https://www.youtube.com/watch?v=dTW0CrXugdQ) [850lbs Crossbow DISTANCE TEST](https://www.youtube.com/watch?v=dTW0CrXugdQ)
