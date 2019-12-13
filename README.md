# gaylorgf_Final_Project
BU CS 521-Fall 2 Final Project Twitter API 
     
![Greg's TWITTER API](https://github.com/GG38040/gaylorgf_Final_Project/blob/master/twit_api_logo.PNG)

Greg's Twitter API

Motivation:
This twitter API creates a custom interface for getting twitter data.  
As a cyber security analyst it is often useful to get real time information.
Real time information from open source tools such as Twitter can be very valuable.
It gives analyst the ability to gain situational awareness around a topic in near real time.
Being able to query the twitter stream's mentions of a Corporation can reveal
data breaches that consumers are mentioning on twitter.  For example with a large data
breach that effects consumers they might start seeing fradulant credit card purchases or spam
email.  If this occurs on a large enough scale users will start reaching out via social media
to mention their concerns.  If a company is able to start mitigating 
this early through thier communications department it can lessen the reputational impact of a 
given data breach.  

Build Status:
This project was created to complete the requirements for CS521 at Boston University.  
I would like to explore sentiment analysis of the twitter stream on future topics.  

Code Style:
This project utilizes python 3 with PEP 8 formating.  

Features:
This api allows the following;
-View current Twitter stream for key a word.
-Get last 10 tweets from #gaylorIii timeline
-Search for a user on twitter and print to file the results
-Search twitter for a key word or topic like "python"

Installation of Required Modules:
This project utilizes the tweepy module.  
Website www.tweepy.org
Docs https://tweepy.readthedocs.io/en/latest/#
GitHub https://github.com/tweepy/tweepy

Installing tweepy
Easiest method is with pip
- "pip install tweepy"

You can also use Git to clone repository 
- "git clone https://github.com/tweepy/tweepy.git"
- "cd tweepy"
- "python setup.py install"

Finally if all else fails
- on https://github.com/tweepy/tweepy
- click "clone or download"
- click "download ZIP"
- navigate to tweepy-master.ZIP
- extract all
- navigate to tweepy folder in favorite terminal/cmd/powershell
- type -"python setup.py install"  

How to Use:
- Navigate to gaylorgf@bu.edu_final_project folder
-ls or dir to confirm file directory contains program files "user_api_interface.py",
"twit_restful.py", "stream_listener.py", and "auth_info.py"
-run "python user_api_interface.py"
-you should see BU ascii art and user input prompt.  
-enter choice and have fun exploring twitter via Greg's api!!

Credits:
Thank you to the developers that made the tweepy module!  This module
has been fun to learn and I enjoyed creating a way to explore the "twitterverse".
Also thank you to Professor Pinsky and the excellent facilitors at Boston University for
passing on their knowledge of python to our class.  

