# Create-Ovito-Movie

This program creates a simple XYZ file that you can load with Ovito

By running the first block you will realise if the file "file.dat exists in the directory "/home/user/folder/".

If the positions are already with units then the pixel pitch is 1.0, otherwise just change PPX, PPY and PPZ for the pixel pitch and the Z separation.

When tracking/linking with IDL or trackpy you usually get different columns, such as positions (x, y, z), brightness, radius, frame, etc... As an example here I use particle positions, "b", "r", "p", "f" and "frame" columns, and as we are only interested in particle positions then I remove "b", "r", "p" and "f".

The output file will be stored in "/home/user/folder/" as "Movie.xyz", "Ntot" is the total number of frames and the XYZ file will cointain frames from 0 to Ntot. You can decide from which to which frame to save.
