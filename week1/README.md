# week1
Week 1 assignment and documentation
I have created a contour detection model using canny edge detection algorythm.
I imported all the dependencies
I defined a custom function for printing the result wherein I compare the original image to it's contour. I have also added the requisite ticks and other visual aids.
I started out with reading the image and converting the same to grayscale using imread cvtColor functions.
I tried many models using the Sobel,scharr and Laplace algorythms separately detecting horizonatal and vertical edges and then using addWeighted function with equal weights of 0.5 but found canny to work the best.
Canny works the best as it employs the principles of noise reduction in images, double thresholding and edge tracking by hysteresis wherein the model ignores pixels below a certain intensity and recognizes till a certain maximum intensity. This efficiently tracks the edge as at the idge intensity changes sharply. It also then uses hysteresis which is its distinguishing feature among all the other algorythms I tried. In hysteresis the model only recognizes those pixels with intermediate intensity that are connected to a pixel of higher intensity and ignores all other disjoint pixels with intermediate intensity.
I also tried the model on an image imported via a link and found the model to be working satisfactorily.
I have attached the resultes herewith. 
