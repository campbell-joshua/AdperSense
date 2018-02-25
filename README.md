# AdperSense
Josh Campbell  
Chris Bell  
2/25/2018  
HackIllinois 2018

**Due to file sizes being too big and running out of time, this link will allow you to download the 
zip of all of the tensorflow and react files**  
https://drive.google.com/file/d/1YvguE_Bdsy4tBfpgSKkL10Q8wr_Gm7as/view?usp=sharing

### Built With
AdperSense is constructed with Google's Tensorflow, MIT's React, NodeJS, Javascript, and Python

### Purpose
Using machine learning, advertisments are anyalized based on data survayed from users.  
Users can upload images to the database, and will be given the potential success rate 
of the advertisemnt, based on a set of data determined by user survays and machine learning.  

This specific dataset included contains data of ~900 different advertisements reviewed by 
18-24 year-old males. We strongly recommend as many data samples as possible, as it makes the model 
more accurate.

### Development
Advertisements to be tested by users are place in ./images_test/  
To pull large quantities of advertisements from a google search, using Fatkun Batch
Download Image is recommended  
Lines 20 and 22 of UserFiltering.py must be changed to reflect the correct path

Users are prompted with an image, which is closed by the first keystroke
The console then prompts for the user to decide if they like the ad, dislike the ad,
would like to ignore the ad, or would like to quit the program.  
Users can stop the program at any point and it will resume where the user left off upon restarting. 
Files that are discarded are placed in ./garbage/, files that are liked or disliked are placed in
the appropraite folders, currently named ./good_images2/ and ./bad_images2/

After 3 sets of data are collected, ConsensusCalculation.py should be ran to determine which ads are
liked or disliked by a majority of the users.  
***Several paths will need to be changed if you are using a different file structure***  
The ads that are liked by a majority of users are placed in ./final_good/ while ones that are disliked by a majority
are placed in ./final_bad/

### Features
The user will navigate to a web app and feed the program an advertisement image. The ad will run it through iterations and come out with a test that matches closer to the more successful advertisements, or the less successful ones, based on patterns given by the previous user group when training the program.

### Why
This project was built so companies can stop spending as much money as they do every year on advertisements that turn out to not be successful because they do not have the data to be able to perfectly hit the correct age groups. Well now they do. The companies can create an ad, run it through the program, and find whether or not this ad will be successful in which age groups.

OSI:  
    AdperSense, Machine Learning to determine success rate of advertisements
    Copyright (C) 2018  Josh Campbell

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
