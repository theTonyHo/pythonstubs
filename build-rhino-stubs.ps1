# configs
$mypath = (Get-Item -Path ".\").FullName
$stubsdest = "$mypath\stubs"
$rhinobase = "C:\Program Files\Rhino 7"
$rhinoplugins = "$rhinobase\Plug-ins"
$rhinosystem = "$rhinobase\System"

cd "builder\bin"

./PyStubbler.exe --dest="$stubsdest\Eto" --search=$rhinosystem "$rhinosystem\Eto.dll"
./PyStubbler.exe --dest="$stubsdest\Rhino" --search=$rhinosystem "$rhinosystem\RhinoCommon.dll"
./PyStubbler.exe --dest="$stubsdest\Grasshopper" --search=$rhinosystem "$rhinoplugins\Grasshopper\Grasshopper.dll"
./PyStubbler.exe --dest="$stubsdest\GH_IO" --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_IO.dll"
./PyStubbler.exe --dest="$stubsdest\GH_Util" --search=$rhinosystem "$rhinoplugins\Grasshopper\GH_Util.dll"

# back to where started
cd $mypath