#RequireAdmin
#include <Array.au3>
#include <MsgBoxConstants.au3>
$Hwd=WinGetHandle("Summoners War - MuMu Player")
WinActive($Hwd)
$Pos=WinGetPos($Hwd)
$x= $Pos[0]
$y= $Pos[1]
Local $location_1 = [[630, 250], [668, 287]]
Local $location_2 = [[707, 248], [746, 287]]
Local $location_3 = [[783, 248], [822, 286]]
Local $location_4 = [[860, 247], [900, 286]]
Local $location_5 = [[628, 325], [669, 364]]
Local $location_6 = [[706, 324], [746, 362]]
Local $location_7 = [[782, 323], [822, 362]]
Local $location_8 = [[860, 323], [899, 362]]
Local $location_9 = [[629, 401], [629, 401]]
Local $location_10 = [[705, 400], [745, 440]]

Func sellItem()
	ControlClick($Hwd,"","","left",1,$x+Random(630,668,1),$y+Random(250,287,1))
	Sleep(1000)
	ControlClick($Hwd,"","","left",1,$x+Random(346,452,1),$y+Random(421,450,1))
	Sleep(1000)
EndFunc
sellItem()
Func getIem()
	ControlClick($Hwd,"","","left",1,$x+Random(504,616,1),$y+Random(418,458,1))
	Sleep(1000)
EndFunc ;==>_Storage_