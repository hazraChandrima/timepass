# Run this python script in your terminal to see ASCII animations : python diwali.py
# NOTE: KEEP THE FONT SIZE IN YOUR TERMINAL VERYY SMALL
# Send this to someone who's as boring as I am ;)
# I don't even think anyone's gonna read this

import time
import os

YELLOW = "\033[93m"
ORANGE = "\033[33m"
RESET = "\033[0m"
MAGENTA = "\033[95m"

frames = [
    f"""
    {ORANGE}
                                             ::                                           
                                           =%-                                            
                                         +@@:                                             
                                       -%@@+                                              
                                      *#-@@.                                              
                                     %+ +@@.                                              
                                    %+  =@@-                                              
                                   #*   .@@*                                              
                                  =%     *@@:                                             
                                  @-      %@%                                             
                                 =%    :: :@@#                                            
                                 #=   :@   -@@*                                           
                                 %:  .+@:   =@@*                                          
                                 @.  +.=@.   +@@+                                         
                                 #:  *  -@=   *@@-                                        
                                 -+  *    *%-  %@@                                         
                                  *. =.    .##.:@@=                                       
                                   +. +      -%-%@-  {RESET}""",
    f"""   
    {ORANGE}                                         
                                           ::                                             
                                            -%=                                           
                                             :@@+                                         
                                              =@@%=                                       
                                               @@=*#                                      
                                               @@* =%.                                    
                                              :@@+  =%                                    
                                              *@@:   *#                                   
                                             :@@#     %=                                  
                                             %@@.     :@.                                 
                                            *@@- ::    #+                                 
                                           +@@=   @-   -%                                 
                                          +@@+   .@*.  .@                                 
                                         =@@*   .%+ *   @                                 
                                        :@@#   =@=  *  .%                                 
                                        @@%  :%*.   *  ==                                 
                                       -@@-.##:     +  #                                  
                                       :@@:@-      = .+    {RESET}"""
]

remaining = f"""                        
                          .:-=++*##%%%@=.-      -*@@@@@@%%%##*++=-:.                        
                 .-+#%@@%#*+=--::..    .:.   .:-       ..::--=+*#%@@%#+-.                 
             .=#@%*=-.                      ::                      .-=*%@#=.             
            *@#-.                         =%@@%=.                         -#@*            
           *@-                        .=#@#-  -#@#=.                        -@*           
           *@#.                   .-*%@#=.       -*@%*-.                   .#@#           
           -@@@%*=-:.     ..:-+*#@%*=:              :=*%@#*+-:..     ..-=*%@@@:           
            #@-:=+*#%%@@@%%##*=-:         .++++.         :-=*##%%@@@%%#*+=:=@*            
             #@-                       :=+= --.-+=:                       -@#             
              *@*                  .=++- :..@@+ . -++=.                  +@*              
               -@%-         .:-=+++-.   +@@:   #@@   .-+++=-:.         -%@-               
                 +@@%+======-:.  .: :@@= :-=**+--: %@*  .  .:-======+%@@+                 
                   =%@+:    .++..@@+ --:=+=.  .=+=.-=:.@@* -+-    :+@%=                   
                     :+%@*-.:%%- .:.-++-.         -++-.:-  #@*.-*@%+:                     
                        .=*@%*+=+++-.                .-+++==*%@*=.                        
                            .-+*%@%#*+==--::::::--==+*#%@%#+-.                             
                                  .:-=++***####***++=-:.    
                                  
                                                                                                                                                                               
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
     {MAGENTA}                                                                                                                                                                                                                                                                                    
            @=    %+       :@=        @@@@=     :@@@@-     +%   *#           :@@@@@       =@     #*   :@    @=       @@        @-        @=           
            @+    %+       @@%        *  +@.    :@  =%-    -@: .@=           :@  .+@:     =@     %#   +@=   @=      .%@-       @-        @+           
            @+    %+       % @-       *   @.    :@   *%     @= =@            :@    %@     =@      @:  @@%   @.      %*%*       @-        @+           
            @+    %+      #% @-       *   @.    :@   *%      @ #-            :@     @     =@      @:  %=@. *@      .@- @.      @-        @+           
            @@@@@@@+      %  :@       *  @@.    :@  :@       +*%             :@     @     =@      *: #% @- *%      =@  @.      @-        @+           
            @+....%+     :@  .@       @@@+-     :@@@*-       :@=             :@     @     =@      :@ #* %- %       #+  -@      @-        @+           
            @+    %+     %@@@@@%      *         :@            @-             :@    .@     =@      :@ #  .@.@       @@@@@@      @-        @+           
            @+    %+     @-   *%      *         :@            @-             :@   .@*     =@       ##@  .@:=      +#    %*     @-        @+           
            @+    %+    ##     @=     *         :@            @-             :@--#@%      =@       #@*   *@=      @+    %#     @*===     @+           
            =:    -:    --     =.     :         .=            =.             .====-       :=       :=.   :=.      =:     =.    =====.    =:                                                                                                                                                     
      {RESET}
"""

clear_screen = "cls" if os.name == "nt" else "clear"

try:
    while True:
        for i in frames:
            os.system(clear_screen)
            print(i+remaining)
            time.sleep(0.1)
except KeyboardInterrupt:
    os.system(clear_screen)
    print("Animation stopped.")
