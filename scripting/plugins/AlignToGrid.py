import pcbnew

class AlignToGrid(pcbnew.ActionPlugin):
    grid = 0.25

    def defaults(self):
        self.name = 'Align To ' + str(self.grid) + ' mm Grid'
        self.category = 'Placement'
        self.description = ''

    def Run(self):
        units = pcbnew.FromMM(self.grid)
        board = pcbnew.GetBoard()
        origin = board.GetDesignSettings().GetGridOrigin()

        for f in board.GetFootprints():
            if not f.IsSelected():
              continue
            x = f.GetPosition().x - origin.x
            y = f.GetPosition().y - origin.y
            xAligned = round(x / units) * units
            yAligned = round(y / units) * units
            f.SetPosition(pcbnew.VECTOR2I(xAligned + origin.x, yAligned + origin.y))

        for f in board.GetTracks():
            if not f.IsSelected():
              continue
            if f.GetClass() != 'PCB_VIA':
              continue
            x = f.GetPosition().x - origin.x
            y = f.GetPosition().y - origin.y
            xAligned = round(x / units) * units
            yAligned = round(y / units) * units
            f.SetPosition(pcbnew.VECTOR2I(xAligned + origin.x, yAligned + origin.y))

        pcbnew.Refresh()

AlignToGrid().register()
