# AdperSense\n
Josh Campbell\n
Chris Bell\n
2/25/2018\n
HackIllinois 2018

Data Collection:
Advertisements to be tested by users are place in ./images_test/
To pull large quantities of advertisements from a google search, using Fatkun Batch
Download Image is recommended
Lines 20 and 22 of UserFiltering.py must be changed to reflect the correct path

Users are prompted with an image, which is closed by the first keystroke
The console then prompts for the user to decide if they like the ad, dislike the ad,
would like to ignore the ad, or would like to quit the program.
Users can stop the program at anypoint and it will resume where the user left off upon restarting
files that are discarded are placed in ./garbage/, files that are liked or disliked are placed in
the appropraite folders, currently named ./good_images2/ and ./bad_images2/

After 3 sets of data are collected, ConsensusCalculation.py should be ran to determine which ads are
liked or disliked by a majority of the users.
***Several paths will need to be changed if you are using a different file structure***
The ads that are liked by a majority of users are placed in ./final_good/ while ones that are disliked by a majority
are placed in ./final_bad/
