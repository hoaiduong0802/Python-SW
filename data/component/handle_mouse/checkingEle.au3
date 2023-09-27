#RequireAdmin
#include <MsgBoxConstants.au3>

$Hwd=WinGetHandle("Summoners War - MuMu Player")
WinActive($Hwd)
$Pos=WinGetPos($Hwd)
$x= $Pos[0]
$y= $Pos[1]

ControlClick("Summoners War - MuMu Player","","","left",1,$x+652,$y+265)
Func sellItem()

EndFunc