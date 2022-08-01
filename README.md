<h1 align="center"> 104intersection <h1>

![image](https://user-images.githubusercontent.com/91891487/182242388-83cb9f94-345b-472f-b7dd-c8d444e22d9e.png)

<h2> Description </h2>

<p>To create synthesis images (when doing ray tracing, for example), potential intersection points between
light rays and scene objects (here cylinders, spheres and cones) must be computed. This is exactly what
you have to do in this project.</p>
<p>To do so, you need to write a 3 dimensional equation of the considered surface, and inject into it the equa-
tion of the straight line representing the light ray. You’ll get a quadratic equation, with 0, 1, 2 or an infinite
number of solutions that will give you the intersection points coordinates.</p>
<p>The straight line is defined by the coordinates of a point by which it passes through and the coordinates of
a parallel vector.</p>
<p>O being the origin of the coordinate system, and X, Y and Z the axis, the surfaces that must be handled
in this project are:</p>

  - O-centered spheres,
  - Cylinders of revolution around Z axis,
  - Cones of revolution around Z axis whose apex is O.
  
<h2> Usage </h2>

![image](https://user-images.githubusercontent.com/91891487/182242942-67f51f25-26ff-4662-b525-98a1d6985bfa.png)

<h2> Example </h2>

![image](https://user-images.githubusercontent.com/91891487/182243073-dcae7f25-288b-4679-b843-3b36dc9a3c61.png)
