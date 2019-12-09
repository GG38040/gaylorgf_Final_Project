"""
Greg Gaylor
Class: CS 521-Fall 2
Date: 12/8/2019
Final Project 
Description: Twitter API
"""

import tweepy
import twitter_streaming
import twitter_restful_api

print(
    """   ----------------------------------         ----------------------   .---------------------     
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs:`      hddhhhhhhhhhhhhhhhhhdd   odhhhhhhhhhhhhhhhhhddd     
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddh+     hdhhhhhhhhhhhhhhhhhhdd   odhhhhhhhhhhhhhhhhhhdd     
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdds-`  hdhhhhhhhhhhhhhhhhhhdd   odhhhhhhhhhhhhhhhhhhdd     
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdd+  hdhhhhhhhhhhhhhhhhhhdd   odhhhhhhhhhhhhhhhhhhdd     
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddo  hdhhhhhhhhhhhhhhhhhhdd   odhhhhhhhhhhhhhhhhhhdd     
     oyyyyddhhhhhhhhddyyyyyyyyyyyhdhhhhhhhhddo  syyyyddhhhhhhhhddhyyyy   +yyyyddhhhhhhhhddyyyyy     
     `````ddhhhhhhhhdd.``````````/dhhhhhhhhddo  ````.ddhhhhhhhhdd+````   `````hdhhhhhhhhdd.````     
          ddhhhhhhhhdd`          :dhhhhhhhhddo      `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhhddo      `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhhddo      `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhhddo      `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd-........../dhhhhhhhhddo      `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhhddddddddddddddhhhhhhhdds- `-+  `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhhhhhhhhhhhhhhhhhhhhhddh- `:yd+  `ddhhhhhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhhhhhhhhhhhhhhhhhhhhddh-:sdNs`   `ddhhddddhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhhhhhhhhhhhhhhhhhhhhhddmNmNy.-:-..ddhmmmdhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhhhhhhhhhhhhhhhhhhhhhdNNddmsssooy/hhdmdmhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdddddddddddddddhhhhhmNNmmhhNNNNNds-.:shhhhhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd.``````````/dhhhhhhmNNmNNNNNNNNmd+``:yddhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhmNNNmdmNNNd+/y+  -mhddd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhmNNdhmdsomNNmo.    :hNdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhNNNNNNmso/hhmNmo-::+hhdd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhmNNNNms//y//oyhys++dhddd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhdNNNNh+yds:+shyo:/+oyhd+            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhhhhhhhhNdyhdmddhs-` `/+osyoo/            hdhhhhhhhhdd`         
          ddhhhhhhhhdd`          :dhhdhhdhh/y::-+dd/`     .:sNNm+.-           hdhhhhhhhhdd`         
     .----ddhhhhhhhhdd:----------+dhhhyho/+m::./-/.`         /o: ::-----------hdhhhhhhhhdd`         
     sdhhhddhhhhhhhhddhhhhhhhhhhhddhhhyss+oN-/---:+. `.`      .  ohhhhhhhhhhhhddhhhhhhhhdd`         
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddmmdyoso/--+:+:` `     `-::ohhhhhhhhhhhhhhhhhhhhhhhdd`         
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhdNNNNNNNh+osyosos:.` `.:osyhhhhhhhhhhhhhhhhhhhhhhhhhddy`         
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhdNNNNmyo/::ss:ohhoshdhyhhhhhhhhhhhhhhhhhhhhhhhhhhhddh/`          
     sdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhmNNN:.- `. ``./so+ymNysdhhhhhhhhhhhhhhhhhhhhhhhddy/`            
     sdddddddddddddddddddddddddddddddmNN-:-.-      -++/sNhyydddddddddddddddddddddddh/`              
     .---------------------------------/shy+:     `sNdmmNmN/o----------------------.                
     /ysssssssssssssssssssssssssssssssssyhmmdo-.-/yNNNNNNNN:dsssssssssssssssssssssssssssyo          
     odhhyyyhhhyyhhyyhhyyyyhhyhhyhhyhhhhhyhyhdhdmNNNdhhhdddhhyyhhyyyhhyyhhyhhyyyyhyhyyhhdh          
     odhh/-:-h-/.s+-:/o--:.y./.y-.+.shhho.o-/h-/yody-s+.+.:y-/:/y-/-+s:/-h-o+--:-s-+--yhdh          
     odhh+`:-h y`+/:++ys/yoy h y/ + hhhhy h-+h/`/ hh-hh.+`yh-++sh:o-/o/o:h/yys:yohy-.yhhdh          
     odhh+.o.h s`oo++-hh:shy y y:.. hhhhy y.oh::. hh.hho +hh.y//h-o`ssos h:shh-yhhh/+hhhdh          
     odhh+++oho++ys++shh+ohh+++h++y+hhhhh+++yh+oy+hy+yhh+hhy+++oy+ss+y++oh+ohy+shhh++hhhdh          
     odhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdh          
     -:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: """
)

if __name__ == '__main__':

    print("WELCOME TO MY TWITTER API!!")

     while True:

        print("1: To look at the current twitter stream for key words.")
        print("2: To look at the last 10 public tweets from @gaylorIii.")
        print("3: To get the information on a twitter user.")
        print("4: To search twitter for a topic.")
        print("5: Press to EXIT.")

        user_input = input("Enter a choice 1-5:")

        if user_input == "5":
            quit()
        elif user_input == "1":
            user_stream = input(
                "Please enter a key word to query twitter stream:")
            listen = stream_listener.Stream_listener(user_input)
            stream_listener.Stream_listener('dominos').stream(listen)
