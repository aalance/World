/***
Author: Lancekaliot
Requirements: System-World; Dreamer; Visualworld; 
***/


from System import System_World
import Dreamer
import Visualworld

Worldnum=Visualworld.epochnum
for world in  range(Worldnum):
	System_World.init()
	Dreamer.config.init()
	for people in range(Dreamer):
		Dreamer.dream()

		
