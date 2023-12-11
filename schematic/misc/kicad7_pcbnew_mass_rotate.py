import pcbnew as p
for lednr in range(1, 97):
    ledn = "D%u" %lednr
    for fp in p.GetBoard().GetFootprints():
        if fp.GetReferenceAsString() == ledn:
            print(ledn)
            degs = 45
            if lednr%2 == 0: degs = 45-180
            fp.SetOrientationDegrees(degs)
p.Refresh()


import pcbnew
board = pcbnew.GetBoard()
for i in board.GetTracks():
	if (i.GetClass() == "PCB_VIA" and i.GetDrill() == 400000 and i.GetWidth() == 800000):
		print(i.GetDrill(), i.GetWidth())
		i.SetDrill(300000)
		i.SetWidth(600000)

for i in board.GetTracks():
	if (i.GetClass() == "PCB_VIA"):
		i.SetDrill(400000)
		i.SetWidth(800000)
