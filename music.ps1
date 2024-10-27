# Ensure that you have VLC media player or MPV installed
# Send this to someone who loves classical music like I do
# Thanks to Ayush Jayaswal for the idea and resource!
 
 $music = "https://live.musopen.org:8085/streamvbr0?1729888126216"

 # if you're using VLC

 if(Get-Process -name "vlc" -ErrorAction SilentlyContinue){
    Stop-Process -Name "vlc"
 }
 else{
    Start-Process "vlc" -ArgumentList $music, "--intf", "dummy", "--loop" 
}


# Or, if you're using MPV

# if (Get-Process -Name "mpv" -ErrorAction SilentlyContinue) {
#     Stop-Process -Name "mpv"
# } else {
#     Start-Process "mpv" -ArgumentList $music -WindowStyle Hidden
# }



