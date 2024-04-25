from well_profile import well_profile

well1 = well_profile.load('t1.xlsx',
                          cells_no=66,
                          units='metric',
                          set_start={'north': 0, 'east': 0, 'depth': 0})
well1_fact = well_profile.load('tf1.xlsx',
                               units='metric',
                               cells_no=137,
                               set_start={'north': 0, 'east': 0, 'depth': 0})
well1.plot(add_well=[well1_fact],names=['t', 'tf']).show()
