 # this one as a powershell script
# Run this powershell script in your terminal:  diwali.ps1
# NOTE: KEEP THE FONT SIZE IN YOUR TERMINAL VERYY SMALL
# Send this to someone who's as boring as I am ;)

$YELLOW = "Yellow"
$ORANGE = "DarkYellow" 
$RED = "Red"
$RESET = ""
$GRAY = "Gray"
$BLACK = "Black"

$frames = @(
    @"
                           
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
                                                           +. +      -%-%@-  
"@,
    @"
                                                                    
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
                                                               :@@:@-      = .+     
"@
)

$remaining = @"
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
"@

try {
    while($true) {
        foreach ($frame in $frames) {
            Clear-Host
            Write-Host $frame -ForegroundColor $ORANGE -BackgroundColor $BLACK
            Write-Host $remaining -ForegroundColor $GRAY -BackgroundColor $BLACK
            Start-Sleep -Milliseconds 100
        }
    }
}
catch {
    Clear-Host
    Write-Host "Wishing You a very Happy Diwali!!" -ForegroundColor $RED
}

